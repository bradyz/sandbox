from PIL import Image

try:
    i = Image.open('asdf.png')
    i.show()
except Exception as e:
    print(e)
