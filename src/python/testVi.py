#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to LabVIEW server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

print("Sending request %s …")
json = '{"message":"frontMostVi"}'
socket.send(json.encode())


#  Get the reply.
message = socket.recv()
print("Received reply %s " % ( message.decode("utf-8")))


print("Sending request %s …")
json = '{"message":"getValue","payload":"Plot"}'
socket.send(json.encode())

#  Get the reply.
message = socket.recv()
print("Received reply %s " % ( message.decode("utf-8")))

print("Sending request %s …")
json = '{"message":"click","payload":"Random"}'
socket.send(json.encode())

#  Get the reply.
message = socket.recv()
print("Received reply %s " % ( message.decode("utf-8")))

print("Sending request %s …")
json = '{"message":"getValue","payload":"Plot"}'
socket.send(json.encode())

#  Get the reply.
message = socket.recv()
print("Received reply %s " % ( message.decode("utf-8")))