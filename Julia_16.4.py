'''
  Copyright 2016 Statoil ASA. 
 
  This file is part of the Open Porous Media project (OPM). 
 
  OPM is free software: you can redistribute it and/or modify 
  it under the terms of the GNU General Public License as published by 
  the Free Software Foundation, either version 3 of the License, or 
  (at your option) any later version. 
  
   OPM is distributed in the hope that it will be useful, 
   but WITHOUT ANY WARRANTY; without even the implied warranty of 
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
   GNU General Public License for more details. 
  
   You should have received a copy of the GNU General Public License 
   along with OPM.  If not, see <http://www.gnu.org/licenses/>. 
'''

from PyQt4.QtGui import (QMainWindow, QApplication)
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from Tools.CoreSimulation import *
from Tools.CTUpscaling import *
from Tools.Optimization import *
import dicom
import os
import sys
import gc
from os import listdir
from mpl_toolkits.mplot3d import Axes3D
from decimal import Decimal
from os.path import join


from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1211, 644)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 336, 590))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.splitter = QtGui.QSplitter(self.tab)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label = QtGui.QLabel(self.splitter)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.splitter)
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.splitter)
        self.splitter_2 = QtGui.QSplitter(self.tab)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.label_2 = QtGui.QLabel(self.splitter_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_2 = QtGui.QLineEdit(self.splitter_2)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.verticalLayout.addWidget(self.splitter_2)
        self.splitter_7 = QtGui.QSplitter(self.tab)
        self.splitter_7.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_7.setObjectName(_fromUtf8("splitter_7"))
        self.label_8 = QtGui.QLabel(self.splitter_7)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.comboBox = QtGui.QComboBox(self.splitter_7)
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 20))
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.verticalLayout.addWidget(self.splitter_7)
        self.splitter_3 = QtGui.QSplitter(self.tab)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.label_4 = QtGui.QLabel(self.splitter_3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalSlider = QtGui.QSlider(self.splitter_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy)
        self.horizontalSlider.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalSlider.setMaximumSize(QtCore.QSize(16777215, 20))
        self.horizontalSlider.setMaximum(500)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.verticalLayout.addWidget(self.splitter_3)
        self.splitter_4 = QtGui.QSplitter(self.tab)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName(_fromUtf8("splitter_4"))
        self.label_3 = QtGui.QLabel(self.splitter_4)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalSlider_2 = QtGui.QSlider(self.splitter_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_2.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_2.setSizePolicy(sizePolicy)
        self.horizontalSlider_2.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalSlider_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.horizontalSlider_2.setMaximum(500)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName(_fromUtf8("horizontalSlider_2"))
        self.verticalLayout.addWidget(self.splitter_4)
        self.splitter_5 = QtGui.QSplitter(self.tab)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName(_fromUtf8("splitter_5"))
        self.label_5 = QtGui.QLabel(self.splitter_5)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalSlider_3 = QtGui.QSlider(self.splitter_5)
        self.horizontalSlider_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.horizontalSlider_3.setMinimum(-50)
        self.horizontalSlider_3.setMaximum(50)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName(_fromUtf8("horizontalSlider_3"))
        self.verticalLayout.addWidget(self.splitter_5)
        self.splitter_6 = QtGui.QSplitter(self.tab)
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName(_fromUtf8("splitter_6"))
        self.label_6 = QtGui.QLabel(self.splitter_6)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalSlider_4 = QtGui.QSlider(self.splitter_6)
        self.horizontalSlider_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.horizontalSlider_4.setMinimum(-50)
        self.horizontalSlider_4.setMaximum(50)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName(_fromUtf8("horizontalSlider_4"))
        self.verticalLayout.addWidget(self.splitter_6)
        self.pushButton_3 = QtGui.QPushButton(self.tab)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout.addWidget(self.pushButton_3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.splitter_8 = QtGui.QSplitter(self.tab)
        self.splitter_8.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_8.setObjectName(_fromUtf8("splitter_8"))
        self.label_36 = QtGui.QLabel(self.splitter_8)
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.spinBox_3 = QtGui.QSpinBox(self.splitter_8)
        self.spinBox_3.setProperty("value", 5)
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.spinBox_4 = QtGui.QSpinBox(self.splitter_8)
        self.spinBox_4.setProperty("value", 5)
        self.spinBox_4.setObjectName(_fromUtf8("spinBox_4"))
        self.verticalLayout.addWidget(self.splitter_8)
        self.splitter_9 = QtGui.QSplitter(self.tab)
        self.splitter_9.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_9.setObjectName(_fromUtf8("splitter_9"))
        self.label_37 = QtGui.QLabel(self.splitter_9)
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.lineEdit_19 = QtGui.QLineEdit(self.splitter_9)
        self.lineEdit_19.setObjectName(_fromUtf8("lineEdit_19"))
        self.verticalLayout.addWidget(self.splitter_9)
        self.splitter_10 = QtGui.QSplitter(self.tab)
        self.splitter_10.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_10.setObjectName(_fromUtf8("splitter_10"))
        self.label_38 = QtGui.QLabel(self.splitter_10)
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.lineEdit_20 = QtGui.QLineEdit(self.splitter_10)
        self.lineEdit_20.setObjectName(_fromUtf8("lineEdit_20"))
        self.verticalLayout.addWidget(self.splitter_10)
        self.pushButton_6 = QtGui.QPushButton(self.tab)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.verticalLayout.addWidget(self.pushButton_6)
        spacerItem1 = QtGui.QSpacerItem(20, 24, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.progressBar = QtGui.QProgressBar(self.tab)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        self.splitter.raise_()
        self.splitter_2.raise_()
        self.splitter_3.raise_()
        self.splitter_4.raise_()
        self.splitter_5.raise_()
        self.splitter_6.raise_()
        self.splitter_7.raise_()
        self.progressBar.raise_()
        self.pushButton_3.raise_()
        self.spinBox_4.raise_()
        self.spinBox_3.raise_()
        self.label_36.raise_()
        self.pushButton_6.raise_()
        self.label_37.raise_()
        self.label_38.raise_()
        self.lineEdit_19.raise_()
        self.lineEdit_20.raise_()
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.splitter_13 = QtGui.QSplitter(self.tab_2)
        self.splitter_13.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_13.setObjectName(_fromUtf8("splitter_13"))
        self.label_7 = QtGui.QLabel(self.splitter_13)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.comboBox_2 = QtGui.QComboBox(self.splitter_13)
        self.comboBox_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.verticalLayout_2.addWidget(self.splitter_13)
        self.splitter_14 = QtGui.QSplitter(self.tab_2)
        self.splitter_14.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_14.setObjectName(_fromUtf8("splitter_14"))
        self.label_9 = QtGui.QLabel(self.splitter_14)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.spinBox = QtGui.QSpinBox(self.splitter_14)
        self.spinBox.setMaximumSize(QtCore.QSize(50, 20))
        self.spinBox.setProperty("value", 10)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.verticalLayout_2.addWidget(self.splitter_14)
        self.splitter_15 = QtGui.QSplitter(self.tab_2)
        self.splitter_15.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_15.setObjectName(_fromUtf8("splitter_15"))
        self.label_10 = QtGui.QLabel(self.splitter_15)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.spinBox_2 = QtGui.QSpinBox(self.splitter_15)
        self.spinBox_2.setMaximumSize(QtCore.QSize(50, 20))
        self.spinBox_2.setMaximum(1000)
        self.spinBox_2.setSingleStep(1)
        self.spinBox_2.setProperty("value", 100)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.verticalLayout_2.addWidget(self.splitter_15)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_12 = QtGui.QLabel(self.tab_2)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 0, 1, 1, 1)
        self.label_13 = QtGui.QLabel(self.tab_2)
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout.addWidget(self.label_13, 0, 2, 1, 1)
        self.label_14 = QtGui.QLabel(self.tab_2)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout.addWidget(self.label_14, 1, 0, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout.addWidget(self.lineEdit_4, 1, 2, 1, 1)
        self.label_15 = QtGui.QLabel(self.tab_2)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout.addWidget(self.label_15, 2, 0, 1, 1)
        self.lineEdit_5 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_5.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.gridLayout.addWidget(self.lineEdit_5, 2, 1, 1, 1)
        self.lineEdit_6 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_6.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.gridLayout.addWidget(self.lineEdit_6, 2, 2, 1, 1)
        self.label_16 = QtGui.QLabel(self.tab_2)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout.addWidget(self.label_16, 3, 0, 1, 1)
        self.lineEdit_7 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_7.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.gridLayout.addWidget(self.lineEdit_7, 3, 1, 1, 1)
        self.lineEdit_8 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_8.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.gridLayout.addWidget(self.lineEdit_8, 3, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.splitter_11 = QtGui.QSplitter(self.tab_2)
        self.splitter_11.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_11.setObjectName(_fromUtf8("splitter_11"))
        self.label_11 = QtGui.QLabel(self.splitter_11)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.lineEdit_9 = QtGui.QLineEdit(self.splitter_11)
        self.lineEdit_9.setMaximumSize(QtCore.QSize(50, 20))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.verticalLayout_2.addWidget(self.splitter_11)
        self.splitter_12 = QtGui.QSplitter(self.tab_2)
        self.splitter_12.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_12.setObjectName(_fromUtf8("splitter_12"))
        self.label_17 = QtGui.QLabel(self.splitter_12)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.lineEdit_10 = QtGui.QLineEdit(self.splitter_12)
        self.lineEdit_10.setMaximumSize(QtCore.QSize(50, 20))
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.verticalLayout_2.addWidget(self.splitter_12)
        self.pushButton_4 = QtGui.QPushButton(self.tab_2)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.verticalLayout_2.addWidget(self.pushButton_4)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.progressBar_2 = QtGui.QProgressBar(self.tab_2)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName(_fromUtf8("progressBar_2"))
        self.verticalLayout_2.addWidget(self.progressBar_2)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_18 = QtGui.QLabel(self.tab_3)
        self.label_18.setMinimumSize(QtCore.QSize(100, 0))
        self.label_18.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.verticalLayout_3.addWidget(self.label_18)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_19 = QtGui.QLabel(self.tab_3)
        self.label_19.setMinimumSize(QtCore.QSize(50, 0))
        self.label_19.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_2.addWidget(self.label_19, 0, 0, 1, 1)
        self.lineEdit_11 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_11.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEdit_11.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.gridLayout_2.addWidget(self.lineEdit_11, 0, 1, 1, 1)
        self.label_24 = QtGui.QLabel(self.tab_3)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout_2.addWidget(self.label_24, 0, 2, 1, 1)
        self.label_20 = QtGui.QLabel(self.tab_3)
        self.label_20.setMinimumSize(QtCore.QSize(50, 0))
        self.label_20.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_2.addWidget(self.label_20, 1, 0, 1, 1)
        self.lineEdit_12 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_12.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEdit_12.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.gridLayout_2.addWidget(self.lineEdit_12, 1, 1, 1, 1)
        self.label_25 = QtGui.QLabel(self.tab_3)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_2.addWidget(self.label_25, 1, 2, 1, 1)
        self.label_21 = QtGui.QLabel(self.tab_3)
        self.label_21.setMinimumSize(QtCore.QSize(50, 0))
        self.label_21.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_2.addWidget(self.label_21, 2, 0, 1, 1)
        self.lineEdit_13 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_13.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEdit_13.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.gridLayout_2.addWidget(self.lineEdit_13, 2, 1, 1, 1)
        self.label_26 = QtGui.QLabel(self.tab_3)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_2.addWidget(self.label_26, 2, 2, 1, 1)
        self.label_28 = QtGui.QLabel(self.tab_3)
        self.label_28.setMinimumSize(QtCore.QSize(50, 0))
        self.label_28.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.gridLayout_2.addWidget(self.label_28, 3, 0, 1, 1)
        self.lineEdit_16 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_16.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEdit_16.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.gridLayout_2.addWidget(self.lineEdit_16, 3, 1, 1, 1)
        self.label_27 = QtGui.QLabel(self.tab_3)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_2.addWidget(self.label_27, 3, 2, 1, 1)
        self.label_23 = QtGui.QLabel(self.tab_3)
        self.label_23.setMinimumSize(QtCore.QSize(50, 0))
        self.label_23.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_2.addWidget(self.label_23, 4, 0, 1, 1)
        self.lineEdit_15 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_15.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEdit_15.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.gridLayout_2.addWidget(self.lineEdit_15, 4, 1, 1, 1)
        self.label_30 = QtGui.QLabel(self.tab_3)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.gridLayout_2.addWidget(self.label_30, 4, 2, 1, 1)
        self.label_22 = QtGui.QLabel(self.tab_3)
        self.label_22.setMinimumSize(QtCore.QSize(50, 0))
        self.label_22.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_2.addWidget(self.label_22, 5, 0, 1, 1)
        self.lineEdit_14 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_14.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEdit_14.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.gridLayout_2.addWidget(self.lineEdit_14, 5, 1, 1, 1)
        self.label_29 = QtGui.QLabel(self.tab_3)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout_2.addWidget(self.label_29, 5, 2, 1, 1)
        self.label_31 = QtGui.QLabel(self.tab_3)
        self.label_31.setMinimumSize(QtCore.QSize(50, 0))
        self.label_31.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.gridLayout_2.addWidget(self.label_31, 6, 0, 1, 1)
        self.lineEdit_17 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_17.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEdit_17.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_17.setObjectName(_fromUtf8("lineEdit_17"))
        self.gridLayout_2.addWidget(self.lineEdit_17, 6, 1, 1, 1)
        self.label_32 = QtGui.QLabel(self.tab_3)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.gridLayout_2.addWidget(self.label_32, 6, 2, 1, 1)
        self.label_33 = QtGui.QLabel(self.tab_3)
        self.label_33.setMinimumSize(QtCore.QSize(50, 0))
        self.label_33.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.gridLayout_2.addWidget(self.label_33, 7, 0, 1, 1)
        self.lineEdit_18 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_18.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEdit_18.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_18.setObjectName(_fromUtf8("lineEdit_18"))
        self.gridLayout_2.addWidget(self.lineEdit_18, 7, 1, 1, 1)
        self.label_34 = QtGui.QLabel(self.tab_3)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.gridLayout_2.addWidget(self.label_34, 7, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.label_35 = QtGui.QLabel(self.tab_3)
        self.label_35.setMinimumSize(QtCore.QSize(100, 0))
        self.label_35.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.verticalLayout_3.addWidget(self.label_35)
        self.textEdit = QtGui.QTextEdit(self.tab_3)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout_3.addWidget(self.textEdit)
        self.pushButton_5 = QtGui.QPushButton(self.tab_3)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.verticalLayout_3.addWidget(self.pushButton_5)
        self.progressBar_3 = QtGui.QProgressBar(self.tab_3)
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName(_fromUtf8("progressBar_3"))
        self.verticalLayout_3.addWidget(self.progressBar_3)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(350, 20, 581, 571))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(940, 20, 261, 471))
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.tabWidget.raise_()
        self.widget.raise_()
        self.textEdit_2.raise_()
        self.progressBar.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1211, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionCreate_model = QtGui.QAction(MainWindow)
        self.actionCreate_model.setObjectName(_fromUtf8("actionCreate_model"))
        self.actionSimulate_model = QtGui.QAction(MainWindow)
        self.actionSimulate_model.setObjectName(_fromUtf8("actionSimulate_model"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Julia", None))
        self.pushButton_2.setText(_translate("MainWindow", "Import Low Energy CT", None))
        self.pushButton.setText(_translate("MainWindow", "Import High Energy CT", None))
        self.label.setText(_translate("MainWindow", "Core diameter (mm)", None))
        self.lineEdit.setText(_translate("MainWindow", "100", None))
        self.label_2.setText(_translate("MainWindow", "Selected Core diameter (mm)", None))
        self.lineEdit_2.setText(_translate("MainWindow", "50", None))
        self.label_8.setText(_translate("MainWindow", "Orientation", None))
        self.label_4.setText(_translate("MainWindow", "Cropping Top (mm)", None))
        self.label_3.setText(_translate("MainWindow", "Cropping Bottom (mm)", None))
        self.label_5.setText(_translate("MainWindow", "Offset X (mm)", None))
        self.label_6.setText(_translate("MainWindow", "Offset Y (mm)", None))
        self.pushButton_3.setText(_translate("MainWindow", "Create Upscaled model", None))
        self.label_36.setText(_translate("MainWindow", "Dimensions (XY,Z)", None))
        self.label_37.setText(_translate("MainWindow", "Porosity", None))
        self.lineEdit_19.setText(_translate("MainWindow", "0.2", None))
        self.label_38.setText(_translate("MainWindow", "Permeability", None))
        self.lineEdit_20.setText(_translate("MainWindow", "200", None))
        self.pushButton_6.setText(_translate("MainWindow", "Create Dummy Model", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Core Model", None))
        self.label_7.setText(_translate("MainWindow", "Experiment type", None))
        self.label_9.setText(_translate("MainWindow", "Number of cycles", None))
        self.label_10.setText(_translate("MainWindow", "Cycle time", None))
        self.label_12.setText(_translate("MainWindow", "Oil", None))
        self.label_13.setText(_translate("MainWindow", "Water", None))
        self.label_14.setText(_translate("MainWindow", "Density", None))
        self.lineEdit_3.setText(_translate("MainWindow", "780", None))
        self.lineEdit_4.setText(_translate("MainWindow", "1000", None))
        self.label_15.setText(_translate("MainWindow", "Viscosity", None))
        self.lineEdit_5.setText(_translate("MainWindow", "1.2", None))
        self.lineEdit_6.setText(_translate("MainWindow", "0.36", None))
        self.label_16.setText(_translate("MainWindow", "Comp", None))
        self.lineEdit_7.setText(_translate("MainWindow", "0", None))
        self.lineEdit_8.setText(_translate("MainWindow", "0", None))
        self.label_11.setText(_translate("MainWindow", "Swir", None))
        self.lineEdit_9.setText(_translate("MainWindow", "0.3", None))
        self.label_17.setText(_translate("MainWindow", "water rate", None))
        self.lineEdit_10.setText(_translate("MainWindow", "12", None))
        self.pushButton_4.setText(_translate("MainWindow", "Run Simulation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Simulation", None))
        self.label_18.setText(_translate("MainWindow", "Oil/Water", None))
        self.label_19.setText(_translate("MainWindow", "Lo", None))
        self.lineEdit_11.setText(_translate("MainWindow", "1", None))
        self.label_24.setText(_translate("MainWindow", "0", None))
        self.label_20.setText(_translate("MainWindow", "Eo", None))
        self.lineEdit_12.setText(_translate("MainWindow", "2", None))
        self.label_25.setText(_translate("MainWindow", "0", None))
        self.label_21.setText(_translate("MainWindow", "To", None))
        self.lineEdit_13.setText(_translate("MainWindow", "2", None))
        self.label_26.setText(_translate("MainWindow", "0", None))
        self.label_28.setText(_translate("MainWindow", "Lw", None))
        self.lineEdit_16.setText(_translate("MainWindow", "1", None))
        self.label_27.setText(_translate("MainWindow", "0", None))
        self.label_23.setText(_translate("MainWindow", "Ew", None))
        self.lineEdit_15.setText(_translate("MainWindow", "2", None))
        self.label_30.setText(_translate("MainWindow", "0", None))
        self.label_22.setText(_translate("MainWindow", "Tw", None))
        self.lineEdit_14.setText(_translate("MainWindow", "2", None))
        self.label_29.setText(_translate("MainWindow", "0", None))
        self.label_31.setText(_translate("MainWindow", "Sorw", None))
        self.lineEdit_17.setText(_translate("MainWindow", "0.2", None))
        self.label_32.setText(_translate("MainWindow", "0", None))
        self.label_33.setText(_translate("MainWindow", "Krw", None))
        self.lineEdit_18.setText(_translate("MainWindow", "0.8", None))
        self.label_34.setText(_translate("MainWindow", "0", None))
        self.label_35.setText(_translate("MainWindow", "Historical data", None))
        self.pushButton_5.setText(_translate("MainWindow", "Fit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Parametrization", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionCreate_model.setText(_translate("MainWindow", "Create model", None))
        self.actionSimulate_model.setText(_translate("MainWindow", "Simulate model", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))




        
        #ADDED
        
	self.grid  = QtGui.QGridLayout(self.widget)
	self.pushButton_3.clicked.connect(self.CreateGrid)
	self.pushButton_4.clicked.connect(self.Simulate)
	self.pushButton_5.clicked.connect(self.Optimize)
	self.pushButton_6.clicked.connect(self.CreateDummyGrid)
	self.pushButton.clicked.connect(self.GetHighEnergy)
	self.pushButton_2.clicked.connect(self.GetLowEnergy)
	self.horizontalSlider.valueChanged.connect(self.UpdatePaddingTop)
	self.horizontalSlider_2.valueChanged.connect(self.UpdatePaddingBottom)
	self.horizontalSlider_3.valueChanged.connect(self.UpdateOffsetX)
	self.horizontalSlider_4.valueChanged.connect(self.UpdateOffsetY)
	self.comboBox.addItems(["Vertical","Horizontal"])
	self.comboBox_2.addItems(["USS","SS"])
	
    def GetValues(self):
    	self.Padding_top=int(self.horizontalSlider.value())
    	self.Padding_bottom=int(self.horizontalSlider_2.value())
    	self.Offsetx=int(self.horizontalSlider_3.value())
    	self.Offsety=int(self.horizontalSlider_4.value())
    	self.Diameter=float(self.lineEdit.text())
    	self.Crop_pct=float(self.lineEdit_2.text())
    	self.Orientation=self.comboBox.currentText()
    	self.nCycle=int(self.spinBox.value())
    	self.clength=int(self.spinBox_2.value())
    	self.Swir=float(self.lineEdit_9.text())
    	self.Method=self.comboBox_2.currentText()
    	self.WaterRate=float(self.lineEdit_10.text())
    	self.Oil_density=float(self.lineEdit_3.text())
    	self.Water_density=float(self.lineEdit_4.text())
    	self.Oil_compressibility=float(self.lineEdit_7.text())
    	self.Water_compressibility=float(self.lineEdit_8.text())
    	self.Oil_viscosity=float(self.lineEdit_5.text())
    	self.Water_viscosity=float(self.lineEdit_6.text())
    	self.nblocks_z=int(self.spinBox_4.value())
    	self.nblocks=int(self.spinBox_3.value())
    	self.Dummyporo=float(self.lineEdit_19.text())
    	self.Dummyperm=float(self.lineEdit_20.text())
    	self.ExpParams=[self.WaterRate,self.Oil_density,self.Water_density,self.Oil_compressibility,self.Water_compressibility,self.Oil_viscosity,self.Water_viscosity,self.Swir,self.Method]
    	self.Lo=float(self.lineEdit_11.text())
    	self.Eo=float(self.lineEdit_12.text())
    	self.To=float(self.lineEdit_13.text())
    	self.Lw=float(self.lineEdit_16.text())
    	self.Ew=float(self.lineEdit_15.text())
    	self.Tw=float(self.lineEdit_14.text())
    	self.Sorw=float(self.lineEdit_17.text())
    	self.Krw=float(self.lineEdit_18.text())
    	
    def UpdatePaddingTop(self):
    	self.Padding_top=self.horizontalSlider.value()
    
    def UpdatePaddingBottom(self):
    	self.Padding_bottom=self.horizontalSlider_2.value()
    
    def UpdateOffsetX(self):
    	self.Offsetx=self.horizontalSlider_3.value()
    	self.UpdateCircle()
    
    def UpdateOffsetY(self):
    	self.Offsety=self.horizontalSlider_4.value()
    	self.UpdateCircle()
    
    def PrintOutput(self,Text):
    	self.textEdit_2.append(Text)
    
    def UpdateCircle(self):
    	self.GetValues()
    	if self.LowEnergyPath=="":return
    	plt.clf()
    	ds1 = dicom.read_file(join(str(self.LowEnergyPath), os.listdir(self.LowEnergyPath)[0]))
    	fig  = plt.figure(facecolor="white")
    	axs  = fig.add_subplot(111)
    	a = ds1.pixel_array.shape[0]/2 
    	Offsetr=2*a*self.Offsetx/self.Diameter
    	Offsetc=2*a*self.Offsety/self.Diameter
    	r=int(ds1.pixel_array.shape[0]*self.Crop_pct/self.Diameter/2)
    	axs.imshow(ds1.pixel_array, cmap=plt.cm.bone)
    	circle=plt.Circle((ds1.pixel_array.shape[0]/2+Offsetr,ds1.pixel_array.shape[0]/2+Offsetc),r,color='r',linewidth=1,fill=False)
    
    	plt.gcf().gca().add_artist(circle)
    	axs.plot((a-10+Offsetr , a+10+Offsetr), (a+Offsetc, a+Offsetc), 'k')
    	axs.plot((a+Offsetr, a+Offsetr),(a-10+Offsetc , a+10+Offsetc), 'k')
    
    	canv = FigureCanvas(fig)   
    	self.grid.addWidget(canv, 0, 0)
    	self.widget.setLayout(self.grid)
    	self.widget.show()
    	self.widget.setFixedSize(600,600)
    
    def GetLowEnergy(self):
    	self.LowEnergyPath=QtGui.QFileDialog.getExistingDirectory()
    
    def GetHighEnergy(self):
    	self.HighEnergyPath=QtGui.QFileDialog.getExistingDirectory()
    
    def SetProgress(self,value,flag):
    	if flag==1:
    		self.progressBar.setProperty("value", value)
    	elif flag==2:
    		self.progressBar_2.setProperty("value", value)
    	elif flag==3:
    		self.progressBar_3.setProperty("value", value)
	app.processEvents()
    
    def Writetoconsole(self,Text,Clear=False):
    	if Clear:self.textEdit_2.clear()
	self.textEdit_2.append(Text)
	app.processEvents()
	
    def ParseInput(self):
    	RawInput=self.textEdit.toPlainText()
	Hist=[str(row) for row in RawInput.split("\n")]
	return Hist
	
    		
    def Simulate(self):
    	self.GetValues()    	
    	WriteDATAfile(self.ExpParams,self.Orientation,self.Padding_top,self.Padding_bottom,self.Crop_pct,self.nblocks,self.nblocks_z,self.Lw,self.Ew,self.Tw,self.Swir,self.Sorw,self.Krw,self.Lo,self.Eo,self.To,0,0,1,1,self.nCycle,self.clength)
    	self.SetProgress(33,2)
    	self.Writetoconsole("Running Eclipse...",True)
    	RunEclipse("temp/CORE_TEST.DATA")
    	self.SetProgress(66,2)
    	self.Writetoconsole("Plotting Results...")
    	FOPT,DIFF=PlotEclipseResults("temp/CORE_TEST",self.ExpParams,self.Orientation,self.nblocks,self.nblocks_z)
    	plt.clf()
    	fig  = plt.figure(facecolor="white")
    	ax  = fig.add_subplot(111)
    	ax.plot(FOPT,'g',DIFF,'r')
    	canv = FigureCanvas(fig)   
    	self.grid.addWidget(canv, 0, 0)
    	self.widget.setLayout(self.grid)
    	self.widget.show()
    	self.SetProgress(0,2)
    	self.Writetoconsole("Simulation Finished")
	
    def Optimize(self):
        self.GetValues()
   	self.hist=self.ParseInput()
    	self.Writetoconsole("Running Optimization...",True)
    	app.processEvents()
    	lb = [0,0,0,0,0.2,0,0,0,0,0,0.25,0.25]
    	ub = [5,5,5,0.5,1,5,5,5,10,10,2,2]       
    	best=Swarm(self.hist,10,3,lb,ub,1,self,app)
    	self.Writetoconsole("Optimization finished")
    
    def CreateDummyGrid(self):
    	    self.GetValues()
       	    self.Writetoconsole("Creating Grid Properties...",True)
	    nblocks_z=self.nblocks_z
	    nblocks=self.nblocks
	    
	    	
	    n=self.Diameter/nblocks
	    n_z=1000/nblocks_z
	    
	    Offsetr=int(nblocks*self.Offsetx/self.Diameter)
    	    Offsetc=int(nblocks*self.Offsety/self.Diameter)

	    X=np.ones((nblocks,nblocks))
	    X=GetMaskedValues(X,Offsetr,Offsetc)

	    ACTNUM=np.ones((nblocks_z,nblocks,nblocks))
	    for i in range(0,nblocks_z):
	    	ACTNUM[i]=X
		
	    PERMX=ACTNUM*self.Dummyperm
	    PORO=ACTNUM*self.Dummyporo
    	    Poro_string="PORO\n"
    	    actnum_string="ACTNUM\n"
    	    permx_string="PERMX\n"
    	    nz=0
	      
    	    if self.Orientation=="Vertical":
    		for k in range(0,nblocks_z):
    		    for j in range(0,nblocks):
    			for i in range(0,nblocks): 
    
    			    porov=PORO[k][j][i]
    			    permxv=PERMX[k][j][i]
    			    actnumv=ACTNUM[k][j][i]
    			    permx_string+=str(int(permxv))+"\t"
    			    Poro_string+='%.2E'%Decimal(porov)+"\t"
    			    actnum_string+=str(int(actnumv))+"\t"
    			    nz+=1
    
    			    if nz%4==0:
    				Poro_string+="\n"
    				permx_string+="\n"
    				actnum_string+="\n"
    
    			    self.SetProgress(float(k)/nblocks_z*100,1)
    	    else:
    		for i in range(0,nblocks):
    		    for j in range(0,nblocks):
    			for k in range(0,nblocks_z):
    			    porov=PORO[k][j][i]
    			    permxv=PERMX[k][j][i]
    			    actnumv=ACTNUM[k][j][i]
    			    permx_string+=str(int(permxv))+"\t"
    			    Poro_string+='%.2E'%Decimal(porov)+"\t"
    			    actnum_string+=str(int(actnumv))+"\t"
    			    nz+=1
                        
    			    if nz%4==0:
    					Poro_string+="\n"
    					permx_string+="\n"
    					actnum_string+="\n"
    			    self.SetProgress(float(k)/nblocks_z*100,1)
    			    
            maxporo=np.max(np.ma.masked_where(ACTNUM==0, PORO))
            minporo=np.min(np.ma.masked_where(ACTNUM==0, PORO))
  
            fig  = plt.figure(facecolor="white")
    	    ax  = fig.add_subplot(111, projection='3d')
    	    for k in range(0,nblocks_z):
    	        self.SetProgress(float(k)/nblocks_z*100,1)	    
    	        for i in range(0,nblocks):
    		    for j in range(0,nblocks):
			    porov=(minporo-PORO[k][j][i])/(minporo-maxporo)
			    r1=[i*n,(i+1)*n]
			    r2=[j*n,(j+1)*n]
			    z=[k*n_z,(k+1)*n_z]
			    X, Y = np.meshgrid(r1, r2)
			    Z,Z = np.meshgrid(z, z)
    			    R,G,B=GetRGB(porov)
			    if ACTNUM[k][j][i]==1:
				if k==0 :
				    ax.plot_surface(X,Y,z[0],color = (R,G,B,0.8) )
				if k==nblocks_z-1:
				    ax.plot_surface(X,Y,z[1],color = (R,G,B,0.8) )
				    
				if j==0:
				    ax.plot_surface(X,r2[0],Z,color = (R,G,B,0.8) )
				    if ACTNUM[k][j][i+1]==0:
				    	ax.plot_surface(r1[0],Y,z,color = (R,G,B,0.8) )
				    if ACTNUM[k][j][i-1]==0:
				    	ax.plot_surface(r1[1],Y,z,color = (R,G,B,0.8) )
				    continue
				if j==nblocks-1:
				    ax.plot_surface(X,r2[1],Z,color = (R,G,B,0.8) )
				    if ACTNUM[k][j][i+1]==0:
			            	ax.plot_surface(r1[0],Y,z,color = (R,G,B,0.8) )
			            if ACTNUM[k][j][i-1]==0:
				    	ax.plot_surface(r1[1],Y,z,color = (R,G,B,0.8) )
				    continue
				    	
				    
				if i==0:
				    ax.plot_surface(r1[0],Y,z,color = (R,G,B,0.8))
				    if ACTNUM[k][j-1][i]==0:
				    	ax.plot_surface(X,r2[0],Z,color = (R,G,B,0.8) )
				    if ACTNUM[k][j+1][i]==0:
				    	ax.plot_surface(X,r2[1],Z,color = (R,G,B,0.8) )
				    continue
				elif i==nblocks-1:
				    ax.plot_surface(r1[1],Y,z,color = (R,G,B,0.8) )
				    if ACTNUM[k][j-1][i]==0:
				    	ax.plot_surface(X,r2[0],Z,color = (R,G,B,0.8) )
				    if ACTNUM[k][j+1][i]==0:
				    	ax.plot_surface(X,r2[1],Z,color = (R,G,B,0.8) )
				    continue
				
				if ACTNUM[k][j-1][i]==0:
				    ax.plot_surface(X,r2[0],Z,color = (R,G,B,0.8) )
				if ACTNUM[k][j+1][i]==0:
				    ax.plot_surface(X,r2[1],Z,color = (R,G,B,0.8) )    	
				if ACTNUM[k][j][i+1]==0:
				    ax.plot_surface(r1[1],Y,z,color = (R,G,B,0.8) )
				if ACTNUM[k][j][i-1]==0:
				    ax.plot_surface(r1[0],Y,z,color = (R,G,B,0.8) )
				    
    	    canv = FigureCanvas(fig)   
    	    self.grid.addWidget(canv, 0, 0)
    	    self.widget.setLayout(self.grid)
    	    self.widget.show()
    	    Poro_string+="\n/\n"
    	    actnum_string+="\n/\n"
    	    permx_string+="\n/\n"
    	    self.progressBar.setProperty("value", 0)
    	    WriteString(actnum_string,"temp/ACTNUM.INC")
    	    WriteString(Poro_string,"temp/PORO.INC")
	    WriteString(permx_string,"temp/PERMX.INC")
	    self.Writetoconsole("Grid Generated")

	    
    def CreateGrid(self):
    	    if self.LowEnergyPath=="" or self.HighEnergyPath=="":
		    self.textEdit_2.clear()
		    self.textEdit_2.append("Error:Folder Path missing !")
		    return
		    
	    self.GetValues()
	    
    	    self.Writetoconsole("Reading DICOM Files...",True)
    	    files=[f for f in os.listdir(self.LowEnergyPath)]
    	    files2=[f for f in os.listdir(self.HighEnergyPath)]
    	    files=sorted(files)
    	    files2=sorted(files2)
    	    length=len(os.listdir(self.HighEnergyPath))-1
    	    Padding_top=self.Padding_top*length/1000  #avoid slices at the beginning
    	    Padding_bottom=self.Padding_bottom*length/1000# avoid Slices at the end
    	    nslices=length-Padding_bottom-Padding_top
    	    nblocks_z,n_z=GetMult(nslices)
	    firstime=True
    	    i=0
    
    	    for f1,f2 in zip(files,files2):
    
    		if i<Padding_top:
    		    i+=1
    		    continue
    		if i>=length-Padding_bottom:break
    
    		self.SetProgress(float(i-Padding_top)*100/(length-Padding_bottom-Padding_top),1)
    		ds1 = dicom.read_file(join(str(self.LowEnergyPath), f1))
    		ds2 = dicom.read_file(join(str(self.HighEnergyPath), f2))
    		a = ds1.pixel_array.shape[0]/2 
    		Offsetr=int(2*a*self.Offsetx/self.Diameter)
    		Offsetc=int(2*a*self.Offsety/self.Diameter)
		
    		x1=GetMaskedValues2(ds1.pixel_array,Offsetr,Offsetc,self.Crop_pct,self.Diameter)
    		x2=GetMaskedValues2(ds2.pixel_array,Offsetr,Offsetc,self.Crop_pct,self.Diameter)
    		

    		if (firstime):
    			nblocks,n=GetMult(x1.shape[0])
    			PORO=np.zeros(shape=(nblocks_z,nblocks,nblocks))
    			ACTNUM=np.zeros(shape=(nblocks_z,nblocks,nblocks))
    			PERMX=np.zeros(shape=(nblocks_z,nblocks,nblocks))
    			self.Writetoconsole("Cropping values:"+"top:"+str(self.Padding_top)+"mm,bottom:"+str(self.Padding_bottom)+"mm")
    			self.Writetoconsole("Offset values:"+"x:"+str(self.Offsetx)+"mm,y:"+str(self.Offsety)+"mm")
    			self.Writetoconsole("Grid size:"+str(nblocks)+","+str(nblocks)+","+str(nblocks_z))
    
    		parameters=[2650,1,-0.77,1.98,1007,36597.06,-35330.83,233946.02]
    		x, y = np.meshgrid(np.arange(x1.shape[0]), np.arange(x1.shape[1]),indexing='ij')
    		z=GetPoro(x1,x2,parameters)
    		poro_coarse=UpscalePoro(z,x,y,nblocks,n)

    		if (firstime):
    		    poro_coarse_avg=poro_coarse
    		    a = poro_coarse.shape[0]/2 
    		    Offsetr=int(2*a*self.Offsetx/self.Crop_pct)
    		    Offsetc=int(2*a*self.Offsety/self.Crop_pct)
    		    firstime=False
    
    
    
    		if (i-Padding_bottom)%n_z==0:
    		    a = poro_coarse.shape[0]/2 
		    Offsetr=int(2*a*self.Offsetx/self.Crop_pct)
    		    Offsetc=int(2*a*self.Offsety/self.Crop_pct)
    		    PORO[(i-Padding_top)/n_z]=poro_coarse_avg 
    		    ACTNUM[(i-Padding_top)/n_z]=GetMaskedValues(poro_coarse_avg,0,0)
    
    
    		else:
    		    poro_coarse_avg=poro_coarse_avg*(i-Padding_top)/((i-Padding_top)+1)+poro_coarse/((i-Padding_top)+1)
    		i+=1
    	    self.progressBar.setProperty("value", 0)
    	    fig = plt.figure()
    	    ax = Axes3D(fig)
    	    PORO[PORO<0]=0
    	    PORO[PORO>1]=1
    
    	    #PORO=PORO*1.7
    	    ACTNUM[ACTNUM!=0]=1
    	    #PERMX=10**(PORO/0.1)
            #
            #Poro-perm correlation with percolation threshold
            #
            PORO[PORO<0.05]=0.05
            PERMX=5*(PORO-0.05)**3.12*PORO*1E5
    	    PERMX[PERMX<10]=10
    	    
    	    self.Writetoconsole("Average Porosity:"+str(np.mean(PORO[PORO!=0])))
    	    self.Writetoconsole("Average Permeability:"+str(np.mean(PERMX)))
    	    self.nblocks=nblocks
    	    self.nblocks_z=nblocks_z
	    self.spinBox_4.setProperty("value", nblocks_z)
    	    self.spinBox_3.setProperty("value", nblocks)
    	    
    	    Poro_string="PORO\n"
    	    actnum_string="ACTNUM\n"
    	    permx_string="PERMX\n"
    	    nz=0
    
    	    self.Writetoconsole("Creating Grid Properties...")
    	    if self.Orientation=="Vertical":
    		for k in range(0,nblocks_z):
    		    for j in range(0,nblocks):
    			for i in range(0,nblocks): 
    
    			    porov=PORO[k][j][i]
    			    permxv=PERMX[k][j][i]
    			    actnumv=ACTNUM[k][j][i]
    			    permx_string+=str(int(permxv))+"\t"
    			    Poro_string+='%.2E'%Decimal(porov)+"\t"
    			    actnum_string+=str(int(actnumv))+"\t"
    			    nz+=1
    
    			    if nz%4==0:
    				Poro_string+="\n"
    				permx_string+="\n"
    				actnum_string+="\n"
    
    			    self.SetProgress(float(k)/nblocks_z*100,1)
    	    else:
    		for i in range(0,nblocks):
    		    for j in range(0,nblocks):
    			for k in range(0,nblocks_z):
    			    porov=PORO[k][j][i]
    			    permxv=PERMX[k][j][i]
    			    actnumv=ACTNUM[k][j][i]
    			    permx_string+=str(int(permxv))+"\t"
    			    Poro_string+='%.2E'%Decimal(porov)+"\t"
    			    actnum_string+=str(int(actnumv))+"\t"
    			    nz+=1
                        
    			    if nz%4==0:
    					Poro_string+="\n"
    					permx_string+="\n"
    					actnum_string+="\n"
    			    self.SetProgress(float(k)/nblocks_z*100,1)
    	      					    
    
                #Plot the 3d plug
            maxporo=np.max(np.ma.masked_where(ACTNUM==0, PORO))
            minporo=np.min(np.ma.masked_where(ACTNUM==0, PORO))
  
            fig  = plt.figure(facecolor="white")
    	    ax  = fig.add_subplot(111, projection='3d')
    	    for k in range(0,nblocks_z):
    	        self.SetProgress(float(k)/nblocks_z*100,1)	    
    	        for i in range(0,nblocks):
    		    for j in range(0,nblocks):
			    porov=(minporo-PORO[k][j][i])/(minporo-maxporo)
			    r1=[i*n,(i+1)*n]
			    r2=[j*n,(j+1)*n]
			    z=[k*n_z,(k+1)*n_z]
			    X, Y = np.meshgrid(r1, r2)
			    Z,Z = np.meshgrid(z, z)
    			    R,G,B=GetRGB(porov)
			    if ACTNUM[k][j][i]==1:
				if k==0 :
				    ax.plot_surface(X,Y,z[0],color = (R,G,B,0.8) )
				if k==nblocks_z-1:
				    ax.plot_surface(X,Y,z[1],color = (R,G,B,0.8) )
				    
				if j==0 and i<>0 and i<>nblocks-1:
				    ax.plot_surface(X,r2[0],Z,color = (R,G,B,0.8) )
				    if ACTNUM[k][j][i+1]==0:
				    	ax.plot_surface(r1[0],Y,z,color = (R,G,B,0.8) )
				    if ACTNUM[k][j][i-1]==0:
				    	ax.plot_surface(r1[1],Y,z,color = (R,G,B,0.8) )
				    continue
				if j==nblocks-1 and i<>0 and i<>nblocks-1:
				    ax.plot_surface(X,r2[1],Z,color = (R,G,B,0.8) )
				    if ACTNUM[k][j][i+1]==0:
			            	ax.plot_surface(r1[0],Y,z,color = (R,G,B,0.8) )
			            if ACTNUM[k][j][i-1]==0:
				    	ax.plot_surface(r1[1],Y,z,color = (R,G,B,0.8) )
				    continue
				    	
				    
				if i==0 and j<>0 and j<>nblocks-1:
				    ax.plot_surface(r1[0],Y,z,color = (R,G,B,0.8))
				    if ACTNUM[k][j-1][i]==0:
				    	ax.plot_surface(X,r2[0],Z,color = (R,G,B,0.8) )
				    if ACTNUM[k][j+1][i]==0:
				    	ax.plot_surface(X,r2[1],Z,color = (R,G,B,0.8) )
				    continue
				if i==nblocks-1 and j<>0 and j<>nblocks-1:
				    ax.plot_surface(r1[1],Y,z,color = (R,G,B,0.8) )
				    if ACTNUM[k][j-1][i]==0:
				    	ax.plot_surface(X,r2[0],Z,color = (R,G,B,0.8) )
				    if ACTNUM[k][j+1][i]==0:
				    	ax.plot_surface(X,r2[1],Z,color = (R,G,B,0.8) )
				    continue
				
				if i<>0 and i<>nblocks-1 and i<>0 and i<>nblocks-1:
					if ACTNUM[k][j-1][i]==0:
					    ax.plot_surface(X,r2[0],Z,color = (R,G,B,0.8) )
					if ACTNUM[k][j+1][i]==0:
					    ax.plot_surface(X,r2[1],Z,color = (R,G,B,0.8) )    	
					if ACTNUM[k][j][i+1]==0:
					    ax.plot_surface(r1[1],Y,z,color = (R,G,B,0.8) )
					if ACTNUM[k][j][i-1]==0:
					    ax.plot_surface(r1[0],Y,z,color = (R,G,B,0.8) )
    				    
	    canv = FigureCanvas(fig)   
	    self.grid.addWidget(canv, 0, 0)
	    self.widget.setLayout(self.grid)
    	    self.widget.show()
    	    Poro_string+="\n/\n"
    	    actnum_string+="\n/\n"
    	    permx_string+="\n/\n"
    	    self.progressBar.setProperty("value", 0)
    	    WriteString(actnum_string,"temp/ACTNUM.INC")
    	    WriteString(Poro_string,"temp/PORO.INC")
	    WriteString(permx_string,"temp/PERMX.INC")
	    self.Writetoconsole("Grid Generated")
	    
if __name__ == '__main__':
   	app = QApplication(sys.argv)
	Mainwindow = QMainWindow()
	gc.disable()
	ui = Ui_MainWindow()	
   	ui.setupUi(Mainwindow)
    	Mainwindow.show()
   	sys.exit(app.exec_())
