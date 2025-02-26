import json
import zmq
from microservice_print import create_table
from microservice_delete import delete_id
from microservice_time import convert_time
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")


while True:
    # get info from client
    info = socket.recv_string()

    # convert into json
    jinfo = json.loads(info)

    # check type of data being sent
    if isinstance(jinfo, dict):
        # delete user shuttle ID
        if jinfo.get("type") == "SID":
            print("requested SID deletion...")
            new_data = delete_id(jinfo)
            socket.send_string(f"Deleted SID {new_data}")
            break
    else:
        for dic in jinfo:
            # print out shuttle times
            if dic.get("type") == "print":
                print("requested print table...")
                # figure out how to send back table
                table = create_table(jinfo)
                socket.send_string(table)
                break

            # find shortest time difference to requested time
            elif dic.get("type") == "requested time":
                print("requested time...")
                sorted_times = convert_time(jinfo)
                json_data = json.dumps(sorted_times)
                socket.send_string(json_data)
            break
