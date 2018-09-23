# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import time

from PIL import Image, ImageDraw, ImageFont
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_suiyin import Ui_MainWindow, jwkj_get_filePath_fileName_fileExt
from gevent import os


save=False
img_url=''
class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        try:
            imgName = self.textBrowser.toPlainText()
            self.img_list = imgName.split('\n')[self.n].replace('\"', '')
            print(self.img_list)
            jpg = QtGui.QPixmap(self.img_list).scaled(self.label_8.width(), self.label_8.height())
            self.label_8.setPixmap(jpg)
        except:
            pass
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        my_file_path=QFileDialog.getOpenFileNames(self,'打开文件','/','PNG Files (*.PNG);;JPG Files (*.JPG);;所有Files (*)')
        print(my_file_path)
        self.lineEdit.setText(str(my_file_path[0])[2:-2])


    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        my_file_path = QFileDialog.getOpenFileNames(self, '打开文件', '/','PNG Files (*.PNG);;JPG Files (*.JPG);;所有Files (*)')
        print(my_file_path)
        self.lineEdit_2.setText(str(my_file_path[0])[2:-2])

        # 自定义函数打水印
    def dashuiyin(self,img_list):
        字号 = int(self.lineEdit_5.text())
        字体 = u'%s' % self.lineEdit_4.text()
        文字和背景向上偏移=400
        文字和背景向上偏移 = 文字和背景向上偏移-int(self.verticalSlider.value())
        单独文字上下偏移 = int(self.horizontalSlider.value())
        文字左右偏移 = int(self.horizontalSlider_2.value())
        黑背景左右偏移 = 0
        文字颜色 = tuple(eval(self.lineEdit_3.text()))
        global im
        print(img_list)
        jpg = QtGui.QPixmap(img_list).scaled(self.label_8.width(), self.label_8.height())
        self.label_8.setPixmap(jpg)
        水印文字 = jwkj_get_filePath_fileName_fileExt(img_list)[1].replace(' ', '')
        file = img_list.replace('\\', '/')
        Round_picture = self.lineEdit_2.text().replace('\\', '/').replace('\"', '')
        Square_picture = self.lineEdit.text().replace('\\', '/').replace('\"', '')

        方背景宽度增加 = -int(字号*0.3)
        ttfont = ImageFont.truetype(字体, 字号)  # 字体，和字体大小
        try:
            im = Image.open(file)  # 要加文字的图
            im = im.convert('RGB')
        except:
            print('没有图片')
            return
        draw = ImageDraw.Draw(im, mode='RGBA')
        if Square_picture=='':
            print('没有选择水印')
            return
        font_background = Image.open(Square_picture)  # 水印背景圆角图
        round = Image.open(Round_picture)
        font = u'%s' % 水印文字

        im_size = im.size  # 原图大小
        font_size = ttfont.getsize(font)  # 文字尺寸
        font_background_a = font_background.resize((font_size[0] + 方背景宽度增加, font_size[1]),
                                                   Image.ANTIALIAS)  # 方背景大小尺寸
        round_W_H = round.resize((font_size[1], font_size[1]), Image.ANTIALIAS)  # 圆的大小
        pos_ads_img = (int(im_size[0] / 2 - font_background_a.size[0] / 2 + 黑背景左右偏移), 文字和背景向上偏移)  # 方图片位置
        round_ads_left = (int(pos_ads_img[0] - round_W_H.size[0] / 2), pos_ads_img[1])  # 圆图1的位置
        font_ads = (int(im_size[0] / 2 - font_size[0] / 2 + 文字左右偏移), 文字和背景向上偏移 + 单独文字上下偏移)
        round_ads_right = (int(pos_ads_img[0] + font_background_a.size[0] - round_W_H.size[0] / 2), pos_ads_img[1])

        im.paste(round_W_H, round_ads_left, mask=round_W_H)  # 圆背景摆放位置
        im.paste(round_W_H, round_ads_right, mask=round_W_H)  # 圆背景摆放位置

        im.paste(font_background_a, pos_ads_img)  # 方形摆放位置
        draw.text(font_ads, font, fill=文字颜色, font=ttfont)  # 文字摆放位置，文字，颜色
        # im.show()
        self.im = im
        im.save(r'a.png')
        if save==True:
            im.save(img_url)
        jpg = QtGui.QPixmap(r'a.png').scaled(self.label_8.width(), self.label_8.height())
        self.label_8.setPixmap(jpg)
        return self.im

    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        self.imgName = self.textBrowser.toPlainText().split('\n')
        print('点击了预览')
        img_url = self.imgName[self.n].replace('\"', '')
        self.dashuiyin(img_url)
        self.n=0

    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        global save,img_url
        print('点击了执行')
        imlis=self.textBrowser.toPlainText().split('\n')
        a_nob=1
        for i in imlis:
            self.progressBar.setValue(a_nob/len(imlis)*100)
            img_url=i.replace('\"', '')
            self.dashuiyin(img_url)
            jpg = QtGui.QPixmap(r'a.png').scaled(self.label_8.width(), self.label_8.height())
            self.label_8.setPixmap(jpg)
            save=True
            self.textBrowser_2.append(str('正在处理'+i))
            # print('正在处理',i)
            sys.stdout.flush()#系统标准刷新率
            a_nob+=1

    @pyqtSlot()
    def on_toolButton_clicked(self):
        my_file_path = QFileDialog.getOpenFileNames(self, '打开文件', 'C:\Windows','ttf Files (*.ttf);;ttc Files (*.ttc);;所有Files (*)')
        print(my_file_path)
        self.lineEdit_4.setText(str(my_file_path[0])[2:-2])

    @pyqtSlot(int)
    def on_verticalSlider_valueChanged(self, value):
        self.imgName = self.textBrowser.toPlainText().split('\n')
        print('值变了')
        vl = self.verticalSlider.value()
        self.lcdNumber_3.display(vl)
        img_url = self.imgName[self.n].replace('\"', '')
        self.dashuiyin(img_url)

    @pyqtSlot(int)
    def on_horizontalSlider_valueChanged(self, value):
        self.imgName = self.textBrowser.toPlainText().split('\n')
        print('值变了')
        # self.n = 0
        vl=self.horizontalSlider.value()
        self.lcdNumber.display(vl)
        img_url = self.imgName[self.n].replace('\"', '')
        self.dashuiyin(img_url)

    @pyqtSlot(int)
    def on_horizontalSlider_2_valueChanged(self, value):
        self.imgName = self.textBrowser.toPlainText().split('\n')
        print('值变了')
        # self.n = 0
        vl = self.horizontalSlider_2.value()
        self.lcdNumber_2.display(vl)
        img_url = self.imgName[self.n].replace('\"', '')
        self.dashuiyin(img_url)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
    

