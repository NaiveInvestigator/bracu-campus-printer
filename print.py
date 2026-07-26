import socket
import sys
import os

if len(sys.argv) < 2:
    print(f"Usage: python3 {sys.argv[0]} file.pdf")
    sys.exit(1)

job_name = os.path.basename(sys.argv[1])

HOST = "172.16.0.111"
PORT = 515
username = "YOUR_STUDENT_ID"
hostname = "CSE-09F-25L-L12"

control = (
    f"H{hostname}\n"
    f"P{username}\n"
    f"J{job_name}\n"
    f"ldfA002{hostname}\n"
    f"UdfA002{hostname}\n"
    f"N{job_name}\n"
).encode()

pdf = open(sys.argv[1], "rb").read()

s = socket.create_connection((HOST, PORT))

# Receive print job
s.sendall(b"\x02secure\n")
s.recv(1)

# Send control file
s.sendall(
    f"\x02{len(control)} cfA002{hostname}\n".encode()
)
s.recv(1)

s.sendall(control + b"\x00")
s.recv(1)

# Send data/PDF file
s.sendall(
    f"\x03{len(pdf)} dfA002{hostname}\n".encode()
)
s.recv(1)

s.sendall(pdf + b"\x00")
s.recv(1)

s.close()
