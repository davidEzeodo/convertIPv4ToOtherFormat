# In this program, the two IP addresses have (inbound_range and outbound_range) been converted from a string
# to a 32-bit packed format using a for-in statement.
# Additionally, the Python hexlify function is called from the binascii module.
# This helps to represent the binary data in a hexadecimal format.

import socket
from binascii import hexlify


def convert_ipv4_address():
    inbound_range_ip = '127.0.0.1'
    outbound_range_ip = '192.168.0.1'
    for ip_addr in [inbound_range_ip, outbound_range_ip]:
        packed_ip_addr = socket.inet_aton(ip_addr)
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
        print("IP Address: %s => Packed: %s,\nUnpacked: %s" % (ip_addr, hexlify(packed_ip_addr), unpacked_ip_addr))


if __name__ == "__main__":
    convert_ipv4_address()
