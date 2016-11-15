# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'something.ui'
#
# Created: Wed Nov 16 01:50:45 2016
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
        Frame.resize(625, 617)
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.gridLayout = QtGui.QGridLayout(Frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.editu_bound = QtGui.QLineEdit(Frame)
        self.editu_bound.setObjectName(_fromUtf8("editu_bound"))
        self.gridLayout.addWidget(self.editu_bound, 4, 1, 1, 1)
        self.ibound_max = QtGui.QLabel(Frame)
        self.ibound_max.setObjectName(_fromUtf8("ibound_max"))
        self.gridLayout.addWidget(self.ibound_max, 4, 2, 1, 1)
        self.w_bound = QtGui.QLabel(Frame)
        self.w_bound.setObjectName(_fromUtf8("w_bound"))
        self.gridLayout.addWidget(self.w_bound, 6, 0, 1, 1)
        self.editw_bound = QtGui.QLineEdit(Frame)
        self.editw_bound.setObjectName(_fromUtf8("editw_bound"))
        self.gridLayout.addWidget(self.editw_bound, 6, 1, 1, 1)
        self.editibound_min = QtGui.QLineEdit(Frame)
        self.editibound_min.setObjectName(_fromUtf8("editibound_min"))
        self.gridLayout.addWidget(self.editibound_min, 1, 3, 1, 1)
        self.nboundary = QtGui.QLabel(Frame)
        self.nboundary.setStatusTip(_fromUtf8(""))
        self.nboundary.setObjectName(_fromUtf8("nboundary"))
        self.gridLayout.addWidget(self.nboundary, 1, 0, 1, 1)
        self.editnboundary = QtGui.QLineEdit(Frame)
        self.editnboundary.setObjectName(_fromUtf8("editnboundary"))
        self.gridLayout.addWidget(self.editnboundary, 1, 1, 1, 1)
        self.kbound_min = QtGui.QLabel(Frame)
        self.kbound_min.setObjectName(_fromUtf8("kbound_min"))
        self.gridLayout.addWidget(self.kbound_min, 3, 2, 1, 1)
        self.editkbound_min = QtGui.QLineEdit(Frame)
        self.editkbound_min.setObjectName(_fromUtf8("editkbound_min"))
        self.gridLayout.addWidget(self.editkbound_min, 3, 3, 1, 1)
        self.editbound_type = QtGui.QLineEdit(Frame)
        self.editbound_type.setObjectName(_fromUtf8("editbound_type"))
        self.gridLayout.addWidget(self.editbound_type, 2, 1, 1, 1)
        self.u_bound = QtGui.QLabel(Frame)
        self.u_bound.setObjectName(_fromUtf8("u_bound"))
        self.gridLayout.addWidget(self.u_bound, 4, 0, 1, 1)
        self.editd_bound = QtGui.QLineEdit(Frame)
        self.editd_bound.setObjectName(_fromUtf8("editd_bound"))
        self.gridLayout.addWidget(self.editd_bound, 3, 1, 1, 1)
        self.p_bound = QtGui.QLabel(Frame)
        self.p_bound.setObjectName(_fromUtf8("p_bound"))
        self.gridLayout.addWidget(self.p_bound, 7, 0, 1, 1)
        self.editp_bound = QtGui.QLineEdit(Frame)
        self.editp_bound.setObjectName(_fromUtf8("editp_bound"))
        self.gridLayout.addWidget(self.editp_bound, 7, 1, 1, 1)
        self.ibound_min = QtGui.QLabel(Frame)
        self.ibound_min.setObjectName(_fromUtf8("ibound_min"))
        self.gridLayout.addWidget(self.ibound_min, 1, 2, 1, 1)
        self.bound_type = QtGui.QLabel(Frame)
        self.bound_type.setObjectName(_fromUtf8("bound_type"))
        self.gridLayout.addWidget(self.bound_type, 2, 0, 1, 1)
        self.jbound_min = QtGui.QLabel(Frame)
        self.jbound_min.setObjectName(_fromUtf8("jbound_min"))
        self.gridLayout.addWidget(self.jbound_min, 2, 2, 1, 1)
        self.editjbound_min = QtGui.QLineEdit(Frame)
        self.editjbound_min.setObjectName(_fromUtf8("editjbound_min"))
        self.gridLayout.addWidget(self.editjbound_min, 2, 3, 1, 1)
        self.jbound_max = QtGui.QLabel(Frame)
        self.jbound_max.setObjectName(_fromUtf8("jbound_max"))
        self.gridLayout.addWidget(self.jbound_max, 5, 2, 1, 1)
        self.editjbound_max = QtGui.QLineEdit(Frame)
        self.editjbound_max.setObjectName(_fromUtf8("editjbound_max"))
        self.gridLayout.addWidget(self.editjbound_max, 5, 3, 1, 1)
        self.d_bound = QtGui.QLabel(Frame)
        self.d_bound.setStatusTip(_fromUtf8(""))
        self.d_bound.setObjectName(_fromUtf8("d_bound"))
        self.gridLayout.addWidget(self.d_bound, 3, 0, 1, 1)
        self.kbound_max = QtGui.QLabel(Frame)
        self.kbound_max.setObjectName(_fromUtf8("kbound_max"))
        self.gridLayout.addWidget(self.kbound_max, 6, 2, 1, 1)
        self.editkbound_max = QtGui.QLineEdit(Frame)
        self.editkbound_max.setObjectName(_fromUtf8("editkbound_max"))
        self.gridLayout.addWidget(self.editkbound_max, 6, 3, 1, 1)
        self.v_bound = QtGui.QLabel(Frame)
        self.v_bound.setObjectName(_fromUtf8("v_bound"))
        self.gridLayout.addWidget(self.v_bound, 5, 0, 1, 1)
        self.editv_bound = QtGui.QLineEdit(Frame)
        self.editv_bound.setObjectName(_fromUtf8("editv_bound"))
        self.gridLayout.addWidget(self.editv_bound, 5, 1, 1, 1)
        self.editibound_max = QtGui.QLineEdit(Frame)
        self.editibound_max.setObjectName(_fromUtf8("editibound_max"))
        self.gridLayout.addWidget(self.editibound_max, 4, 3, 1, 1)
        self.Save = QtGui.QPushButton(Frame)
        self.Save.setObjectName(_fromUtf8("Save"))
        self.gridLayout.addWidget(self.Save, 0, 1, 1, 1)
        self.Reset = QtGui.QPushButton(Frame)
        self.Reset.setObjectName(_fromUtf8("Reset"))
        self.gridLayout.addWidget(self.Reset, 0, 3, 1, 1)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(_translate("Frame", "Frame", None))
        self.editu_bound.setStatusTip(_translate("Frame", "edit u_bound", None))
        self.ibound_max.setText(_translate("Frame", "ibound_max", None))
        self.w_bound.setText(_translate("Frame", "w_bound", None))
        self.editw_bound.setStatusTip(_translate("Frame", "edit w_bound", None))
        self.editibound_min.setStatusTip(_translate("Frame", "edit ibound_min", None))
        self.nboundary.setText(_translate("Frame", "nboundary", None))
        self.editnboundary.setStatusTip(_translate("Frame", "edit nboundary", None))
        self.kbound_min.setText(_translate("Frame", "kbound_min", None))
        self.editkbound_min.setStatusTip(_translate("Frame", "edit kbound_min", None))
        self.editbound_type.setStatusTip(_translate("Frame", "edit bound_type", None))
        self.u_bound.setText(_translate("Frame", "u_bound", None))
        self.editd_bound.setStatusTip(_translate("Frame", "edit d_bound", None))
        self.p_bound.setText(_translate("Frame", "p_bound", None))
        self.editp_bound.setStatusTip(_translate("Frame", "edit p_bound", None))
        self.ibound_min.setText(_translate("Frame", "ibound_min", None))
        self.bound_type.setText(_translate("Frame", "bound_type", None))
        self.jbound_min.setText(_translate("Frame", "jbound_min", None))
        self.editjbound_min.setStatusTip(_translate("Frame", "edit jbound_min", None))
        self.jbound_max.setText(_translate("Frame", "jbound_max", None))
        self.editjbound_max.setStatusTip(_translate("Frame", "edit jbound_max", None))
        self.d_bound.setText(_translate("Frame", "d_bound", None))
        self.kbound_max.setText(_translate("Frame", "kbound_max", None))
        self.editkbound_max.setStatusTip(_translate("Frame", "edit kbound_max", None))
        self.v_bound.setText(_translate("Frame", "v_bound", None))
        self.editv_bound.setStatusTip(_translate("Frame", "edit v_bound", None))
        self.editibound_max.setStatusTip(_translate("Frame", "edit ibound_max", None))
        self.Save.setStatusTip(_translate("Frame", "Save the variables", None))
        self.Save.setText(_translate("Frame", "Save", None))
        self.Save.setShortcut(_translate("Frame", "Ctrl+S", None))
        self.Reset.setText(_translate("Frame", "Reset", None))
        self.Reset.setShortcut(_translate("Frame", "Ctrl+R", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Frame = QtGui.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())

