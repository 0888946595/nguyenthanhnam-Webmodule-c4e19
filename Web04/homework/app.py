from flask import *
from models.service import Service, User
from tkinter import *

import mlab 

mlab.connect()
app = Flask(__name__)
app.secret_key = 'secret key'


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
    service = Service.objects.with_id(service_id)
    if request.method == "GET":
        return render_template('edit.html')
    elif request.method == "POST":
        
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

@app.route('/login/', methods = ['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        form = request.form
        user = form['username']
        password = form['password']
        id = User.objects()
        
        query = id(username = user, password = password)
        result = query()
        if result:
            session['logged in'] = True
            return redirect(url_for('index'))
            if user == "admin" and password == "admin":
                return redirect (url_for('admin'))
        
        else:
            
            return redirect(url_for('signin'))
   
@app.route('/signin', methods = ["GET", "POST"])
def signin():
    if request.method == "GET":
        return render_template ('signin.html')
    elif request.method == "POST":
        form = request.form
        user = form['username']
        password = form['password']

        new_user = User(
            username = user,
            password = password
        )

        new_user.save()
        
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    del session['logged in']
    return redirect(url_for('index'))
if __name__ == '__main__':
  app.run(debug=True)
