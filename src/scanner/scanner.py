import os
import socket
import sys
import pyfiglet

version = "1.0.0"

class wires():
    def __main__():
        host = sys.argv[1]
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        for port in range(1, 65501):
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"{port} is opened")
            else:
                pass
    def __scan__():
        print(pyfiglet.figlet_format("Wires"))
        print("[*] {Version 1.0.0}")
        wires.__main__()

if __name__ == "__main__":
    wires.__scan__()
