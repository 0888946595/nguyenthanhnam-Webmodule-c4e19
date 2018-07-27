from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    
    posts = [
        {
            "tittle": "Thơ con cóc",
            "content":  "Hello Babe",
            "author": "Tuấn Anh",
            "gender": 1
        },
        {
            "tittle": "Thơ xàm",
            "content": "hi hi",
            "author": "Liên",
            "gender": 0
        }   
    ]
    
    return render_template(
        
        "index.html", posts   = posts
        )

# @app.route('/hello')
# def hello ():
#     return "C4E19"


# @app.route('/say-hi/<name>/<age>')
# def say_hi (name, age):
#     return "Hi {0}! You're {1} year old".format(name, age)


@app.route('/sum/<int:numb1>/<int:numb2>')
def sum (numb1, numb2):
    # return "Tong cua {0}, {1} la {2}".format(numb1, numb2, tong)
    return str(numb1 + numb2)


if __name__ == '__main__':      
  app.run(debug=True)
 
 