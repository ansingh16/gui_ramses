# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RamsesGui.ui'
#
# Created: Mon Nov 14 16:49:13 2016
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QImage

import sys

import Forms
import popup 


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
        MainWindow.resize(869, 603)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.EditPhy = QtGui.QPushButton(self.centralwidget)
        self.EditPhy.setObjectName(_fromUtf8("EditPhy"))
        self.gridLayout.addWidget(self.EditPhy, 0, 0, 1, 1)
        self.Physical = QtGui.QLabel(self.centralwidget)
        self.Physical.setObjectName(_fromUtf8("Physical"))
        self.gridLayout.addWidget(self.Physical, 0, 1, 1, 1)
        self.EditPoison = QtGui.QPushButton(self.centralwidget)
        self.EditPoison.setObjectName(_fromUtf8("EditPoison"))
        self.gridLayout.addWidget(self.EditPoison, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 3, 1, 1)
        self.EditAMR = QtGui.QPushButton(self.centralwidget)
        self.EditAMR.setObjectName(_fromUtf8("EditAMR"))
        self.gridLayout.addWidget(self.EditAMR, 1, 0, 1, 1)
        self.AMR = QtGui.QLabel(self.centralwidget)
        self.AMR.setObjectName(_fromUtf8("AMR"))
        self.gridLayout.addWidget(self.AMR, 1, 1, 1, 1)
        self.EditRun_2 = QtGui.QPushButton(self.centralwidget)
        self.EditRun_2.setObjectName(_fromUtf8("EditRun_2"))
        self.gridLayout.addWidget(self.EditRun_2, 2, 0, 1, 1)
        self.Run = QtGui.QLabel(self.centralwidget)
        self.Run.setObjectName(_fromUtf8("Run"))
        self.gridLayout.addWidget(self.Run, 2, 1, 1, 1)
        self.EditOut = QtGui.QPushButton(self.centralwidget)
        self.EditOut.setObjectName(_fromUtf8("EditOut"))
        self.gridLayout.addWidget(self.EditOut, 3, 0, 1, 1)
        self.Output = QtGui.QLabel(self.centralwidget)
        self.Output.setObjectName(_fromUtf8("Output"))
        self.gridLayout.addWidget(self.Output, 3, 1, 1, 1)
        self.EditInit = QtGui.QPushButton(self.centralwidget)
        self.EditInit.setObjectName(_fromUtf8("EditInit"))
        self.gridLayout.addWidget(self.EditInit, 4, 0, 1, 1)
        self.Initial = QtGui.QLabel(self.centralwidget)
        self.Initial.setObjectName(_fromUtf8("Initial"))
        self.gridLayout.addWidget(self.Initial, 4, 1, 1, 1)
        self.Bin = QtGui.QLabel(self.centralwidget)
        self.Bin.setObjectName(_fromUtf8("Bin"))
        self.gridLayout.addWidget(self.Bin, 4, 3, 1, 1)
        self.BinFileInput = QtGui.QLineEdit(self.centralwidget)
        self.BinFileInput.setObjectName(_fromUtf8("BinFileInput"))
        self.gridLayout.addWidget(self.BinFileInput, 4, 4, 1, 1)
        self.ChooseFileBin = QtGui.QPushButton(self.centralwidget)
        self.ChooseFileBin.setObjectName(_fromUtf8("ChooseFileBin"))
        self.gridLayout.addWidget(self.ChooseFileBin, 4, 5, 1, 1)
        self.EditRefine = QtGui.QPushButton(self.centralwidget)
        self.EditRefine.setObjectName(_fromUtf8("EditRefine"))
        self.gridLayout.addWidget(self.EditRefine, 5, 0, 1, 1)
        self.Refinement = QtGui.QLabel(self.centralwidget)
        self.Refinement.setObjectName(_fromUtf8("Refinement"))
        self.gridLayout.addWidget(self.Refinement, 5, 1, 1, 1)
        self.Namelist = QtGui.QLabel(self.centralwidget)
        self.Namelist.setObjectName(_fromUtf8("Namelist"))
        self.gridLayout.addWidget(self.Namelist, 5, 3, 1, 1)
        self.NamefileInput = QtGui.QLineEdit(self.centralwidget)
        self.NamefileInput.setObjectName(_fromUtf8("NamefileInput"))
        self.gridLayout.addWidget(self.NamefileInput, 5, 4, 1, 1)
        self.ChooseNameFile = QtGui.QPushButton(self.centralwidget)
        self.ChooseNameFile.setObjectName(_fromUtf8("ChooseNameFile"))
        self.gridLayout.addWidget(self.ChooseNameFile, 5, 5, 1, 1)
        self.EditBound = QtGui.QPushButton(self.centralwidget)
        self.EditBound.setObjectName(_fromUtf8("EditBound"))
        self.gridLayout.addWidget(self.EditBound, 6, 0, 1, 1)
        self.Boundary = QtGui.QLabel(self.centralwidget)
        self.Boundary.setObjectName(_fromUtf8("Boundary"))
        self.gridLayout.addWidget(self.Boundary, 6, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)
        self.EditGlobal = QtGui.QLabel(self.centralwidget)
        self.EditGlobal.setObjectName(_fromUtf8("EditGlobal"))
        self.gridLayout.addWidget(self.EditGlobal, 1, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 869, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionEdir = QtGui.QAction(MainWindow)
        self.actionEdir.setObjectName(_fromUtf8("actionEdir"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.menuFile.addAction(self.actionEdir)
        self.menuFile.addAction(self.actionQuit)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())


        #editing for a pop-up menu

        self.EditPhy.clicked.connect(self.Phys_pop)
        self.EditAMR.clicked.connect(self.AMR_pop)
        self.EditInit.clicked.connect(self.Init_pop)
        self.EditOut.clicked.connect(self.Out_pop)
        self.EditBound.clicked.connect(self.Boundary_pop)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.EditPhy.setStatusTip(_translate("MainWindow", "Edit Physical Parameters", None))
        self.EditPhy.setText(_translate("MainWindow", "Edit", None))
        self.Physical.setText(_translate("MainWindow", "Physical Parameters", None))
        self.EditPoison.setStatusTip(_translate("MainWindow", "Edit Poisson Parameters", None))
        self.EditPoison.setText(_translate("MainWindow", "Edit", None))
        self.label.setText(_translate("MainWindow", "Poisson Parameters", None))
        self.EditAMR.setStatusTip(_translate("MainWindow", "Edit AMR Parameters", None))
        self.EditAMR.setText(_translate("MainWindow", "Edit", None))
        self.AMR.setText(_translate("MainWindow", "AMR Parameters", None))
        self.EditRun_2.setStatusTip(_translate("MainWindow", "Edit Run Parameters", None))
        self.EditRun_2.setText(_translate("MainWindow", "Edit", None))
        self.Run.setText(_translate("MainWindow", "Run Parameters", None))
        self.EditOut.setStatusTip(_translate("MainWindow", "Edit Output Parameters", None))
        self.EditOut.setText(_translate("MainWindow", "Edit", None))
        self.Output.setText(_translate("MainWindow", "Output Parameters", None))
        self.EditInit.setStatusTip(_translate("MainWindow", "Edit Initial Conditions", None))
        self.EditInit.setText(_translate("MainWindow", "Edit", None))
        self.Initial.setText(_translate("MainWindow", "Initial Condition Parameters", None))
        self.Bin.setText(_translate("MainWindow", "Ramses Bin ", None))
        self.ChooseFileBin.setText(_translate("MainWindow", "File", None))
        self.EditRefine.setStatusTip(_translate("MainWindow", "Edit Refinement Parameters", None))
        self.EditRefine.setText(_translate("MainWindow", "Edit", None))
        self.Refinement.setText(_translate("MainWindow", "Refinement Parameters", None))
        self.Namelist.setText(_translate("MainWindow", "Namelist Didirectory", None))
        self.ChooseNameFile.setText(_translate("MainWindow", "File", None))
        self.EditBound.setStatusTip(_translate("MainWindow", "Edit Bounday Parameters", None))
        self.EditBound.setText(_translate("MainWindow", "Edit", None))
        self.Boundary.setText(_translate("MainWindow", "Bounday Condition Parameters", None))
        self.pushButton.setStatusTip(_translate("MainWindow", "EditGlobal", None))
        self.pushButton.setText(_translate("MainWindow", "Edit", None))
        self.EditGlobal.setText(_translate("MainWindow", "Global Parameters", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionEdir.setText(_translate("MainWindow", "Edir", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S", None))


    def Phys_pop(self):
        self.dialog = popup.PhyPopupDialog()
    def AMR_pop(self):
        self.dialog = popup.AMRPopupDialog()
    def Init_pop(self):
        self.dialog = popup.InitPopupDialog()
    def Out_pop(self):
        self.dialog = popup.OutputPopupDialog()
    def Boundary_pop(self):
        self.dialog = popup.BoundaryPopupDialog()
    
    
    

    
    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    """
    palette = QtGui.QPalette()
    palette.setBrush(QPalette.Background,QBrush(QPixmap("result.jpg")))
    MainWindow.setPalette(palette)
    """
   # MainWindow.setStyleSheet(" background-image: url(./result.jpg);")

   
    MainWindow.setWindowTitle("RamsesGui")
    MainWindow.show()
    sys.exit(app.exec_())

