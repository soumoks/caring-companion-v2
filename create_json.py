import json
import uuid
from pprint import pprint
#Used to create modify json file before loading data into dynamoDB
"""
https://docs.python.org/3/library/uuid.html
Generates a random UUID
uuid.uuid4()
"""
fin = open('input_data.json')
#input data
citizens = json.load(fin)

#create empty list for data
data = list()
for citizen in citizens:
    #Append UUID as citizenID to each citizen object
    #citizenID is used as partition key on DynamoDB
    citizen['citizenid'] = str(uuid.uuid4())
    data.append(citizen)
#Write data to file
with open('citizendata.json','w',encoding='utf-8') as fout:
    json.dump(data,fout, ensure_ascii=False, indent=4)
