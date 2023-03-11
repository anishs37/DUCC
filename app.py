from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html', active={
        'home': True,
        'about': False,
        'tutorial': True,
        'upload': False
    })

@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')

app.debug = True
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)