import sys
import Pyro4.util
from client import Client
import socket


sys.excepthook = Pyro4.util.excepthook

machine1 = Pyro4.Proxy("PYRONAME:example.fileserverone11")
machine2 = Pyro4.Proxy("PYRONAME:example.fileservertwo22")

client2 = Client("mohcene")

IP = socket.gethostbyname(socket.gethostname())
PORT = 6666
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[CONNECTED] to [NAME SERVER] at [{IP}:{PORT}]")

    auth = client.recv(SIZE).decode(FORMAT)
    if auth == "auth":
        client.send("CLIENT".encode(FORMAT))

    while True:
        request = client2.treeviewer()
        if request:
            client.send(request.encode(FORMAT))
            reply = client.recv(SIZE).decode(FORMAT)
            print(f"NAME SERVER> REPLY : {reply}")
            if reply == "machine1":
                print(f"[FILE FOUND] FILE : {request} | LOCATION : {reply}")
                print(f"REACHING... {reply}")
                client2.call(machine1, request)
            elif reply == "machine2":
                print(f"[FILE FOUND] FILE : {request} | LOCATION : {reply}")
                print(f"REACHING... {reply}")
                client2.call(machine2, request)
        else:
            print("[ERROR] PLEASE SELECT A FILE TO OPEN")
            continue


if __name__ == "__main__":
    main()
