# start server first
import json
from rich.console import Console
from rich.table import Table
import zmq
import time
from microservice_print  import create_table
from microservice_delete import delete_id
from microservice_time import convert_time
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")

# could add a type in the json so you know what the request is
# example: "type": delete   "type": print table
while True:
    # get info from client
    info = socket.recv_string()

    # convert into json
    jinfo = json.loads(info)
    # unpack
    # print out shuttle times

    for dic in jinfo:

        if dic.get("type") == "print":
            print("print")
            # figure out how to send back table
            table = create_table(jinfo)
            socket.send_string(table)
            break
        elif "SID" in dic:
            print("SID")
            print(jinfo)
            print(dic)
            new_data = delete_id(jinfo)
            print(new_data)
            socket.send_string("Deleted SID")
            break
        elif dic.get("type") == "requested time":
            print("requested time")
            sorted_times = convert_time(jinfo)
            json_data = json.dumps(sorted_times)
            socket.send_string(json_data)

    time.sleep(1)






# for the delete user story you can just delete the arrival and departing time

