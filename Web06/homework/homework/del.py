from flask import Flask, render_template
from models.service import Service
import mlab 
app = Flask(__name__)

mlab.connect()
# @app.route('/')
# def index():
#     return render_template('index.html')

service = Service.objects.delete()
print ("done")
# if __name__ == '__main__':
#   app.run(debug=True)
 