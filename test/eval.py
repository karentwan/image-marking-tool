import cv2
import os


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
    # cv2.namedWindow('image show')
    # cv2.imshow('image show', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    cv2.imwrite(os.path.join(outpath, '{}.jpg'.format(name)), img)


if __name__ == '__main__':
    root_dir = r'E:\water_meter\license_plate\label'
    file_list = os.listdir(root_dir)
    outpath = r'E:\water_meter\license_plate\test'
    for item in file_list:
        name = item.split('.')[0]
        eval(name, outpath)
