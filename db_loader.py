from pymongo import MongoClient
client = MongoClient('localhost', 27017)
print("Connected")
db = client.Citizens

"""
Citizen object fields
#     #     self.name = name
#     #     self.descr = descr
#     #     self.home = home
#     #     self.interests = interests
#     #     self.timeslots = timeslots
"""
posts = db.posts
#posts.drop()
post_1 = {
    'name': 'John',
    'descr': 'John is a retired army veteran who is always ready to impart wisdom and lend an ear. He is an excellent guitar player, and was known for bringing up morale at his army base with his light hearted country singing and guitar playing!',
    'home': 'Beautiful Life Retirement',
    'interests' : ['music','chess'],
    'timeslots' : ['2-4','4-6'],
    'profile' : 'https://caring-companions.s3.amazonaws.com/profile_pictures/citizens/200px/male3.jpg
}
post_2 = {
    'name': 'Judy',
    'descr': 'Judy is a retired nurse with an abundance of exciting and unnerving stories about her days working in the intensive care units in various hospitals. She is passionate about photography, and loves revisiting old photo albums to keep the memories fresh and alive.',
    'home': 'Tranquility Retirement',
    'interests' : ['games','photography'],
    'timeslots' : ['2-4','4-6'],
    'profile' : 'https://caring-companions.s3.amazonaws.com/profile_pictures/citizens/200px/female2.jpg
}
post_3 = {
    'name': 'Than',
    'descr': 'By profession, Than is an ex-banker, however, his real passion lies in homebuilding. Along with his farmhouse which he built board by board from the ground up, Than was also actively involved in volunteering to build homes for the less fortunate.',
    'home': 'Beautiful Life Retirement',
    'interests' : ['watching TV','home building'],
    'timeslots' : ['2-4','4-6','7-9'],
    'profile' : 'https://caring-companions.s3.amazonaws.com/profile_pictures/citizens/200px/male4.jpg
}
post_4 = {
    'name': 'Steph',
    'descr': 'Steph is a much adored ex-school teacher. She has taught students of all ages and backgrounds, and is extremely passionate about passing on her knowledge. She also loves board games and chats!',
    'home': 'Utopia Terrace Retirement',
    'interests' : ['helping kids','sleeping'],
    'timeslots' : ['7-9','4-6'],
    'profile' : 'https://caring-companions.s3.amazonaws.com/profile_pictures/citizens/200px/female.jpg
}
post_5 = {
    'name': 'Amanda',
    'descr': 'Amanda is a world renowned geologist, and was instrumental in Upstream Oil and Gas development. She has worked endlessly to promote the Oil and Gas industry in Calgary. She is also an avid reader!',
    'home': 'Beutiful Life Retirement',
    'interests' : ['science','reading'],
    'timeslots' : ['2-4','4-6'],
    'profile' : 'https://caring-companions.s3.amazonaws.com/profile_pictures/citizens/200px/female5.jpg
}
post_6 = {
    'name': 'Mark',
    'descr': 'Mark is an ex-architect who was instrumental in the design of the Calgary Tower! He is also an avid chess player.',
    'home': 'Tranquility Retirement',
    'interests' : ['design','chess'],
    'timeslots' : ['2-4','4-6'],
    'profile' : 'https://caring-companions.s3.amazonaws.com/profile_pictures/citizens/200px/male1.jpg
}
post_7 = {
    'name': 'Randall',
    'descr': 'Randall was once the premier of Calgary, and was one of the most influential people in overcoming the economic downturn encountered in the 1980s. He also loves cooking and trying out new recipies!',
    'home': 'Beautiful Life Retirement',
    'interests' : ['politics','cooking'],
    'timeslots' : ['2-4','4-6'],
    'profile' : 'https://caring-companions.s3.amazonaws.com/profile_pictures/citizens/200px/male2.jpg
}
post_8 = {
    'name': 'Jonah',
    'descr': 'Jonah is a well published romance novelist. He is alwasy optimistic, and gives great advice. Jonah loves long walks in the garden, as this is the source of many of his ideas.',
    'home': 'Utopia Terrace Retirement',
    'interests' : ['poetry','garden walks'],
    'timeslots' : ['2-4','4-6'],
    'profile' : 'https://caring-companions.s3.amazonaws.com/profile_pictures/citizens/200px/female1.jpg
}
post_9 = {
    'name': 'Camille',
    'descr': 'Camille is passionate about world food, and was famous for her fusion Thai inspired meat loaf back in the day! She is amazing at knitting Christmas sweaters and enjoys long walks.',
    'home': 'Utopia Terrace Retirement',
    'interests' : ['knitting','long walks'],
    'timeslots' : ['2-4','4-6'],
    'profile' : 'https://caring-companions.s3.amazonaws.com/profile_pictures/citizens/200px/male.jpg
}
post_10 = {
    'name': 'Meghan',
    'descr': 'Meghan is a retired cardiothoracic surgeon, so if you ever want to know anything about hearts(physical or otherwise), she is the person to go to! She also loves music and reading.',
    'home': 'Tranquility Retirement',
    'interests' : ['reading','music'],
    'timeslots' : ['2-4','4-6'],
    'profile' : 'https://caring-companions.s3.amazonaws.com/profile_pictures/citizens/200px/female4.jpg
}

new_result = posts.insert_many([post_1, post_2, post_3,post_4,post_5,post_6,post_7,post_8,post_9,post_10])

print('Multiple posts: {0}'.format(new_result.inserted_ids))

for post in posts.find():
        print(post)

# new_list = [post for post in posts.find()]

# #Find one 
# print(posts.find_one({'name':'Sourabh'}))

#senior_list = [post['interests'] for post in posts.find()]
#for senior in senior_list:
#    print(senior)