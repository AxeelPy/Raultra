import socket
import time


def handler(sock: socket.socket):
    
    while True:
    
        data_b = sock.recv(1024)
        
        data = data_b.decode('utf-8')
        
        if not data:
            time.sleep(1)
            continue
        
        print(f"Data: {data}")