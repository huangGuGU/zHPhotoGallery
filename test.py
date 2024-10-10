import os
import cv2
path = r'static/images'
city_name = os.listdir(path)
try:
    city_name.remove('.DS_Store')
except:
    pass

city_images = {}
for city in city_name:
    img_name = [f for f in os.listdir(os.path.join(path, city)) if f.endswith('.jpg') or f.endswith('.png')]
    img_name = [os.path.join(city,f) for f in img_name ]
    vertical = []
    horizontal = []
    for i in img_name:
        img = cv2.imread(os.path.join("static/images",i))
        if img.shape[0]<img.shape[1]:
            horizontal.append(i)
        else:
            vertical.append(i)
    city_images[city] = [horizontal,vertical]


print(city_images)



