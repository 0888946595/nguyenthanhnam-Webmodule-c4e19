from models.service import Customer
import mlab

mlab.connect()


all_info = Customer.objects()
