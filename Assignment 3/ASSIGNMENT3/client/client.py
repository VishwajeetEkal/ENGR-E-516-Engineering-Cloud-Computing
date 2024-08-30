import socket
import sys
from hashlib import sha256

def verify_file(file_path, expected_checksum):
    with open(file_path, 'rb') as f:
        data = f.read()
    calculated_checksum = sha256(data).hexdigest()
    return calculated_checksum == expected_checksum, calculated_checksum

def main(server_ip, server_port):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))
        
        with open('/clientdata/received_file.txt', 'wb') as f:
            data = client_socket.recv(1024)
            while data:
                f.write(data)
                data = client_socket.recv(1024)     
        received_checksum = client_socket.recv(64).decode()
        valid, calculated_checksum = verify_file('/clientdata/received_file.txt', received_checksum)
        
        if valid:
            print("File received and verified successfully.")
        else:
            print(f"File verification failed. Expected {received_checksum}, got {calculated_checksum}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        client_socket.close()
        input("Press Enter to exit...")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python client.py <server_ip> <server_port>")
        sys.exit(1)
    
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    main(server_ip, server_port)
