import time

LOG_FILE = "/var/log/apache2/access.log"
IP_FILE = "malicious_ips.txt"

def load_ips():
    with open(IP_FILE, "r") as f:
        return [line.strip() for line in f]

def follow(file):
    file.seek(0, 2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.5)
            continue
        yield line

def analyze():
    malicious_ips = load_ips()

    with open(LOG_FILE, "r") as f:
        loglines = follow(f)

        print(" Monitoring for malicious IPs...\n")

        for line in loglines:
            for ip in malicious_ips:
                if ip in line:
                    print("\n Malicious IP detected!")
                    print(f"IP: {ip}")
                    print(f"Log: {line}")

if __name__ == "__main__":
    analyze()
