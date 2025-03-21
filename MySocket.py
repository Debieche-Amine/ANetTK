import socket
from sys import stderr


# this is a module that provide you with the TCP class, wich is a simplified way to interact with sokcets (tcp ipv4 only)
# to use just import the TCP class from the module..


# the module writes only to stderr
VERBOSE = True  #set verbose to False if you dont wants any writes to stderr
REUSE = True

def printerr(string,verbose = True):
    if verbose:
        stderr.write(string+"\n")


class TCP:
    def __init__(self, ip = "0.0.0.0", port = 7070, verbose = VERBOSE, reuse = REUSE):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = ip
        self.port = port
        self.verbose = verbose
        self.type = None # "server", "client", None
        if REUSE:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


    def listen(self, ip = None, port = None,max_connections = 1, verbose = True):
        if port:
            self.port = port
        else:
            port = self.port
        if ip:
            self.ip = ip
        else:
            ip = self.ip
        port = port if port else self.port  # setting defualt values to ip and port if not given
        ip = ip if ip else self.ip
        self.type = "server"
        self.socket.bind((ip, port))
        self.socket.listen(max_connections)
        printerr(f"Server listening on port {port}...", self.verbose)
        return 0


    def accept(self) -> "TCP":
        s,addr = self.socket.accept()
        sock = TCP(ip = addr[0], port = addr[1])
        sock.type = "client"
        sock.socket = s
        printerr(f"connected from {addr}",self.verbose)
        return sock



    def connect(self,ip = None, port = None):
        if port:
            self.port = port
        else:
            port = self.port
        if ip:
            self.ip = ip
        else:
            ip = self.ip
        self.socket.connect((ip, port))
        self.type = "client"

    def send(self, bytes):
        self.socket.send(bytes)
    def recv(self,n_bytes) -> bytes:
        return self.socket.recv(n_bytes)
    def close(self):
        self.socket.close()








