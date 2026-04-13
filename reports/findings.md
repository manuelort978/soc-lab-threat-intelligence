# Findings – Threat Intelligence Lab

## Summary
Malicious IP detection was successfully implemented by comparing log entries with a predefined threat intelligence list (malicious_ips.txt).

## Observations
- Traffic from a flagged IP was detected
- Real-time alerting worked correctly

## Analysis
This approach simulates how SOC teams correlate logs with threat intelligence feeds.

## Recommendations
- Integrate external threat feeds
- Automate response actions
- Enrich alerts with geolocation data
