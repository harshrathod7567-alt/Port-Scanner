import socket

def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)  # wait max 0.5 seconds per port
    result = sock.connect_ex((target, port))  # returns 0 if port is open
    sock.close()
    return result == 0

target = "127.0.0.1"  # your own computer, safe to scan
port = 80  # let's test one port first

if scan_port(target, port):
    print(f"Port {port} is OPEN")
else:
    print(f"Port {port} is CLOSED")
