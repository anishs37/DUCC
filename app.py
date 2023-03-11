from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html', active={
        'home': True,
        'about': False,
        'tutorial': False,
        'upload': False
    })
