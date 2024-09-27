import os
from sys import argv
import skimage as ski
from skimage import io, util
import numpy as np
import random


dir_path = argv[1]
params = []
argv.pop(0)
argv.pop(0)

for param in argv:
    params.append(param)


numbers = []
image_list = []
for filename in os.listdir(dir_path):
    if filename.endswith(".jpg"):
        file_path = os.path.join(dir_path, filename)
        image_list.append(io.imread(file_path))
        number = int(os.path.splitext(filename)[0])
        numbers.append(number)
list_length = len(image_list)-1


def invert_pic(picture):
    inverted_picture = ski.util.invert(picture)
    inverted_picture = util.img_as_ubyte(inverted_picture)
    return inverted_picture


def rotate_pic(picture):
    rotated_picture = ski.transform.rotate(picture, 45)
    rotated_picture = util.img_as_ubyte(rotated_picture)
    return rotated_picture


def resize_pic(picture):
    resized_picture = ski.transform.resize(picture, ([150, 150]))
    resized_picture = util.img_as_ubyte(resized_picture)
    return resized_picture


def swirl_pic(picture):
    swirl_picture = ski.transform.swirl(picture, strength=50)
    swirl_picture = util.img_as_ubyte(swirl_picture)
    return swirl_picture


def to_gray_pic(picture):
    grey_pic = ski.color.rgb2gray(picture)
    grey_pic = util.img_as_ubyte(grey_pic)
    return grey_pic


def complex_transform_pic(picture):
    complex_pic = ski.color.rgb2gray(picture)
    complex_pic = ski.transform.swirl(complex_pic, strength=50)
    complex_pic = ski.transform.resize(complex_pic, ([150, 150]))
    complex_pic = ski.transform.rotate(complex_pic, np.pi/4)
    complex_pic = util.img_as_ubyte(complex_pic)
    return complex_pic


def save_augmented_pic(picture):
    max_num = max(numbers)
    current_index = max_num + 1
    io.imsave(f"{dir_path}/{current_index:04}.jpg", picture)


val = random.randint(0, list_length)
img = image_list[val]
augmented_pic = img.copy()

for param in params:
    if param == "--invert":
        augmented_pic = invert_pic(augmented_pic)
    elif param == "--resize":
        augmented_pic = resize_pic(augmented_pic)
    elif param == "--rotate":
        augmented_pic = rotate_pic(augmented_pic)
    elif param == "--swirl":
        augmented_pic = swirl_pic(augmented_pic)
    elif param == "--2gray":
        augmented_pic = to_gray_pic(augmented_pic)
    elif param == "--complex":
        augmented_pic = complex_transform_pic(augmented_pic)
    else:
        raise BaseException("Invalid transform parameter")
    save_augmented_pic(augmented_pic)
