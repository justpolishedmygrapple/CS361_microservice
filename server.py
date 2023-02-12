import time
import zmq
import csv

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv().decode()
    response = ""

    with open("games.csv", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            if message == row[0]:
                response = "Name: {}\n" \
                           "Rating Average: {}\n"\
                            "Complexity Average: {}".format(row[0], row[1], row[2])
                socket.send(response.encode())
                break

    if response == "":
        response = "{} could not be found in the game database".format(message).encode()
        socket.send(response)

    time.sleep(1)
