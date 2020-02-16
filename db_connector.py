from pymongo import MongoClient
from mongoengine import *
from Citizen import Citizen
client = MongoClient('localhost', 27017)
print("Connected")
db = client.pymongo_test
posts = db.posts
post_data = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
# result = posts.insert_one(post_data)
# print('One post: {0}'.format(result.inserted_id))


post_1 = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
post_2 = {
    'title': 'Virtual Environments',
    'content': 'Use virtual environments, you guys',
    'author': 'Scott'
}
post_3 = {
    'title': 'Learning Python',
    'content': 'Learn Python, it is easy',
    'author': 'Bill'
}

# new_result = posts.insert_many([post_1, post_2, post_3])

# print('Multiple posts: {0}'.format(new_result.inserted_ids))

# bills_post = posts.find({'author': 'Scott'})
#print(bills_post)
# for post in bills_post:
#     print(post)

connect('mongoengine_test', host='localhost', port=27017)

citizen1 = Citizen(
    name="Sourabh",
    descr="Hello",
    home="calgary",
    interests=["playing","badminton"],
    timeslots=["2-5","6-8"]
)
#citizen1.save()

for citizen in Citizen.objects:
    print(citizen.get_json())
