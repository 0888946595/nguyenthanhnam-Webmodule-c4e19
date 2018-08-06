from flask import Flask, render_template
from mongoengine import *
from model.service import WarmWinter

import mlab

app = Flask(__name__)

mlab.connect()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<g>')
def search(g):
    all_service =WarmWinter.objects(gender=g, yob__lte = 1998,address__contains = "US")
    return render_template('search.html', all_service = all_service)



@app.route('/customer')
def customer():
    info_customers = Service.objects()
    return render_template('info.html')

if __name__ == '__main__':
  app.run(debug=True) 