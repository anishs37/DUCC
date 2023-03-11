from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html', active={
        'home': True,
        'about': False,
        'tutorial': False,
        'upload': False
    })

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    return render_template('upload.html', active={
        'home': False,
        'about': False,
        'tutorial': False,
        'upload': True
    })