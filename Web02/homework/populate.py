from models.service import Customer
import mlab
from faker import Faker
from random import randint, choice

mlab.connect()

fake = Faker()
# print (fake.address())
for i in range (50):
    print ("Saving Service", i+1, "......")
    new_service = Customer(
        name = fake.name(),
        job = fake.job(),
        gender = randint (0,1),
        phone = fake.phone_number(),
        company = fake.company(),
        status = choice[(True, False)]
        
    )
    new_service.save()