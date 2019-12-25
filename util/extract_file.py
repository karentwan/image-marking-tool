import glob
import os
import shutil


def extract_image_from_dir():
    base_dir = r'E:\water_meter\train_ocr\pan'
    dst_dir = r'E:\water_meter\train_ocr\data'

    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    file_list = glob.glob('{}/*.png'.format(base_dir))

    for item in file_list:
        image_name = item.split('\\')[-1]
        shutil.copy(item, os.path.join(dst_dir, image_name))


def extract_file():
    base_dir = r'E:\water_meter\data\320'
    dst_dir = r'E:\water_meter\data\select'
    file_list = glob.glob('{}/*/*.jpg'.format(base_dir))
    for i, item in enumerate(file_list):
        print(item)
        out_name = '{}/{}.jpg'.format(dst_dir, i)
        shutil.copy(item, out_name)


if __name__ == '__main__':
    extract_file()
