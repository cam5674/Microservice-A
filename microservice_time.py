import datetime
import json

from datetime import datetime


def convert_time(info):
    """
    Sorts the arrival times of info. The id of the arrival time is put in a
    tuple. The tuples are stored in the list arrival_times. The arrival_times
    is then sorted. The ids of the list are checked with the ids in info. The
    closest times are then stored as a new list of dictionaries in sorted
    times.
    :param info: list of dictionaries
    :return:  Sorted times of arrivals in info
    """
    # store list of arrival times and ids
    arrival_times = []

    # get requested time and store arrival times and ids in arrival_times
    for dic in info:
        if "time" in dic:
            rt = datetime.fromisoformat(dic["time"])
        if "departure time" in dic:
            id_time = datetime.fromisoformat(dic['departure time']), dic['id']
            arrival_times.append(id_time)

    # To sort the times
    time_difference = []

    # Sort times, shortest difference to requested time
    # try to put in loop above
    for time in arrival_times:
        abs_time = abs(time[0] - rt)
        id_time = abs_time, time[1]
        time_difference.append(id_time)

    print(time_difference)
    # sort by ints(time)
    times = sorted(time_difference, key=lambda i: i[0])

    # make new json file with a list of closest departing times to requested time
    sorted_times = []
    for x in times:
        for dic in info:
            if dic.get("id") == x[1]:
                sorted_times.append(dic)
                break

    # rewrite file with new sorted times
    with open("database.json", "w") as file:
        json.dump(sorted_times, file, indent=4)
        file.close()
    return sorted_times
