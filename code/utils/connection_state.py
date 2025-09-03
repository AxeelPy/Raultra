import socket
import multiprocessing as mp

class ConnectionState:
    
    @property
    def isConnected(self):
        if not self.connection:
            return False
        return True
    
    def __init__(self):
        
        self.connection: socket.socket | None
        self.sink = mp.Queue()