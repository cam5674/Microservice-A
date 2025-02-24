import json


def delete_id(data):
    """
    Deletes the SID from the JSON and writes a new file.
    :param data: dictionary
    :return: dictionary with null as the SID
    """
    data['SID'] = None

    with open("database.json", "w") as f:
        json.dump(data, f, indent=4)
        f.close()
    new_data = json.dumps(data)
    return new_data

