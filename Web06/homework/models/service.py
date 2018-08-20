from mongoengine import *
from random import choice

class Service(Document):
    name = StringField()
    yob = DateTimeField()
    address = StringField()
    gender = IntField()
    email = EmailField()
    phone = StringField()
    job = StringField()
    company = StringField()
    status = BooleanField()
    image = StringField()
    description = ListField()
    measurement = ListField()
    oders = BooleanField()
class User(Document):
    username = StringField()
    password = StringField()

class Order(Document):
    service_id = ReferenceField(Service)
    user_id = ReferenceField(User)
    time = DateTimeField()
    is_accept = BooleanField()


    
