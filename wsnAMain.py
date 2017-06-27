# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\untitled.ui'
#
# Created: Sat Jun 17 21:17:35 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
# Author: Zhang T

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
from TaskWatch import NodeLogcalls
from TaskWatch import get_route_related_fun
import os

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


# A tiny function to print logs to console.
def print_log(types='INFO', msg=None):
    all_types = {'warning': 'WARNING', 'err': 'ERROR', 'info': 'INFO'}
    colors = {
        'warning': '\033[1;32m',
        'err': '\033[1;31m',
        'info': '\033[0m',
        'default': '\033[0m'
    }
    print colors[types] + '[' + all_types[types] + ']:\t' + colors['default'] + msg


class Ui_Dialog(QtGui.QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(769, 567)
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(0, -10, 75, 581))
        self.scrollArea.setStyleSheet(
            _fromUtf8("background-image: url(./resource/main.jpg);"))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 73, 579))
        self.scrollAreaWidgetContents.setObjectName(
            _fromUtf8("scrollAreaWidgetContents"))
        self.pushButton_addfile = QtGui.QPushButton(
            self.scrollAreaWidgetContents)
        self.pushButton_addfile.setGeometry(QtCore.QRect(20, 50, 31, 31))
        self.pushButton_addfile.setStyleSheet(
            _fromUtf8("background-image: url(./resource/add.png);"))
        self.pushButton_addfile.setText(_fromUtf8(""))
        self.pushButton_addfile.setObjectName(_fromUtf8("pushButton"))

        self.pushButton_start = QtGui.QPushButton(
            self.scrollAreaWidgetContents)
        self.pushButton_start.setGeometry(QtCore.QRect(20, 120, 31, 31))
        self.pushButton_start.setStyleSheet(
            _fromUtf8("background-image: url(./resource/start.png);"))
        self.pushButton_start.setText(_fromUtf8(""))
        self.pushButton_start.setObjectName(_fromUtf8("pushButton_start"))
        self.pushButton_Ftest = QtGui.QPushButton(
            self.scrollAreaWidgetContents)
        self.pushButton_Ftest.setGeometry(QtCore.QRect(20, 190, 31, 31))
        self.pushButton_Ftest.setStyleSheet(
            _fromUtf8("background-image: url(./resource/F-test.png);"))
        self.pushButton_Ftest.setText(_fromUtf8(""))
        self.pushButton_Ftest.setObjectName(_fromUtf8("pushButton_Ftest"))
        self.pushButton_Interpolation = QtGui.QPushButton(
            self.scrollAreaWidgetContents)
        self.pushButton_Interpolation.setGeometry(
            QtCore.QRect(20, 260, 31, 31))
        self.pushButton_Interpolation.setStyleSheet(
            _fromUtf8("background-image: url(./resource/Interpolation.png);"))
        self.pushButton_Interpolation.setText(_fromUtf8(""))
        self.pushButton_Interpolation.setObjectName(
            _fromUtf8("pushButton_Interpolation"))
        self.pushButton_about = QtGui.QPushButton(
            self.scrollAreaWidgetContents)
        self.pushButton_about.setGeometry(QtCore.QRect(20, 510, 31, 31))
        self.pushButton_about.setStyleSheet(
            _fromUtf8("background-image: url(./resource/about.png);"))
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
        ''' The above codes was created by Qt designer. '''

        self.pushButton_about.clicked.connect(self._about)
        self.pushButton_start.clicked.connect(self.create_node_obj)
        self.pushButton_addfile.clicked.connect(self.add_logcallsfile)
        self.pushButton_Ftest.clicked.connect(self.ANOVA)
        self.pushButton_Interpolation.clicked.connect(self.plot_interpolation)

        # for matplotlib
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(270, 0, 501, 531))
        self.verticalLayoutWidget.setObjectName(
            _fromUtf8("verticalLayoutWidget"))
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
        ''' format: {Numer of logcalls file path: node object}
            ex:{1: node_1}
            Number of logcalls rely on the addition sequence of logcalls file.
        '''
        self.nodes = dict()
        self.progress_bar_value = 0

        # all name of function / Task called.
        # It will be convert to a dict {index: name of function / Task} as the success of node created.
        self.called_func = list()

        # all function / Task related route.
        self.called_func_route = list()

        # store the path of logcalls file from simulation.
        self.logcallsfile_path = dict()

        # The default path to opening logcalls file when initializtion.
        self.default_path = '/'
        ''' The below codes was created by Qt designer. '''
        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def add_logcallsfile(self):
        ''' Add logcalls and put it's path on the GUI.
        '''

        file_path = QtGui.QFileDialog.getOpenFileName(
            self, 'add logcalls file', self.default_path)

        # Reset the default_path to the path containing the logcalls file after a file was selected.
        if os.path.isfile(file_path):
            tmp = str(file_path[::-1])
            self.default_path = file_path[:len(file_path) - tmp.find('/')]

        if len(file_path) == 0:
            return

        if file_path in self.logcallsfile_path.values():
            print_log('warning', 'Already existed file path ')
            return

        self.logcallsfile_path[len(self.logcallsfile_path) + 1] = file_path

        self.textBro_logcalls.setText(
            '[Notice]:\nmust be a file containing logcalls.\n')
        for e in self.logcallsfile_path.keys():
            self.textBro_logcalls.append('[' + str(e) + '] ' +
                                         self.logcallsfile_path[e])

        print_log('info', 'Add a new logcalls file where [' + file_path + ']')

    def create_node_obj(self):
        """ binding the button of start.
            create NodeLogcalls obeject.
        """
        self.called_func = list()  # Reset it.
        progress_value = 0
        self.progressBar.setValue(0)

        for k in self.logcallsfile_path:
            progress_value += 1
            if self.logcallsfile_path[k] not in self.nodes:
                self.nodes[k] = NodeLogcalls(self.logcallsfile_path[k])
                self.progressBar.setValue(
                    float(progress_value) / len(self.logcallsfile_path) * 100)

        for k in self.nodes:
            self.called_func += self.nodes[k].called_func

        self.called_func = list(set(self.called_func))

        tmp = dict()

        def assign(v):
            tmp[self.called_func.index(v)] = v

        map(assign, self.called_func)
        self.called_func = tmp

        self.textBro_func.setText('')  # Clear it.
        for e in self.called_func:
            self.textBro_func.append('[' + str(e) + '] ' + self.called_func[e])

    def ANOVA(self):
        """ 方差分析与路由相关函数, 并显示在面板上
        """
        # self.called_func is a list when it was initialized, and became a dict after [start].
        if not isinstance(self.called_func, dict):
            print_log('err', 'Please click the button of [start]')
            return

        # initializtion of it.
        self.called_func_route = list()

        progress_value = 0
        self.progressBar.setValue(0)
        for e in self.called_func.values():
            # 使用默认的显著水平, 即alpha = 5%, 时间窗口为1000ms
            if get_route_related_fun(self.nodes, e, 1000):
                self.called_func_route.append(e)

            progress_value += 1
            self.progressBar.setValue(
                float(progress_value) / len(self.called_func.values()) * 100)

        self.textBro_routed.setText('')  # Clear it.
        for e in self.called_func_route:
            reverse_dict = {v: k for k, v in self.called_func.items()}
            self.textBro_routed.append('[' + str(reverse_dict[e]) + '] ' + e)

        print_log('info', 'ANOVA was finished.')
        self.plot_all_logcalls()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            _translate("Dialog", "wsnA - a TinyOS analysis tool", None))
        self.pushButton_addfile.setToolTip(
            _translate(
                "Dialog",
                "<html><head/><body><p>Add logcalls file</p></body></html>",
                None))
        self.pushButton_start.setToolTip(
            _translate("Dialog",
                       "<html><head/><body><p>Start</p></body></html>", None))
        self.pushButton_Ftest.setToolTip(
            _translate("Dialog",
                       "<html><head/><body><p>ANOVA</p></body></html>", None))
        self.pushButton_Interpolation.setToolTip(
            _translate("Dialog",
                       "<html><head/><body><p>Interpolation</p></body></html>",
                       None))
        self.pushButton_about.setToolTip(
            _translate("Dialog",
                       "<html><head/><body><p>About</p></body></html>", None))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_1),
            _translate("Dialog", "logcalls file", None))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2),
            _translate("Dialog", "all func", None))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_3),
            _translate("Dialog", "routed", None))
        #self.pushButton.setText(_translate("Dialog", "Add", None))

    def get_sub_two_interpolation_func(self, x=[], fx=[]):
        """ 获得分段二次插值函数
        """

        def sub_two_interpolation_func(Lx):
            result = 0
            for index in range(len(x) - 2):
                if Lx >= x[index] and Lx <= x[index + 2]:
                    result = fx[index]*(Lx-x[index+1])*(Lx-x[index+2])/(x[index]-x[index+1])/(x[index]-x[index+2]) + \
                          fx[index+1]*(Lx-x[index])*(Lx-x[index+2])/(x[index+1]-x[index])/(x[index+1]-x[index+2]) + \
                          fx[index+2]*(Lx-x[index])*(Lx-x[index+1])/(x[index+2]-x[index])/(x[index+2]-x[index+1])
            return result

        return sub_two_interpolation_func

    def plot_interpolation(self):
        """ Draw graph by Interpolation.
        """
        self.plot_all_logcalls(True)
        print_log('info', 'Interpolation was finished.')

    def plot_all_logcalls(self, interpolation=False):
        """ drawing logcalls pattern figure
            param: interpolation   enable/disable interpolation.
        """

        # instead of ax.hold(False)
        self.figure.clear()

        # create an axis
        self.ax1 = self.figure.add_subplot(111)
        self.ax1.set_title('Logcalls pattern')

        any_node_logcalls = dict()
        sr_x = list()

        for e in self.called_func_route:
            for i in self.nodes:
                (i not in sr_x) and sr_x.append(i)
                if e not in any_node_logcalls:
                    any_node_logcalls[e] = list()
                any_node_logcalls[e].append(self.nodes[i].get_func_count(e))

        progress_value = 0
        self.progressBar.setValue(0)
        for e in self.called_func_route:
            sr_fx = any_node_logcalls[e]
            self.ax1.plot(sr_x, sr_fx, linestyle='', marker='o', color='b')

            if interpolation:
                Lx = self.get_sub_two_interpolation_func(sr_x, sr_fx)
                # Enlargement the range to 10 folds for drawing the result of interpolation.
                self.tmp_x = [
                    i / 10.0 for i in range(sr_x[0] * 10, sr_x[-1] * 10 + 1)
                ]
                self.tmp_y = [Lx(i) for i in self.tmp_x]
                self.ax1.plot(
                    self.tmp_x, self.tmp_y, linestyle='--', marker='', label=e)
            else:
                self.ax1.plot(sr_x, sr_fx, linestyle='--', marker='o', label=e)

            progress_value += 1
            self.progressBar.setValue(
                float(progress_value) / len(self.called_func_route) * 100)

        self.ax1.legend(loc='best')

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
        self.label.setStyleSheet(_fromUtf8("\n" "font: 46pt \"Forte\";"))
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName(_fromUtf8("label"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(90, 80, 64, 65))
        self.widget.setStyleSheet(
            _fromUtf8("background-image: url(./resource/logo.png);"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 140, 181, 41))
        self.label_2.setStyleSheet(_fromUtf8("font: 9pt \"新宋体\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(150, 190, 81, 21))
        self.label_3.setStyleSheet(
            _fromUtf8("font: 10pt \"Baskerville Old Face\";"))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.screen = QtGui.QDesktopWidget().screenGeometry()
        self.size = self.geometry()
        self.move((self.screen.width() - self.size.width()) / 2,
                  (self.screen.height() - self.size.height()) / 2)

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
