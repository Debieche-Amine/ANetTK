# ANetTK --- Amine Network Tool Kit
# Description

A collection of custom made network tools, more tools will be added soon.

# Version
ANetTK 1.0.1
# installation
```bash
git clone https://github.com/Debieche-Amine/ANetTK.git
cd ANetTK
```
# Tools
## 1- PortForward
### Description
Forwards a remote port to a local port on your machine

### how to use
```bash
python PortForward.py target_ip:target_port my_ip:my_port
```
 example:
 ```bash
python PortForward 192.168.1.5:22 0.0.0.0:8000
```
this would forward 192.168.1.5:22 to your machine on port 8000  (0.0.0.0 indicates all the interfaces)

tested on ssh, text me if you find a case that doesnt work

# Core modules
## 1- MySocket

### Description
A python module that simplifies dealing with sockets
### how to use
```python
from MySocket import TCP
```
structure
```python
class TCP:
	def __init__(self, ip = "0.0.0.0", port = 7070, verbose = VERBOSE, reuse = REUSE)
		self.socket # the socket from socket module
        self.ip # default 0.0.0.0
        self.port # default 7070
        self.type # autoselected, values:("server", "client", None) 
        self.verbose # default True, writes to stderr, if False: write nothing
        
	def listen(self, ip = None, port = None,max_connections = 1, verbose = True)
	def accept(self) -> "TCP"
	def connect(self,ip = None, port = None)
	def send(self, bytes)
	def recv(self,n_bytes) -> bytes
	def close(self)
```

