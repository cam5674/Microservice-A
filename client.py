import zmq
import json
"""
This client can send a request to the microservice to create a table, a JSON
containing an organized list of dictionaries that are ordered by the shortest
difference to the requested time, or a JSON with the deleted SID.

To use the microservice make sure that the type of request is correct.

Types:

print--> creates a table of arrival and departing shuttle times

requested time --> creates a JSON containing an organized list of dictionaries 
that are ordered by the shortest difference to the requested time.

SID --> creates a JSON with the deleted SID set to null

"""

print("Connecting to server...")
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5556")

print("Sending request...")

# Example data for printing out arriving and departing shuttles
test_print = [{"type": "print"},
              {
     "id": 12345,
     "departure": "Station A",
     "destination": "Station B",
     "departure time": "2025-02-15T14:48:00Z",
     "arrival time": "2025-02-15T15:05:00Z"
   },
   {
     "id": 12346,
     "departure": "Station C",
     "destination": "Station D",
     "departure time": "2025-02-15T15:30:00Z",
     "arrival time": "2025-02-15T16:00:00Z"
   },
   {
     "id": 12347,
     "departure": "Station E",
     "destination": "Station F",
     "departure time": "2025-02-15T14:48:00Z",
     "arrival time": "2025-02-15T16:45:00Z"
  }]

# username: bob123, SID: 12347

# for deleting a shuttle request
test_sid = {"type": "SID", "username": "bob123", "SID": 12347}


# Example data for picking a shuttle time that is the shortest difference
# to the user's desired time
test_requested_time = [{"type": "requested time", "time": "2025-02-15T08:47:00Z"},
                       {
                           "id": 12357,
                           "departure": "Station A",
                           "destination": "Station B",
                           "departure time": "2025-02-14T08:00:00Z",
                           "arrival time": "2025-02-14T08:45:00Z"
                       },
                       {
                           "id": 12358,
                           "departure": "Station C",
                           "destination": "Station D",
                           "departure time": "2025-02-14T09:15:00Z",
                           "arrival time": "2025-02-14T09:50:00Z"
                       },
                       {
                           "id": 12359,
                           "departure": "Station E",
                           "destination": "Station F",
                           "departure time": "2025-02-14T10:05:00Z",
                           "arrival time": "2025-02-14T10:35:00Z"
                       },
                       {
                           "id": 12360,
                           "departure": "Station G",
                           "destination": "Station H",
                           "departure time": "2025-02-15T11:00:00Z",
                           "arrival time": "2025-02-15T11:40:00Z"
                       },
                       {
                           "id": 12361,
                           "departure": "Station I",
                           "destination": "Station J",
                           "departure time": "2025-02-15T12:10:00Z",
                           "arrival time": "2025-02-15T12:55:00Z"
                       },
                       {
                           "id": 12362,
                           "departure": "Station K",
                           "destination": "Station L",
                           "departure time": "2025-02-15T13:20:00Z",
                           "arrival time": "2025-02-15T13:50:00Z"
                       },
                       {
                           "id": 12363,
                           "departure": "Station M",
                           "destination": "Station N",
                           "departure time": "2025-02-16T14:30:00Z",
                           "arrival time": "2025-02-16T15:10:00Z"
                       },
                       {
                           "id": 12364,
                           "departure": "Station O",
                           "destination": "Station P",
                           "departure time": "2025-02-16T15:45:00Z",
                           "arrival time": "2025-02-16T16:25:00Z"
                       },
                       {
                           "id": 12365,
                           "departure": "Station Q",
                           "destination": "Station R",
                           "departure time": "2025-02-16T17:00:00Z",
                           "arrival time": "2025-02-16T17:35:00Z"
                       },
                       {
                           "id": 12366,
                           "departure": "Station S",
                           "destination": "Station T",
                           "departure time": "2025-02-16T18:10:00Z",
                           "arrival time": "2025-02-16T18:50:00Z"
                       }]

# send data to server
json_data = json.dumps(test_print)
socket.send_string(json_data)

# Get reply
repy = socket.recv_string()
print("Received")
print(repy)
