import re
from collections import Counter
LOG_FILE = "/var/log/auth.log"
THRESHOLD = 3   # adjust as needed
ip_list = []
with open(LOG_FILE, "r") as file:
    for line in file:
        if "Failed password" in line:
            ip_match = re.search(r'from\s+([0-9a-fA-F:.]+)', line)
            if ip_match:
                ip_list.append(ip_match.group(1))
ip_count = Counter(ip_list)
for ip, count in ip_count.items():
    if count >= THRESHOLD:
        print(f"ALERT: {ip} → {count} failed login attempts")
