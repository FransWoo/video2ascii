# coding:utf-8

# @Time   : 2020/1/16 11:41
# @Author : franswu

from PIL import Image
import imageio
import cv2
import skimage
import numpy as np
from bin.image2ascii import get_gray_str
from io import BytesIO as Bytes2Data


class VideoUtil:
    def __init__(self, path):
        # self.vid = imageio.get_reader(path, 'ffmpeg')
        self.vc = cv2.VideoCapture(path)

    def trans_images(self, step):
        images = list()
        i = 0
        while True:
            rval, frame = self.vc.read()
            cv2.imshow("capture", frame)
            if not rval:
                break
            i += 1
            if i % step == 0:
                images.append(frame)
        self.vc.release()
        # for i, img in enumerate(self.vid):
        #     if i % step == 0:
        #         image1 = Image.open(BytesIO(skimage.img_as_float(img).astype(np.float64)))
        #         # image2 = Image.open(BytesIO(skimage.img_as_ubyte(img)))
        #         # image2 = Image.open(BytesIO(img))
        #         # image = skimage.img_as_float(img).astype(np.float32)
        #         # image = skimage.img_as_ubyte(img)
        #         images.append(img)
        #         print(type(img))
        return images

from io import BytesIO
if __name__ == '__main__':
    util = VideoUtil(r'E:\video\bar.flv')
    images = util.trans_images(120)
    print(images)
    # for img in images:
    #     fp = Bytes2Data(img)
    #     # image = Image.open(BytesIO(img))
    #     gray_list = get_gray_str(img, 150, 50)
    #     for gray in gray_list:
    #         print(gray)
