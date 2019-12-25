from GUI.widget import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import glob
import shutil
# import cv2
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
        self.list_widget = self.ui.listWidget
        self.list_widget.clicked.connect(self.slot_list_widget)
        self.img_widget = self.ui.show_img_widget
        self.label_show = self.ui.label
        self.files = None  # 所有图片的文件夹
        self.default_dir = None
        self.current_img_index = -1
        self.length = 0
        self.img_name = ''
        # 设置按钮快捷键
        self.set_shortcut()

    def set_shortcut(self):
        self.ui.next_btn.setShortcut('w')
        self.ui.previous_btn.setShortcut('e')
        self.ui.selectbtn.setShortcut('l')

    def slot_list_widget(self, item):
        print('list widget...')
        if self.list_widget.count() != 0:
            self.current_img_index = item.row()
            self.refresh_img()

    def slot_opendir(self):
        if self.files is not None:
            print('已经选中文件夹.....')
            return
        print('opendir')
        dir = QtWidgets.QFileDialog.getExistingDirectory(caption='选择打开的文件夹',
                                                         directory='E:/water_meter/data/0-500')
        print(dir)
        # 读取文件并按照文件名里面的数字大小排序
        self.files = sorted(glob.glob('{}/*'.format(dir)), key=lambda x: int(x.split('\\')[-1].split('.')[0]))
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
        self.img_name = path.split('\\')[-1]
        print('img_name:{}'.format(self.img_name))
        pixmap = QtGui.QPixmap(path)
        self.img_widget.setPixmap(pixmap)
        self.label_show.setText('当前显示的图片为：{}'.format(self.img_name))

    def slot_next_btn(self):
        print('next image')
        self.current_img_index += 1
        self.current_img_index %= self.length
        self.refresh_img()

    def slot_previous_btn(self):
        print('previous image')
        self.current_img_index = self.current_img_index - 1 if self.current_img_index >= 0 else 0
        self.refresh_img()

    def slot_set_default_dir(self):
        print('set default dir')
        self.default_dir = QtWidgets.QFileDialog.getExistingDirectory(caption='选择打开的文件夹')

    def slot_select_image(self):
        print('选中图片:{}'.format(self.img_name))
        if self.default_dir is None:
            print('请设置默认文件夹...')
            QtWidgets.QMessageBox.warning(self, '警告', self.tr('请选择要默认保存文件夹!!!'), QMessageBox.Close)
            return
        path = os.path.join(self.default_dir, self.img_name)
        print('path:{}'.format(path))
        shutil.copy(self.files[self.current_img_index], path)
        str_infor = '复制成功！目的路径为:{}'.format(path)
        self.label_show.setText(str_infor)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
