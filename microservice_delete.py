import json


# read JSON file and then delete the id in the file
def delete_id(data):
    del data['SID']

    new_data = json.dumps(data)
    return new_data

