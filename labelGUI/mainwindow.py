from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from labelGUI.widget import Ui_MainWindow
import glob
import os
from PyQt5.Qt import *


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.opendirbtn.clicked.connect(self.slot_opendir)
        self.ui.nextbtn.clicked.connect(self.slot_next_btn)
        self.ui.previousbtn.clicked.connect(self.slot_previous_btn)
        self.ui.setdefaultdirbtn.clicked.connect(self.slot_set_default_dir)
        self.ui.savebtn.clicked.connect(self.slot_save_txt)
        self.list_widget = self.ui.listWidget
        self.img_widget = self.ui.img_show
        self.label_show = self.ui.label
        self.files = None  # 所有图片的文件夹
        self.default_dir = None
        self.current_img_index = -1
        self.length = 0
        self.img_name = ''
        # 设置软件快捷键
        self.set_shortcut()

    def set_shortcut(self):
        self.ui.nextbtn.setShortcut('w')
        self.ui.previousbtn.setShortcut('e')
        self.ui.savebtn.setShortcut('s')

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
            item_widget = QtWidgets.QListWidgetItem()
            item_widget.setText(item)
            self.list_widget.addItem(item_widget)

    def slot_next_btn(self):
        print('next image')
        if self.files is None:
            print('请选择文件夹')
            return
        self.img_widget.clear_shape()
        self.current_img_index += 1
        self.current_img_index %= self.length
        path = self.files[self.current_img_index]
        self.img_name = path.split('\\')[-1]
        print('img_name:{}'.format(self.img_name))
        pixmap = QtGui.QPixmap(path)
        width = pixmap.width()
        height = pixmap.height()
        self.ui.img_show.setFixedSize(width, height)
        label_wdith = self.ui.img_show.width()
        label_height = self.ui.img_show.height()
        print('label_width:{}\tlabel_height:{}'.format(label_wdith, label_height))
        print('width:{}\theight:{}'.format(width, height))
        self.img_widget.set_WH(width, height)
        self.img_widget.setPixmap(pixmap)
        self.label_show.setAlignment(Qt.AlignCenter)
        self.label_show.setText('当前显示的图片为：{}'.format(self.img_name))

    def slot_previous_btn(self):
        print('previous image')
        self.current_img_index -= 1
        if self.current_img_index < 0:
            self.current_img_index = 0
        self.img_widget.clear_shape()
        path = self.files[self.current_img_index]
        self.img_name = path.split('\\')[-1]
        pixmap = QtGui.QPixmap(path)
        width = pixmap.width()
        height = pixmap.height()
        self.ui.img_show.setFixedSize(width, height)
        label_wdith = self.ui.img_show.width()
        label_height = self.ui.img_show.height()
        print('label_width:{}\tlabel_height:{}'.format(label_wdith, label_height))
        print('width:{}\theight:{}'.format(width, height))
        self.img_widget.set_WH(width, height)
        self.img_widget.setPixmap(pixmap)
        self.label_show.setText('当前显示的图片为：{}'.format(self.img_name))

    def slot_set_default_dir(self):
        print('set default dir')
        self.default_dir = QtWidgets.QFileDialog.getExistingDirectory(caption='选择打开的文件夹')

    def slot_save_txt(self):
        if self.default_dir is None:
            print('请选择保存txt的文件夹...')
            return
        path = os.path.join(self.default_dir, '{}.txt'.format(self.img_name.split('.')[0]))
        print(path)
        self.img_widget.write_file(path)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
