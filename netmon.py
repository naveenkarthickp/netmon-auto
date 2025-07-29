import yaml
from pythonping import ping
import pandas as pd
import time
import os

# Load config
with open('config.yaml') as f:
    config = yaml.safe_load(f)

os.makedirs('data', exist_ok=True)

def ping_device(ip):
    ping_res = ping(ip, count=2, timeout=1)
    return ping_res.rtt_avg_ms

def log_result(device, latency):
    log_file = 'data/sample_log.csv'
    row = {'time': pd.Timestamp.now(), 'device': device['name'], 'ip': device['ip'], 'latency': latency}
    if not os.path.exists(log_file):
        pd.DataFrame([row]).to_csv(log_file, index=False)
    else:
        pd.read_csv(log_file).append(row, ignore_index=True).to_csv(log_file, index=False)

for device in config['devices']:
    latency = ping_device(device['ip'])
    print(f"{device['name']} ({device['ip']}): {latency:.2f} ms")
    log_result(device, latency)
    if latency > config['thresholds']['ping_latency']:
        print(f"ALERT: {device['name']} has high latency [{latency:.2f} ms]")
        # Optionally: from alert import send_email_alert; send_email_alert(...)

# Will call report.py daily to generate reports
