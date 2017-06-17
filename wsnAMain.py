# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\untitled.ui'
#
# Created: Sat Jun 17 21:17:35 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas  
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar  
import matplotlib.pyplot as plt  
import pylab as pl  
import warnings  
import matplotlib.backends.backend_qt5agg  
import math  
import numpy as np
import sys  


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

class Ui_Dialog(QtGui.QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(769, 567)
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(0, -10, 75, 581))
        self.scrollArea.setStyleSheet(_fromUtf8("background-image: url(/media/tete/F/TinyOS/wsnA/main.jpg);"))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 73, 579))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.pushButton_2 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 50, 31, 31))
        self.pushButton_2.setStyleSheet(_fromUtf8("background-image: url(/media/tete/F/TinyOS/wsnA/start.png);"))
        self.pushButton_2.setText(_fromUtf8(""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 120, 31, 31))
        self.pushButton_3.setStyleSheet(_fromUtf8("background-image: url(/media/tete/F/TinyOS/wsnA/F-test.png);"))
        self.pushButton_3.setText(_fromUtf8(""))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 190, 31, 31))
        self.pushButton_4.setStyleSheet(_fromUtf8("background-image: url(/media/tete/F/TinyOS/wsnA/Interpolation.png);"))
        self.pushButton_4.setText(_fromUtf8(""))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 510, 31, 31))
        self.pushButton_5.setStyleSheet(_fromUtf8("background-image: url(/media/tete/F/TinyOS/wsnA/about.png);"))
        self.pushButton_5.setText(_fromUtf8(""))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(600, 540, 151, 20))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(80, 20, 191, 541))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.textBrowser = QtGui.QTextBrowser(self.tab_1)
        self.textBrowser.setGeometry(QtCore.QRect(-10, 1, 201, 521))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.tabWidget.addTab(self.tab_1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.tab_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(-10, 0, 201, 521))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.textBrowser_3 = QtGui.QTextBrowser(self.tab_3)
        self.textBrowser_3.setGeometry(QtCore.QRect(-10, 1, 201, 521))
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 0, 191, 21))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))


	# for matplotlib
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(270, 0, 501, 531))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))

	
	self.pushButton_5.clicked.connect(self.plot)

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)
	self.verticalLayout_2.addWidget(self.toolbar)
	self.verticalLayout_2.addWidget(self.canvas)



        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton_2.setToolTip(_translate("Dialog", "<html><head/><body><p>Start</p></body></html>", None))
        self.pushButton_3.setToolTip(_translate("Dialog", "<html><head/><body><p>F-test</p></body></html>", None))
        self.pushButton_4.setToolTip(_translate("Dialog", "<html><head/><body><p>Interpolation</p></body></html>", None))
        self.pushButton_5.setToolTip(_translate("Dialog", "<html><head/><body><p>About</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("Dialog", "csc file", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "all calllogs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "routed", None))
        self.pushButton.setToolTip(_translate("Dialog", "<html><head/><body><p>Add csc file</p></body></html>", None))
        self.pushButton.setText(_translate("Dialog", "Add", None))


    def get_sub_two_interpolation_func(self, x = [], fx = []):
	       
        def sub_two_interpolation_func(Lx):
            result = 0
            for index in range(len(x)-2):
                if Lx >= x[index] and Lx <= x[index+2]:
		    result = fx[index]*(Lx-x[index+1])*(Lx-x[index+2])/(x[index]-x[index+1])/(x[index]-x[index+2]) + \
			         fx[index+1]*(Lx-x[index])*(Lx-x[index+2])/(x[index+1]-x[index])/(x[index+1]-x[index+2]) + \
			         fx[index+2]*(Lx-x[index])*(Lx-x[index+1])/(x[index+2]-x[index])/(x[index+2]-x[index+1])
            return result
		     
        return sub_two_interpolation_func

    def plot(self):
        ''' plot some random stuff '''
	print 'hao'
        # random data
	import random
        data = [random.random() for i in range(10)]

        # instead of ax.hold(False)
        self.figure.clear()

        # create an axis
        self.ax1 = self.figure.add_subplot(121)
	# create an axis
        self.ax2 = self.figure.add_subplot(122)

        # discards the old graph
        # ax.hold(False) # deprecated, see above

        sr_x = [i for i in range(-50, 51, 5)]
        sr_fx = [i*random.randint(0, 4) for i in sr_x]
     
        Lx = self.get_sub_two_interpolation_func(sr_x, sr_fx)             
        self.tmp_x = [i for i in range(-50, 51)]      
        self.tmp_y = [Lx(i) for i in self.tmp_x]           

        # plot data
        #ax.plot(data, '*-')
        self.ax1.plot(sr_x, sr_fx, linestyle = ' ', marker='o', color='b')
        self.ax2.plot(self.tmp_x, self.tmp_y, linestyle = '--', color='r')

        # refresh canvas
        self.canvas.draw()

if __name__ == '__main__':
	import sys                                                                                                     
	app = QtGui.QApplication(sys.argv)                                                                             
	w = QtGui.QWidget()                                                                                            
	ui = Ui_Dialog()                                                                                               
	ui.setupUi(w)                                                                                                  
	w.show()                                                                                                       
	sys.exit(app.exec_())     




