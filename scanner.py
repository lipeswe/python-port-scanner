import socket
import argparse
import time
import threading
from queue import Queue

# parse command-line arguments
parser = argparse.ArgumentParser(description="Simple Python Port Scanner with Multithreading")
parser.add_argument("target", help="Target IP or hostname")
parser.add_argument("-p", "--ports", default="1-1024", help="Port range (default: 1-1024)")

args = parser.parse_args()

target = args.target
port_range = args.ports.split("-")
start_port = int(port_range[0])
end_port = int(port_range[1])

print(f"\nScanning target: {target}")
print(f"Port range: {start_port}-{end_port}\n")

# resolve hostname to IP
try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Hostname could not be resolved.")
    exit()

# queue to store ports
port_queue = Queue()

# lock to avoid messy terminal output
print_lock = threading.Lock()

# function executed by each thread
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

# fill the queue with ports
for port in range(start_port, end_port + 1):
    port_queue.put(port)

start_time = time.time()

# create and start threads
threads = []
for _ in range(50):
    thread = threading.Thread(target=scan_port)
    thread.start()
    threads.append(thread)

# wait until all ports are scanned
port_queue.join()

end_time = time.time()

print(f"\nScan completed in {round(end_time - start_time, 2)} seconds")