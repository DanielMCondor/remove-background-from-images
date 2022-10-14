from rembg import remove
from PIL import Image

img = Image.open('img/photo.jpg')
img_without_back = remove(img)
img_without_back.save('img/photo.png')
