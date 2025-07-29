import yaml, pandas as pd, time
from pythonping import ping
from pysnmp.hlapi import *
import yagmail, requests

with open('config.yaml') as f:
    config = yaml.safe_load(f)

def ping_device(ip):
    resp = ping(ip, count=4, timeout=1)
    return resp.rtt_avg_ms

def log_result(device, latency):
    # simple CSV log for demo
    with open('data/sample_log.csv','a') as f:
        f.write(f"{time.time()},{device['ip']},{latency}\n")

for device in config['devices']:
    if device['monitor']:
        latency = ping_device(device['ip'])
        log_result(device, latency)
        if latency > config['thresholds']['ping_latency']:
            print(f"ALERT: High latency on {device['name']} [{latency:.2f} ms]")
# Add SNMP polling & alert integration below, plus reporting
