import cv2
import os


input_img = r'E:\water_meter\data\all_img'
output_txt = r'E:\water_meter\data\label'
image_name = '0.jpg'

img = cv2.imread(os.path.join(input_img, image_name))
txt_file = os.path.join(output_txt, '{}.txt'.format(image_name.split('.')[0]))
print('txt_file:{}'.format(txt_file))
size = img.shape
print(size)


class Shape(object):

    def __init__(self):
        self.key = 0
        self.tlx = 0
        self.tly = 0
        self.brx = 0
        self.bry = 0
        self.blx = 0
        self.bly = 0
        self.trx = 0
        self.try_ = 0


shape = Shape()


def handle_mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if shape.key == 0:
            shape.tlx = str(round(x/size[1] * 1000000) / 1000000)
            shape.tly = str(round(y/size[0] * 1000000) / 1000000)
            shape.key += 1
            print('key 0')
        elif shape.key == 1:
            print('key 1')
            shape.trx = str(round(x/size[1] * 1000000) / 1000000)
            shape.try_ = str(round(y/size[0] * 1000000) / 1000000)
            shape.key += 1
        elif shape.key == 2:
            print('key 2')
            shape.brx = str(round(x / size[1] * 1000000) / 1000000)
            shape.bry = str(round(y / size[0] * 1000000) / 1000000)
            shape.key += 1
        elif shape.key == 3:
            print('key 3')
            shape.blx = str(round(x / size[1] * 1000000) / 1000000)
            shape.bly = str(round(y / size[0] * 1000000) / 1000000)
            shape.key += 1
        xy = "%d,%d" % (x, y)
        print(xy)
        cv2.circle(img, (x, y), 1, (255, 0, 0), thickness=-1)
        cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (0, 0, 0), thickness=1)
        cv2.imshow("image", img)


cv2.namedWindow("image")
cv2.setMouseCallback("image", handle_mouse_event)
cv2.imshow("image", img)

while (True):
    try:
        cv2.waitKey(100)
        if shape.key == 4:
            with open(txt_file, 'w') as f:
                s = '4,{},{},{},{},{},{},{},{},,'.format(shape.tlx, shape.trx,
                                                           shape.brx, shape.blx, 
                                                           shape.tly, shape.try_,
                                                           shape.bry, shape.bly)
                print(s)
                f.write(s)
            print('over...')
            shape.key += 1
            cv2.destroyAllWindows()
            break
    except Exception:
        cv2.destroyWindow("image")
        break
