# start server first
import json
from rich.console import Console
from rich.table import Table
import zmq
import time
from microservice_print  import create_table
from microservice_delete import delete_id

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
        if "departure" in dic:
            # figure out how to send back table
            table = create_table(jinfo)
            socket.send_string(table)
            break
        if "SID" in dic:
            print(jinfo)
            print(dic)
            new_data = delete_id(jinfo)
            print(new_data)
            socket.send_string("Deleted SID")
            break

    time.sleep(1)
    break





# for the delete user story you can just delete the arrival and departing time

