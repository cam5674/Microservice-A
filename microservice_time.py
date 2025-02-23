# get closest time to requested time

import datetime
import heapq
import json
# only for current day

from datetime import datetime


def convert_time(info):
    with open("database.json", "w" ) as f:
        json.dump(info, f, indent=4)
        f.close()
    arrival_times = []
    for dic in info:
        if "rt" in dic:
            rt = datetime.fromisoformat(dic["rt"])
            print(rt)
        if "arrival time" in dic:
            id_time = datetime.fromisoformat(dic['departure time']), dic['id']
            arrival_times.append(id_time)

    time_difference = []
    for time in arrival_times:
        test = abs(time[0] - rt)
        id_time = test, time[1]
        time_difference.append(id_time)

    # sort by ints(time)
    times = sorted(time_difference, key=lambda x: x[0])
    print(times)
    counter = 0
    sorted_times = []
    for x in times:
        for dic in info:
            if dic.get("id") == x[1]:
                print("yes")
                sorted_times.append(dic)
                break

    return sorted_times

