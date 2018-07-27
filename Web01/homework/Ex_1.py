from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/about')
def about():
    about = [{
        "name": "Nguyen Thanh Nam",
        "work": "Student",
        "school": "Techkids",
        "hobbies": "Play PS4",
       
    }
    ]
    return render_template("index.html", about = about)

@app.route('/school')
def school():
    return redirect("http://techkids.vn")

if __name__ == '__main__':
  app.run(debug=True)
 