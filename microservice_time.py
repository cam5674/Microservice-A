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

    # don't need this
    with open("database.json", "w" ) as f:
        json.dump(info, f, indent=4)
        f.close()

    # store list of arrival times and ids
    arrival_times = []

    # get requested time and store arrival times and ids in arrival_times
    for dic in info:
        if "rt" in dic:
            rt = datetime.fromisoformat(dic["rt"])
        if "arrival time" in dic:
            id_time = datetime.fromisoformat(dic['departure time']), dic['id']
            arrival_times.append(id_time)

    # To sort the times
    time_difference = []

    # Sort times, closest time to requested time is first
    for time in arrival_times:
        test = abs(time[0] - rt)
        id_time = test, time[1]
        time_difference.append(id_time)

    # sort by ints(time)
    times = sorted(time_difference, key=lambda x: x[0])

    # make new json with closest times first
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

