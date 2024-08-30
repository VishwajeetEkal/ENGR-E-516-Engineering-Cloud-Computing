import socket
import os
from hashlib import sha256

def generate_file(path, size=1024):
    random_data = os.urandom(size)
    with open(path, 'wb') as file:
        file.write(random_data)
    return sha256(random_data).hexdigest()

def main(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(1)
    print(f"Server listening on port {port}")
    while True:
        client_socket, client_addr = server_socket.accept()
        print(f"Connection from {client_addr}")
        checksum = generate_file('/serverdata/file.txt')
        with open('/serverdata/file.txt', 'rb') as file:
            client_socket.sendall(file.read())
            client_socket.sendall(checksum.encode())
        client_socket.close()

if __name__ == '__main__':
    import sys
    port = int(sys.argv[1])
    main(port)
