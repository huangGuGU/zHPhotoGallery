import cv2
from flask import Flask, render_template
import os

app = Flask(__name__)

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


@app.route('/')
def choose_city_index():
    return render_template('choose_city.html')


@app.route('/<city>')
def city_gallery(city):
    print(city)
    print(city_images)
    images = city_images.get(city)
    print(images)
    return render_template('gallery.html', city=city, images=images)


if __name__ == '__main__':
    app.run(debug=False, port=5001)
