from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout
import socket
from threading import Thread

from handler import handler


def client():
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("192.168.1.107", 45000))
    
    session = PromptSession()
    
    handler_ = Thread(target=handler, args=(sock,))
    handler_.start()
    
    with patch_stdout():
        while True:
            
            a = session.prompt("> ")
            
            sock.send(a.encode("utf-8"))
        
        
if __name__ == "__main__":
    client()