# Detecting Phishing Links & Identifying Black Hats (VENGER)

## Project Overview

**Detecting Phishing Links & Identifying Black Hats (VENGER)** is a cybersecurity project designed to tackle the rising threat of phishing attacks. Phishing attackers often create convincing schemes to deceive individuals and organizations, tricking them into revealing sensitive information or downloading malware. Unlike existing solutions that primarily focus on detecting or blocking threats, VENGER takes an extra step by aiming to identify the attackers themselves, helping to safeguard users from future attacks.

## Problem Statement

With the rapid increase in online connectivity, users face an ever-growing risk of phishing attacks, where attackers use carefully crafted malicious links to extract sensitive data. Many existing solutions only aim to block these attacks, overlooking the identity of the attackers. This leaves users vulnerable without any clear means of recourse against such threats.

## Proposed Solution

VENGER provides a multi-layered approach for detecting phishing attempts and identifying attackers. The main components of the solution include:

1. **Isolated Sandbox Environment**:
   - VENGER uses virtual machines (VMs) and monitoring tools such as **Wireshark** and **Zeek** to safely analyze phishing links in an isolated environment, protecting the system from potential harm while inspecting threats.

2. **Threat Intelligence Integration**:
   - The project integrates with established threat intelligence databases like **VirusTotal** and **AbuseIPDB**. By cross-referencing with these sources, VENGER can accurately identify malicious links and detect potential attack patterns.

3. **Data Visualization**:
   - Leveraging the **ELK stack (Elasticsearch, Logstash, Kibana)**, VENGER visualizes and analyzes collected data, enabling a more comprehensive understanding of phishing attempts and automating malicious link detection.

4. **Attacker Identification with Reverse Shell**:
   - Upon detecting phishing links, VENGER deploys a **Reverse Shell** payload to gather information about the sender. This information can then be reported to cyber authorities, aiding in the identification and tracking of black hat hackers.

5. **User Protection**:
   - VENGER also aims to safeguard vulnerable users, such as children, from various online threats, including cyberbullying, viruses, invasive advertisements, and phishing attacks, fostering a safer digital environment.

## Technical Components

- **Tools & Technologies**:
  - **Zeek**: Network security monitor for real-time traffic analysis.
  - **Wireshark**: Packet capture tool for analyzing data packets and identifying suspicious activities.
  - **Docker**: Containerization tool used to create isolated environments for secure phishing link analysis.
  - **Custom Sandbox**: An environment specifically configured to run tests on phishing links without risking security.
  - **Reverse Shell Payload**: Allows VENGER to gather identifying data from malicious sources, supporting attacker tracking.

- **Dependencies**:
  - **Libpcap / tcpdump**: Packet capture utilities critical for analyzing network traffic.
  - **Glib and GTK**: Necessary for running Wireshark's graphical interface on Linux systems.
  - **SSL Libraries (e.g., OpenSSL)**: Essential for decrypting HTTPS traffic for inspection.
  - **Lua (optional)**: Allows custom scripting within Wireshark to extend functionality.

---

## Summary

**VENGER** represents an innovative approach to cybersecurity, addressing not only phishing detection but also attacker identification. By combining sandboxing, threat intelligence, data visualization, and reverse shell techniques, VENGER provides users with proactive protection against phishing attacks and enhances online safety for vulnerable groups. This dual approach of threat detection and attacker identification makes VENGER a powerful tool in the fight against cyber threats.
