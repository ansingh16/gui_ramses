# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'something.ui'
#
# Created: Wed Nov 16 16:08:42 2016
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

class Ui_cosmo(object):
    def setupUi(self, cosmo):
        cosmo.setObjectName(_fromUtf8("cosmo"))
        cosmo.resize(548, 278)
        cosmo.setFrameShape(QtGui.QFrame.StyledPanel)
        cosmo.setFrameShadow(QtGui.QFrame.Raised)
        self.gridLayout = QtGui.QGridLayout(cosmo)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gravity_type = QtGui.QLabel(cosmo)
        self.gravity_type.setStatusTip(_fromUtf8(""))
        self.gravity_type.setObjectName(_fromUtf8("gravity_type"))
        self.gridLayout.addWidget(self.gravity_type, 0, 0, 1, 1)
        self.editgravity_type = QtGui.QLineEdit(cosmo)
        self.editgravity_type.setObjectName(_fromUtf8("editgravity_type"))
        self.gridLayout.addWidget(self.editgravity_type, 0, 1, 1, 1)
        self.cg_levelmin = QtGui.QLabel(cosmo)
        self.cg_levelmin.setObjectName(_fromUtf8("cg_levelmin"))
        self.gridLayout.addWidget(self.cg_levelmin, 0, 2, 1, 1)
        self.editcg_levelmin = QtGui.QLineEdit(cosmo)
        self.editcg_levelmin.setObjectName(_fromUtf8("editcg_levelmin"))
        self.gridLayout.addWidget(self.editcg_levelmin, 0, 3, 1, 2)
        self.epsilon = QtGui.QLabel(cosmo)
        self.epsilon.setObjectName(_fromUtf8("epsilon"))
        self.gridLayout.addWidget(self.epsilon, 1, 0, 1, 1)
        self.editepsilon = QtGui.QLineEdit(cosmo)
        self.editepsilon.setObjectName(_fromUtf8("editepsilon"))
        self.gridLayout.addWidget(self.editepsilon, 1, 1, 1, 1)
        self.cic_levelmax = QtGui.QLabel(cosmo)
        self.cic_levelmax.setObjectName(_fromUtf8("cic_levelmax"))
        self.gridLayout.addWidget(self.cic_levelmax, 1, 2, 1, 2)
        self.editcic_levelmax = QtGui.QLineEdit(cosmo)
        self.editcic_levelmax.setObjectName(_fromUtf8("editcic_levelmax"))
        self.gridLayout.addWidget(self.editcic_levelmax, 1, 4, 1, 1)
        self.gravity_params = QtGui.QLabel(cosmo)
        self.gravity_params.setStatusTip(_fromUtf8(""))
        self.gravity_params.setObjectName(_fromUtf8("gravity_params"))
        self.gridLayout.addWidget(self.gravity_params, 2, 0, 1, 1)
        self.editgravity_params = QtGui.QLineEdit(cosmo)
        self.editgravity_params.setObjectName(_fromUtf8("editgravity_params"))
        self.gridLayout.addWidget(self.editgravity_params, 2, 1, 1, 1)

        self.retranslateUi(cosmo)
        QtCore.QMetaObject.connectSlotsByName(cosmo)

    def retranslateUi(self, cosmo):
        cosmo.setWindowTitle(_translate("cosmo", "Frame", None))
        self.gravity_type.setText(_translate("cosmo", "gravity_type", None))
        self.editgravity_type.setStatusTip(_translate("cosmo", "edit gravity_type", None))
        self.cg_levelmin.setText(_translate("cosmo", "cg_levelmin", None))
        self.editcg_levelmin.setStatusTip(_translate("cosmo", "edit cg_levelmin", None))
        self.epsilon.setText(_translate("cosmo", "epsilon", None))
        self.editepsilon.setStatusTip(_translate("cosmo", "edit epsilon", None))
        self.cic_levelmax.setText(_translate("cosmo", "cic_levelmax", None))
        self.editcic_levelmax.setStatusTip(_translate("cosmo", "edit cic_levelmax", None))
        self.gravity_params.setText(_translate("cosmo", "gravity_params", None))
        self.editgravity_params.setStatusTip(_translate("cosmo", "edit gravity_params", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    cosmo = QtGui.QFrame()
    ui = Ui_cosmo()
    ui.setupUi(cosmo)
    cosmo.show()
    sys.exit(app.exec_())

