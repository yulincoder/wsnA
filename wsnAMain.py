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
        self.pushButton_addfile = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_addfile.setGeometry(QtCore.QRect(20, 50, 31, 31))
        self.pushButton_addfile.setStyleSheet(_fromUtf8("background-image: url(/media/tete/F/TinyOS/wsnA/add.png);"))
        self.pushButton_addfile.setText(_fromUtf8(""))
        self.pushButton_addfile.setObjectName(_fromUtf8("pushButton"))

        self.pushButton_start = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_start.setGeometry(QtCore.QRect(20, 120, 31, 31))
        self.pushButton_start.setStyleSheet(_fromUtf8("background-image: url(/media/tete/F/TinyOS/wsnA/start.png);"))
        self.pushButton_start.setText(_fromUtf8(""))
        self.pushButton_start.setObjectName(_fromUtf8("pushButton_start"))
        self.pushButton_Ftest = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_Ftest.setGeometry(QtCore.QRect(20, 190, 31, 31))
        self.pushButton_Ftest.setStyleSheet(_fromUtf8("background-image: url(/media/tete/F/TinyOS/wsnA/F-test.png);"))
        self.pushButton_Ftest.setText(_fromUtf8(""))
        self.pushButton_Ftest.setObjectName(_fromUtf8("pushButton_Ftest"))
        self.pushButton_Interpolation = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_Interpolation.setGeometry(QtCore.QRect(20, 260, 31, 31))
        self.pushButton_Interpolation.setStyleSheet(_fromUtf8("background-image: url(/media/tete/F/TinyOS/wsnA/Interpolation.png);"))
        self.pushButton_Interpolation.setText(_fromUtf8(""))
        self.pushButton_Interpolation.setObjectName(_fromUtf8("pushButton_Interpolation"))
        self.pushButton_about = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_about.setGeometry(QtCore.QRect(20, 510, 31, 31))
        self.pushButton_about.setStyleSheet(_fromUtf8("background-image: url(/media/tete/F/TinyOS/wsnA/about.png);"))
        self.pushButton_about.setText(_fromUtf8(""))
        self.pushButton_about.setObjectName(_fromUtf8("pushButton_about"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(600, 540, 151, 20))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(80, 15, 191, 516))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.textBro_logcalls = QtGui.QTextBrowser(self.tab_1)
        self.textBro_logcalls.setGeometry(QtCore.QRect(-1, -1, 201, 511))
        self.textBro_logcalls.setObjectName(_fromUtf8("textBro_logcalls"))
        self.tabWidget.addTab(self.tab_1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.textBro_func = QtGui.QTextBrowser(self.tab_2)
        self.textBro_func.setGeometry(QtCore.QRect(-1, -1, 201, 511))
        self.textBro_func.setObjectName(_fromUtf8("textBro_func"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.textBro_routed = QtGui.QTextBrowser(self.tab_3)
        self.textBro_routed.setGeometry(QtCore.QRect(-1, -1, 201, 511))
        self.textBro_routed.setObjectName(_fromUtf8("textBro_routed"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        #self.pushButton = QtGui.QPushButton(Dialog)
        #self.pushButton.setGeometry(QtCore.QRect(80, 0, 191, 21))
        #self.pushButton.setObjectName(_fromUtf8("pushButton"))



        self.pushButton_about.clicked.connect(self._about)
        self.pushButton_start.clicked.connect(self.plot)
        self.pushButton_addfile.clicked.connect(self.add_logcallsfile)

        # for matplotlib
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(270, 0, 501, 531))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))

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


        # store the path of logcalls file from simulation.
        self.logcallsfile_path = dict()


    def add_logcallsfile(self):
        ''' Add logcalls and put it's path on the GUI.
        '''
        file_path = QtGui.QFileDialog.getOpenFileName(self, 'add logcalls file', '/')
        if len(file_path) == 0:
            return

        self.logcallsfile_path[len(self.logcallsfile_path)+1] = file_path
        
        self.textBro_logcalls.setText('[Notice]:\nmust be a file containing logcalls.\n')
        for e in self.logcallsfile_path.keys():
            self.textBro_logcalls.append('[' + str(e)  +'] ' + self.logcallsfile_path[e])




    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "wsnA - a TinyOS analysis tool", None))
        self.pushButton_addfile.setToolTip(_translate("Dialog", "<html><head/><body><p>Add logcalls file</p></body></html>", None))
        self.pushButton_start.setToolTip(_translate("Dialog", "<html><head/><body><p>Start</p></body></html>", None))
        self.pushButton_Ftest.setToolTip(_translate("Dialog", "<html><head/><body><p>F-test</p></body></html>", None))
        self.pushButton_Interpolation.setToolTip(_translate("Dialog", "<html><head/><body><p>Interpolation</p></body></html>", None))
        self.pushButton_about.setToolTip(_translate("Dialog", "<html><head/><body><p>About</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("Dialog", "csc file", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "all calllogs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "routed", None))
        #self.pushButton.setText(_translate("Dialog", "Add", None))


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

        #sr_x = [i for i in range(-50, 51, 5)]
        # processbar example:
        sr_x = list()
        import time
        for i in range(-50, 51, 5):
            sr_x.append(i)
            time.sleep(0.3)
            self.progressBar.setValue(i+50)


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

    def _about(self):
        self.about_window = AboutWindow()

        self.about_window = QtGui.QWidget()
        self.about_ui = AboutWindow()
        self.about_ui.setupUi(self.about_window)
        self.about_window.show()

class AboutWindow(QtGui.QWidget):

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("wsnA - About"))
        Form.resize(400, 300)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 80, 151, 65))
        self.label.setStyleSheet(_fromUtf8("\n"
"font: 46pt \"Forte\";"))
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName(_fromUtf8("label"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(90, 80, 64, 65))
        self.widget.setStyleSheet(_fromUtf8("background-image: url(/media/tete/F/TinyOS/wsnA/logo.png);"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 140, 181, 41))
        self.label_2.setStyleSheet(_fromUtf8("font: 9pt \"新宋体\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(150, 190, 81, 21))
        self.label_3.setStyleSheet(_fromUtf8("font: 10pt \"Baskerville Old Face\";"))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.screen = QtGui.QDesktopWidget().screenGeometry()
        self.size = self.geometry()
        self.move((self.screen.width() - self.size.width())/2, (self.screen.height() - self.size.height())/2)


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "wsnA - About", None))
        self.label.setText(_translate("Form", "wsnA", None))
        self.label_2.setText(_translate("Form", "TinyOS无线传感器网络分析软件", None))
        self.label_3.setText(_translate("Form", "Power by Qt", None))



if __name__ == '__main__':
	import sys
	app = QtGui.QApplication(sys.argv)
	w = QtGui.QWidget()
	ui = Ui_Dialog()
	ui.setupUi(w)
	w.show()
	sys.exit(app.exec_())
