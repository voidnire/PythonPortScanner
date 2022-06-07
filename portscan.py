import socket

ports = [21, 23, 80, 443, 8080, 4040, 4444]

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.1)
    code = sock.connect_ex(('DOMAINORIP',port))
    if code == 0:
        print(port, "IS OPEN")
