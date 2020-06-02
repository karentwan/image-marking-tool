from GUI.widget import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import glob
import cv2
from PyQt5.Qt import *


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.open_dirbtn.clicked.connect(self.slot_opendir)
        self.ui.next_btn.clicked.connect(self.slot_next_btn)
        self.ui.previous_btn.clicked.connect(self.slot_previous_btn)
        self.ui.set_default_dirbtn.clicked.connect(self.slot_set_default_dir)
        self.ui.selectbtn.clicked.connect(self.slot_select_image)
        self.ui.rotate.clicked.connect(self.slot_rotate)
        self.list_widget = self.ui.listWidget
        self.list_widget.clicked.connect(self.slot_list_widget)
        self.img_widget = self.ui.show_img_widget
        self.label_show = self.ui.label
        self.label_show.setAlignment(Qt.AlignCenter)
        self.files = []  # 所有图片的文件夹
        self.default_dir = None
        self.current_img_index = -1
        self.length = 0
        self.img_name = ''
        # 设置按钮快捷键
        self.set_shortcut()
        self.img = None

    def set_shortcut(self):
        self.ui.next_btn.setShortcut('e')
        self.ui.previous_btn.setShortcut('w')
        self.ui.selectbtn.setShortcut('Return')
        self.ui.rotate.setShortcut('r')

    def slot_rotate(self):
        print('开始旋转...')
        if self.img is None:
            return
        self.img = cv2.rotate(self.img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        [h, w, c] = self.img.shape
        q_img = QtGui.QImage(self.img.data, w, h, w * c, QtGui.QImage.Format_RGB888)
        self.img_widget.setPixmap(QtGui.QPixmap.fromImage(q_img))

    def slot_list_widget(self, item):
        print('list widget...')
        if self.list_widget.count() != 0:
            self.current_img_index = item.row()
            self.refresh_img()

    def slot_opendir(self):
        print('opendir')
        dir = QtWidgets.QFileDialog.getExistingDirectory(caption='选择打开的文件夹',
                                                         directory='E:/water_meter/data/0-500')
        print(dir)
        # 读取文件并按照文件名里面的数字大小排序
        extentions = ['jpg', 'jpeg', 'png']
        for item in extentions:
            self.files.extend(glob.glob('{}/*.{}'.format(dir, item)))
        print(self.files)
        self.length = len(self.files)
        for item in self.files:
            self.list_widget.addItem(item)

    def refresh_img(self):
        if self.files is None:
            print('请选择文件夹')
            QtWidgets.QMessageBox.warning(self, '警告', self.tr('请选择文件夹!!!'), QMessageBox.Close)
            return
        path = self.files[self.current_img_index]
        self.img_name = os.path.split(path)[-1]
        print('img_name:{}'.format(self.img_name))
        ######################## 使用 opencv读取图片，然后使用QLabel显示图片
        self.img = cv2.imread(path)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        [h, w, c] = self.img.shape
        q_img = QtGui.QImage(self.img.data, w, h, w * c, QtGui.QImage.Format_RGB888)
        self.img_widget.setPixmap(QtGui.QPixmap.fromImage(q_img))
        self.label_show.setText('当前显示的图片为：{}'.format(self.img_name))

    def slot_next_btn(self):
        print('next image')
        self.current_img_index = self.current_img_index + 1 \
            if self.current_img_index < self.length - 1 else self.length - 1
        self.refresh_img()

    def slot_previous_btn(self):
        print('previous image')
        self.current_img_index = self.current_img_index - 1 if self.current_img_index > 0 else 0
        self.refresh_img()

    def slot_set_default_dir(self):
        print('set default dir')
        self.default_dir = QtWidgets.QFileDialog.getExistingDirectory(caption='选择打开的文件夹')

    def slot_select_image(self):
        print('选中图片:{}'.format(self.img_name))
        if self.default_dir is None:
            print('请设置默认文件夹...')
            QtWidgets.QMessageBox.warning(self, '警告', self.tr('请选择要默认保存文件夹!!!'), QMessageBox.Close)
            self.default_dir = QtWidgets.QFileDialog.getExistingDirectory(caption='选择要保存Txt文件的默认文件夹')
            return
        path = os.path.join(self.default_dir, self.img_name)
        print('path:{}'.format(path))
        cv2.imwrite(path, cv2.cvtColor(self.img, cv2.COLOR_RGB2BGR))
        str_infor = '已安排上!!!目的路径为:{}'.format(path)
        self.label_show.setText(str_infor)
        self.slot_next_btn()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
