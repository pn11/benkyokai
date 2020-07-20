import argparse
import socket

def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('target_address', help='target address')
    parser.add_argument('port', help='port', nargs='?')
    args = parser.parse_args()

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', int(args.port)))
    s.setsockopt(socket.IPPROTO_IP,
                socket.IP_ADD_MEMBERSHIP,
                socket.inet_aton(args.target_address) + socket.inet_aton("0.0.0.0"))

    while True:
        print(s.recvfrom(1500))

    return None


if __name__ == "__main__":
    main()
