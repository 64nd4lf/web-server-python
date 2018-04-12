#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket

serverSocket.bind(('', 1618))
serverSocket.listen(1)

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()        
    try:
        message =  connectionSocket.recv(1024)              
        filename = message.split()[1]                 
        f = open(filename[1:])                        
        outputdata = f.read()
        #Send one HTTP header line into socket
        
        connectionSocket.send('HTTP/1.1 200 OK \r\n\r\n')
                      
        
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):           
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        
        print 'Error 404. Page not found'
        connectionSocket.send('HTTP/1.1 404 Not Found \r\n\r\n') 
        connectionSocket.send('404 Not Found')
        

        #Close client socket
        connectionSocket.close()  
    
    #Close connection when control-c is pressed on terminal
    except KeyboardInterrupt:
        connectionSocket.close()
        serverSocket.close()          

serverSocket.close()