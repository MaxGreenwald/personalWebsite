from flask import Flask, send_from_directory, render_template
app = Flask(__name__)

@app.route('/')
def home():
    #return 'hello'
    return send_from_directory('templates', 'bootstrapMain.html')

@app.route('/userView')
def user():
    #return 'hello'
    return send_from_directory('templates', 'userView.html')

if __name__ == '__main__':
    app.run(debug = True)