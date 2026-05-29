import sys
try:
    from scapy.all import sniff, IP, TCP, UDP
except ImportError:
    print("Error: scapy library is required. Install it using 'pip install scapy'")
    sys.exit(1)

def packet_callback(packet):
    # Check if the packet has an IP layer
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        proto = ip_layer.proto
        
        # Determine protocol type
        protocol_name = "Other"
        if packet.haslayer(TCP):
            protocol_name = "TCP"
        elif packet.haslayer(UDP):
            protocol_name = "UDP"
        elif proto == 1:
            protocol_name = "ICMP"
            
        print(f"[+] Packet: {src_ip} --> {dst_ip} | Protocol: {protocol_name} | Length: {len(packet)} bytes")

def start_sniffing():
    print("-" * 60)
    print("[-] Starting Network Packet Sniffer... (Press Ctrl+C to stop)")
    print("[-] Monitoring real-time network traffic...")
    print("-" * 60)
    
    # Sniff traffic (requires root/administrator privileges in Linux Kali)
    try:
        sniff(prn=packet_callback, store=False)
    except PermissionError:
        print("[!] Error: Root privileges required. Run this script using 'sudo'.")
    except KeyboardInterrupt:
        print("\n[-] Sniffing stopped by user. Exiting.")

if __name__ == "__main__":
    start_sniffing()
