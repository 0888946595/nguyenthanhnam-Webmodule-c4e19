from flask import Flask, render_template
from mongoengine import *
from models.service import Customer


import mlab

mlab.connect()
app = Flask(__name__)

find_id = "5b6316cfdb57d22354d4cf85"

service = Customer.objects.with_id(find_id)
# service = Customer.objects.get(id=find_id)

# print (service.name)
# print ("* " * 5)
if service is not None:
    # service.delete()
    # print ("Đã Xóa Thành Công ")

    # upadte
    print (service.to_mongo())
    service.update(set__name="Ngoc", set__yob = 2000)
    service.reload()
    print (service.to_mongo())
else:
    print ("Not Found")