import json
with open('data.json','r+') as f:
    json_str = json.loads(f.read())
    #for i in json_str:
        #print(i['fa_address'])

with open('church_data.json','r+') as f:
    json_str = json.loads(f.read())['church']
    for i in json_str:
        data = json_str[i]
        print(data['address'])
    