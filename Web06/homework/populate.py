from models.service import *
import mlab
from faker import Faker
from random import randint,choice, sample
import datetime

from pymongo import *

mlab.connect()

fake = Faker()

descrip = ['dễ thương', 'ngoan hiền', 'yêu pets', 'ế trầm trọng', 'chưa có gấu']

measure = [90,60,70,80,69,56,89,100]
for i in range (50):
    print ("Saving Collection", i+1, "......")
    new_service = Service(
        name = fake.name(),
        job = fake.job(),
        yob = fake.date_of_birth( minimum_age=18, maximum_age=35),
        address = fake.address(),
        gender = randint (0,1),
        phone = fake.phone_number(),
        company = fake.company(),
        email = fake.free_email(),
        status = choice ([True, False]),
        description = [choice(descrip) for i in range (3)],
        measurement = [choice(measure)for i in range (3)],
     
        

    )

    # new_order = Order(
    #     user_id = User.objects(),
    #     service_id = Service.objects(),            
    #     time = datetime.datetime.now,
    #     is_accept = False
    # )

    # new_order.save()
    
    new_service.save()

