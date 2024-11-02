import socket
import sys 
import os

# Create a TCP server socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Prepare the server socket
# FillInStart
serverPort = 8080  # Choose the desired port (use a higher port if permission issues occur with 80)
serverSocket.bind(('', serverPort))  # Bind the socket to the server port
serverSocket.listen(1)  # Listen for incoming connections
print('The web server is up on port:', serverPort)
# FillInEnd

while True:    
    print('Ready to serve...') 
    # Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept()

    try: 
        # Receive the request message from the client
        # FillInStart
        message = connectionSocket.recv(1024).decode()
        # FillInEnd 
        
        # Extract the path of the requested object from the message
        # The path is the second part of HTTP header, identified by [1]
        filename = message.split()[1]
        # Because the extracted path of the HTTP request includes 
        # a character '/', we read the path from the second character 
        f = open(filename[1:])     
        # Store the entire content of the requested file in a buffer
        outputdata = f.read()
        
        # Send the HTTP response header line to the connection socket
        # FillInStart       
        connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())
        connectionSocket.send('Content-Type: text/html\r\n\r\n'.encode())
        # FillInEnd

        # Send the content of the requested file to the client 
        connectionSocket.send(outputdata.encode())
        
        # Close client socket 
        connectionSocket.close() 
    
    except IOError:
        # Send HTTP response message for file not found
        # FillInStart
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n'.encode())
        connectionSocket.send('Content-Type: text/html\r\n\r\n'.encode())
        connectionSocket.send('<html><body><h1>404 Not Found</h1></body></html>\r\n'.encode())
        # FillInEnd 
        
        # Close client socket 
        connectionSocket.close()

# Terminate the program
serverSocket.close()
sys.exit()
