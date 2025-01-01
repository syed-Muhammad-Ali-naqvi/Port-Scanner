import socket

def scan(target, ports):
	print("\nStarting scanning for " + str(target))
	for port in range(1, ports + 1):
		scan_ports(target, port)
	print(f"\n[*] Scan completed for {target}. Scanned {ports} ports.")


def  scan_ports(ip_address, port):
	try:
		sock = socket.socket()
		sock.settimeout(0.5)
		sock.connect((ip_address, port))
		print("[+] Port opened  " + str(port))
	except:
		# print("[-] Port closed " + str(port))
		pass

def validate_ports(input_ports):
	if 1 <= input_ports <= 65535:
		return input_ports
	else:
		raise ValueError("Please enter a valid port range (1–65535).")

targets = input("[*] Scan targets to Scans(Separated by comma): ")
ports = validate_ports(int(input("[*] Enter number of ports you want to scan (1 - 65535): ")))



if ',' in targets:
	print("[*] Scanning multiple ports:")
	print("\nScanning might take a few seconds if the port range is large.")
	for ip_addr in targets.split(","):
		scan(ip_addr.strip(" "), ports)
else:
	scan(targets.strip(" "), ports)
