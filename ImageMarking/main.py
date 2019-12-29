from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ImageMarking.widget import Ui_MainWindow
import glob
import os
from PyQt5.Qt import *
import cv2
import numpy as np
from ImageMarking.model import Mode


class MainWindow(QtWidgets.QMainWindow):

    BASE_RATIO = 0.3  # 基础放大倍率

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.opendirbtn.clicked.connect(self.slot_opendir)
        self.ui.nextbtn.clicked.connect(self.slot_next_btn)
        self.ui.previousbtn.clicked.connect(self.slot_previous_btn)
        self.ui.setdefaultdirbtn.clicked.connect(self.slot_set_default_dir)
        self.ui.savebtn.clicked.connect(self.slot_save_txt)
        self.ui.zoom_inbtn.clicked.connect(self.slot_zoom_in)
        self.ui.zoom_out_btn.clicked.connect(self.slot_zoom_out)
        self.list_widget = self.ui.listWidget
        self.list_widget.clicked.connect(self.slot_list_widget)
        self.ui.markinbtn.clicked.connect(self.slot_marking)
        self.ui.drag_imgbtn.clicked.connect(self.slot_drag)
        self.img_widget = self.ui.img_show
        self.label_show = self.ui.label
        self.files = None  # 所有图片的文件夹
        self.default_dir = None
        self.current_img_index = -1
        self.length = 0
        self.img_name = ''
        self.label_show.setAlignment(Qt.AlignCenter)
        self.img = None
        self.back_img = None
        self.scale_ratio = 1
        self.offset_x = 0
        self.offset_y = 0
        self.translation_offset_x = 0
        self.translation_offset_y = 0

    def slot_marking(self):
        print('开始打标模式')
        self.img_widget.set_mode(Mode.MARKING)

    def slot_drag(self):
        print('拖动图像的模式')
        self.img_widget.set_mode(Mode.DRAG)

    def zoom_refresh(self):
        mouse_point = self.img_widget.get_mouse_point()
        mouse_x = mouse_point.x
        mouse_y = mouse_point.y
        print('mouse point x:{}\ty:{}'.format(mouse_point.x, mouse_point.y))
        # 先保证图像在鼠标的相对位置不变
        new_x = int(mouse_x * self.scale_ratio)
        new_y = int(mouse_y * self.scale_ratio)
        offset_x = new_x - mouse_x
        offset_y = new_y - mouse_y
        self.offset_x = (self.scale_ratio - 1) * mouse_x
        self.offset_y = (self.scale_ratio - 1) * mouse_y
        # 裁剪图片
        self.img = self.img[offset_y:, offset_x:, :]
        print('offset x:{}\toffset y:{}'.format(offset_x, offset_y))
        print('scale ratio：{}'.format(self.scale_ratio))
        # [h, w, c] = self.img.shape
        # q_img = QtGui.QImage(self.img.data.tobytes(), w, h, w * c, QtGui.QImage.Format_RGB888)
        # self.img_widget.set_img(q_img)
        self.img_widget.set_img(self.img)
        self.img_widget.set_offset(self.offset_x, self.offset_y)
        self.img_widget.set_scale_ratio(self.scale_ratio)

    def slot_zoom_in(self):
        print('图像放大')
        if self.img is None:
            print('请先选择图片')
            return
        if self.translation_offset_x == 0:
            self.translation_offset_x, self.translation_offset_y = self.img_widget.get_translation_offset()
            print('self.translation_offset_x:{}\ttranslation_offset_y:{}'.format(self.translation_offset_x,
                                                                                 self.translation_offset_y))
            self.back_img = self.back_img[self.translation_offset_y:, self.translation_offset_x:, :]
        # self.back_img = self.img_widget.cv_img
        [h, w, c] = self.back_img.shape
        self.scale_ratio += MainWindow.BASE_RATIO
        self.img = np.zeros(shape=(h, w, c), dtype=np.uint8)
        self.img[...] = self.back_img[...]
        self.img = cv2.resize(self.img, (int(w * self.scale_ratio), int(h * self.scale_ratio)))
        self.zoom_refresh()

    def slot_zoom_out(self):
        print('图像缩小')
        if self.img is None:
            print('请先选择图片先')
            return
        [h, w, c] = self.back_img.shape
        # self.scale_count = 0 if self.scale_count <= 0 else self.scale_count - 1
        self.scale_ratio = 1 if self.scale_ratio <= 1 else self.scale_ratio - MainWindow.BASE_RATIO
        new_h = int(h * self.scale_ratio)
        new_w = int(w * self.scale_ratio)
        print('new_h:{}\tnewe_w:{}\th:{}\tw:{}'.format(new_h, new_w, h, w))
        self.img = np.zeros(shape=(h, w, c), dtype=np.uint8)
        self.img[...] = self.back_img[...]
        self.img = cv2.resize(self.img, (new_w, new_h))
        self.zoom_refresh()

    def slot_list_widget(self, item):
        print('list widget...')
        if self.list_widget.count() != 0:
            self.current_img_index = item.row()
            self.refresh_img()

    def slot_opendir(self):
        print('opendir')
        dir = QtWidgets.QFileDialog.getExistingDirectory(caption='选择打开的文件夹',
                                                         directory='E:/water_meter/data/test')
        print(dir)
        # 读取文件并按照文件名里面的数字大小排序
        self.files = sorted(glob.glob('{}/*'.format(dir)), key=lambda x: int(x.split('\\')[-1].split('.')[0]))
        print(self.files)
        self.length = len(self.files)
        for item in self.files:
            self.list_widget.addItem(item)

    def clear_state(self):
        self.scale_ratio = 1
        self.offset_x = 0
        self.offset_y = 0
        self.translation_offset_x = 0
        self.translation_offset_y = 0
        self.img_widget.clear_shape()

    def refresh_img(self):
        if self.files is None:
            print('请选择文件夹')
            QtWidgets.QMessageBox.warning(self, '警告', self.tr('请选择文件夹!!!'), QMessageBox.Close)
            return
        # self.img_widget.clear_shape()
        self.clear_state()
        path = self.files[self.current_img_index]
        self.img_name = path.split('\\')[-1]
        print('img_name:{}'.format(self.img_name))
        self.img = cv2.imread(path)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        [h, w, c] = self.img.shape
        self.back_img = np.zeros(shape=(h, w, c), dtype=np.uint8)
        self.back_img[...] = self.img[...]
        self.scale_ratio = 1
        self.img_widget.set_WH(w, h)
        # q_img = QtGui.QImage(self.img.data, w, h, w * c, QtGui.QImage.Format_RGB888)
        # self.img_widget.set_img(q_img)
        self.img_widget.set_img(self.img)
        self.label_show.setText('当前显示的图片为：{}'.format(self.img_name))

    def slot_next_btn(self):
        print('next image')
        self.current_img_index = self.current_img_index + 1 if self.current_img_index < self.length - 1 else self.length - 1
        self.refresh_img()

    def slot_previous_btn(self):
        print('previous image')
        self.current_img_index = self.current_img_index - 1 if self.current_img_index >= 0 else 0
        self.refresh_img()

    def slot_set_default_dir(self):
        print('set default dir')
        self.default_dir = QtWidgets.QFileDialog.getExistingDirectory(caption='选择要保存Txt文件的默认文件夹')

    def slot_save_txt(self):
        if self.default_dir is None:
            print('请选择保存txt的文件夹...')
            QtWidgets.QMessageBox.warning(self, '警告', self.tr('请选择要保存txt的文件夹!!'), QMessageBox.Close)
            self.default_dir = QtWidgets.QFileDialog.getExistingDirectory(caption='选择要保存Txt文件的默认文件夹')
            return
        path = os.path.join(self.default_dir, '{}.txt'.format(self.img_name.split('.')[0]))
        infor_str = '保存成功！保存的路径在:{}'.format(path)
        self.label_show.setText(infor_str)
        print(path)
        self.img_widget.write_file(path)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
