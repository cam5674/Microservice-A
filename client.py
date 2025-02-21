import zmq
import time
import json

"""
Will send the specific data/request to be fulfilled. Will need to be in a 
specific format.
"""

print("Connecting to server...")
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5556")

print("Sending request...")
# example data: [

data_test = [
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
  } ]

# username: bob123, SID: 12347

# test_id = {"username": "bob123", "SID": 12347}
json_data = json.dumps(data_test)
socket.send_string(json_data)

# Get reply
repy = socket.recv_string()
print(repy)
