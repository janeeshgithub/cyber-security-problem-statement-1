import re
from urllib.parse import urlparse

# Keywords to identify possible phishing and malware links
phishing_keywords = [
    "login", "verify", "update", "secure", "account", "signin",
    "bank", "password", "confirm", "click", "reset", "security"
]

malware_keywords = [
    "free", "download", "crack", "install", "update", "hack", "casino",
    "bet", "cheap", "offer", "bonus"
]

# Suspicious domain patterns (shortened URLs, unusual TLDs, IP addresses)
suspicious_domains = ["bit.ly", "goo.gl", "tinyurl", "ow.ly"]
unusual_tlds = ["xyz", "top", "click", "work", "club", "gq", "ml", "ga", "cf"]

def is_ip(url):
    # Checks if the domain is an IP address
    ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return bool(ip_pattern.match(url))

def detect_malicious_phishing_link(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    path = parsed_url.path

    # Check for IP address in the domain
    if is_ip(domain):
        return "Suspicious - Contains IP address"

    # Check for suspicious domain and TLD
    for shortener in suspicious_domains:
        if shortener in domain:
            return "Suspicious - URL shortener detected"
    
    for tld in unusual_tlds:
        if domain.endswith("." + tld):
            return "Suspicious - Unusual TLD detected"

    # Check for phishing and malware keywords in the path
    for keyword in phishing_keywords:
        if keyword in path:
            return "Suspicious - Phishing keyword detected"

    for keyword in malware_keywords:
        if keyword in path:
            return "Suspicious - Malware keyword detected"

    return "Safe - No suspicious patterns found"

# Test URLs
test_urls = [
    "http://bit.ly/suspicious-link",
    "http://example.xyz/login",
    "https://192.168.0.1/verify",
    "http://safe-site.com/welcome"
]

for url in test_urls:
    result = detect_malicious_phishing_link(url)
    print(f"URL: {url} - Status: {result}")