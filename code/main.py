from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout
from threading import Thread
from handler import handler
from listener import listener


if __name__ == "__main__":
    
    socket = listener()
    
    session = PromptSession()
    
    handler_ = Thread(target=handler, args=(socket,))
    handler_.start()
    
    while True:
        
        a = session.prompt("> ")
        
        socket.send(a.encode("utf-8"))