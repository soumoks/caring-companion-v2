import boto3
import json
#Loader file for DynamoDB
#Reference:
#https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.02.html
"""
Sample JSON
{
        "descr": "Meghan is a retired cardiothoracic surgeon, so if you ever want to know anything about hearts(physical or otherwise), she is the person to go to! She also loves music and reading.",
        "home": "Tranquility Retirement",
        "interests": [
            "reading",
            "music"
        ],
        "name": "Meghan",
        "profile": "https://caring-companions.s3.amazonaws.com/profile_pictures/citizens/seniors-citizen-age-@1X.jpg",
        "timeslots": [
            "2-4",
            "4-6"
        ],
        "citizenid": "c9f8c668-5b8b-4801-bfcd-b4b480657981"
    }
"""
dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="https://dynamodb.us-east-1.amazonaws.com")
table = dynamodb.Table('citizens')
with open('D:\Python-Hack-Projects\caring-companion-v2\citizendata.json') as json_file:
    citizens = json.load(json_file)
    for citizen in citizens:
        citizenid = citizen['citizenid']
        desc = citizen['descr']
        name = citizen['name']
        home = citizen['home']
        interests = citizen['interests']
        profile = citizen['profile']
        timeslots = citizen['timeslots']
        response = table.put_item(
            Item = {
                'citizenid':citizenid,
                'desc':desc,
                'name':name,
                'home':home,
                'interests':interests,
                'profile':profile,
                'timeslots':timeslots,
            }
        )
        print("Put item succeeded")
        print(json.dumps(response, indent=4))
        

