import sys
import socket


if len(sys.argv) not in [2, 3]:
    print('Too Many Or Not Enough Arguments Error')
    sys.exit(1)

if len(sys.argv) == 2:
    port_num = 80
else:
    try:
        port_num = int(sys.argv[2])
    except TypeError:
        print('Port Number type error')
    if not 0 < int(port_num) < 65535:
        print('Invalid Port Number Error')
        sys.exit(2)

server_addr = sys.argv[1]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5)
try:
    sock.connect((server_addr, port_num))
except socket.gaierror:
    print('Connection Error')
    sys.exit(3)
except socket.timeout:
    print('TimeOut Error')
    sys.exit(4)
  

sock.send(
    b"HEAD / HTTP/1.1\r\nHost: " +
    bytes(server_addr, "utf8") +
    b"\r\nConnection: close\r\n\r\n"
    )
reply = sock.recv(10000)
sock.shutdown(socket.SHUT_RDWR)
sock.close()
print(f'Server: {server_addr} is live!')



