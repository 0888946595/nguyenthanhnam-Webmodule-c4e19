from flask import *
from models.service import *
from tkinter import *
import datetime

import mlab 

mlab.connect()
app = Flask(__name__)
app.secret_key = 'secret key'


@app.route('/')
def index():
    customer = Service.objects()
    return render_template('index.html', customer = customer)


@app.route('/admin', methods = ["GET", "POST"])
def admin():
    if 'logged_in' in session:
        if request.method == 'GET':
            all_admin = Service.objects()
            return render_template('admin.html', all_admin = all_admin)
        elif request.method == 'POST':
            return redirect (url_for('login'))

    else:
        return redirect(url_for('index'))
   
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
    if 'logged in' in session:
        session ['logged in'] = True
        service = Service.objects.with_id(service_id)
        return render_template('detail.html', service = service)
    else:
        return redirect(url_for('login'))

@app.route('/login/', methods = ['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        form = request.form
        user = form['username']
        password = form['password']
        # id = User.objects()
        # query = id(username = user, password = password)
        result = User.objects(username =user, password = password)
        if result:
            session['logged in'] = False
            return redirect(url_for('index'))
        elif user == "admin" and password == "admin":
            session['logged_in'] = True
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
    if "logged_in" in session:
        del session['logged_in']
        return redirect(url_for('index'))
    elif "logged in" in session:
        del session['logged in']
        return redirect(url_for('index'))
@app.route('/order/<service_id>')
def order(service_id):

    if "logged in" in session:
        new_order = Order(
            service_id = Service.objects.with_id(service_id),
            user_id = session['logged in'],
            time = datetime.datetime.now,
            is_accept = False     
        )
        new_order.save()
        return ("Đã gửi yêu cầu")
    else:
        return ("Đăng nhập") 

if __name__ == '__main__':
  app.run(debug=True)



# session['logged_in'] = True

# session['us']