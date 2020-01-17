# coding:utf-8

# @Time   : 2020/1/17 11:12
# @Author : franswu

import sys
import os
from argparse import ArgumentParser
sys.path.append(f'{os.path.abspath(os.path.dirname(__file__))}/..')
from lib.video import VideoUtil
from bin.image2ascii import gif_main


def main(path, nw, nh, step, duration):
    filename = VideoUtil(path).trans_gif(step, duration)
    gif_main(filename, nw, nh)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--path', type=str, required=True, help='视频路径')
    parser.add_argument('--step', type=int, required=False, default=1, help='间隔多少帧取一个图片')
    parser.add_argument('--duration', type=float, required=False, default=1/24, help='gif速度')
    parser.add_argument('--nw', type=int, required=True, help='图片宽度分割数量')
    parser.add_argument('--nh', type=int, required=True, help='图片高度分割数量')
    args = parser.parse_args()
    main(args.path, args.nw, args.nh, args.step, args.duration)
