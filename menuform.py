# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'something.ui'
#
# Created: Mon Nov 14 23:14:17 2016
#      by: PyQt4 UI code generator 4.10.1
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
        Frame.resize(736, 564)
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.gridLayout = QtGui.QGridLayout(Frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.a_reion = QtGui.QLabel(Frame)
        self.a_reion.setObjectName(_fromUtf8("a_reion"))
        self.gridLayout.addWidget(self.a_reion, 6, 0, 1, 1)
        self.isothermal = QtGui.QLabel(Frame)
        self.isothermal.setObjectName(_fromUtf8("isothermal"))
        self.gridLayout.addWidget(self.isothermal, 1, 0, 1, 1)
        self.isothermal_2 = QtGui.QLineEdit(Frame)
        self.isothermal_2.setObjectName(_fromUtf8("isothermal_2"))
        self.gridLayout.addWidget(self.isothermal_2, 1, 1, 1, 1)
        self.aspec = QtGui.QLabel(Frame)
        self.aspec.setObjectName(_fromUtf8("aspec"))
        self.gridLayout.addWidget(self.aspec, 5, 0, 1, 1)
        self.metal = QtGui.QLabel(Frame)
        self.metal.setObjectName(_fromUtf8("metal"))
        self.gridLayout.addWidget(self.metal, 2, 0, 1, 1)
        self.cooling = QtGui.QLabel(Frame)
        self.cooling.setObjectName(_fromUtf8("cooling"))
        self.gridLayout.addWidget(self.cooling, 0, 0, 1, 1)
        self.cooling_2 = QtGui.QLineEdit(Frame)
        self.cooling_2.setObjectName(_fromUtf8("cooling_2"))
        self.gridLayout.addWidget(self.cooling_2, 0, 1, 1, 1)
        self.tstar = QtGui.QLineEdit(Frame)
        self.tstar.setObjectName(_fromUtf8("tstar"))
        self.gridLayout.addWidget(self.tstar, 0, 3, 1, 1)
        self.f_w = QtGui.QLabel(Frame)
        self.f_w.setObjectName(_fromUtf8("f_w"))
        self.gridLayout.addWidget(self.f_w, 4, 2, 1, 1)
        self.f_w_2 = QtGui.QLineEdit(Frame)
        self.f_w_2.setObjectName(_fromUtf8("f_w_2"))
        self.gridLayout.addWidget(self.f_w_2, 4, 3, 1, 1)
        self.gstar_2 = QtGui.QLineEdit(Frame)
        self.gstar_2.setObjectName(_fromUtf8("gstar_2"))
        self.gridLayout.addWidget(self.gstar_2, 2, 3, 1, 1)
        self.yield = QtGui.QLabel(Frame)
        self.yield.setObjectName(_fromUtf8("yield"))
        self.gridLayout.addWidget(self.yield, 3, 2, 1, 1)
        self.yield_2 = QtGui.QLineEdit(Frame)
        self.yield_2.setObjectName(_fromUtf8("yield_2"))
        self.gridLayout.addWidget(self.yield_2, 3, 3, 1, 1)
        self.startime = QtGui.QLabel(Frame)
        self.startime.setObjectName(_fromUtf8("startime"))
        self.gridLayout.addWidget(self.startime, 0, 2, 1, 1)
        self.delstar = QtGui.QLabel(Frame)
        self.delstar.setObjectName(_fromUtf8("delstar"))
        self.gridLayout.addWidget(self.delstar, 1, 2, 1, 1)
        self.delstar_2 = QtGui.QLineEdit(Frame)
        self.delstar_2.setObjectName(_fromUtf8("delstar_2"))
        self.gridLayout.addWidget(self.delstar_2, 1, 3, 1, 1)
        self.gstar = QtGui.QLabel(Frame)
        self.gstar.setObjectName(_fromUtf8("gstar"))
        self.gridLayout.addWidget(self.gstar, 2, 2, 1, 1)
        self.z_reion = QtGui.QLineEdit(Frame)
        self.z_reion.setObjectName(_fromUtf8("z_reion"))
        self.gridLayout.addWidget(self.z_reion, 6, 1, 1, 1)
        self.hm = QtGui.QLabel(Frame)
        self.hm.setObjectName(_fromUtf8("hm"))
        self.gridLayout.addWidget(self.hm, 3, 0, 1, 1)
        self.metal_2 = QtGui.QLineEdit(Frame)
        self.metal_2.setObjectName(_fromUtf8("metal_2"))
        self.gridLayout.addWidget(self.metal_2, 2, 1, 1, 1)
        self.hm_2 = QtGui.QLineEdit(Frame)
        self.hm_2.setObjectName(_fromUtf8("hm_2"))
        self.gridLayout.addWidget(self.hm_2, 3, 1, 1, 1)
        self.J21_2 = QtGui.QLineEdit(Frame)
        self.J21_2.setObjectName(_fromUtf8("J21_2"))
        self.gridLayout.addWidget(self.J21_2, 4, 1, 1, 1)
        self.J21 = QtGui.QLabel(Frame)
        self.J21.setObjectName(_fromUtf8("J21"))
        self.gridLayout.addWidget(self.J21, 4, 0, 1, 1)
        self.a_spec = QtGui.QLineEdit(Frame)
        self.a_spec.setObjectName(_fromUtf8("a_spec"))
        self.gridLayout.addWidget(self.a_spec, 5, 1, 1, 1)
        self.z_ave_2 = QtGui.QLineEdit(Frame)
        self.z_ave_2.setObjectName(_fromUtf8("z_ave_2"))
        self.gridLayout.addWidget(self.z_ave_2, 7, 1, 1, 1)
        self.z_ave = QtGui.QLabel(Frame)
        self.z_ave.setObjectName(_fromUtf8("z_ave"))
        self.gridLayout.addWidget(self.z_ave, 7, 0, 1, 1)
        self.ndebris_2 = QtGui.QLineEdit(Frame)
        self.ndebris_2.setObjectName(_fromUtf8("ndebris_2"))
        self.gridLayout.addWidget(self.ndebris_2, 5, 3, 1, 1)
        self.ndebris = QtGui.QLabel(Frame)
        self.ndebris.setObjectName(_fromUtf8("ndebris"))
        self.gridLayout.addWidget(self.ndebris, 5, 2, 1, 1)
        self.f_ek = QtGui.QLabel(Frame)
        self.f_ek.setObjectName(_fromUtf8("f_ek"))
        self.gridLayout.addWidget(self.f_ek, 6, 2, 1, 1)
        self.f_ek_2 = QtGui.QLineEdit(Frame)
        self.f_ek_2.setObjectName(_fromUtf8("f_ek_2"))
        self.gridLayout.addWidget(self.f_ek_2, 6, 3, 1, 1)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(_translate("Frame", "Frame", None))
        self.a_reion.setText(_translate("Frame", "z_reion", None))
        self.isothermal.setText(_translate("Frame", "isothermal", None))
        self.aspec.setText(_translate("Frame", "a_spec", None))
        self.metal.setText(_translate("Frame", "metal", None))
        self.cooling.setText(_translate("Frame", "cooling", None))
        self.f_w.setText(_translate("Frame", "f_w=10.0, r_bubble=0", None))
        self.yield.setText(_translate("Frame", "eta_sn=0.0, yield=0.1", None))
        self.startime.setText(_translate("Frame", "t_star=0.0, eps_star", None))
        self.delstar.setText(_translate("Frame", "n_star=0.1, del_star=200", None))
        self.gstar.setText(_translate("Frame", "T2_star=0.0, g_star=1.6", None))
        self.hm.setText(_translate("Frame", "haardt_madau", None))
        self.J21.setText(_translate("Frame", "J21", None))
        self.z_ave.setText(_translate("Frame", "z_ave", None))
        self.ndebris.setText(_translate("Frame", "ndebris = 1", None))
        self.f_ek.setText(_translate("Frame", "f_ek = 1", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Frame = QtGui.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())

