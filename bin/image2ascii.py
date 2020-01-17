# coding:utf-8

# @Time   : 2020/1/16 11:45
# @Author : franswu

import sys
import os
from argparse import ArgumentParser
sys.path.append(f'{os.path.abspath(os.path.dirname(__file__))}/..')
from lib.image import ImageUtil, GifUtil


GRAY_STR = """@#$%MEWHXA8D4wp03u?7i{+tc*!<"~:,^`. """


def get_gray_str(util, nw, nh):
    if isinstance(util, ImageUtil):
        res_list = util.seg_image(nw, nh)
        return [''.join(map(lambda x: GRAY_STR[int(x*(len(GRAY_STR)-1)/255)], res)) for res in res_list]
    elif isinstance(util, GifUtil):
        image_list = util.seg_image(nw, nh)
        return [[''.join(map(lambda x: GRAY_STR[int(x*(len(GRAY_STR)-1)/255)], res)) for res in image] for image in image_list]


def main(path, nw, nh):
    util = ImageUtil(path)
    gray_list = get_gray_str(util, nw, nh)
    for gray in gray_list:
        print(gray)


def gif_main(path, nw, nh):
    util = GifUtil(path)
    gray_image_list = get_gray_str(util, nw, nh)
    for gray_image in gray_image_list:
        os.system('cls')
        print('\n'.join(gray_image), flush=True)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--path', type=str, required=True, help='图片路径')
    parser.add_argument('--nw', type=int, required=True, help='图片宽度分割数量')
    parser.add_argument('--nh', type=int, required=True, help='图片高度分割数量')
    parser.add_argument('--gif', action='store_true', help='图片高度分割数量')
    args = parser.parse_args()
    if args.gif:
        gif_main(args.path, args.nw, args.nh)
    else:
        main(args.path, args.nw, args.nh)
