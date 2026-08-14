import socket

def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((target, port))
    sock.close()
    return result == 0

def scan_range(target, start_port, end_port):
    open_ports = []
    print(f"Scanning {target} from port {start_port} to {end_port}...")
    
    for port in range(start_port, end_port + 1):
        if scan_port(target, port):
            print(f"Port {port} is OPEN")
            open_ports.append(port)
    
    return open_ports

target = "127.0.0.1"
open_ports = scan_range(target, 1, 1024)  # scan common ports 1-1024

print("\nScan complete.")
print(f"Open ports: {open_ports}" if open_ports else "No open ports found.")
