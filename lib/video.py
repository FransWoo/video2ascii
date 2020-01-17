# coding:utf-8

# @Time   : 2020/1/16 11:41
# @Author : franswu

import os
import imageio
import time
import skimage
import numpy as np


class VideoUtil:
    def __init__(self, path):
        self.vid = imageio.get_reader(path, 'ffmpeg')

    def trans_gif(self, step, duration=1 / 24, delete_frame_file=True):
        output_dir = f'{os.path.abspath(os.path.dirname(__file__))}/../out'
        index = 0
        for i, img in enumerate(self.vid):
            if i % step == 0:
                image = skimage.img_as_float(img).astype(np.float64)
                imageio.imsave(f'{output_dir}/{index}.jpg', image)
                index += 1

        frames = [imageio.imread(f'{output_dir}/{i}.jpg') for i in range(index)]
        filename = f'{output_dir}/output-{int(time.time())}.gif'
        imageio.mimsave(filename, frames, 'GIF', duration=duration)
        if delete_frame_file:
            for i in range(index):
                os.remove(f'{output_dir}/{i}.jpg')
        return filename


if __name__ == '__main__':
    util = VideoUtil(r'E:\video\bar.flv')
    util.trans_gif(120)
