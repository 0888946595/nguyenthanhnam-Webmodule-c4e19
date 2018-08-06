from flask import Flask, render_template
from random import randint
from mongoengine import *
from faker import Faker

import mlab



app = Flask(__name__)

mlab.connect()

# design database
class WarmWinter(Document):

    new_service = Service(
        name = fake.name(),
        yob = randint(1990, 2000),
        gender = randint (0,1),
        height = randint (150, 190),
        phone = fake.phone_number(),
        address = fake.address(),
        status = choice ([True, False]),
        company = fake.company()
    )
    
# new_service = Service(
#     name = "Tuấn Anh",
#     yob = 1995,
#     gender = 0,
#     height = 150,
#     phone = "0969696969",
#     address = "Ha Noi",
#     status = False
# )

new_service.save()

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
  app.run(debug=True)
 