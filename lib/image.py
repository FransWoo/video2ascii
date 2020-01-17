# coding:utf-8

# @Time   : 2020/1/16 10:52
# @Author : franswu

from PIL import Image, ImageSequence


def get_xy_gray(pix, x, y):
    r, g, b = pix[x, y]
    return int(0.3 * r + 0.59 * g + 0.11 * b)


def get_average_gray(pix, offset_x, offset_y, width, height):
    return int(sum([get_xy_gray(pix, x + offset_x, y + offset_y) for x in range(width) for y in range(height)])
               / (width * height))


def get_best_seg(width, height, nw, nh):
    seg_w = int(width / nw)
    seg_h = int(height / nh)
    return int(width / seg_w), int(height / seg_h)


class ImageUtil:
    def __init__(self, op):
        self.image = Image.open(op)
        self.image = self.image.convert('RGB')
        self.width = self.image.size[0]
        self.height = self.image.size[1]
        self.pix = self.image.load()

    def seg_image(self, nw, nh):
        assert 1 <= nw <= self.width, '切割的数量必须大于等于1小于等于宽度'
        assert 1 <= nh <= self.height, '切割的数量必须大于等于1小于等于高度'
        nw, nh = get_best_seg(self.width, self.height, nw, nh)
        seg_w = int(self.width / nw)
        seg_h = int(self.height / nh)
        result = list()
        for y in range(nh):
            result.append(list())
            for x in range(nw):
                result[y].append(get_average_gray(self.pix, x * seg_w, y * seg_h, seg_w, seg_h))
        return result


class GifUtil:
    def __init__(self, op):
        self.images = ImageSequence.Iterator(Image.open(op))

    def seg_image(self, nw, nh):
        results = list()
        for image in self.images:
            image = image.convert('RGB')
            pix = image.load()
            width = image.size[0]
            height = image.size[1]
            assert 1 <= nw <= width, '切割的数量必须大于等于1小于等于宽度'
            assert 1 <= nh <= height, '切割的数量必须大于等于1小于等于高度'
            nw, nh = get_best_seg(width, height, nw, nh)
            seg_w = int(width / nw)
            seg_h = int(height / nh)
            result = list()
            for y in range(nh):
                result.append(list())
                for x in range(nw):
                    result[y].append(get_average_gray(pix, x * seg_w, y * seg_h, seg_w, seg_h))
            results.append(result)
        return results


if __name__ == '__main__':
    # im_util = GifUtil(r'E:\picture\2016071115340721509.gif')
    # imgs = im_util.seg_image(50, 50)
    # for img in imgs:
    #     for line in img:
    #         print(line)
    im_util = ImageUtil(r'E:\picture\微信图片_20200116175102.jpg')
    res = im_util.seg_image(50, 25)
    for r in res:
        print(r)
