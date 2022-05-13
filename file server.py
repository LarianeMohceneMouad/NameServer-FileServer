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
        update = "1" + state
        print("SENDING STATE")
        conn.send(update.encode(FORMAT))


@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class Fileserver(object):
    def __init__(self):
        self.F3 = {
            "Name": "F3",
            "Path": r"C:\\Users\\HP\Desktop\\SYED Python TP2\\root\\A\\F3.txt"
        }

        self.F2 = {
            "Name": "F3",
            "Path": r"C:\\Users\\HP\Desktop\\SYED Python TP2\\root\\A\\F2.txt"
        }

        self.files = [self.F3, self.F2]

    def handler(self, file):
        print(f"[FILE SERVER 1] DISTANCE OPENING FILE : {file}")
        if file == "F3":
            os.startfile(
                    self.files[self.files.index(self.F3)].get("Path")
                )
        elif file == "F2":
            os.startfile(
                    self.files[self.files.index(self.F2)].get("Path")
                )


def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect(ADDR)
    print(f"[CONNECTED] to [NAME SERVER] at [{IP}:{PORT}]")
    req = server.recv(SIZE).decode(FORMAT)
    if req == "auth":
        server.send("FILE SERVER".encode(FORMAT))

    print("STARTING UPDATER THREAD")
    updater_thread = threading.Thread(target=updater, args=(server,))
    updater_thread.start()
    print("UPDATER STARTED")

    Pyro4.Daemon.serveSimple(
        {
            Fileserver: "example.fileserverone11"
        },
        ns=True)


if __name__ == "__main__":
    main()
