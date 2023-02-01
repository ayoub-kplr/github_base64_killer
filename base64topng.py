import base64


def convert(img_data, filename):
    imgdata = base64.b64decode(img_data)
    with open(filename, 'wb') as f:
        f.write(imgdata)
