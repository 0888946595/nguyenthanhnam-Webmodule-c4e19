from flask import *
from models.service import Customer
from faker import Faker 
import mlab
app = Flask(__name__)

mlab.connect()

fake = Faker()



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info')
def customer():
    all_customer = Customer.objects()
    return render_template('info.html', all_customer = all_customer)

@app.route('/top-male')
def firstmale():
    all_customer = Customer.objects(gender = 1)
    search = all_customer[0:10]
    return render_template('topman.html', search = search)

@app.route('/admin')
def admin():
    all_service = Customer.objects()
    return render_template('admin.html', all_service = all_service)

@app.route('/delete/<service_id>')
def delete(service_id):

    all_service = Customer.objects.with_id(service_id)
    if all_service is not None:
        all_service.delete()
        return redirect(url_for('admin')) 
    else:
        return "Not Found"
@app.route('/new-service', methods = ["GET", "POST"])
def creat():
    if request.method == "GET":
        return render_template ('new-service.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        job = form ['job']
        phone = form ['phone']
        new_service = Customer(name=name, job=job, phone = phone)
        new_service.save()
        

        return redirect(url_for('admin'))

if __name__ == '__main__':
  app.run(debug=True)
 