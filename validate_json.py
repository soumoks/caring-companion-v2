import json
from pprint import pprint
data = {
	"volunteer_name": "Thanmayee",
	"volunteer_email": "thanmayee.mudigonda@gmail.com",
	"senior_citizen": {
		"name": "Sourabh",
		"descr": "PyMongo is fun, you guys",
		"home": "A",
		"interests": ["biking", "hiking"],
		"timeslots": ["2-4", "4-6"],
		"profile": "https://caring-companions.s3.amazonaws.com/profile_pictures/citizens/179127-275x390-senior-man-wearing-sweater.jpg"
	},
	"time_slot": "2-4"
}
s1 = json.dumps(data)
data_json = json.loads(s1)
print(data_json['senior_citizen']['name'])
#