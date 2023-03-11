from flask import Flask, render_template, request
app = Flask(__name__)

from keras.models import load_model
from PIL import Image
import numpy as np

model = load_model('melanoma_inceptionv3.h5')

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', active={
        'home': True,
        'methods': False,
        'tutorial': False,
        'upload': False
    })

@app.route('/methods')
def methods():
    return render_template('methods.html', active={
        'home': False,
        'methods': True,
        'tutorial': False,
        'upload': False
    })

@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html', active={
        'home': False,
        'methods': False,
        'tutorial': True,
        'upload': False
    })

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']

        img = Image.open(f)
        img = img.resize((224, 224))
        img = img.convert('RGB')
        img.save('static/img/uploaded.jpg')
        img = np.array(img).reshape(-1, 224, 224, 3)

        prediction = model.predict(img)

        print(prediction)

        return render_template('result.html', prediction=prediction, active={
            'home': False,
            'methods': False,
            'tutorial': False,
            'upload': True
        })
    
    return render_template('upload.html', active={
        'home': False,
        'methods': False,
        'tutorial': False,
        'upload': True
    })

app.debug = True
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
