import base64


def convert(img_data, filename):
    file_content = base64.b64decode(img_data)
    with open(filename, "w") as f:
        f.write(file_content.decode("utf-8"))
