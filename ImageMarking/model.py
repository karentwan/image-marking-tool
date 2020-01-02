from PyQt5.Qt import *
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np


class Shape(object):

    def __init__(self):
        self.ltx = 0
        self.lty = 0
        self.rbx = 0
        self.rby = 0
        self.lbx = 0
        self.lby = 0
        self.rtx = 0
        self.rty = 0
        self.width = 0
        self.height = 0
        # 要保存在txt文件里面的坐标
        self.ltx_ = None
        self.lty_ = None
        self.rbx_ = None
        self.rby_ = None
        self.lbx_ = None
        self.lby_ = None
        self.rtx_ = None
        self.rty_ = None
        self.offset_x = 0
        self.offset_y = 0
        self.scale_ratio = 1
        self.temp_offset_x = 0
        self.temp_offset_y = 0
        self.translation_offset_x = 0
        self.translation_offset_y = 0

    def set_offset(self, x, y):
        self.offset_x = x
        self.offset_y = y

    def set_temp_offset(self, x, y):
        self.temp_offset_x = x
        self.temp_offset_y = y
        # print('self.temp_offset_x:{}\tself.temp_offset_y:{}'.format(self.temp_offset_x, self.temp_offset_y))
        if self.temp_offset_x < 0:
            self.translation_offset_x -= self.temp_offset_x
        if self.temp_offset_y < 0:
            self.translation_offset_y -= self.temp_offset_y

    def set_scale_ratio(self, scale_ratio):
        self.scale_ratio = scale_ratio

    def set_WH(self, width, height):
        self.width = width
        self.height = height

    def set_lt(self, ltx, lty):
        self.ltx = ltx
        self.lty = lty
        ltx += self.offset_x
        ltx /= self.scale_ratio
        lty += self.offset_y
        lty /= self.scale_ratio
        ltx += self.translation_offset_x
        lty += self.translation_offset_y
        # print('offset_x:{}  offset_y:{} '
        #       ' scale ratio:{}  ltx:{} '
        #       ' lty:{} origin x:{}  origin y:{}'.format(self.offset_x, self.offset_y,
        #                                                 self.scale_ratio, self.ltx, self.lty, ltx, lty))
        self.ltx_ = str(round(ltx / self.width * 1000000) / 1000000)
        self.lty_ = str(round(lty / self.height * 1000000) / 1000000)

    def set_rt(self, rtx, rty):
        self.rtx = rtx
        self.rty = rty
        rtx += self.offset_x
        rtx /= self.scale_ratio
        rty += self.offset_y
        rty /= self.scale_ratio
        rtx += self.translation_offset_x
        rty += self.translation_offset_y
        self.rtx_ = str(round(rtx / self.width * 1000000) / 1000000)
        self.rty_ = str(round(rty / self.height * 1000000) / 1000000)

    def set_rb(self, rbx, rby):
        self.rbx = rbx
        self.rby = rby
        rbx += self.offset_x
        rbx /= self.scale_ratio
        rby += self.offset_y
        rby /= self.scale_ratio
        rbx += self.translation_offset_x
        rby += self.translation_offset_y
        self.rbx_ = str(round(rbx / self.width * 1000000) / 1000000)
        self.rby_ = str(round(rby / self.height * 1000000) / 1000000)

    def set_lb(self, lbx, lby):
        self.lbx = lbx
        self.lby = lby
        lbx += self.offset_x
        lbx /= self.scale_ratio
        lby += self.offset_y
        lby /= self.scale_ratio
        lbx += self.translation_offset_x
        lby += self.translation_offset_y
        self.lbx_ = str(round(lbx / self.width * 1000000) / 1000000)
        self.lby_ = str(round(lby / self.height * 1000000) / 1000000)

    def clear(self):
        self.ltx = 0
        self.lty = 0
        self.rbx = 0
        self.rby = 0
        self.lbx = 0
        self.lby = 0
        self.rtx = 0
        self.rty = 0
        self.width = 0
        self.height = 0
        self.ltx_ = None
        self.lty_ = None
        self.rbx_ = None
        self.rby_ = None
        self.lbx_ = None
        self.lby_ = None
        self.rtx_ = None
        self.rty_ = None
        self.offset_x = 0
        self.offset_y = 0
        self.scale_ratio = 1
        self.temp_offset_x = 0
        self.temp_offset_y = 0
        self.translation_offset_x = 0
        self.translation_offset_y = 0


class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_xy(self, x, y):
        self.x = x
        self.y = y


class Mode(object):

    MARKING = 0
    DRAG = 1


class ImageShow(QtWidgets.QLabel):

    def __init__(self, *args):
        QtWidgets.QLabel.__init__(self, *args)
        self.shape = Shape()
        self.count = 0
        self.cv_img = None   # opencv矩阵类型
        self.img = None      # QImg, 要画的图
        self.setMouseTracking(True)
        self.mouse_point = Point()
        self.mode = Mode.DRAG
        self.drag_flag = False

    def get_translation_offset(self):
        return self.shape.translation_offset_x, self.shape.translation_offset_y

    def set_mode(self, mode):
        self.mode = mode
        if self.mode == Mode.MARKING:
            self.setCursor(Qt.CrossCursor)
        else:
            self.setCursor(Qt.ArrowCursor)

    def set_scale_ratio(self, scale_ratio):
        self.shape.set_scale_ratio(scale_ratio)

    def get_offset(self):
        return self.shape.offset_x, self.shape.offset_y

    def set_offset(self, x, y):
        self.shape.set_offset(x, y)

    def get_mouse_point(self):
        return self.mouse_point

    def set_img(self, cv_img):
        self.cv_img = cv_img
        [h, w, c] = cv_img.shape
        # print('img.shape:{}'.format(img.shape))
        self.img = QtGui.QImage(cv_img.data.tobytes(), w, h, w * c, QtGui.QImage.Format_RGB888)
        self.update()

    def refresh_img(self):
        print('开始拖动图像...')
        [h, w, c] = self.cv_img.shape
        print('offset x:{}\toffset y:{}'.format(self.shape.temp_offset_x, self.shape.temp_offset_y))
        if self.shape.temp_offset_x <= 0 and self.shape.temp_offset_y <= 0:  # 左上移动
            self.cv_img = self.cv_img[-self.shape.temp_offset_y:, -self.shape.temp_offset_x:, :]
        elif self.shape.temp_offset_x < 0 and self.shape.temp_offset_y > 0:  # 左下
            pass
        elif self.shape.temp_offset_x > 0 and self.shape.temp_offset_y < 0:  # 右下
            pass
        elif self.shape.temp_offset_x > 0 and self.shape.temp_offset_y > 0:  # 右下
            pass
            # [h, w, c] = self.cv_back_img.shape
            # self.cv_img = np.zeros(shape=(h - self.shape.offset_y, w - self.shape.offset_x, c), dtype=np.uint8)
            # self.cv_img = self.cv_back_img[:h - self.shape.offset_y, :w - self.shape.offset_y, :]
        [h, w, c] = self.cv_img.shape
        self.img = QtGui.QImage(self.cv_img.data.tobytes(), w, h, w * c, QtGui.QImage.Format_RGB888)
        self.update()

    def clear_shape(self):
        self.shape.clear()
        self.count = 0

    def write_file(self, path):
        print('开始写入文件.....')
        print('offset x:{}\ty:{}'.format(self.shape.offset_x, self.shape.offset_y))
        print('img width:{}\timg height:{}'.format(self.shape.width, self.shape.height))
        with open(path, 'w') as f:
            s = '4,{},{},{},{},{},{},{},{},,'.format(self.shape.ltx_, self.shape.rtx_,
                                                     self.shape.rbx_, self.shape.lbx_,
                                                     self.shape.lty_, self.shape.rty_,
                                                     self.shape.rby_, self.shape.lby_)
            print(s)
            f.write(s)

    def set_WH(self, width, height):
        self.shape.set_WH(width, height)

    def paintEvent(self, evt):
        super(ImageShow, self).paintEvent(evt)
        painter = QtGui.QPainter(self)
        painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        if self.img is not None:
            # print('开始画图像')
            w = self.width()
            h = self.height()
            source = QRect(0, 0, w, h)
            painter.drawImage(source, self.img, source)
        if self.shape.ltx != 0 and self.shape.lty != 0:  # 左上
            x = self.shape.ltx
            y = self.shape.lty
            painter.drawEllipse(x-3, y-3, 5, 5)
        if self.shape.rtx != 0 and self.shape.rty != 0:  # 右上
            x = self.shape.rtx
            y = self.shape.rty
            painter.drawEllipse(x-3, y-3, 5, 5)
        if self.shape.rbx != 0 and self.shape.rby != 0:  # 右下
            x = self.shape.rbx
            y = self.shape.rby
            painter.drawEllipse(x-3, y-3, 5, 5)
        if self.shape.lbx != 0 and self.shape.lby != 0:  # 左下
            x = self.shape.lbx
            y = self.shape.lby
            painter.drawEllipse(x-3, y-3, 5, 5)
        # 画鼠标的十字线
        if self.mode == Mode.MARKING:
            w = self.width()
            h = self.height()
            x = self.mouse_point.x
            y = self.mouse_point.y
            if x > 0 and x < w and y > 0 and y < h:
                painter.setPen(QPen(Qt.gray, 2, Qt.SolidLine))
                painter.drawLine(QPointF(0, self.mouse_point.y), QPointF(self.width(), self.mouse_point.y))  # 水平线
                painter.drawLine(QPointF(self.mouse_point.x, 0), QPointF(self.mouse_point.x, self.height()))  # 垂直线

    def keyPressEvent(self, evt):
        super(ImageShow, self).keyPressEvent(evt)

    def keyReleaseEvent(self, evt):
        super(ImageShow, self).keyReleaseEvent(evt)

    def leaveEvent(self, evt):
        super(ImageShow, self).leaveEvent(evt)
        self.mouse_point.set_xy(0, 0)
        print('鼠标移出控件')

    def mousePressEvent(self, evt):
        super(ImageShow, self).mousePressEvent(evt)
        s = evt.pos()
        x = s.x()
        y = s.y()
        if self.mode == Mode.MARKING:
            print('选中的坐标 x:{}\ty:{}'.format(s.x(), s.y()))
            if self.count == 0:  # 左上
                self.shape.set_lt(x, y)
            elif self.count == 1:  # 右上
                self.shape.set_rt(x, y)
            elif self.count == 2:  # 右下
                self.shape.set_rb(x, y)
            elif self.count == 3:   # 左下
                self.shape.set_lb(x, y)
            self.count += 1
            self.count %= 5  # 限制在4以内
        else:
            self.drag_flag = True
        self.update()

    def mouseReleaseEvent(self, evt):
        super(ImageShow, self).mouseReleaseEvent(evt)
        self.drag_flag = False

    def mouseMoveEvent(self, evt):
        super(ImageShow, self).mouseMoveEvent(evt)
        s = evt.pos()
        x = s.x()
        y = s.y()
        if self.drag_flag is True:
            # print('-------------开始移动图像')
            offset_x = x - self.mouse_point.x
            offset_y = y - self.mouse_point.y
            if offset_x < 0 and offset_y < 0:
                self.shape.set_temp_offset(offset_x, offset_y)
                self.refresh_img()
        self.mouse_point.set_xy(x, y)
        self.update()

