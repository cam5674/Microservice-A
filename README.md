# Microservice-A for CS361

Communication pipeline: ZMQ

A)   
  - 1a) To request a table with all the vaiable shuttle times, you need to send a request like this: [{"type": "print"}, { "id": 12345, "departure": "Station A", "destination": "Station B", "departure time": "2025-02-15T14:48:00Z", "arrival time": "2025-02-15T15:05:00Z"}, {"id": 12346, "departure": "Station C", "destination": "Station D", "departure time": "2025-02-15T15:30:00Z", "arrival time": "2025-02-15T16:00:00Z" }] 
    -  This will return a stringified table of the arrival and departing times.
  - 2a) To request a list of the shortest difference between the requested time and the list of all departing Shuttles, you need to send the request like this: [{"type": "requested time", "time":"2025-02-15T14:47:00Z" }, { "id": 12345, "departure": "Station A", "destination": "Station B", "departure time": "2025-02-15T14:48:00Z", "arrival time": "2025-02-15T15:05:00Z"}, {"id": 12346, "departure": "Station C", "destination": "Station D", "departure time": "2025-02-15T15:30:00Z", "arrival time": "2025-02-15T16:00:00Z" }]
    - Need to change type to requested time and give the time that you want to compare against all departing shuttles. This request will create a JSON file of the above list of dictionaries sorted by shortest difference to the requested time.
  - 3a) To reqest a shuttle Identification number (SID) to be deleted, make the request like this: {"type": "SID", "username": "bob123", "SID": 12347}
    - This will make a JSON file with the SID set to null.

B)
