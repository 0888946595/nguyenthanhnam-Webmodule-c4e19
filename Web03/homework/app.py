from flask import *
from models.service import Service
from tkinter import *

import mlab 

mlab.connect()
app = Flask(__name__)



@app.route('/')
def index():
    customer = Service.objects()
    return render_template('index.html', customer = customer)


@app.route('/admin')
def admin():
    all_admin = Service.objects()

    return render_template('admin.html', all_admin = all_admin)
   
@app.route('/delete/<service_id>')
def delete(service_id):
    service = Service.objects.with_id(service_id)
    if service is not None:
        service.delete()
        return redirect(url_for('admin'))
    else:
        return "Not Found"

@app.route('/edit/<service_id>', methods = ["GET", "POST"])
def edit(service_id):
    
    if request.method == "GET":
        return render_template('edit.html')
    elif request.method == "POST":
        service = Service.objects.with_id(service_id)
        form = request.form 
        name = form['name']
        job = form ['job']
        company = form['company']
        phone = form['name']
        email = form['email']

        edits = service.update(
            set__name = name,
            set__job = job,
            set__company = company,
            set__phone = phone,
            set__email = email
        )
        
        service.reload()    
        return redirect(url_for('admin'))
        

@app.route('/detail/<service_id>')
def detail(service_id):
    service = Service.objects.with_id(service_id)
    return render_template('detail.html', service = service)

if __name__ == '__main__':
  app.run(debug=True)
