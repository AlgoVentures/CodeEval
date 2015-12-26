import json


with open(sys.argv[1], 'r') as f:
    json_objects = (json.loads(l) for l in f)
    for json_object in json_objects:
        #grab all itemts
        items = (item for item in json_object['menu']['items'] if item)
        #get values of every items into a list
        ids = (item['id'] for item in items if 'label' in item)
        print(sum(ids))
