from flask import Flask, render_template
from mongoengine import *
import mlab

app = Flask(__name__)

mlab.connect()

# design database
class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField ()
    phone = StringField()
    address = StringField()
    status = BooleanField()     

# new_service = Service(
#     name = "Tuấn Anh",
#     yob = 1995,
#     gender = 0,
#     height = 150,
#     phone = "0969696969",
#     address = "Ha Noi",
#     status = False
# )

# new_service.save()

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
  app.run(debug=True)
 