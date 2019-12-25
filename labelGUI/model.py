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

    def set_WH(self, width, height):
        self.width = width
        self.height = height

    def set_lt(self, ltx, lty):
        self.ltx = ltx
        self.lty = lty
        self.ltx_ = str(round(ltx / self.width * 1000000) / 1000000)
        self.lty_ = str(round(lty / self.height * 1000000) / 1000000)

    def set_rt(self, rtx, rty):
        self.rtx = rtx
        self.rty = rty
        self.rtx_ = str(round(rtx / self.width * 1000000) / 1000000)
        self.rty_ = str(round(rty / self.height * 1000000) / 1000000)

    def set_rb(self, rbx, rby):
        self.rbx = rbx
        self.rby = rby
        self.rbx_ = str(round(rbx / self.width * 1000000) / 1000000)
        self.rby_ = str(round(rby / self.height * 1000000) / 1000000)

    def set_lb(self, lbx, lby):
        self.lbx = lbx
        self.lby = lby
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


class ImageShow(QtWidgets.QLabel):

    def __init__(self, *args):
        QtWidgets.QLabel.__init__(self, *args)
        self.setCursor(Qt.CrossCursor)
        self.shape = Shape()
        self.count = 0

    def clear_shape(self):
        self.shape.clear()
        self.count = 0

    def write_file(self, path):
        print('开始写入文件.....')
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
        # print('开始重绘.....')
        painter = QtGui.QPainter(self)
        painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
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

    def keyPressEvent(self, evt):
        super(ImageShow, self).keyPressEvent(evt)
        # print('键盘按下事件产生')

    def keyReleaseEvent(self, evt):
        super(ImageShow, self).keyReleaseEvent(evt)
        # print('键盘释放事件产生')

    def mousePressEvent(self, evt):
        super(ImageShow, self).mousePressEvent(evt)
        # print('鼠标按下事件产生')
        s = evt.windowPos()
        x = s.x()
        y = s.y()
        print('x:{}\ty:{}'.format(s.x(), s.y()))
        self.setMouseTracking(True)
        if self.count == 0:  # 左上
            self.shape.set_lt(x, y)
            # self.shape.ltx = x
            # self.shape.lty = y
        elif self.count == 1:  # 右上
            self.shape.set_rt(x, y)
            # self.shape.rtx = x
            # self.shape.rty = y
        elif self.count == 2:  # 右下
            self.shape.set_rb(x, y)
            # self.shape.rbx = x
            # self.shape.rby = y
        elif self.count == 3:   # 左下
            self.shape.set_lb(x, y)
            # self.shape.lbx = x
            # self.shape.lby = y
        self.count += 1
        self.count %= 5  # 限制在4以内
        self.update()

    def mouseReleaseEvent(self, evt):
        super(ImageShow, self).mouseReleaseEvent(evt)
        # print('鼠标释放事件产生')
