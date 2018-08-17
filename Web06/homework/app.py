from flask import *
from models.video import Video
from youtube_dl import YoutubeDL
import mlab

mlab.connect()
app = Flask(__name__)
app.secret_key = 'a super secret key' 
# session yeu cau 1 secret key




@app.route('/')
def index():
    videos = Video.objects()
    return render_template('index.html', videos = videos)

@app.route('/admin', methods = ["GET", "POST"])
def admin():
    if 'logged in' in session:
        if request.method == 'GET':
            videos = Video.objects()
            return render_template('admin.html', videos = videos)
        elif request.method == 'POST':
            form = request.form 
            link = form['link']
            
            ydl = YoutubeDL()
            data = ydl.extract_info(link, download = False)

            title = data['title']
            views = data['view_count']
            thumbnail = data['thumbnail']
            youtube_id = data['id']

            new_video = Video(
                title = title,
                thumbnail = thumbnail,
                views = views,
                youtube_id = youtube_id,
                link = link
            )
            
            new_video.save()
            return redirect(url_for('admin'))
    else:
        return "...."        
@app.route('/detail/<id>')
def detail(id):    
    return render_template ('detail.html', youtube_id = id)

@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == "POST":
        form = request.form
        user = form['username']
        password = form['password']
        # return render_template ('admin.html')
        if user == 'admin' and password == 'admin':
            session['logged in'] = True
            return redirect(url_for('admin'))
        else:
            return "Sai tên đăng nhập hoặc mật khẩu"

@app.route('/logout')
def logout():
    del session ['logged in']
    return redirect(url_for('index'))
if __name__ == '__main__':
  app.run(debug=True)
 