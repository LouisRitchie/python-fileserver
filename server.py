import socket
import threading
import os

# Threading function
def RetrFile(name, sock):
    filename = sock.recv(1024)
    if os.path.isfile(filename):
        sock.send("EXISTS " + str(os.path.getsize(filename)))
        userResponse = sock.recv(1024)
        if userResponse[:2] == OK:
            with open(filename, 'rb') as f:
                bytesToSend = f.read(1024)
                sock.send(bytesToSend)
                while bytesToSend != '':
                    bytesToSend = f.read(1024)
                    sock.send(bytesToSend)
    else:
        sock.send("ERR")

    sock.close()

def Main():
    host = '127.0.0.1'
    port = 5000

    # defaults to TCP with no params
    s = socket.socket()
    s.bind((host, port))

    s.listen(5)

    print "Server Started."

    while True:
        c, addr = s.accept()
        print "Client connected ip:<" + str(addr) + ">"
        t = threading.Thread(target = RetrFile, args=("retrThread", c))
        t.start()

    s.close()

if __name__ == '__main__':
    Main()
