import xml.etree.ElementTree as ET
import os
import glob

classes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h


# 对于单个xml的处理
def convert_annotation(image_add, file_path, label_path):
    image_name = image_add.split('/')[-1]
    print(image_name)
    image_name = image_name.replace('.png', '')  # 删除后缀，现在只有文件名
    in_file = open(os.path.join(file_path, '{}.xml'.format(image_name)))  # 图片对应的xml地址
    out_file = open(os.path.join(label_path, '{}.txt'.format(image_name)), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    # 在一个XML中每个Object的迭代
    for obj in root.iter('object'):
        # iter()方法可以递归遍历元素/树的所有子元素
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        # 如果训练标签中的品种不在程序预定品种，或者difficult = 1，跳过此object
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)  # 这里取索引，避免类别名是中文，之后运行yolo时要在cfg将索引与具体类别配对
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(
            xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


def generate_txt(label_path, train_path, file_path):
    if not os.path.exists(label_path):  # 不存在文件夹
        os.makedirs(label_path)
    image_adds = open(train_path)
    for image_add in image_adds:
        image_add = image_add.strip()
        convert_annotation(image_add, file_path, label_path)


def generate_train_txt(root, train_path, prefix=None):
    file_list = glob.glob('{}/*.png'.format(root))
    # file_list = os.listdir(root)
    file_list = [item.split('\\')[-1] for item in file_list]
    if prefix is None:
        file_list = [os.path.join(root, item).replace('\\', '/') for item in file_list]
    else:
        file_list = [os.path.join(prefix, item).replace('\\', '/') for item in file_list]
    print(file_list)
    with open(train_path, 'w') as f:
        for item in file_list:
            f.write(item)
            f.write('\n')


if __name__ == '__main__':
    generate_train_txt(root=r'E:\water_meter\train_ocr\pan',
                       train_path="E:/water_meter/train_ocr/train.txt",
                       prefix='/home/tang/data/detection/images')
    generate_txt(label_path='E:/water_meter/train_ocr/labels',
                 train_path='E:/water_meter/train_ocr/train.txt',
                 file_path=r'E:\water_meter\train_ocr\pan')
