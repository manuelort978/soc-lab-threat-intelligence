# Setup Guide – Threat Intelligence Lab

## Requirements

* Ubuntu server
* Apache logs
* Attacker machine (Ubuntu)
* Python 3

---

## Steps

1. Create malicious IP list:
```
   nano malicious_ips.txt
```

2. Add test IPs (include the IP address of the attacker machine)

3. Run script:
```
   sudo python3 threat_intel_detector.py
```

4. Generate traffic from attacker
```
curl http://<IP_SERVer>/login
```

---

## Expected Result

Detection of malicious IP in logs
