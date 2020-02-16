from flask import Flask
from flask_cors import CORS,cross_origin
from flask import jsonify,request
from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import json

#Extending JSONencoder to support Object_ID returned by MongoDB
#https://stackoverflow.com/questions/16586180/typeerror-objectid-is-not-json-serializable

"""
Referenced from
https://medium.com/@riken.mehta/full-stack-tutorial-flask-react-docker-ee316a46e876
"""
class JSONEncoder(json.JSONEncoder):
    ''' extend json-encoder class'''

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)

app = Flask(__name__)
app.json_encoder = JSONEncoder

@app.route("/")
def hello_world():
    return jsonify(s1.__dict__)

"""
Get all citizens present in the DB
"""
@app.route("/getcitizens")
@cross_origin()
def get_citizens():
    new_list = [post for post in posts.find()]
    return jsonify(new_list)

"""
Create citizens in the DB
"""
@app.route("/putcitizen",methods=['POST'])
def create_citizen():
    if request.method == 'POST':
        data = request.get_json(force=True,cache=False)
        pprint(data)
        return jsonify({'ok': True, 'message': 'User created successfully!'}), 200


"""
Get citizens that have more than 50% match in interests
"""
@app.route("/getmatchingcitizens")
@cross_origin()
def get_matching_citizens():
    dummy_volunteer_interest_list = ['biking']
    matching_list = []
    senior_list = [post for post in posts.find()]
    for senior in senior_list:
        match = len(set(dummy_volunteer_interest_list) & set(senior['interests'])) / float(len(set(dummy_volunteer_interest_list) | set(senior['interests']))) * 100
        if match >= 30:
            matching_list.append(senior)
    return jsonify(matching_list)





@app.route("/sendemail", methods = ["POST"])
@cross_origin()
def send_email():
    sendgrid_api_key = ''
    if request.method == 'POST':
        """The returned data will be in the following format:
        {
            volunteer_name: "name",
            senior_citizen: {Senior object},
            volunteer_email: "email"
            time_slot: "chosen time slot"
        }
        """
        data = request.get_json(force=True,cache=False)
        #data = data.__dict__
        vol_email = str(data.get("volunteer_email"))
        vol_name = str(data.get("volunteer_name"))
        senior_name = str(data.get('senior_citizen').get('name'))
        time_slot = str(data.get('time_slot'))
        vol_content = "You have requested to visit "+ senior_name+" at a timeslot of "+time_slot+". \n Thank you for your interest and we will get back to you."
        home_content = vol_name+' whose email is: '+vol_email+' has requested to be a Caring Companion for '+ senior_name+'.\n The time slot requested is: '+ time_slot+'.\n '+ vol_name+' is awaiting your response!'
        messag_to_vol = Mail(
            from_email='email@em4292.sourabh.org',
            to_emails=vol_email,
            subject='Thank you for requesting to be a Caring Companion!',
            html_content=vol_content)
        messag_to_home = Mail(
            from_email='email@em4292.sourabh.org',
            to_emails='thanmayee.mudigonda@gmail.com',
            subject=vol_name+' has requested to be a Caring Companion!',
            html_content=home_content)
        try:
            sg = SendGridAPIClient(sendgrid_api_key)
            response_to_vol = sg.send(messag_to_vol)
            response_to_home = sg.send(messag_to_home)
            print(response_to_vol.status_code)
            print(response_to_vol.body)
            print(response_to_vol.headers)
            print(response_to_home.status_code)
            print(response_to_home.body)
            print(response_to_home.headers)
        except Exception as e:
            print(e.message)
        return jsonify({'ok': True, 'message': 'Email sent successfully!'}), 200
    else:
        return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400


if __name__ == "__main__":
    client = MongoClient('localhost', 27017)
    print("Connected to MongoDB..")
    #Choose Database citizens
    db = client.Citizens
    #Choose collections posts
    posts = db.posts
    app.run(port=80)
