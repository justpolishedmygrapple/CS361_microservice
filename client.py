import zmq


context = zmq.Context()

#  Socket to talk to server
print("Connecting to games microservice…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

request = input("Enter game you'd like to search for: ")


socket.send(request.encode())

response = socket.recv().decode()
print("Response from server:\n{}".format(response))
