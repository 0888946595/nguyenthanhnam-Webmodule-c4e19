from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bmi/<int:weight>/<int:height>')
def bmi (weight, height):
    bmi = weight/((height*height)*(10**(-4)))
    
    if 16 <= bmi <= 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 25:
        return "Normal"
    elif 25 <= bmi <= 30:
        return "Overweight"
    else:
        return "Obese"
    
if __name__ == '__main__':
  app.run(debug=True)