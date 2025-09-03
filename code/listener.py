import socket


def listener() -> socket.socket:
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("192.168.1.107", 45000))
    server.listen(5)
    
    while True:
        
        conn, addr = server.accept()

        return conn