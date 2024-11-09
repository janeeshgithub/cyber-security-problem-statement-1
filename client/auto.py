import os
import subprocess
import json
import psutil
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'
app.config['ALLOWED_EXTENSIONS'] = {'exe', 'bat', 'sh', 'msi', 'apk', 'jar'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def run_in_sandbox(file_path):
    """
    Runs the file in a Docker sandbox environment and captures logs for analysis.
    """
    container_name = "sandbox_container"
    image_name = "ubuntu:latest"

    # Create Docker container (isolated environment)
    subprocess.run(["docker", "run", "-d", "--name", container_name, "--network", "none", image_name])

    # Copy the file to the container
    subprocess.run(["docker", "cp", file_path, f"{container_name}:/tmp/{os.path.basename(file_path)}"])

    # Run the file inside the container (use appropriate command based on file type)
    subprocess.run(["docker", "exec", container_name, "bash", "-c", f"/tmp/{os.path.basename(file_path)}"])

    # Capture logs from the container (behavior analysis)
    logs = subprocess.run(["docker", "logs", container_name], capture_output=True, text=True)

    # Clean up container after execution
    subprocess.run(["docker", "rm", "-f", container_name])

    return logs.stdout

def monitor_file_behavior(file_path):
    """
    Monitor system activities such as CPU, disk, and network activities while the file is running.
    """
    pid = os.spawnl(os.P_NOWAIT, file_path)
    process = psutil.Process(pid)
    network_connections = process.connections(kind='inet')
    cpu_usage = process.cpu_percent(interval=1)
    disk_io = process.io_counters()

    return {
        "network_connections": network_connections,
        "cpu_usage": cpu_usage,
        "disk_io": disk_io
    }

def classify_malware(behavior_data):
    """
    Classify the malware based on its behavior.
    """
    if "suspicious_connection" in [conn.laddr for conn in behavior_data["network_connections"]]:
        return "Trojan"
    if behavior_data["cpu_usage"] > 80:
        return "Ransomware"
    return "Adware"

def generate_report(file_path, malware_type, infected_files, recommendations):
    """
    Generates a report in JSON format after analyzing the malware.
    """
    report = {
        "file": file_path,
        "malware_type": malware_type,
        "infected_files": infected_files,
        "recommendations": recommendations
    }
    report_file = f"{file_path}_report.json"
    with open(report_file, "w") as f:
        json.dump(report, f, indent=4)

    return report_file

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Run the file in the sandbox
        logs = run_in_sandbox(filepath)
        
        # Monitor the file behavior
        behavior_data = monitor_file_behavior(filepath)
        
        # Classify the malware based on behavior
        malware_type = classify_malware(behavior_data)
        
        # Generate a report based on the analysis
        infected_files = ["C:\\Program Files\\malware.exe"]  # Example, in real-life scenario, it would be more dynamic
        recommendations = "Update antivirus and restore system from backup"
        report_file = generate_report(filepath, malware_type, infected_files, recommendations)

        return jsonify({
            "status": "File analyzed",
            "logs": logs,
            "report": f"Report generated: {report_file}",
            "malware_type": malware_type,
            "infected_files": infected_files,
            "recommendations": recommendations
        })
    
    return jsonify({"error": "Invalid file type"}), 400

if __name__ == "__main__":
    app.run(debug=True)
