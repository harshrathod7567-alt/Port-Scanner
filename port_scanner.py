import socket
import time

def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((target, port))
    sock.close()
    return result == 0

def scan_range(target, start_port, end_port):
    open_ports = []
    print(f"Scanning {target} from port {start_port} to {end_port}...")
    start_time = time.time()
    
    for port in range(start_port, end_port + 1):
        if scan_port(target, port):
            print(f"Port {port} is OPEN")
            open_ports.append(port)
    
    elapsed = time.time() - start_time
    print(f"\nScan finished in {elapsed:.2f} seconds")
    return open_ports

def write_report(target, open_ports, output_file="scan_report.txt"):
    with open(output_file, 'w') as f:
        f.write(f"=== Port Scan Report for {target} ===\n\n")
        if open_ports:
            f.write("Open ports found:\n")
            for port in open_ports:
                f.write(f"  Port {port}: OPEN\n")
        else:
            f.write("No open ports found.\n")
    print(f"Report saved to {output_file}")

target = "127.0.0.1"
open_ports = scan_range(target, 1, 1024)
write_report(target, open_ports)
