import socket
localIP = "localhost"
localPort = 1025
bufferSize = pow(2,10)

# Create a datagram socket (AF_INET --> IPv4, SOCK_DGRAM --> UDP)
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind to Address and IP
UDPServerSocket.bind((localIP, localPort))
print("UDP Server up!")
# Listen for incoming datagrams
while (True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    messageDecoded = format(bytesAddressPair[0])
    addressDecoded = format(bytesAddressPair[1])
    print("Message from Client", addressDecoded, "received:", messageDecoded)
    # Sending reply to client
    UDPServerSocket.sendto(str.encode("Message received on the Server!"), bytesAddressPair[1])


