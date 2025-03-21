from os import system as run # for the ping command
from ipaddress import ip_network
from threading import Thread



def get_network(CIDR): # 192.168.1.0/24 to a network (an iterator of ip addresses)
    network = ip_network(CIDR, strict=False)
    return network.hosts()


def probe_single_ip(ip,count = 2,wait = 1):
    result = run(f"ping -c {str(count)} -W {str(wait)} {ip} > /dev/null 2>&1")
    return result == 0

def probe_network(CIDR) -> list:
    network = get_network(CIDR)
    active_ips = []
    threads = []

    def probe_and_store(ip):
        if probe_single_ip(ip):
            if __name__ == "__main__":
                print(ip)
            active_ips.append(ip)

    for ip in network:
        ip_str = str(ip)
        t = Thread(target=probe_and_store, args=(ip_str,))
        threads.append(t)
        t.start()
        

    for t in threads:
        try:
            t.join() # Wait for all threads to complete
        except KeyboardInterrupt:
            exit(1)
        

    active_ips.sort()
    return active_ips


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description='multi-ping utility to probe network addresses for reachable hosts'
    )
    
    parser.add_argument('ip', type=str,
                        help='Target IP address or IP range to ping (e.g. 192.168.1.0/24)')
    parser.add_argument('-c', '--count', type=int, default=2,
                        help='Number of attempts(default 2)')
    parser.add_argument('-w', '--wait', type=int, default=1,
                        help='Wait time between attamps in seconds(default 1)')

    args = parser.parse_args()

    ip = args.ip
    count = args.count
    wait = args.wait

    probe_network(ip)

