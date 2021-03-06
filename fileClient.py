import socket

def Main():
    # We could easily grab the host and the port from the command line.
    host = "127.0.0.1"
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    filename = raw_input("Filename? -> ")
    if filename != "q":
        s.send(filename)
        data = s.recv(1024)
        if data[:6] == "EXISTS":
            filesize = long(data[6:])
            message = raw_input("File Exists, " + str(filesize) + \
                    " bytes, download? (Y,N)? -> ")
            if message == "Y":
                s.send("OK")
                # 'wb' param is write binary
                f.open("new_" + filename, 'wb')
                data = s.recv(1024)
                totalRecv = len(data)
                f.write(data)
                while totalRecv < fileSize:
                    data = s.recv(1024)
                    totalRecv += len(data)
                    f.write(data)
                    print "{0:.2f}".format((totalRecv/float(filesize))*100)+\
                            "% Done"
                    print "Download Complete!"
        else:
            print "File does not exist!"
    s.close()

if __name__ == '__main__':
    Main()
