import zmq

context = zmq.Context()

#  Socket to talk to server
socket = context.socket(zmq.REQ)
socket.connect("tcp://10.0.0.14:5555")

#  Do 10 requests, waiting each time for a response
name = raw_input("Input Your name: ")

print("Connect to server as %s" % name)


while True:
    input = raw_input("Message: ")
    input = name+": "+input
    socket.send(input)

    message = socket.recv()
    print(message)
