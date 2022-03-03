import socket
import sys

# tcpGetRPort(server_address, n_port, req_code) takes a string and two integers as input, and
#   creates a TCP socket for the server, and recieves a string as the r_port for later UDP use.
# 
# n_port: a fixed port for setting up TCP connection. (Integer)
# req_code: a code that the client sends to server to verify identity. (Integer)
# server_address: the address of the server where Server.py is running on. (String)
def tcpGetRPort(server_address, n_port, req_code):
    # create TCP socket for server
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((server_address, n_port))

    # send req_code for identification
    clientSocket.send(req_code.encode())

    # get back with a random port number <r_port> where
    # it will be listening for the actual request
    r_port = clientSocket.recv(1024).decode()

    # check if r_port exists and can be changed to integer
    try:
        ran_port = int(r_port)
    except:
        print("Incorrect <req_code>, please make sure you have entered the right req_code.")
        return -1
    else:
        # closes the TCP connection with the server after recieving the r_port
        clientSocket.close()
        return ran_port

# udpHandleMessageInput(server_address, r_port, message) takes two integers and a string as input,
#   creates a UDP socket for the server, sends the message to it and gets back a reverse message
# 
# server_address: the address of the server where Server.py is running on. (String)
# r_port: is the real port for UDP socket. (Integer)
# message: the data client sends to server for being inversed. (String)
def udpHandleMessageInput(server_address, r_port, message):
    # create a UDP socket for server
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #send into socket with server name, port, and message
    clientSocket.sendto(message.encode(), (server_address, r_port))
    
    # read reply characters from socket into string, and save to modifiedMessage
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    
    print(modifiedMessage)

    clientSocket.close()

def main():
    try:
        # checks if the both n_port and req_code are both integers and there's at least four command line arguments
        server_address = sys.argv[1]
        n_port = int(sys.argv[2])
        req_code = int(sys.argv[3])
        message = sys.argv[4]
    except:
        # if not give detailed instruction on how to run Client.py
        print("Run Client: python Client.py <server_address> <n_port> <req_code> <message>\n")
        print("Where <server_address> & <message> should be Strings, and <n_port> & <req_code> be Integers.")
    else:
        # get r_port from Server
        r_port = tcpGetRPort(server_address, n_port, str(req_code))

        # check if r_port exists
        if r_port != -1:
            udpHandleMessageInput(server_address, r_port, message)

if __name__ == "__main__":
    main()