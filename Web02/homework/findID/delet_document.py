from flask import Flask, render_template
from mongoengine import *
from model.service import Service


import mlab

mlab.connect()
app = Flask(__name__)

find_id = "5b5b1e83db57d20bc4320b2c"

all_service = Service.objects.get(id = find_id)

# print (all_service.name)
# print ("* " * 5)

del_id = all_service.delete()
print ("Đã Xóa Thành Công ")