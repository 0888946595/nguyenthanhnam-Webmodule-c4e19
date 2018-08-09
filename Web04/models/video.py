from mongoengine import *

class Video(Document):
    name = StringField()
    title = StringField()
    link = StringField()
    views = IntField()
    thumbnail = StringField()
    youtube_id = StringField()