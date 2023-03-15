import requests
from io import BytesIO
from PIL import Image

r = requests.get(
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQl0gOVnXUPTb3jBvxTXuOa7XDkidpg67WTK1yAJXsE&s')

print("Status", r.status_code)

image = Image.open(BytesIO(r.content))

print(image.size, image.format, image.mode)

path = "./image1.jpg" + image.format

try:
    image.save(path, image.format)
except IOError:
    print("Cannot save image.")
