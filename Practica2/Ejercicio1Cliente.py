import socket
serverAddressPort = ("localhost", 1025)
bufferSize = 1024

# Create UDP Socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Send message to server
UDPClientSocket.sendto(str.encode("Message from client"), serverAddressPort)
# Receive message from server
print("Connection established!")
print("Reply from server:", format(UDPClientSocket.recvfrom(bufferSize)[0]))
