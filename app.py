from flask import Flask, render_template, url_for, request, Response
import os
from werkzeug.utils import redirect, secure_filename
from sqlalchemy.orm import defaultload
from models import Img
from database import db_init, db

IMAGES_FOLDER = 'static/images/'

app = Flask(__name__)

app.config['IMAGES_FOLDER'] = IMAGES_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db_init(app)


@app.route('/', methods=['GET'])
def getall_images():
    try:
        images = Img.query.order_by(Img.date_created).all()
        print(images)
        return render_template('index.html', images=images)
    except:
        return render_template('index.html')



@app.route('/', methods=['POST'])
def upload_image():
    file = request.files['file']
    if file:
        filename = secure_filename(file.filename)
        mimetype = file.mimetype
        img = Img(img=file.read(), mimetype=mimetype, name=filename)
        db.session.add(img)
        db.session.commit()
        return 'Image has been uploaded!'


@app.route('/show/<int:id>', methods=['GET'])
def display_image(id):
    image = Img.query.filter_by(id=id).first()
    if not image:
        return 'No image with that id'
    return Response(image.img, mimetype=image.mimetype)

if __name__ == "__main__":
    app.run(debug=True)
