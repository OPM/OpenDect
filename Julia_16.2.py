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


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Julia.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from Tools.CoreSimulation import *
from Tools.CTUpscaling import *
import dicom
import os
from os import listdir
from os.path import join

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
    HighEnergyPath=""
    LowEnergyPath=""
    Padding_top=0
    Padding_bottom=0
    Offsetx=0
    Offsety=0
    Diameter=10
    Crop_pct=1
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1244, 663)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 431, 601))
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
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName(_fromUtf8("horizontalSlider_4"))
        self.verticalLayout.addWidget(self.splitter_6)
        self.pushButton_3 = QtGui.QPushButton(self.tab)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout.addWidget(self.pushButton_3)
        self.progressBar = QtGui.QProgressBar(self.tab)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(580, 60, 551, 521))
        self.widget.setObjectName(_fromUtf8("widget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1244, 26))
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
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Julia", None))
        self.pushButton_2.setText(_translate("MainWindow", "Import Low Energy CT", None))
        self.pushButton.setText(_translate("MainWindow", "Import High Energy CT", None))
        self.pushButton.clicked.connect(self.GetHighEnergy)
        self.pushButton_2.clicked.connect(self.GetLowEnergy)
        self.label.setText(_translate("MainWindow", "Core diameter (mm)", None))
        self.label_2.setText(_translate("MainWindow", "Selected Core diameter (mm)", None))
        self.label_4.setText(_translate("MainWindow", "Cropping Top (mm)", None))
        self.label_3.setText(_translate("MainWindow", "Cropping Bottom (mm)", None))
        self.label_5.setText(_translate("MainWindow", "Offset X (mm)", None))
        self.label_6.setText(_translate("MainWindow", "Offset Y (mm)", None))
        self.pushButton_3.setText(_translate("MainWindow", "Create Upscaled model", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Core Model", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Simulation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Parametrization", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionCreate_model.setText(_translate("MainWindow", "Create model", None))
        self.actionSimulate_model.setText(_translate("MainWindow", "Simulate model", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.pushButton_3.clicked.connect(self.CreateGrid)
	self.grid  = QtGui.QGridLayout(self.widget)

    def plotCT(self,plot):
    	fig  = plt.figure()
	axs  = fig.add_subplot(111)
	axs.plot([1,2,3,4],[5,6,7,8])
	canv = FigureCanvas(fig)   
	canv.setMaximumHeight(100) 
	self.grid.addWidget(canv, 0, 0)
	self.grid.addWidget(QtGui.QLabel('test'),1,0)
	win.setLayout(grid)
	win.show()
	win.setFixedSize(150,100)
	
    def GetLowEnergy(self):
   	self.LowEnergyPath=QtGui.QFileDialog.getExistingDirectory()
   	ds1 = dicom.read_file(join(str(self.LowEnergyPath), os.listdir(self.LowEnergyPath)[0]))
	fig  = plt.figure()
	axs  = fig.add_subplot(111)

	axs.imshow(ds1.pixel_array, cmap=pylab.cm.bone)
	canv = FigureCanvas(fig)   
	self.grid.addWidget(canv, 0, 0)
	self.widget.setLayout(grid)
	self.widget.show()
	self.widget.setFixedSize(550,550)
   
    def GetHighEnergy(self):
	self.HighEnergyPath=QtGui.QFileDialog.getExistingDirectory()

    def CreateGrid(self):
    
	    files=[f for f in listdir(self.HighEnergyPath)]
	    files2=[f for f in listdir(self.LowEnergyPath)]
	    files=sorted(files)
	    files2=sorted(files2)
	    length=min(len(listdir(self.HighEnergyPath))-1,len(listdir(self.LowEnergyPath))-1)
	    nslices=length-self.Padding_bottom-self.Padding_top
	    nblocks_z,n_z=GetMult(nslices)
	    firstime=True
	    i=0
	    
	    for f1,f2 in zip(files,files2):
		if i<self.Padding_top:
		    i+=1
		    continue
		if i>=length-self.Padding_bottom:break

		self.progressBar.setProperty("value", float(i-self.Padding_top)*100/(length-self.Padding_bottom-self.Padding_top))

		ds1 = dicom.read_file(join(str(self.LowEnergyPath), f1))
		ds2 = dicom.read_file(join(str(self.HighEnergyPath), f2))
		a = ds1.pixel_array.shape[0]/2 
		Offsetr=2*a*self.Offsetx/self.Diameter
		Offsetc=2*a*self.Offsety/self.Diameter

		x1=GetMaskedValues2(ds1.pixel_array,Offsetr,Offsetc,self.Crop_pct,self.Diameter)
		x2=GetMaskedValues2(ds2.pixel_array,Offsetr,Offsetc,self.Crop_pct,self.Diameter)

		if (firstime):
			n,nblocks=GetMult(x1.shape[0])
			fig  = plt.figure()
			axs  = fig.add_subplot(111)
			a=int(ds1.pixel_array.shape[0]*self.Crop_pct/self.Diameter/2)
			axs.imshow(ds1.pixel_array, cmap=pylab.cm.bone)
			circle=plt.Circle((ds1.pixel_array.shape[0]/2+Offsetr,ds1.pixel_array.shape[0]/2+Offsetc),a,color='r',linewidth=1,fill=False)
			plt.gcf().gca().add_artist(circle)
			axs.plot((a-10+Offsetr , a+10+Offsetr), (a+Offsetc, a+Offsetc), 'k')
			axs.plot((a+Offsetr, a+Offsetr),(a-10+Offsetc , a+10+Offsetc), 'k')

			canv = FigureCanvas(fig)   
			self.grid.addWidget(canv, 0, 0)
			self.widget.setLayout(self.grid)
			self.widget.show()
			self.widget.setFixedSize(550,550)
			PORO=np.zeros(shape=(nblocks_z,nblocks,nblocks))
			ACTNUM=np.zeros(shape=(nblocks_z,nblocks,nblocks))
			PERMX=np.zeros(shape=(nblocks_z,nblocks,nblocks))

		parameters=[2650,1,-0.77,1.98,1007,36597.06,-35330.83,233946.02]
		x, y = np.meshgrid(np.arange(x1.shape[0]), np.arange(x1.shape[1]),indexing='ij')
		z=GetPoro(x1,x2,parameters)
		poro_coarse=UpscalePoro(z,x,y,nblocks,n)


		if (firstime):
		    poro_coarse_avg=poro_coarse
		    a = poro_coarse.shape[0]/2 
		    Offsetr=2*a*self.Offsetx/self.Crop_pct
		    Offsetc=2*a*self.Offsety/self.Crop_pct
		    firstime=False



		if (i-self.Padding_bottom)%n_z==0:
		    PORO[(i-self.Padding_top)/n_z]=poro_coarse_avg
		    ACTNUM[(i-self.Padding_top)/n_z]=GetMaskedValues(poro_coarse_avg,Offsetr,Offsetc)


		else:
		    poro_coarse_avg=poro_coarse_avg*(i-self.Padding_top)/((i-self.Padding_top)+1)+poro_coarse/((i-self.Padding_top)+1)
	        i+=1
	    self.progressBar.setProperty("value", 0)

if __name__ == "__main__":
    import sys
    app = QtGui .QApplication(sys.argv)
    Mainwindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Mainwindow)
    Mainwindow.show()
    sys.exit(app.exec_())
