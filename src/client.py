import socket
import sys
from colorama import init
init()
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        host = str(input("What IP Is Hosting Spice.Net? : \u001b[36m"))
        port = 1337

        s.connect((host, port))
        print("""\u001b[35m
      █████████             ███                       ██████   █████           █████
     ███░░░░░███           ░░░                       ░░██████ ░░███           ░░███
    ░███    ░░░  ████████  ████   ██████   ██████     ░███░███ ░███   ██████  ███████
    ░░█████████ ░░███░░███░░███  ███░░███ ███░░███    ░███░░███░███  ███░░███░░░███░
     ░░░░░░░░███ ░███ ░███ ░███ ░███ ░░░ ░███████     ░███ ░░██████ ░███████   ░███
     ███    ░███ ░███ ░███ ░███ ░███  ███░███░░░      ░███  ░░█████ ░███░░░    ░███ ███
    ░░█████████  ░███████  █████░░██████ ░░██████  ██ █████  ░░█████░░██████   ░░█████
     ░░░░░░░░░   ░███░░░  ░░░░░  ░░░░░░   ░░░░░░  ░░ ░░░░░    ░░░░░  ░░░░░░     ░░░░░
                 ░███
                 █████
                ░░░░░
    --------------------- Version 1.0 --------- Created By @SpiceSouls -----------------\n\u001b[0m""")
        while True:
            message = input(f"\u001b[36m{host}\u001b[0m@spice.net-+> ")
            if message == "disconnect":
                break
            s.sendall(bytes(message, "utf-8"))
            print(str(s.recv(4096), "utf-8"))
except ConnectionResetError:
    print('[-] Connection Closed By Server.')
except KeyboardInterrupt:
    quit()
