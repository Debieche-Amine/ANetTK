# ANetTK --- Amine Network Tool Kit

# Description
These custom network tools are my own creation, designed only for Linux. They’re more of a fun project—for serious work, use real tools instead!
more tools will be added soon..

# Version

ANetTK 1.1

# installation

```bash
git clone https://github.com/Debieche-Amine/ANetTK.git
cd ANetTK
```

# Tools

## 1- PortForward

### Description

Forwards a remote port to a local port on your machine, Tested on http,ssh --- Text me if you find a case that doesnt work

### how to use
```bash
python PortForward.py target_ip:target_port my_ip:my_port
```
**example:**
```bash
python PortForward.py 192.168.1.5:22 0.0.0.0:8000
```
this would forward 192.168.1.5:22 to your machine on port 8000 (0.0.0.0 indicates all the interfaces)

**or**
```python
from PortForward import port_forward

target_ip = "192.168.1.1"
target_port = 22
my_ip = "0.0.0.0"
my_port = 7070
port_forward(target_ip, target_port, my_ip, my_port)
```

  ## 2- IPProbe
  ### Description
ping multiple IPs to get reachable hosts
### how to use
```bash
python IPProbe.py [-c COUNT] [-w WAIT] ip
```

**example:**
```bash
python IPProbe.py 192.168.1.0/24
```
this will ping hosts starting from 192.168.1.1 to 192.168.1.254
output example: ( writes to stdout )
```bash
192.168.1.1
192.168.1.3
192.168.1.4
```
**or**
```python
from IPProbe  import  probe_network

CIDR  = "192.168.43.0/24"
active_ips = probe_network(CIDR) #doesnt write to stdout
for ip in active_ips:
print(ip)
```

# Core modules

## 1- MySocket

### Description
A python module that simplifies dealing with sockets
### how to use

```python
from MySocket import TCP
```

**structure**

```python
class  TCP:
	def __init__(self, ip = "0.0.0.0", port = 7070, verbose = VERBOSE, reuse = REUSE)
		self.socket # the socket from socket module
		self.ip # default 0.0.0.0
		self.port # default 7070
		self.type # autoselected, values:("server", "client", None)
		self.verbose # default True, writes to stderr, if False: write nothing
	def listen(self, ip = None, port = None,max_connections = 1, verbose = True)
	def accept(self) -> "TCP"
	def connect(self,ip = None, port = None) ->  int
	def send(self, bytes)
	def recv(self,n_bytes) ->  bytes
	def close(self)
```
