import socket
import sys

# getRandomPort() gets a random free port, an integer, for UDP socket
def getRandomPort():
    rSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    rSock.bind(("", 0))
    _, r_port = rSock.getsockname()
    rSock.close()

    return r_port

# tcpRespondRPort(n_port, req_code) takes two integer inputs n_port and req_code, create
#   a TCP socket for server and verifies the client with req_code.
# 
# n_port: a fixed port for setting up TCP connection. (Integer)
# req_code: a code that the client sends to server to verify identity. (Integer)
def tcpRespondRPort(n_port, req_code):
    try: 
        # create TCP welcoming socket
        serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSock.bind(("", n_port))
    except:
        print("Address in use, please change to another port")
    else:
        # server begins listening for incoming TCP requests
        serverSock.listen(1)
        print("TCP up")

        try:
            while True:
                print("TCP cycle starts")
                # server waits on accept() for incoming requests, new socket created on return
                connectionSocket, addr = serverSock.accept()

                # getting the req_code send from client (read bytes from socket)
                k_req_code = connectionSocket.recv(1024).decode()

                # check the identity
                if k_req_code == req_code:
                    # getting a random free port number
                    r_port = getRandomPort()

                    # server now sends the r_port back to the client
                    connectionSocket.send(str(r_port).encode())

                    # connectionSocket.close()

                    # start the UDP process for reverse a message
                    updInverseMessage(r_port)
                else:
                    # client fails to send the intended <req_code>, 
                    # the server closes the TCP connection
                    connectionSocket.close()
                    print("TCP closed")
                print("TCP cycle ends")
        except KeyboardInterrupt:
            print("\n...exiting program...")

# updInverseMessage(r_port) takes an interger r_port as input, creates a UDP socket, 
#   and reverts the message the client sent to the server and sent the reverted message back.
def updInverseMessage(r_port):
    # create UDP socket
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # bind socket to port number
    serverSocket.bind(("", int(r_port)))
    print("UDP ready")

    print("UDP cycle starts")
    message, clientAddress = serverSocket.recvfrom(2048)
    
    # after recieving the message, reverse it
    modifiedMessage = message[::-1]

    # send back to the client
    serverSocket.sendto(modifiedMessage, clientAddress)
    print("UDP cycle ends")

def main():
    try:
        # checks if the both n_port and req_code are both integers. and there's at least 2 command line arguments
        n_port = int(sys.argv[1])
        req_code = int(sys.argv[2])
    except:
        # if not give detailed instruction on how to run Server.py
        print("Run Server: python Server.py <n_port> <req_code>")
        print("Where both <n_port> & <req_code> should be Integers.")
    else:
        tcpRespondRPort(n_port, str(req_code))

if __name__ == "__main__":
    main()