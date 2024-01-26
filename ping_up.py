import ipaddress
import concurrent.futures
import subprocess

def check_ip(ip):
    result = subprocess.run(['ping', '-c', '1', '-W', '1', str(ip)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if result.returncode == 0:
        print(f"{ip} is up")

network = ipaddress.ip_network('IP_RANGE', strict=False)   #change the IP_RANGE for the actual range of ip that you want to scan

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(check_ip, network.hosts())
