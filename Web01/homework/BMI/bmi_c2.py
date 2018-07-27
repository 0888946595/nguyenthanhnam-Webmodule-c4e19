from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bmi/<int:weight>/<int:height>')
def bmi (weight, height):
    bmi = weight/((height*height)*(10**(-4)))
    return render_template ('index.html', bmis = bmi)
    
if __name__ == '__main__':
  app.run(debug=True)