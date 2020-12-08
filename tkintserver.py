import socket
import sys
import os
from tkinter import *

master = Tk()

def setup_listen():

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('localhost', 10000)
    t.insert(INSERT, 'starting up on {} port {}'.format(*server_address) + '\n')
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    os.system('echo_client.py')
    
    while True:
        # Wait for a connection
        t.insert(INSERT, 'waiting for a connection' + '\n')
        connection, client_address = sock.accept()
        try:
            t.insert(INSERT, 'connection from: ' + str(client_address + '\n'))

           # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(16)
                t.insert(INSERT, 'received {!r}'.format(data) + '\n')
                if data:
                    t.insert(INSERT, 'sending data back to the client' + '\n')
                    connection.sendall(data)
                else:
                    t.insert(INSERT, 'no data from' + str(client_address + '\n'))
                    break

        finally:
            # Clean up the connection
            connection.close()
        
l = Label(master, text = 'Connection Details: ')
l.grid(row=0, column=0)

t = Text(master, width=20, height = 8)
t.grid(row = 0, column = 1)

b = Button(master, text = 'Setup_Listen', command=setup_listen)
b.grid(row = 0, column = 5)

master.geometry('415x195')

master.title('Joshs Server')
