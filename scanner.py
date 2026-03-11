import socket
import argparse
import time

# configurar argumentos de linha de comando
parser = argparse.ArgumentParser(description="Simple Python Port Scanner")
parser.add_argument("target", help="Target IP or hostname")
parser.add_argument("-p", "--ports", default="1-1024", help="Port range (default: 1-1024)")

args = parser.parse_args()

target = args.target
port_range = args.ports.split("-")
start_port = int(port_range[0])
end_port = int(port_range[1])

print(f"\nScanning target: {target}")
print(f"Port range: {start_port}-{end_port}\n")

start_time = time.time()

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Hostname could not be resolved.")
    exit()

for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target_ip, port))

    if result == 0:
        print(f"[OPEN] Port {port}")

    s.close()

end_time = time.time()

print(f"\nScan completed in {round(end_time - start_time, 2)} seconds")