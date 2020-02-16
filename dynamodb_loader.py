import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('citizens')
table.put_item(
    Item={
        'name': 'Sourabh',
        'descr': 'PyMongo is fun, you guys',
        'home': 'A',
        'interests' : ['biking','hiking'],
        'timeslots' : ['2-4','4-6'],
        'profile' : 'https://caring-companions.s3.amazonaws.com/profile_pictures/citizens/179127-275x390-senior-man-wearing-sweater.jpg'
    }
)