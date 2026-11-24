# 089 · Networking: Sockets, HTTP and urllib — Example 3: URL parsing and UDP
# Run: python example_3.py

from urllib.parse import urlparse, parse_qs, urlencode, quote
import socket

url = "https://shop.example.com:8443/search?q=python+book&page=2#results"
p = urlparse(url)
print(p.scheme, p.hostname, p.port, p.path, parse_qs(p.query), p.fragment)
print("build:", "https://api.site.com/items?" + urlencode({"q": "नमस्ते", "limit": 10}))
print("quote:", quote("file name.pdf"))

receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver.bind(("127.0.0.1", 0))
sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sender.sendto(b"udp packet!", receiver.getsockname())
data, addr = receiver.recvfrom(1024)
print("UDP received:", data, "from", addr[0])
sender.close(); receiver.close()
