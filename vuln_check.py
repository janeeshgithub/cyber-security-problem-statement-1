#!/usr/bin/env python3

import re
from urllib.parse import urlparse, unquote

# Patterns for vulnerabilities
redirect_patterns = [r"redirect=", r"next=", r"url=", r"dest=", r"destination="]
sql_patterns = [r"'", r'"', r" OR ", r" AND ", r"--", r";", r"DROP", r"SELECT", r"INSERT", r"DELETE"]
xss_patterns = [r"<script>", r"javascript:", r"onerror", r"onload", r"alert("]
traversal_patterns = [r"\.\./", r"\.\.\\", r"%2e%2e%2f", r"%2e%2e%5c"]
obfuscation_patterns = [r"%[0-9a-fA-F]{2}", r"\\x[0-9a-fA-F]{2}"]

def check_vulnerabilities(url):
    parsed_url = urlparse(url)
    path = unquote(parsed_url.path)
    query = parsed_url.query

    vulnerabilities = []

    # Detect Open Redirect
    if any(re.search(p, query) for p in redirect_patterns):
        vulnerabilities.append("Open Redirect")

    # Detect SQL Injection
    if any(re.search(p, path, re.IGNORECASE) for p in sql_patterns):
        vulnerabilities.append("SQL Injection")

    # Detect XSS
    if any(re.search(p, path, re.IGNORECASE) for p in xss_patterns):
        vulnerabilities.append("XSS")

    # Detect Directory Traversal
    if any(re.search(p, path) for p in traversal_patterns):
        vulnerabilities.append("Directory Traversal")

    # Detect URL Obfuscation
    if any(re.search(p, path) for p in obfuscation_patterns):
        vulnerabilities.append("URL Obfuscation")

    return vulnerabilities if vulnerabilities else ["No vulnerabilities detected"]

# Test URLs
urls = [
    "http://example.com/path?redirect=http://malicious.com",
    "http://example.com/login?id=1' OR '1'='1",
    "http://example.com/search?q=<script>alert(1)</script>",
    "http://example.com/../../etc/passwd",
    "http://example.com/%2e%2e%2fadmin",
    "http://safe-site.com/welcome"
]

for url in urls:
    results = check_vulnerabilities(url)
    print(f"URL: {url} - Vulnerabilities: {', '.join(results)}")
