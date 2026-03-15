import socket
import argparse
import time
import threading
from queue import Queue

# Argument parser
parser = argparse.ArgumentParser(description="Multithreaded TCP Port Scanner")

parser.add_argument("target", help="Target IP or hostname")
parser.add_argument("-p", "--ports", default="1-1024", help="Port range (example: 20-80)")
parser.add_argument("-t", "--threads", type=int, default=50, help="Number of threads (default: 50)")

args = parser.parse_args()

target = args.target
thread_count = args.threads

# Parse port range
try:
    start_port, end_port = map(int, args.ports.split("-"))
except ValueError:
    print("Invalid port range format. Use something like 20-80.")
    exit()

# Resolve hostname
try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Hostname could not be resolved.")
    exit()

print(f"\nScanning target: {target} ({target_ip})")
print(f"Port range: {start_port}-{end_port}")
print(f"Threads: {thread_count}\n")

# Queue and threading setup
port_queue = Queue()
print_lock = threading.Lock()

def scan_port():
    while not port_queue.empty():
        port = port_queue.get()

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((target_ip, port))

        if result == 0:
            with print_lock:
                print(f"[OPEN] Port {port}")

        s.close()
        port_queue.task_done()

# Fill queue
for port in range(start_port, end_port + 1):
    port_queue.put(port)

start_time = time.time()

# Create threads
threads = []
for _ in range(thread_count):
    thread = threading.Thread(target=scan_port)
    thread.start()
    threads.append(thread)

# Wait for completion
port_queue.join()

end_time = time.time()

print(f"\nScan completed in {round(end_time - start_time, 2)} seconds")