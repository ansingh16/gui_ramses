# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'attempt.ui'
#
# Created: Mon Nov 14 00:03:33 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
import sys
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
        MainWindow.resize(504, 496)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.le = QtGui.QLineEdit(self.centralwidget)
        self.PushButton2 = QtGui.QPushButton(self.centralwidget)

        self.le.setObjectName("host")
        self.le.setText("Host")


        self.PushButton2.clicked.connect(self.my_func)

        self.PushButton2.setGeometry(QtCore.QRect(10, 190, 91, 27))
        self.PushButton2.setObjectName(_fromUtf8("PushButton2"))
        self.PushButton1 = QtGui.QPushButton(self.centralwidget)

        self.PushButton1.clicked.connect(self.acquire_it)

        self.PushButton1.setGeometry(QtCore.QRect(9, 132, 90, 27))
        self.PushButton1.setObjectName(_fromUtf8("PushButton1"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 504, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.Quit = QtGui.QAction(MainWindow)
        
        self.Quit.triggered.connect(self.end_fn)

        self.Quit.setObjectName(_fromUtf8("Quit"))
        self.menuFile.addAction(self.Quit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def my_func(self):
        print "M here"
        sys.exit()

    def end_fn(self):
        sys.exit()

    def acquire_it(self):

        text = self.le.text()
        print text
        


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.PushButton2.setStatusTip(_translate("MainWindow", "Push me tooo", None))
        self.PushButton2.setText(_translate("MainWindow", "PushButton2", None))
        self.PushButton1.setStatusTip(_translate("MainWindow", "push me", None))
        self.PushButton1.setText(_translate("MainWindow", "PushButton1", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.Quit.setText(_translate("MainWindow", "Quit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

