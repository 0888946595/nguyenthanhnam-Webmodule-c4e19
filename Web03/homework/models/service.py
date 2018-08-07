from mongoengine import *
from random import choice
from PIL import Image
class Service(Document):
    name = StringField()
    gender = IntField()
    email = EmailField()
    phone = StringField()
    job = StringField()
    company = StringField()
    status = BooleanField()
    image = StringField()
    description = ListField()
    measurement = ListField()
