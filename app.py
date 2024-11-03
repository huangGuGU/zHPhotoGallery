import cv2
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import logging
app = Flask(__name__)
file_handler = logging.FileHandler('flask.log')
file_handler.setLevel(logging.DEBUG)
app.logger.addHandler(file_handler)
path = r'static/images'
city_name = os.listdir(path)
try:
    city_name.remove('.DS_Store')
except:
    pass

city_images = {}
for city in city_name:
    img_name = [f for f in os.listdir(os.path.join(path, city)) if f.endswith('.jpg') or f.endswith('.png')]
    img_name = [os.path.join(city, f) for f in img_name]
    vertical = []
    horizontal = []
    for i in img_name:
        img = cv2.imread(os.path.join("static/images", i))
        if img.shape[0] < img.shape[1]:
            horizontal.append(i)
        else:
            vertical.append(i)
    city_images[city] = [horizontal, vertical]


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gallery.db'
db = SQLAlchemy(app)
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    likes = db.Column(db.Integer, default=0)



@app.route('/gallery')
def gallery():
    print(city)
    images = city_images[city]  # 确保这里的 city 是定义过的
    # 获取所有图片的点赞数据
    image_likes = {image.name: image.likes for image in Image.query.all()}
    return render_template('gallery.html', images=images, image_likes=image_likes)


@app.route('/like_image', methods=['POST'])
def like_image():
    data = request.get_json()
    image_name = data.get('image')

    # 查找图片并增加点赞数
    image = Image.query.filter_by(name=image_name).first()
    if image:
        image.likes += 1
    else:
        image = Image(name=image_name, likes=1)
        db.session.add(image)

    db.session.commit()
    return jsonify({'likes': image.likes})

@app.route('/')
def hello_page():
    return render_template('hello.html')


@app.route('/choose_city')
def choose_city_index():
    return render_template('choose_city.html')


@app.route('/choose_city/<city>')
def city_gallery(city):
    images = city_images.get(city)
    image_likes = {image.name: image.likes for image in Image.query.all()}
    return render_template('gallery.html', images=images, image_likes=image_likes, city=city)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=443,
            ssl_context=('/Users/hzh/Library/Mobile Documents/com~apple~CloudDocs/程序/网页设计/utils/zhphotography.site_bundle.pem', '/Users/hzh/Library/Mobile Documents/com~apple~CloudDocs/程序/网页设计/utils/zhphotography.site.key'))
