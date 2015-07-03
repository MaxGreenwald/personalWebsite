from flask import Flask, send_from_directory, render_template
app = Flask(__name__)
import settings

@app.route('/')
def home():
    return send_from_directory('templates', 'home.html')

@app.route('/blog')
def home():
    return send_from_directory('templates', 'blog.html')

if __name__ == '__main__':
    app.run(settings.HOST, debug = settings.DEBUG)