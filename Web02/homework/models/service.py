from mongoengine import *
from random import choice

class Customer(Document):
    name = StringField()
    gender = IntField()
    gender = IntField()
    email = StringField()
    phone = StringField()
    job = StringField()
    company = StringField()
    status = StringField()

# new_customer = Customer(
#     name = "Herra",
#     gender = 1,
#     email = "namnguyen@gmail.com",
#     phone = "01692126595",
#     job = "Student",
#     company = "nothing"
# )

# new_customer.save()
