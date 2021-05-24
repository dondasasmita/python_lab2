import json


# Get the json file from elsewhere
def load_json_to_dict(path):
    with open(path) as file:
        return json.load(file)


# Get the object
def get_data(data_dict, key):
    return data_dict[key]


# Demo Operation that access each object in the array
def print_info(data_array):
    for media_dict in data_array:
        print(media_dict['id'] + ' : ' + media_dict['name'])


data1 = load_json_to_dict('files/gallery1.json')
data2 = load_json_to_dict('files/gallery2.json')

media_items_array1 = get_data(data1, 'media_items')
media_items_array2 = get_data(data2, 'media_items')

print_info(media_items_array1)
print('--------------')
print_info(media_items_array2)
