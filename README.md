# Assignment 1

  
name: Yunjie Zhang 

number: 20872676 

id: y3446zha


## How to run my code:

- Run server: python Server.py n_port req_code

- Run client: python Client.py server_address n_port req_code message

n_port: a fixed port for setting up TCP connection. (Integer)

req_code: a code that the client sends to server to verify identity. (Integer)

server_address: the address of the server where Server.py is running on. (String)

message: the data client sends to server for being inversed. (String)



## How did I test my:

- My Server.py runs at y3446zha@ubuntu2004-002

- My Client.py runs at y3446zha@ubuntu2004-004

  

### Example Excecution:

- For server: y3446zha@ubuntu2004-002:~/cs436/A1$ python Server.py 12001 20306

- For client: y3446zha@ubuntu2004-004:~/cs436/A1$ python Client.py ubuntu2004-002.student.cs.uwaterloo.ca 12001 20306 'A man, a plan, a canal - Panama!'

  

## version:

Python 2 && Python 3 should both work