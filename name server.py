import socket
import threading

IP = socket.gethostbyname(socket.gethostname())
PORT = 6666
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

repository = {
    'machine1': ["F2", "F3"],
    'machine2': ["F4"]
}
states = {
    'machine1': "AVAILABLE",
    'machine2': "AVAILABLE"
}


def stripper(sm):
    state = sm[1:]
    machine = sm[0]
    return machine, state


def request_handler(fn):
    keys = repository.keys()
    for key in keys:
        if fn in repository.get(key):
            return key


def handle_server(c, addr):
    print(f"[NEW FILE SERVER CONNECTION] [{addr[0]}:{addr[1]}] ")
    while True:
        msg = c.recv(SIZE).decode(FORMAT)
        m, s = stripper(msg)
        print(f"[NEW UPDATE MESSAGE] STATE: {s} | SOURCE : [{addr[0]}:{addr[1]}] | MACHINE{m}")
        target = 'machine'+m
        states.update({target: s})
        print(f"MACHINE {m}  STATE : {states.get(target)}")


def handle_client(c, addr):
    print(f"[NEW CLIENT CONNECTION] [{addr[0]}:{addr[1]}] ")

    while True:
        msg = c.recv(SIZE).decode(FORMAT)
        print(f" [RECEIVED]  REQUEST : {msg} SOURCE : [{addr[0]}:{addr[1]}] ")
        reply = request_handler(msg)
        if reply:
            if states.get(reply) == "AVAILABLE":
                c.send(reply.encode(FORMAT))
            else:
                c.send("REQUESTED SERVER IS UNAVAILABLE".encode(FORMAT))

        else:
            c.send("FILE NOT FOUND".encode(FORMAT))


    c.close()


def main():
    print("[STARTING NAME SERVER]")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] ON  [{IP}:{PORT}]")

    while True:
        conn, addr = server.accept()
        conn.send("auth".encode(FORMAT))
        auth = conn.recv(SIZE).decode(FORMAT)
        if auth == "CLIENT":
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
        elif auth == "FILE SERVER":
            thread = threading.Thread(target=handle_server, args=(conn, addr))
            thread.start()


if __name__ == "__main__":
    main()
