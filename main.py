import socket
from PIL import Image
import sys


HOST = "flood.schenklflut.de"
PORT = 1234
offsetx = 1000
offsety = 800


def main():

    imagename = str(sys.argv[1]) # Adjust this to the name of the iamge



    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the port
    server_address = (HOST, PORT)
    sock.connect(server_address)
    print("Connected")

    sock.send(b"PX 100 100\n")
    datastream = sock.recv(1024)
    print(datastream.decode())




    im = Image.open(imagename)  # Can be many different formats.
    pix = im.load()
    size = im.size
    print(size) #Absolutey not necessary only here for fucking testing shit
    x, y = im.size #Split the shit into x,y values
    print(x)
    print(y)
    #print(pix[500, 500])

    #Parse image into more convenient data type

    pixelarray = [[0] * y for _ in range(x)]


    for i in range(x):
        for j in range(y):

            r, g, b, t = pix[i, j]
            pixelarray[i][j] = '{:02x}{:02x}{:02x}'.format(r, g, b)

    #Do the actual dump to the server

    while True:

        for i in range(x):
            for j in range(y):

                sendbuffer = "PX " + str(i+offsetx) + " " + str(j+offsety) + " " + str(pixelarray[i][j]) + "\n"
                sock.send(sendbuffer.encode())
                print(sendbuffer)

    sock.close()

main()