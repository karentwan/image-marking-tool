import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

# name = '00057'


def eval(name, outpath):
    img_path = os.path.join(r'E:\water_meter\license_plate\cars_train/', '{}.jpg'.format(name))
    label = os.path.join(r'E:\water_meter\license_plate\label/', '{}.txt'.format(name))
    img = cv2.imread(img_path)
    [h, w, _] = img.shape
    print('width:{}\theight:{}'.format(w, h))
    f = open(label, 'r')
    str = f.readlines()[0]
    f.close()
    s = str.split(',')
    points = [float(s[i]) for i in range(1, 9)]
    d_points = [(int(points[0] * w), int(points[4] * h)),
                (int(points[1] * w), int(points[5] * h)),
                (int(points[2] * w), int(points[6] * h)),
                (int(points[3] * w), int(points[7] * h))]
    for p in d_points:
        print('坐标：{}'.format(p))
        cv2.circle(img, p, 1, (0, 0, 255), 4)
    cv2.imwrite(os.path.join(outpath, '{}.jpg'.format(name)), img)


def draw_box(img, box_path):
    # delimiter数据是以什么字符分割的, 默认是空格, usecols:选中要读取的列数
    pts = np.loadtxt(box_path, delimiter=',', usecols=(1, 2, 3, 4, 5, 6, 7, 8))
    pts = np.reshape(pts, (2, 4))
    wh = np.reshape(img.shape[1::-1], (2, 1))
    pts = (pts * wh).astype(np.int)
    print(pts)
    pre_point = tuple(pts[:, 0])
    for i in range(4):
        p = tuple(pts[:, i])  # numpy数组转元组
        cv2.circle(img, p, 5, color=(255, 255, 255), thickness=3)
        cv2.line(img, pre_point, p, color=(255, 255, 255), thickness=3)
        pre_point = p
    cv2.line(img, pre_point, tuple(pts[:, 0]), color=(255, 255, 255), thickness=3)


if __name__ == '__main__':
    # root_dir = r'E:\water_meter\license_plate\label'
    # file_list = os.listdir(root_dir)
    # outpath = r'E:\water_meter\license_plate\test'
    # for item in file_list:
    #     name = item.split('.')[0]
    #     eval(name, outpath)
    path = r'E:\experimental\wm_recognition\TestImg/24441.jpg'
    img = cv2.imread(path)
    img_name = os.path.split(path)[-1]
    txt_path = os.path.join(r'E:\experimental\wm_recognition\label_test', '{}.txt'.format(img_name.split('.')[0]))
    draw_box(img, txt_path)
    plt.imshow(img)
    plt.show()
