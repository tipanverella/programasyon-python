# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route("/")
# def index():
#    print("Index Triggered")
#    return "The server is up, running, and printing statements"
#
#
# app.run()

#!/usr/bin/python           # This ins server.py file

import socket  # Import socket module

s = socket.socket()  # Create a socket object
host = socket.gethostname()  # Get local machine name
port = 5000  # Reserve a port for your service.
s.bind((host, port))  # Bind to the port

s.listen(5)  # Now wait for client connection.
while True:
    c, addr = s.accept()  # Establish connection with client.
    print("Got connection from", addr)
    c.send("Thank you for connecting")
    c.close()  # Close the connection
