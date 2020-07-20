import argparse
import socket

def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('target_address', help='target address')
    parser.add_argument('port', help='port', nargs='?')
    parser.add_argument('message', help='message', nargs='?')
    args = parser.parse_args()

    # socket.AF_INET -> ipv4 のソケット
    # SOCK_STREAM -> TCP
    # SOCK_DGRAM -> UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_IF, socket.inet_aton("0.0.0.0"))
    s.sendto(args.message.encode('utf-8'), (args.target_address, int(args.port)))
    s.settimeout(0.2)
    s.close()

    return None

if __name__ == "__main__":
    main()

