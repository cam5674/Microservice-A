import json


def delete_id(data):
    del data['SID']

    new_data = json.dumps(data)
    return new_data

