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
import shutil
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
        MainWindow.resize(1211, 773)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 336, 710))
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
        self.lineEdit.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(50, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.splitter)
        self.splitter_2 = QtGui.QSplitter(self.tab)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.label_2 = QtGui.QLabel(self.splitter_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_2 = QtGui.QLineEdit(self.splitter_2)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(50, 20))
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
        self.label_4.setMinimumSize(QtCore.QSize(150, 0))
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
        self.label_40 = QtGui.QLabel(self.splitter_3)
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.verticalLayout.addWidget(self.splitter_3)
        self.splitter_4 = QtGui.QSplitter(self.tab)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName(_fromUtf8("splitter_4"))
        self.label_3 = QtGui.QLabel(self.splitter_4)
        self.label_3.setMinimumSize(QtCore.QSize(150, 0))
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
        self.label_41 = QtGui.QLabel(self.splitter_4)
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.verticalLayout.addWidget(self.splitter_4)
        self.splitter_5 = QtGui.QSplitter(self.tab)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName(_fromUtf8("splitter_5"))
        self.label_5 = QtGui.QLabel(self.splitter_5)
        self.label_5.setMinimumSize(QtCore.QSize(150, 0))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalSlider_3 = QtGui.QSlider(self.splitter_5)
        self.horizontalSlider_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.horizontalSlider_3.setMinimum(-50)
        self.horizontalSlider_3.setMaximum(50)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName(_fromUtf8("horizontalSlider_3"))
        self.label_42 = QtGui.QLabel(self.splitter_5)
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.verticalLayout.addWidget(self.splitter_5)
        self.splitter_6 = QtGui.QSplitter(self.tab)
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName(_fromUtf8("splitter_6"))
        self.label_6 = QtGui.QLabel(self.splitter_6)
        self.label_6.setMinimumSize(QtCore.QSize(150, 0))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalSlider_4 = QtGui.QSlider(self.splitter_6)
        self.horizontalSlider_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.horizontalSlider_4.setMinimum(-50)
        self.horizontalSlider_4.setMaximum(50)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName(_fromUtf8("horizontalSlider_4"))
        self.label_43 = QtGui.QLabel(self.splitter_6)
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.verticalLayout.addWidget(self.splitter_6)
        self.pushButton_3 = QtGui.QPushButton(self.tab)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout.addWidget(self.pushButton_3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.splitter_16 = QtGui.QSplitter(self.tab)
        self.splitter_16.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_16.setObjectName(_fromUtf8("splitter_16"))
        self.label_39 = QtGui.QLabel(self.splitter_16)
        self.label_39.setMinimumSize(QtCore.QSize(150, 0))
        self.label_39.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.lineEdit_21 = QtGui.QLineEdit(self.splitter_16)
        self.lineEdit_21.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_21.setObjectName(_fromUtf8("lineEdit_21"))
        self.verticalLayout.addWidget(self.splitter_16)
        self.splitter_8 = QtGui.QSplitter(self.tab)
        self.splitter_8.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_8.setObjectName(_fromUtf8("splitter_8"))
        self.label_36 = QtGui.QLabel(self.splitter_8)
        self.label_36.setMinimumSize(QtCore.QSize(150, 0))
        self.label_36.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.spinBox_3 = QtGui.QSpinBox(self.splitter_8)
        self.spinBox_3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spinBox_3.setProperty("value", 5)
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.spinBox_4 = QtGui.QSpinBox(self.splitter_8)
        self.spinBox_4.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spinBox_4.setProperty("value", 5)
        self.spinBox_4.setObjectName(_fromUtf8("spinBox_4"))
        self.verticalLayout.addWidget(self.splitter_8)
        self.splitter_9 = QtGui.QSplitter(self.tab)
        self.splitter_9.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_9.setObjectName(_fromUtf8("splitter_9"))
        self.label_37 = QtGui.QLabel(self.splitter_9)
        self.label_37.setMinimumSize(QtCore.QSize(150, 0))
        self.label_37.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.lineEdit_19 = QtGui.QLineEdit(self.splitter_9)
        self.lineEdit_19.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_19.setObjectName(_fromUtf8("lineEdit_19"))
        self.verticalLayout.addWidget(self.splitter_9)
        self.splitter_10 = QtGui.QSplitter(self.tab)
        self.splitter_10.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_10.setObjectName(_fromUtf8("splitter_10"))
        self.label_38 = QtGui.QLabel(self.splitter_10)
        self.label_38.setMinimumSize(QtCore.QSize(150, 0))
        self.label_38.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.lineEdit_20 = QtGui.QLineEdit(self.splitter_10)
        self.lineEdit_20.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_20.setObjectName(_fromUtf8("lineEdit_20"))
        self.verticalLayout.addWidget(self.splitter_10)
        self.pushButton_6 = QtGui.QPushButton(self.tab)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.verticalLayout.addWidget(self.pushButton_6)
        spacerItem1 = QtGui.QSpacerItem(20, 24, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.splitter_17 = QtGui.QSplitter(self.tab)
        self.splitter_17.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_17.setObjectName(_fromUtf8("splitter_17"))
        self.progressBar = QtGui.QProgressBar(self.splitter_17)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.pushButton_7 = QtGui.QPushButton(self.splitter_17)
        self.pushButton_7.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.verticalLayout.addWidget(self.splitter_17)
        self.splitter_8.raise_()
        self.splitter_9.raise_()
        self.splitter_10.raise_()
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
        self.pushButton_6.raise_()
        self.label_39.raise_()
        self.lineEdit_21.raise_()
        self.label_40.raise_()
        self.label_41.raise_()
        self.label_42.raise_()
        self.label_43.raise_()
        self.pushButton_7.raise_()
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
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_19 = QtGui.QLabel(self.tab_2)
        self.label_19.setMinimumSize(QtCore.QSize(50, 0))
        self.label_19.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_3.addWidget(self.label_19, 0, 0, 1, 1)
        self.lineEdit_11 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_11.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEdit_11.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.gridLayout_3.addWidget(self.lineEdit_11, 0, 1, 1, 1)
        self.label_44 = QtGui.QLabel(self.tab_2)
        self.label_44.setMaximumSize(QtCore.QSize(20, 20))
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.gridLayout_3.addWidget(self.label_44, 0, 2, 1, 1)
        self.lineEdit_22 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_22.setMaximumSize(QtCore.QSize(50, 20))
        self.lineEdit_22.setObjectName(_fromUtf8("lineEdit_22"))
        self.gridLayout_3.addWidget(self.lineEdit_22, 0, 3, 1, 1)
        self.label_20 = QtGui.QLabel(self.tab_2)
        self.label_20.setMinimumSize(QtCore.QSize(50, 0))
        self.label_20.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_3.addWidget(self.label_20, 1, 0, 1, 1)
        self.lineEdit_12 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_12.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEdit_12.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.gridLayout_3.addWidget(self.lineEdit_12, 1, 1, 1, 1)
        self.label_45 = QtGui.QLabel(self.tab_2)
        self.label_45.setMaximumSize(QtCore.QSize(20, 20))
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.gridLayout_3.addWidget(self.label_45, 1, 2, 1, 1)
        self.lineEdit_23 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_23.setMaximumSize(QtCore.QSize(50, 20))
        self.lineEdit_23.setObjectName(_fromUtf8("lineEdit_23"))
        self.gridLayout_3.addWidget(self.lineEdit_23, 1, 3, 1, 1)
        self.label_21 = QtGui.QLabel(self.tab_2)
        self.label_21.setMinimumSize(QtCore.QSize(50, 0))
        self.label_21.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_3.addWidget(self.label_21, 2, 0, 1, 1)
        self.lineEdit_13 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_13.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEdit_13.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.gridLayout_3.addWidget(self.lineEdit_13, 2, 1, 1, 1)
        self.label_46 = QtGui.QLabel(self.tab_2)
        self.label_46.setMaximumSize(QtCore.QSize(20, 20))
        self.label_46.setObjectName(_fromUtf8("label_46"))
        self.gridLayout_3.addWidget(self.label_46, 2, 2, 1, 1)
        self.lineEdit_24 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_24.setMaximumSize(QtCore.QSize(50, 20))
        self.lineEdit_24.setObjectName(_fromUtf8("lineEdit_24"))
        self.gridLayout_3.addWidget(self.lineEdit_24, 2, 3, 1, 1)
        self.label_28 = QtGui.QLabel(self.tab_2)
        self.label_28.setMinimumSize(QtCore.QSize(50, 0))
        self.label_28.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.gridLayout_3.addWidget(self.label_28, 3, 0, 1, 1)
        self.lineEdit_16 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_16.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEdit_16.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.gridLayout_3.addWidget(self.lineEdit_16, 3, 1, 1, 1)
        self.label_47 = QtGui.QLabel(self.tab_2)
        self.label_47.setMaximumSize(QtCore.QSize(20, 20))
        self.label_47.setObjectName(_fromUtf8("label_47"))
        self.gridLayout_3.addWidget(self.label_47, 3, 2, 1, 1)
        self.lineEdit_25 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_25.setMaximumSize(QtCore.QSize(50, 20))
        self.lineEdit_25.setObjectName(_fromUtf8("lineEdit_25"))
        self.gridLayout_3.addWidget(self.lineEdit_25, 3, 3, 1, 1)
        self.label_23 = QtGui.QLabel(self.tab_2)
        self.label_23.setMinimumSize(QtCore.QSize(50, 0))
        self.label_23.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_3.addWidget(self.label_23, 4, 0, 1, 1)
        self.lineEdit_15 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_15.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEdit_15.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.gridLayout_3.addWidget(self.lineEdit_15, 4, 1, 1, 1)
        self.label_22 = QtGui.QLabel(self.tab_2)
        self.label_22.setMinimumSize(QtCore.QSize(50, 0))
        self.label_22.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_3.addWidget(self.label_22, 5, 0, 1, 1)
        self.lineEdit_14 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_14.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEdit_14.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.gridLayout_3.addWidget(self.lineEdit_14, 5, 1, 1, 1)
        self.label_31 = QtGui.QLabel(self.tab_2)
        self.label_31.setMinimumSize(QtCore.QSize(50, 0))
        self.label_31.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.gridLayout_3.addWidget(self.label_31, 6, 0, 1, 1)
        self.lineEdit_17 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_17.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEdit_17.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_17.setObjectName(_fromUtf8("lineEdit_17"))
        self.gridLayout_3.addWidget(self.lineEdit_17, 6, 1, 1, 1)
        self.label_33 = QtGui.QLabel(self.tab_2)
        self.label_33.setMinimumSize(QtCore.QSize(50, 0))
        self.label_33.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.gridLayout_3.addWidget(self.label_33, 7, 0, 1, 1)
        self.lineEdit_18 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_18.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEdit_18.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_18.setObjectName(_fromUtf8("lineEdit_18"))
        self.gridLayout_3.addWidget(self.lineEdit_18, 7, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.pushButton_4 = QtGui.QPushButton(self.tab_2)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.verticalLayout_2.addWidget(self.pushButton_4)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.splitter_18 = QtGui.QSplitter(self.tab_2)
        self.splitter_18.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_18.setObjectName(_fromUtf8("splitter_18"))
        self.progressBar_2 = QtGui.QProgressBar(self.splitter_18)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName(_fromUtf8("progressBar_2"))
        self.pushButton_8 = QtGui.QPushButton(self.splitter_18)
        self.pushButton_8.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.verticalLayout_2.addWidget(self.splitter_18)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_18 = QtGui.QLabel(self.tab_3)
        self.label_18.setMinimumSize(QtCore.QSize(100, 0))
        self.label_18.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.verticalLayout_5.addWidget(self.label_18)
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.label_107 = QtGui.QLabel(self.tab_3)
        self.label_107.setObjectName(_fromUtf8("label_107"))
        self.gridLayout_7.addWidget(self.label_107, 0, 0, 1, 1)
        self.spinBox_5 = QtGui.QSpinBox(self.tab_3)
        self.spinBox_5.setObjectName(_fromUtf8("spinBox_5"))
        self.gridLayout_7.addWidget(self.spinBox_5, 0, 1, 1, 1)
        self.label_24 = QtGui.QLabel(self.tab_3)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout_7.addWidget(self.label_24, 0, 2, 1, 1)
        self.spinBox_33 = QtGui.QSpinBox(self.tab_3)
        self.spinBox_33.setProperty("value", 5)
        self.spinBox_33.setObjectName(_fromUtf8("spinBox_33"))
        self.gridLayout_7.addWidget(self.spinBox_33, 0, 3, 1, 1)
        self.checkBox = QtGui.QCheckBox(self.tab_3)
        self.checkBox.setText(_fromUtf8(""))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout_7.addWidget(self.checkBox, 0, 4, 1, 1)
        self.label_108 = QtGui.QLabel(self.tab_3)
        self.label_108.setObjectName(_fromUtf8("label_108"))
        self.gridLayout_7.addWidget(self.label_108, 1, 0, 1, 1)
        self.spinBox_6 = QtGui.QSpinBox(self.tab_3)
        self.spinBox_6.setObjectName(_fromUtf8("spinBox_6"))
        self.gridLayout_7.addWidget(self.spinBox_6, 1, 1, 1, 1)
        self.label_25 = QtGui.QLabel(self.tab_3)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_7.addWidget(self.label_25, 1, 2, 1, 1)
        self.spinBox_36 = QtGui.QSpinBox(self.tab_3)
        self.spinBox_36.setProperty("value", 5)
        self.spinBox_36.setObjectName(_fromUtf8("spinBox_36"))
        self.gridLayout_7.addWidget(self.spinBox_36, 1, 3, 1, 1)
        self.checkBox_2 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_2.setText(_fromUtf8(""))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.gridLayout_7.addWidget(self.checkBox_2, 1, 4, 1, 1)
        self.label_113 = QtGui.QLabel(self.tab_3)
        self.label_113.setObjectName(_fromUtf8("label_113"))
        self.gridLayout_7.addWidget(self.label_113, 2, 0, 1, 1)
        self.spinBox_7 = QtGui.QSpinBox(self.tab_3)
        self.spinBox_7.setObjectName(_fromUtf8("spinBox_7"))
        self.gridLayout_7.addWidget(self.spinBox_7, 2, 1, 1, 1)
        self.label_26 = QtGui.QLabel(self.tab_3)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_7.addWidget(self.label_26, 2, 2, 1, 1)
        self.spinBox_43 = QtGui.QSpinBox(self.tab_3)
        self.spinBox_43.setProperty("value", 5)
        self.spinBox_43.setObjectName(_fromUtf8("spinBox_43"))
        self.gridLayout_7.addWidget(self.spinBox_43, 2, 3, 1, 1)
        self.checkBox_3 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_3.setText(_fromUtf8(""))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.gridLayout_7.addWidget(self.checkBox_3, 2, 4, 1, 1)
        self.label_103 = QtGui.QLabel(self.tab_3)
        self.label_103.setObjectName(_fromUtf8("label_103"))
        self.gridLayout_7.addWidget(self.label_103, 3, 0, 1, 1)
        self.spinBox_8 = QtGui.QSpinBox(self.tab_3)
        self.spinBox_8.setObjectName(_fromUtf8("spinBox_8"))
        self.gridLayout_7.addWidget(self.spinBox_8, 3, 1, 1, 1)
        self.label_27 = QtGui.QLabel(self.tab_3)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_7.addWidget(self.label_27, 3, 2, 1, 1)
        self.spinBox_41 = QtGui.QSpinBox(self.tab_3)
        self.spinBox_41.setProperty("value", 5)
        self.spinBox_41.setObjectName(_fromUtf8("spinBox_41"))
        self.gridLayout_7.addWidget(self.spinBox_41, 3, 3, 1, 1)
        self.checkBox_4 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_4.setText(_fromUtf8(""))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.gridLayout_7.addWidget(self.checkBox_4, 3, 4, 1, 1)
        self.label_114 = QtGui.QLabel(self.tab_3)
        self.label_114.setObjectName(_fromUtf8("label_114"))
        self.gridLayout_7.addWidget(self.label_114, 4, 0, 1, 1)
        self.spinBox_9 = QtGui.QSpinBox(self.tab_3)
        self.spinBox_9.setObjectName(_fromUtf8("spinBox_9"))
        self.gridLayout_7.addWidget(self.spinBox_9, 4, 1, 1, 1)
        self.label_30 = QtGui.QLabel(self.tab_3)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.gridLayout_7.addWidget(self.label_30, 4, 2, 1, 1)
        self.spinBox_40 = QtGui.QSpinBox(self.tab_3)
        self.spinBox_40.setMinimumSize(QtCore.QSize(20, 0))
        self.spinBox_40.setProperty("value", 5)
        self.spinBox_40.setObjectName(_fromUtf8("spinBox_40"))
        self.gridLayout_7.addWidget(self.spinBox_40, 4, 3, 1, 1)
        self.checkBox_5 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_5.setText(_fromUtf8(""))
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.gridLayout_7.addWidget(self.checkBox_5, 4, 4, 1, 1)
        self.label_104 = QtGui.QLabel(self.tab_3)
        self.label_104.setObjectName(_fromUtf8("label_104"))
        self.gridLayout_7.addWidget(self.label_104, 5, 0, 1, 1)
        self.spinBox_10 = QtGui.QSpinBox(self.tab_3)
        self.spinBox_10.setObjectName(_fromUtf8("spinBox_10"))
        self.gridLayout_7.addWidget(self.spinBox_10, 5, 1, 1, 1)
        self.label_29 = QtGui.QLabel(self.tab_3)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout_7.addWidget(self.label_29, 5, 2, 1, 1)
        self.spinBox_39 = QtGui.QSpinBox(self.tab_3)
        self.spinBox_39.setProperty("value", 5)
        self.spinBox_39.setObjectName(_fromUtf8("spinBox_39"))
        self.gridLayout_7.addWidget(self.spinBox_39, 5, 3, 1, 1)
        self.checkBox_6 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_6.setText(_fromUtf8(""))
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.gridLayout_7.addWidget(self.checkBox_6, 5, 4, 1, 1)
        self.label_112 = QtGui.QLabel(self.tab_3)
        self.label_112.setObjectName(_fromUtf8("label_112"))
        self.gridLayout_7.addWidget(self.label_112, 6, 0, 1, 1)
        self.spinBox_11 = QtGui.QSpinBox(self.tab_3)
        self.spinBox_11.setObjectName(_fromUtf8("spinBox_11"))
        self.gridLayout_7.addWidget(self.spinBox_11, 6, 1, 1, 1)
        self.label_32 = QtGui.QLabel(self.tab_3)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.gridLayout_7.addWidget(self.label_32, 6, 2, 1, 1)
        self.spinBox_42 = QtGui.QSpinBox(self.tab_3)
        self.spinBox_42.setProperty("value", 1)
        self.spinBox_42.setObjectName(_fromUtf8("spinBox_42"))
        self.gridLayout_7.addWidget(self.spinBox_42, 6, 3, 1, 1)
        self.checkBox_7 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_7.setText(_fromUtf8(""))
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))
        self.gridLayout_7.addWidget(self.checkBox_7, 6, 4, 1, 1)
        self.label_111 = QtGui.QLabel(self.tab_3)
        self.label_111.setObjectName(_fromUtf8("label_111"))
        self.gridLayout_7.addWidget(self.label_111, 7, 0, 1, 1)
        self.spinBox_12 = QtGui.QSpinBox(self.tab_3)
        self.spinBox_12.setObjectName(_fromUtf8("spinBox_12"))
        self.gridLayout_7.addWidget(self.spinBox_12, 7, 1, 1, 1)
        self.label_34 = QtGui.QLabel(self.tab_3)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.gridLayout_7.addWidget(self.label_34, 7, 2, 1, 1)
        self.spinBox_35 = QtGui.QSpinBox(self.tab_3)
        self.spinBox_35.setProperty("value", 1)
        self.spinBox_35.setObjectName(_fromUtf8("spinBox_35"))
        self.gridLayout_7.addWidget(self.spinBox_35, 7, 3, 1, 1)
        self.checkBox_8 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_8.setText(_fromUtf8(""))
        self.checkBox_8.setObjectName(_fromUtf8("checkBox_8"))
        self.gridLayout_7.addWidget(self.checkBox_8, 7, 4, 1, 1)
        self.label_106 = QtGui.QLabel(self.tab_3)
        self.label_106.setObjectName(_fromUtf8("label_106"))
        self.gridLayout_7.addWidget(self.label_106, 8, 0, 1, 1)
        self.spinBox_13 = QtGui.QSpinBox(self.tab_3)
        self.spinBox_13.setObjectName(_fromUtf8("spinBox_13"))
        self.gridLayout_7.addWidget(self.spinBox_13, 8, 1, 1, 1)
        self.label_48 = QtGui.QLabel(self.tab_3)
        self.label_48.setObjectName(_fromUtf8("label_48"))
        self.gridLayout_7.addWidget(self.label_48, 8, 2, 1, 1)
        self.spinBox_38 = QtGui.QSpinBox(self.tab_3)
        self.spinBox_38.setProperty("value", 10)
        self.spinBox_38.setObjectName(_fromUtf8("spinBox_38"))
        self.gridLayout_7.addWidget(self.spinBox_38, 8, 3, 1, 1)
        self.checkBox_9 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_9.setText(_fromUtf8(""))
        self.checkBox_9.setObjectName(_fromUtf8("checkBox_9"))
        self.gridLayout_7.addWidget(self.checkBox_9, 8, 4, 1, 1)
        self.label_105 = QtGui.QLabel(self.tab_3)
        self.label_105.setObjectName(_fromUtf8("label_105"))
        self.gridLayout_7.addWidget(self.label_105, 9, 0, 1, 1)
        self.spinBox_14 = QtGui.QSpinBox(self.tab_3)
        self.spinBox_14.setObjectName(_fromUtf8("spinBox_14"))
        self.gridLayout_7.addWidget(self.spinBox_14, 9, 1, 1, 1)
        self.label_49 = QtGui.QLabel(self.tab_3)
        self.label_49.setObjectName(_fromUtf8("label_49"))
        self.gridLayout_7.addWidget(self.label_49, 9, 2, 1, 1)
        self.spinBox_44 = QtGui.QSpinBox(self.tab_3)
        self.spinBox_44.setProperty("value", 10)
        self.spinBox_44.setObjectName(_fromUtf8("spinBox_44"))
        self.gridLayout_7.addWidget(self.spinBox_44, 9, 3, 1, 1)
        self.checkBox_10 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_10.setText(_fromUtf8(""))
        self.checkBox_10.setObjectName(_fromUtf8("checkBox_10"))
        self.gridLayout_7.addWidget(self.checkBox_10, 9, 4, 1, 1)
        self.label_109 = QtGui.QLabel(self.tab_3)
        self.label_109.setObjectName(_fromUtf8("label_109"))
        self.gridLayout_7.addWidget(self.label_109, 10, 0, 1, 1)
        self.spinBox_16 = QtGui.QSpinBox(self.tab_3)
        self.spinBox_16.setObjectName(_fromUtf8("spinBox_16"))
        self.gridLayout_7.addWidget(self.spinBox_16, 10, 1, 1, 1)
        self.label_50 = QtGui.QLabel(self.tab_3)
        self.label_50.setObjectName(_fromUtf8("label_50"))
        self.gridLayout_7.addWidget(self.label_50, 10, 2, 1, 1)
        self.spinBox_34 = QtGui.QSpinBox(self.tab_3)
        self.spinBox_34.setProperty("value", 1)
        self.spinBox_34.setObjectName(_fromUtf8("spinBox_34"))
        self.gridLayout_7.addWidget(self.spinBox_34, 10, 3, 1, 1)
        self.checkBox_11 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_11.setText(_fromUtf8(""))
        self.checkBox_11.setObjectName(_fromUtf8("checkBox_11"))
        self.gridLayout_7.addWidget(self.checkBox_11, 10, 4, 1, 1)
        self.label_110 = QtGui.QLabel(self.tab_3)
        self.label_110.setObjectName(_fromUtf8("label_110"))
        self.gridLayout_7.addWidget(self.label_110, 11, 0, 1, 1)
        self.spinBox_15 = QtGui.QSpinBox(self.tab_3)
        self.spinBox_15.setObjectName(_fromUtf8("spinBox_15"))
        self.gridLayout_7.addWidget(self.spinBox_15, 11, 1, 1, 1)
        self.label_51 = QtGui.QLabel(self.tab_3)
        self.label_51.setObjectName(_fromUtf8("label_51"))
        self.gridLayout_7.addWidget(self.label_51, 11, 2, 1, 1)
        self.spinBox_37 = QtGui.QSpinBox(self.tab_3)
        self.spinBox_37.setProperty("value", 1)
        self.spinBox_37.setObjectName(_fromUtf8("spinBox_37"))
        self.gridLayout_7.addWidget(self.spinBox_37, 11, 3, 1, 1)
        self.checkBox_12 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_12.setText(_fromUtf8(""))
        self.checkBox_12.setObjectName(_fromUtf8("checkBox_12"))
        self.gridLayout_7.addWidget(self.checkBox_12, 11, 4, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_7)
        self.label_35 = QtGui.QLabel(self.tab_3)
        self.label_35.setMinimumSize(QtCore.QSize(100, 0))
        self.label_35.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.verticalLayout_5.addWidget(self.label_35)
        self.textEdit = QtGui.QTextEdit(self.tab_3)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout_5.addWidget(self.textEdit)
        self.pushButton_5 = QtGui.QPushButton(self.tab_3)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.verticalLayout_5.addWidget(self.pushButton_5)
        self.splitter_39 = QtGui.QSplitter(self.tab_3)
        self.splitter_39.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_39.setObjectName(_fromUtf8("splitter_39"))
        self.progressBar_3 = QtGui.QProgressBar(self.splitter_39)
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName(_fromUtf8("progressBar_3"))
        self.pushButton_17 = QtGui.QPushButton(self.splitter_39)
        self.pushButton_17.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_17.setObjectName(_fromUtf8("pushButton_17"))
        self.verticalLayout_5.addWidget(self.splitter_39)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(350, 20, 841, 531))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(350, 560, 841, 161))
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
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
        self.label_40.setText(_translate("MainWindow", "0", None))
        self.label_3.setText(_translate("MainWindow", "Cropping Bottom (mm)", None))
        self.label_41.setText(_translate("MainWindow", "0", None))
        self.label_5.setText(_translate("MainWindow", "Offset X (mm)", None))
        self.label_42.setText(_translate("MainWindow", "0", None))
        self.label_6.setText(_translate("MainWindow", "Offset Y (mm)", None))
        self.label_43.setText(_translate("MainWindow", "0", None))
        self.pushButton_3.setText(_translate("MainWindow", "Create Upscaled model", None))
        self.label_39.setText(_translate("MainWindow", "Height (mm)", None))
        self.lineEdit_21.setText(_translate("MainWindow", "1000", None))
        self.label_36.setText(_translate("MainWindow", "Dimensions (XY,Z)", None))
        self.label_37.setText(_translate("MainWindow", "Porosity", None))
        self.lineEdit_19.setText(_translate("MainWindow", "0.2", None))
        self.label_38.setText(_translate("MainWindow", "Permeability (mD)", None))
        self.lineEdit_20.setText(_translate("MainWindow", "200", None))
        self.pushButton_6.setText(_translate("MainWindow", "Create Dummy Model", None))
        self.pushButton_7.setText(_translate("MainWindow", "Stop", None))
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
        self.label_19.setText(_translate("MainWindow", "Lo", None))
        self.lineEdit_11.setText(_translate("MainWindow", "1", None))
        self.label_44.setText(_translate("MainWindow", "Ao", None))
        self.lineEdit_22.setText(_translate("MainWindow", "1", None))
        self.label_20.setText(_translate("MainWindow", "Eo", None))
        self.lineEdit_12.setText(_translate("MainWindow", "2", None))
        self.label_45.setText(_translate("MainWindow", "Aw", None))
        self.lineEdit_23.setText(_translate("MainWindow", "1", None))
        self.label_21.setText(_translate("MainWindow", "To", None))
        self.lineEdit_13.setText(_translate("MainWindow", "2", None))
        self.label_46.setText(_translate("MainWindow", "Co", None))
        self.lineEdit_24.setText(_translate("MainWindow", "0", None))
        self.label_28.setText(_translate("MainWindow", "Lw", None))
        self.lineEdit_16.setText(_translate("MainWindow", "1", None))
        self.label_47.setText(_translate("MainWindow", "Cw", None))
        self.lineEdit_25.setText(_translate("MainWindow", "0", None))
        self.label_23.setText(_translate("MainWindow", "Ew", None))
        self.lineEdit_15.setText(_translate("MainWindow", "2", None))
        self.label_22.setText(_translate("MainWindow", "Tw", None))
        self.lineEdit_14.setText(_translate("MainWindow", "2", None))
        self.label_31.setText(_translate("MainWindow", "Sorw", None))
        self.lineEdit_17.setText(_translate("MainWindow", "0.2", None))
        self.label_33.setText(_translate("MainWindow", "Krw", None))
        self.lineEdit_18.setText(_translate("MainWindow", "0.8", None))
        self.pushButton_4.setText(_translate("MainWindow", "Run Simulation", None))
        self.pushButton_8.setText(_translate("MainWindow", "Stop", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Simulation", None))
        self.label_18.setText(_translate("MainWindow", "Oil/Water", None))
        self.label_107.setText(_translate("MainWindow", "Lo", None))
        self.label_24.setText(_translate("MainWindow", "0", None))
        self.label_108.setText(_translate("MainWindow", "Eo", None))
        self.label_25.setText(_translate("MainWindow", "0", None))
        self.label_113.setText(_translate("MainWindow", "To", None))
        self.label_26.setText(_translate("MainWindow", "0", None))
        self.label_103.setText(_translate("MainWindow", "Lw", None))
        self.label_27.setText(_translate("MainWindow", "0", None))
        self.label_114.setText(_translate("MainWindow", "Ew", None))
        self.label_30.setText(_translate("MainWindow", "0", None))
        self.label_104.setText(_translate("MainWindow", "Tw", None))
        self.label_29.setText(_translate("MainWindow", "0", None))
        self.label_112.setText(_translate("MainWindow", "Sorw", None))
        self.label_32.setText(_translate("MainWindow", "0", None))
        self.label_111.setText(_translate("MainWindow", "Krw", None))
        self.label_34.setText(_translate("MainWindow", "0", None))
        self.label_106.setText(_translate("MainWindow", "Ao", None))
        self.label_48.setText(_translate("MainWindow", "0", None))
        self.label_105.setText(_translate("MainWindow", "Aw", None))
        self.label_49.setText(_translate("MainWindow", "0", None))
        self.label_109.setText(_translate("MainWindow", "Co", None))
        self.label_50.setText(_translate("MainWindow", "0", None))
        self.label_110.setText(_translate("MainWindow", "Cw", None))
        self.label_51.setText(_translate("MainWindow", "0", None))
        self.label_35.setText(_translate("MainWindow", "Historical data", None))
        self.pushButton_5.setText(_translate("MainWindow", "Fit", None))
        self.pushButton_17.setText(_translate("MainWindow", "Stop", None))
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
	self.pushButton_7.clicked.connect(self.Stop)
	self.pushButton_8.clicked.connect(self.Stop)
	self.pushButton_17.clicked.connect(self.Stop)
	self.pushButton.clicked.connect(self.GetHighEnergy)
	self.pushButton_2.clicked.connect(self.GetLowEnergy)
	self.horizontalSlider.sliderReleased.connect(self.UpdatePaddingTop)
	self.horizontalSlider_2.sliderReleased.connect(self.UpdatePaddingBottom)
	self.horizontalSlider_3.sliderReleased.connect(self.UpdateOffsetX)
	self.horizontalSlider_4.sliderReleased.connect(self.UpdateOffsetY)
	self.comboBox.addItems(["Vertical","Horizontal"])
	self.comboBox_2.addItems(["USS","SS"])
	self.fig  = plt.figure(facecolor="white")
	self.canv = FigureCanvas(self.fig)   
	self.grid.addWidget(self.canv, 0, 0)
	self.widget.setLayout(self.grid)
    	self.RemoveTemp()
	
    def GetValues(self):
    	plt.clf()
    	self.StopAction=False
    	self.height=int(self.lineEdit_21.text())
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
    	self.Ao=float(self.lineEdit_22.text())
    	self.Aw=float(self.lineEdit_23.text())
    	self.Co=float(self.lineEdit_24.text())
    	self.Cw=float(self.lineEdit_25.text())
    	self.StaticParams=[self.Lo,self.Eo,self.To,self.Lw,self.Ew,self.Tw,self.Sorw,self.Krw,self.Ao,self.Aw,self.Co,self.Cw]
    	self.DynamicParams=self.StaticParams
    	self.ActiveParams=[self.checkBox.isChecked(),self.checkBox_2.isChecked(),self.checkBox_3.isChecked(),self.checkBox_4.isChecked(),self.checkBox_5.isChecked(),self.checkBox_6.isChecked(),self.checkBox_7.isChecked(),self.checkBox_8.isChecked(),self.checkBox_9.isChecked(),self.checkBox_10.isChecked(),self.checkBox_11.isChecked(),self.checkBox_12.isChecked()]
    	self.Lowerbounds=[int(self.spinBox_5.value()),int(self.spinBox_6.value()),int(self.spinBox_7.value()),int(self.spinBox_8.value()),int(self.spinBox_9.value()),int(self.spinBox_10.value()),int(self.spinBox_11.value()),int(self.spinBox_12.value()),int(self.spinBox_13.value()),int(self.spinBox_14.value()),int(self.spinBox_16.value()),int(self.spinBox_15.value())]
    	self.Upperbounds=[int(self.spinBox_33.value()),int(self.spinBox_36.value()),int(self.spinBox_43.value()),int(self.spinBox_41.value()),int(self.spinBox_40.value()),int(self.spinBox_39.value()),int(self.spinBox_42.value()),int(self.spinBox_35.value()),int(self.spinBox_38.value()),int(self.spinBox_44.value()),int(self.spinBox_34.value()),int(self.spinBox_37.value())]
    
    def RemoveTemp(self):
    	if  os.path.exists("./temp"):
    		shutil.rmtree("./temp")
	
    def CreateTemp(self):
    	if not os.path.exists("./temp"):
    		os.makedirs("./temp")
		
    def Stop(self,number):
    	self.StopAction=True
    	self.SetProgress(0,1)
    	self.SetProgress(0,2)
    	self.SetProgress(0,3)
    	app.processEvents()
    	
    def UpdatePaddingTop(self):
    	self.Padding_top=self.horizontalSlider.value()
    	self.label_40.setText(str(self.Padding_top))
    
    def UpdatePaddingBottom(self):
    	self.Padding_bottom=self.horizontalSlider_2.value()
    	self.label_41.setText(str(self.Padding_bottom))
    
    def UpdateOffsetX(self):
    	self.Offsetx=self.horizontalSlider_3.value()
    	self.label_42.setText(str(self.Offsetx))
    	self.UpdateCircle()
    
    def UpdateOffsetY(self):
    	self.Offsety=self.horizontalSlider_4.value()
    	self.label_43.setText(str(self.Offsety))
    	self.UpdateCircle()
    
    def PrintOutput(self,Text):
    	self.textEdit_2.append(Text)
    
    def UpdateCircle(self):
    	self.GetValues()
    	if self.LowEnergyPath=="":return
    	plt.clf()
    	ds1 = dicom.read_file(join(str(self.LowEnergyPath), os.listdir(self.LowEnergyPath)[0]))
    	
    	axs  = self.fig.add_subplot(111)
    	a = ds1.pixel_array.shape[0]/2 
    	Offsetr=2*a*self.Offsetx/self.Diameter
    	Offsetc=2*a*self.Offsety/self.Diameter
    	r=int(ds1.pixel_array.shape[0]*self.Crop_pct/self.Diameter/2)
    	axs.imshow(ds1.pixel_array, cmap=plt.cm.bone)
    	circle=plt.Circle((ds1.pixel_array.shape[0]/2+Offsetr,ds1.pixel_array.shape[0]/2+Offsetc),r,color='r',linewidth=1,fill=False)
    
    	plt.gcf().gca().add_artist(circle)
    	axs.plot((a-10+Offsetr , a+10+Offsetr), (a+Offsetc, a+Offsetc), 'k')
    	axs.plot((a+Offsetr, a+Offsetr),(a-10+Offsetc , a+10+Offsetc), 'k')
    	self.canv.draw()

    
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
	Hist = filter(None, Hist) 
	return Hist
	
    		
    def Simulate(self):
    	self.GetValues()    	
    	WriteDATAfile(self.height,self.ExpParams,self.Orientation,self.Padding_top,self.Padding_bottom,self.Crop_pct,self.nblocks,self.nblocks_z,self.Lw,self.Ew,self.Tw,self.Swir,self.Sorw,self.Krw,self.Lo,self.Eo,self.To,self.Cw,self.Co,self.Aw,self.Ao,self.nCycle,self.clength)
    	self.SetProgress(33,2)
    	self.Writetoconsole("Running Eclipse...",True)
    	RunEclipse("temp/CORE_TEST-0.DATA")
    	self.SetProgress(66,2)
    	self.Writetoconsole("Plotting Results...")
    	FOPT,FWPT,DIFF=PlotEclipseResults("temp/CORE_TEST-0",self.ExpParams,self.Orientation,self.nblocks,self.nblocks_z)
    	ax  = self.fig.add_subplot(221)
    	ax.plot(FOPT,"g")
    	ax  = self.fig.add_subplot(222)
    	ax.plot(FWPT,"b")
    	ax  = self.fig.add_subplot(223)
    	ax.plot(DIFF,"r")
    	self.canv.draw()
    	self.SetProgress(0,2)
    	self.Writetoconsole("Simulation Finished")
	
    def Optimize(self):
        self.GetValues()
   	self.hist=self.ParseInput()
    	self.Writetoconsole("Running Optimization...",True)
    	app.processEvents()
    	lb = []
    	ub = []
    	
    	index=0
        for i,param in enumerate(self.StaticParams):
		if self.ActiveParams[i]:
			lb+=[self.Lowerbounds[i]]
			ub+=[self.Upperbounds[i]]
			index+=1
      	if len(lb)==0:
      		self.Writetoconsole("No Active modifiers !")
      		return

    	best=Swarm(100,10,lb,ub,1,self,app)
    	self.Writetoconsole("Optimization finished")
    
    def CreateDummyGrid(self):
    	    self.GetValues()
	    self.CreateTemp()
       	    self.Writetoconsole("Creating Grid Properties...",True)
	    nblocks_z=self.nblocks_z
	    nblocks=self.nblocks
	    
	    	
	    n=self.Diameter/nblocks
	    n_z=self.height/nblocks_z
	    
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
    			    
  	    size_x=round(self.Crop_pct/float(nblocks),2)
	    size_z=round((self.height-self.Padding_top-self.Padding_bottom)/float(nblocks_z),2)
	    
    	    ax  = self.fig.add_subplot(111, projection='3d')
    	    for k in range(0,nblocks_z):
    	        self.SetProgress(float(k)/nblocks_z*100,1)
		if self.StopAction: 
			self.Writetoconsole("Stopped by user")
    			return
    	        for i in range(0,nblocks):
    		    for j in range(0,nblocks):
			    r1=[i*size_x,(i+1)*size_x]
			    r2=[j*size_x,(j+1)*size_x]
			    z=[k*size_z,(k+1)*size_z]
			    X, Y = np.meshgrid(r1, r2)
			    Z,Z = np.meshgrid(z, z)
			    if ACTNUM[k][j][i]==1:
				if k==0 :
				    ax.plot_surface(X,Y,z[0],color = (1,0,0,0.8) )
				if k==nblocks_z-1:
				    ax.plot_surface(X,Y,z[1],color = (1,0,0,0.8) )
				    
				if j==0:
				    ax.plot_surface(X,r2[0],Z,color = (1,0,0,0.8) )
				    if ACTNUM[k][j][i+1]==0:
				    	ax.plot_surface(r1[0],Y,z,color = (1,0,0,0.8) )
				    if ACTNUM[k][j][i-1]==0:
				    	ax.plot_surface(r1[1],Y,z,color = (1,0,0,0.8) )
				    continue
				if j==nblocks-1:
				    ax.plot_surface(X,r2[1],Z,color = (1,0,0,0.8) )
				    if ACTNUM[k][j][i+1]==0:
			            	ax.plot_surface(r1[0],Y,z,color = (1,0,0,0.8) )
			            if ACTNUM[k][j][i-1]==0:
				    	ax.plot_surface(r1[1],Y,z,color = (1,0,0,0.8) )
				    continue
				    	
				    
				if i==0:
				    ax.plot_surface(r1[0],Y,z,color = (1,0,0,0.8))
				    if ACTNUM[k][j-1][i]==0:
				    	ax.plot_surface(X,r2[0],Z,color = (1,0,0,0.8) )
				    if ACTNUM[k][j+1][i]==0:
				    	ax.plot_surface(X,r2[1],Z,color = (1,0,0,0.8) )
				    continue
				elif i==nblocks-1:
				    ax.plot_surface(r1[1],Y,z,color = (1,0,0,0.8) )
				    if ACTNUM[k][j-1][i]==0:
				    	ax.plot_surface(X,r2[0],Z,color = (1,0,0,0.8) )
				    if ACTNUM[k][j+1][i]==0:
				    	ax.plot_surface(X,r2[1],Z,color = (1,0,0,0.8) )
				    continue
				
				if ACTNUM[k][j-1][i]==0:
				    ax.plot_surface(X,r2[0],Z,color = (1,0,0,0.8) )
				if ACTNUM[k][j+1][i]==0:
				    ax.plot_surface(X,r2[1],Z,color = (1,0,0,0.8) )    	
				if ACTNUM[k][j][i+1]==0:
				    ax.plot_surface(r1[1],Y,z,color = (1,0,0,0.8) )
				if ACTNUM[k][j][i-1]==0:
				    ax.plot_surface(r1[0],Y,z,color = (1,0,0,0.8) )
				    
	    self.canv.draw()
    	    Poro_string+="\n/\n"
    	    actnum_string+="\n/\n"
    	    permx_string+="\n/\n"
    	    self.progressBar.setProperty("value", 0)

    	    WriteString(actnum_string,"temp/ACTNUM.INC")
    	    WriteString(Poro_string,"temp/PORO.INC")
	    WriteString(permx_string,"temp/PERMX.INC")
	    self.Writetoconsole("Grid Generated")

	    
    def CreateGrid(self):
    	    self.GetValues()
	    self.CreateTemp()
    	    try:
    	    	self.LowEnergyPath
	    except:
		    self.Writetoconsole("Error:Folder Path missing !",True)
		    return	    

	    
    	    self.Writetoconsole("Reading DICOM Files...",True)
    	    files=[f for f in os.listdir(self.LowEnergyPath)]
    	    files2=[f for f in os.listdir(self.HighEnergyPath)]
    	    files=sorted(files)
    	    files2=sorted(files2)
    	    length=len(os.listdir(self.HighEnergyPath))-1
    	    Padding_top=self.Padding_top*length/self.height  #avoid slices at the beginning
    	    Padding_bottom=self.Padding_bottom*length/self.height# avoid Slices at the end
    	    nslices=length-Padding_bottom-Padding_top
    	    nblocks_z,n_z=GetMult(nslices)
	    firstime=True
    	    i=0
    
    	    for f1,f2 in zip(files,files2):
    		if self.StopAction: 
    			self.Writetoconsole("Stopped by user")
    			return
    		
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
  
	    size_x=round(self.Crop_pct/float(nblocks),2)
	    size_z=round((self.height-self.Padding_top-self.Padding_bottom)/float(nblocks_z),2)
	    
    	    ax  = self.fig.add_subplot(111, projection='3d')
    	    for k in range(0,nblocks_z):
    	        self.SetProgress(float(k)/nblocks_z*100,1)	    
    	        for i in range(0,nblocks):
    		    for j in range(0,nblocks):
			    porov=(minporo-PORO[k][j][i])/(minporo-maxporo)
			    r1=[i*size_x,(i+1)*size_x]
			    r2=[j*size_x,(j+1)*size_x]
			    z=[k*size_z,(k+1)*size_z]
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
    				    
	    self.canv.draw()
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
