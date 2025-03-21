from MySocket import TCP
from threading import Thread
from sys import argv, stderr


# this module forward a target_port from a target_ip to my_port.
# to use import the port_forward function to your code, or just run the script.
# example:
# python3 PortForward 192.168.1.5:22 0.0.0.0:8000
# this would foward 192.168.1.5:22 to your machine on port 8000  (0.0.0.0 indicate all the interfaces)
# wich mean: connecting to your machine on port 8000 will be the same as connecting to 192.168.1.5:22



def forward(socket1,socket2):
    while True:
        bytes = socket1.recv(1024)
        if bytes:
            socket2.send(bytes)


def port_forward(target_ip, target_port, my_ip = "0.0.0.0", my_port = 7070):
    linstener = TCP(ip = my_ip, port = my_port)
    

    linstener.listen(max_connections = 255)
    i = 0

    sockets = []
    while True:
        my_socket = linstener.accept()
        target_socket = TCP(ip = target_ip, port = target_port)
        target_socket.connect()
        sockets.append((my_socket,target_socket))
        Thread(target=forward, args=(sockets[i][0],sockets[i][1])).start()
        Thread(target=forward, args=(sockets[i][1],sockets[i][0])).start()
        i+=1




def printerr(string):
    stderr.write(string+"\n")

def usage(argv0):
    printerr(f"Usage: {argv[0]} target_ip:target_port my_ip:my_port\n example:\npython3 PortForward 192.168.1.5:22 0.0.0.0:8000\nthis would forward 192.168.1.5:22 to your machine on port 8000  (0.0.0.0 indicates all the interfaces)")

if __name__ == "__main__":
    if len(argv) <= 1:
        usage(argv[0])
        exit(1)

    tmp, target_ip_port, my_ip_port = argv
    target_ip, target_port = target_ip_port.split(":") # 192.168.1.1:8000 to 192.168.1.1 8000
    my_ip, my_port = my_ip_port.split(":")
    target_port, my_port = int(target_port), int(my_port)

    port_forward(target_ip, target_port, my_ip, my_port)







