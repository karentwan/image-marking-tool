from PyQt5.Qt import *
from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.scale_ratio = 1.

    def set_scale_ratio(self, scale_ratio):
        self.scale_ratio = scale_ratio

    def set_WH(self, width, height):
        self.width = width
        self.height = height

    def set_lt(self, ltx, lty):
        self.ltx = ltx
        self.lty = lty
        ltx /= self.scale_ratio
        lty /= self.scale_ratio
        self.ltx_ = str(round(ltx / self.width * 1000000) / 1000000)
        self.lty_ = str(round(lty / self.height * 1000000) / 1000000)

    def set_rt(self, rtx, rty):
        self.rtx = rtx
        self.rty = rty
        rtx /= self.scale_ratio
        rty /= self.scale_ratio
        self.rtx_ = str(round(rtx / self.width * 1000000) / 1000000)
        self.rty_ = str(round(rty / self.height * 1000000) / 1000000)

    def set_rb(self, rbx, rby):
        self.rbx = rbx
        self.rby = rby
        rbx /= self.scale_ratio
        rby /= self.scale_ratio
        self.rbx_ = str(round(rbx / self.width * 1000000) / 1000000)
        self.rby_ = str(round(rby / self.height * 1000000) / 1000000)

    def set_lb(self, lbx, lby):
        self.lbx = lbx
        self.lby = lby
        lbx /= self.scale_ratio
        lby /= self.scale_ratio
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
        self.scale_ratio = 1


class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_xy(self, x, y):
        self.x = x
        self.y = y


class ImageShow(QtWidgets.QLabel):

    def __init__(self, *args):
        QtWidgets.QLabel.__init__(self, *args)
        self.shape = Shape()
        self.count = 0
        self.cv_img = None   # opencv矩阵类型
        self.img = None      # QImg, 要画的图
        self.setMouseTracking(True)
        self.mouse_point = Point()
        self.start_mark = False

    def switch_mode(self):
        if self.start_mark:
            self.setCursor(Qt.CrossCursor)
        else:
            self.setCursor(Qt.ArrowCursor)
        self.update()

    def start_work(self):
        self.start_mark = True
        self.switch_mode()

    def exit_work(self):
        self.start_mark = False
        self.switch_mode()

    def set_scale_ratio(self, scale_ratio):
        self.shape.set_scale_ratio(scale_ratio)

    def get_mouse_point(self):
        return self.mouse_point

    def set_img(self, cv_img):
        self.cv_img = cv_img
        [h, w, c] = cv_img.shape
        self.img = QtGui.QImage(cv_img.data.tobytes(), w, h, w * c, QtGui.QImage.Format_RGB888)
        self.update()

    def clear_shape(self):
        self.shape.clear()
        self.count = 0

    def write_file(self, path):
        print('开始写入文件.....')
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
        painter.setPen(QPen(Qt.white, 2, Qt.SolidLine))
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
        if self.start_mark:
            w = self.width()
            h = self.height()
            x = self.mouse_point.x
            y = self.mouse_point.y
            # 如果鼠标在屏幕内, 则根据鼠标的位置画屏幕线
            if x > 0 and x < w and y > 0 and y < h:
                painter.setPen(QPen(Qt.gray, 2, Qt.SolidLine))
                painter.drawLine(QPointF(0, self.mouse_point.y), QPointF(self.width(), self.mouse_point.y))  # 水平线
                painter.drawLine(QPointF(self.mouse_point.x, 0), QPointF(self.mouse_point.x, self.height()))  # 垂直线

    def leaveEvent(self, evt):
        super(ImageShow, self).leaveEvent(evt)
        self.mouse_point.set_xy(0, 0)
        print('鼠标移出控件')

    def mousePressEvent(self, evt):
        super(ImageShow, self).mousePressEvent(evt)
        s = evt.pos()
        x = s.x()
        y = s.y()
        if self.start_mark:
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
        self.update()

    def mouseReleaseEvent(self, evt):
        super(ImageShow, self).mouseReleaseEvent(evt)

    def mouseMoveEvent(self, evt):
        super(ImageShow, self).mouseMoveEvent(evt)
        s = evt.pos()
        x = s.x()
        y = s.y()
        self.mouse_point.set_xy(x, y)
        self.update()

