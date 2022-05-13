import Pyro4
import os
import threading
import time
import random
import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 6666
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"


# Run : python -m Pyro4.naming first ..................... IMPORTANT to start a name server
# Run : python -m Pyro4.nsc list To see what all known registered objects in the naming server are


def updater(conn):
    while True:
        time.sleep(random.randint(0, 100))
        states = ["AVAILABLE", "UNAVAILABLE"]
        state = random.choice(states)
        print("UPDATING STATE TO ", state)
        update = "2" + state
        print("SENDING STATE")
        conn.send(update.encode(FORMAT))


@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class Fileserver2(object):
    def __init__(self):
        self.F4 = {
            "Name": "F4",
            "Path": r"C:\\Users\\HP\Desktop\\SYED Python TP2\\root\\B\\F4.txt"
        }

        self.files = [self.F4]

    def handler(self, file):
        if file == "F4":
            os.startfile(
                self.files[self.files.index(self.F4)].get("Path")
            )


def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect(ADDR)
    print(f"[CONNECTED] to [NAME SERVER] at [{IP}:{PORT}]")
    req = server.recv(SIZE).decode(FORMAT)
    if req == "auth":
        server.send("FILE SERVER".encode(FORMAT))

    print("STARTING UPDATER THREAD")
    thread = threading.Thread(target=updater, args=(server,))
    thread.start()
    print("UPDATER STARTED")

    Pyro4.Daemon.serveSimple(
        {
            Fileserver2: "example.fileservertwo22"
        },
        ns=True)


if __name__ == "__main__":
    main()
