import re
import json
from collections import Counter

LOG_FILE = "/var/log/myapp/myapp.log"
REPORT_FILE = "/var/log/myapp/log_report.json"

log_levels = Counter()
endpoints = Counter()
slow_requests = []

ip_pattern = re.compile(r"([0-9]{1,3}\.){3}[0-9]{1,3}")
endpoint_pattern = re.compile(r"accessed (\S+)")

with open(LOG_FILE, "r") as f:
    for line in f:
        # Count log levels
        if "INFO" in line:
            log_levels["INFO"] += 1
        elif "WARNING" in line:
            log_levels["WARNING"] += 1
        elif "ERROR" in line:
            log_levels["ERROR"] += 1

        # Extract endpoint
        endpoint_match = endpoint_pattern.search(line)
        if endpoint_match:
            endpoints[endpoint_match.group(1)] += 1

        # Detect slow requests
        if "Slow response" in line:
            timestamp = line.split()[0] + " " + line.split()[1]
            endpoint = endpoint_match.group(1) if endpoint_match else "unknown"
            slow_requests.append({"timestamp": timestamp, "endpoint": endpoint})

report = {
    "log_levels": dict(log_levels),
    "endpoint_requests": dict(endpoints),
    "slow_requests": slow_requests
}

with open(REPORT_FILE, "w") as f:
    json.dump(report, f, indent=2)

print(f"Report generated at {REPORT_FILE}")
