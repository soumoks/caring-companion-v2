#from mongoengine import *
import json
from marshmallow import schema
# class Citizen(Document):
#     name = StringField(required=True,max_length=20)
#     descr = StringField(required=True,max_length=200)
#     home = StringField(required=True,max_length=20)
#     interests = ListField(required=True)
#     timeslots = ListField(required=True)

#     def __str__(self):
#         return self.name + " " + self.descr
#     def get_json(self):
#         return Citizen.__dict__
#     # def __init__(self,name,descr,home,interests=[],timeslots=[]):
#     #     self.name = name
#     #     self.descr = descr
#     #     self.home = home
#     #     self.interests = interests
#     #     self.timeslots = timeslots
class Citizen(schema):
    name = fields.Str()
    descr = fields.Str()
    home = fields.Str()
    interests = fields.
    