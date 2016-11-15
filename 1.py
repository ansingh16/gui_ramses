# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created: Wed Nov 16 02:11:32 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

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

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName(_fromUtf8("Frame"))
        Frame.resize(400, 300)
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.Save = QtGui.QPushButton(Frame)
        self.Save.setGeometry(QtCore.QRect(0, 0, 85, 27))
        self.Save.setObjectName(_fromUtf8("Save"))
        self.Reset = QtGui.QPushButton(Frame)
        self.Reset.setGeometry(QtCore.QRect(90, 0, 85, 27))
        self.Reset.setObjectName(_fromUtf8("Reset"))

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(_translate("Frame", "Frame", None))
        self.Save.setStatusTip(_translate("Frame", "Save variables", None))
        self.Save.setText(_translate("Frame", "Save", None))
        self.Reset.setStatusTip(_translate("Frame", "Reset value", None))
        self.Reset.setText(_translate("Frame", "Reset", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Frame = QtGui.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())

