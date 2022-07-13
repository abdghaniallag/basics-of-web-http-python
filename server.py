from socket import *


def creatserver():
    serversocket = socket(AF_INET, SOCK_STREAM)
    try:
        serversocket.bind(("localhost", 9558))
        serversocket.listen(5)

        while True:
            (clientside, address) = serversocket.accept()
            print(address)
            reciveddata = clientside.recv(5000).decode()
            pieces = reciveddata.split("\n")
            if len(pieces) > 0 : print(pieces[0])

            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type : text/html ; charset:utf-8\r\n\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"
            clientside.sendall(data.encode())
            clientside.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print("\nShutting down\n")
    except Exception as exeption:
        print("\nError\n")
        print(exeption)

    serversocket.close()


print("running ........")
creatserver()
