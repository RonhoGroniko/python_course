from PIL import Image
import os
from sys import argv

params = argv
params.pop(0)

filetype = None
flag = False

for param in params:
    if param == "--ftype" and flag is False:
        flag = True
    elif flag is True:
        filetype = param
        flag = False


if filetype is None:
    raise BaseException("No --ftype parameter")

for filename in os.listdir("."):
    file_extension = filename.split(".").pop()
    if file_extension == filetype:
        with Image.open(filename) as img:
            img = img.resize((50, 50))
            img.show()
