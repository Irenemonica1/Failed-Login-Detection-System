# Failed Login Detection System (SOC Project)
## Objective
Detect brute-force SSH login attempts by analyzing Linux authentication logs and generating alerts based on failed login thresholds.
## Tools & Technologies
- Python 3
- Linux (Kali)
- SSH
- Authentication logs (auth.log)
## How It Works
1. Parses authentication logs
2. Identifies failed SSH login attempts
3. Extracts source IP addresses (IPv4 & IPv6)
4. Counts failed attempts per IP
5. Generates alert when threshold is exceeded
## How to Run
```bash
sudo python3 detect_failed_logins.py
