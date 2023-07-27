# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RamsesGui.ui'
#
# Created: Mon Nov 14 16:49:13 2016
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QImage
from PyQt4.QtGui import * 
import sys

import Forms
import popup 

from subprocess import call


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
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeMono"))
        font.setBold(True)



        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.centralwidget.setStyleSheet("background-color:  #A2C7DA ;")

        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        
        #Directory choosing buttons
        self.ChooseFileBin = QtGui.QPushButton(self.centralwidget)
        self.ChooseFileBin.setObjectName(_fromUtf8("ChooseFileBin"))
        self.ChooseNameFile = QtGui.QPushButton(self.centralwidget)
        self.ChooseNameFile.setObjectName(_fromUtf8("ChooseNameFile"))




        self.EditGlobal = QtGui.QRadioButton(self.centralwidget)
        #self.EditGlobal.setStyleSheet("background-color:  #A3C1DA")
        self.EditGlobal.setObjectName(_fromUtf8("EditGlobal"))
        


        self.gridLayout.addWidget(self.EditGlobal, 0, 0, 1, 1)
        self.Global = QtGui.QLabel(self.centralwidget)
        self.Global.setObjectName(_fromUtf8("Global"))
    


        self.gridLayout.addWidget(self.Global, 0, 1, 1, 1)

        self.EditPoisson = QtGui.QRadioButton(self.centralwidget)
        self.EditPoisson.setObjectName(_fromUtf8("EditPoisson"))
        
        self.gridLayout.addWidget(self.EditPoisson, 0, 2, 1, 1)
        self.Poisson = QtGui.QLabel(self.centralwidget)
        self.Poisson.setObjectName(_fromUtf8("Poisson"))
        self.gridLayout.addWidget(self.Poisson, 0, 3, 1, 1)
        
        self.EditAMR = QtGui.QRadioButton(self.centralwidget)
        self.EditAMR.setObjectName(_fromUtf8("EditAMR"))
        
        self.gridLayout.addWidget(self.EditAMR, 1, 0, 1, 1)
        self.AMR = QtGui.QLabel(self.centralwidget)
        self.AMR.setObjectName(_fromUtf8("AMR"))
        self.gridLayout.addWidget(self.AMR, 1, 1, 1, 1)
       

        self.EditHydro = QtGui.QRadioButton(self.centralwidget)
        self.EditHydro.setObjectName(_fromUtf8("EditHydro"))
        
        self.gridLayout.addWidget(self.EditHydro, 1, 2, 1, 1)
        self.Hydro = QtGui.QLabel(self.centralwidget)
        self.Hydro.setObjectName(_fromUtf8("Hydro"))
        self.gridLayout.addWidget(self.Hydro, 1, 3, 1, 1)


        self.EditOut = QtGui.QRadioButton(self.centralwidget)
        self.EditOut.setObjectName(_fromUtf8("EditOut"))

        self.gridLayout.addWidget(self.EditOut, 2, 0, 1, 1)
        self.Output = QtGui.QLabel(self.centralwidget)
        self.Output.setObjectName(_fromUtf8("Output"))
        self.gridLayout.addWidget(self.Output, 2, 1, 1, 1)

        self.EditPhy = QtGui.QRadioButton(self.centralwidget)
        self.EditPhy.setObjectName(_fromUtf8("EditPhy"))

        self.gridLayout.addWidget(self.EditPhy, 2, 2, 1, 1)
        self.Physical = QtGui.QLabel(self.centralwidget)
        self.Physical.setObjectName(_fromUtf8("Physical"))
        self.gridLayout.addWidget(self.Physical, 2, 3, 1, 1)

        self.EditInit = QtGui.QRadioButton(self.centralwidget)
        self.EditInit.setObjectName(_fromUtf8("EditInit"))

        self.gridLayout.addWidget(self.EditInit, 3, 0, 1, 1)
        self.Initial = QtGui.QLabel(self.centralwidget)
        self.Initial.setObjectName(_fromUtf8("Initial"))
        self.gridLayout.addWidget(self.Initial, 3, 1, 1, 1)

        self.EditRefine = QtGui.QRadioButton(self.centralwidget)
        self.EditRefine.setObjectName(_fromUtf8("EditRefine"))

        self.gridLayout.addWidget(self.EditRefine, 4, 0, 1, 1)
        self.Refinement = QtGui.QLabel(self.centralwidget)
        self.Refinement.setObjectName(_fromUtf8("Refinement"))
        self.gridLayout.addWidget(self.Refinement, 4, 1, 1, 1)

        self.Bin = QtGui.QLabel(self.centralwidget)
        self.Bin.setObjectName(_fromUtf8("Bin"))
        self.gridLayout.addWidget(self.Bin, 4, 3, 1, 1)
        self.BinFileInput = QtGui.QLineEdit(self.centralwidget)
        self.BinFileInput.setObjectName(_fromUtf8("BinFileInput"))
        self.gridLayout.addWidget(self.BinFileInput, 4, 4, 1, 1)
       
        self.gridLayout.addWidget(self.ChooseFileBin, 4, 5, 1, 1)

        self.EditBound = QtGui.QRadioButton(self.centralwidget)
        self.EditBound.setObjectName(_fromUtf8("EditBound"))

        self.gridLayout.addWidget(self.EditBound, 5, 0, 1, 1)
        self.Boundary = QtGui.QLabel(self.centralwidget)
        self.Boundary.setObjectName(_fromUtf8("Boundary"))
        self.gridLayout.addWidget(self.Boundary, 5, 1, 1, 1)
        self.Namelist = QtGui.QLabel(self.centralwidget)
        self.Namelist.setObjectName(_fromUtf8("Namelist"))
        self.gridLayout.addWidget(self.Namelist, 5, 3, 1, 1)
        self.NamefileInput = QtGui.QLineEdit(self.centralwidget)
        self.NamefileInput.setObjectName(_fromUtf8("NamefileInput"))
        self.gridLayout.addWidget(self.NamefileInput, 5, 4, 1, 1)
       
        self.gridLayout.addWidget(self.ChooseNameFile, 5, 5, 1, 1)
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
        self.actionEdit = QtGui.QAction(MainWindow)
        self.actionEdit.setObjectName(_fromUtf8("actionEdir"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.menuFile.addAction(self.actionEdit)
        self.menuFile.addAction(self.actionQuit)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())


        #ADDING QUICKVIEW
        self.actionQUICKVIEW = QtGui.QAction( QtGui.QIcon('ramses.jpg'),'Have a quick view',MainWindow)
        self.actionQUICKVIEW.setObjectName(_fromUtf8("QUICKVIEW"))
       
        self.actionQUICKVIEW.triggered.connect(self.AMRVIEWER)
        self.toolBar = MainWindow.addToolBar("QuickView")
        self.toolBar.addAction(self.actionQUICKVIEW)
        
        #ADDING YT BUTTON

        self.actionYT = QtGui.QAction( QtGui.QIcon('yt.png'),'Analysis using yt',MainWindow)
        self.actionYT.setObjectName(_fromUtf8("YT"))
       
        self.actionYT.triggered.connect(self.YT_ANA)
        self.toolBar = MainWindow.addToolBar("YT")
        self.toolBar.addAction(self.actionYT)
        


        #editing for a pop-up menu
        
        self.EditPhy.toggled.connect(self.Phys_pop)
        self.EditAMR.toggled.connect(self.AMR_pop)
        self.EditInit.toggled.connect(self.Init_pop)
        self.EditOut.toggled.connect(self.Out_pop)
        self.EditBound.toggled.connect(self.Boundary_pop)
        self.EditGlobal.toggled.connect(self.Global_pop)
        self.EditHydro.toggled.connect(self.Hydro_pop)
        self.EditRefine.toggled.connect(self.Refine_pop)
        self.EditPoisson.toggled.connect(self.Poisson_pop)

        
        #editing for collecting namelist directories and bin directories


        self.ChooseFileBin.clicked.connect(self.ChooseBinDir)
        self.ChooseNameFile.clicked.connect(self.ChooseNameDir)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.EditGlobal.setStatusTip(_translate("MainWindow", "Edit Global Parameters", None))
        self.EditGlobal.setText(_translate("MainWindow", "Edit", None))
        self.Global.setText(_translate("MainWindow", "Global Parameters", None))
        self.EditPoisson.setStatusTip(_translate("MainWindow", "Edit Poisson Parameters", None))
        self.EditPoisson.setText(_translate("MainWindow", "Edit", None))
        self.Poisson.setText(_translate("MainWindow", "Poisson Parameters", None))
        self.EditAMR.setStatusTip(_translate("MainWindow", "Edit AMR Parameters", None))
        self.EditAMR.setText(_translate("MainWindow", "Edit", None))
        self.AMR.setText(_translate("MainWindow", "AMR Parameters", None))
        self.EditHydro.setStatusTip(_translate("MainWindow", "edit hydrodynamics solver parameters", None))
        self.EditHydro.setText(_translate("MainWindow", "Edit", None))
        self.Hydro.setStatusTip(_translate("MainWindow", "edit hydrodynamics solver parameters", None))
        self.Hydro.setText(_translate("MainWindow", "Hydrodynamics Solver Parameters", None))
        self.EditOut.setStatusTip(_translate("MainWindow", "Edit Output Parameters", None))
        self.EditOut.setText(_translate("MainWindow", "Edit", None))
        self.Output.setText(_translate("MainWindow", "Output Parameters", None))
        self.EditPhy.setStatusTip(_translate("MainWindow", "Edit Physical Parameters", None))
        self.EditPhy.setText(_translate("MainWindow", "Edit", None))
        self.Physical.setText(_translate("MainWindow", "Physical Parameters", None))
        self.EditInit.setStatusTip(_translate("MainWindow", "Edit Initial Conditions", None))
        self.EditInit.setText(_translate("MainWindow", "Edit", None))
        self.Initial.setText(_translate("MainWindow", "Initial Condition Parameters", None))
        self.EditRefine.setStatusTip(_translate("MainWindow", "Edit Refinement Parameters", None))
        self.EditRefine.setText(_translate("MainWindow", "Edit", None))
        self.Refinement.setText(_translate("MainWindow", "Refinement Parameters", None))
        self.Bin.setText(_translate("MainWindow", "Ramses Bin ", None))
        self.ChooseFileBin.setText(_translate("MainWindow", "File", None))
        self.EditBound.setStatusTip(_translate("MainWindow", "Edit Bounday Parameters", None))
        self.EditBound.setText(_translate("MainWindow", "Edit", None))
        self.Boundary.setText(_translate("MainWindow", "Bounday Condition Parameters", None))
        self.Namelist.setText(_translate("MainWindow", "Namelist Directory", None))
        self.ChooseNameFile.setText(_translate("MainWindow", "File", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionEdit.setText(_translate("MainWindow", "Edit", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+I", None))


    def Phys_pop(self):
        self.EditPhy.setText("Done")
        self.EditPhy.setIcon(QtGui.QIcon('check.png'))
        self.EditPhy.setStyleSheet("background-color: green")
        self.dialog = popup.PhyPopupDialog()
    def AMR_pop(self):
        self.EditAMR.setText("Done")
        self.EditAMR.setIcon(QtGui.QIcon('check.png'))
        self.EditAMR.setStyleSheet("background-color: green")
        self.dialog = popup.AMRPopupDialog()
    def Init_pop(self):
        self.EditInit.setText("Done")
        self.EditInit.setIcon(QtGui.QIcon('check.png'))
        self.EditInit.setStyleSheet("background-color: green")
        self.dialog = popup.InitPopupDialog()
    def Out_pop(self):
        self.EditAMR.setText("Done")
        self.EditOut.setIcon(QtGui.QIcon('check.png'))
        self.EditOut.setStyleSheet("background-color: green")
        self.dialog = popup.OutputPopupDialog()
    def Boundary_pop(self):
        self.EditBound.setText("Done")
        self.EditBound.setIcon(QtGui.QIcon('check.png'))
        self.EditBound.setStyleSheet("background-color: green")
        self.dialog = popup.BoundaryPopupDialog()
    def Global_pop(self):
        self.EditGlobal.setText("Done")
        self.EditGlobal.setIcon(QtGui.QIcon('check.png'))
        self.EditGlobal.setStyleSheet("background-color: green")
        self.dialog = popup.GlobalPopupDialog()
    def Hydro_pop(self):
        self.EditHydro.setText("Done")
        self.EditHydro.setIcon(QtGui.QIcon('check.png'))
        self.EditHydro.setStyleSheet("background-color: green")
        self.dialog = popup.HydroPopupDialog()
    def Refine_pop(self):
        self.EditRefine.setText("Done")
        self.EditRefine.setIcon(QtGui.QIcon('check.png'))
        self.EditRefine.setStyleSheet("background-color: green")
        self.dialog = popup.RefinePopupDialog()
    def Poisson_pop(self):
        self.EditPoisson.setText("Done")
        self.EditPoisson.setIcon(QtGui.QIcon('check.png'))
        self.EditPoisson.setStyleSheet("background-color: green")
        self.dialog = popup.PoissonPopupDialog()
    

    #functions for choosing directories
    
    def ChooseBinDir(self):
        name = str(QFileDialog.getExistingDirectory(self.centralwidget, "Select Directory"))
        self.BinFileInput.setText(name)
    def ChooseNameDir(self):
        name = str(QFileDialog.getExistingDirectory(self.centralwidget, "Select Directory"))
        self.NamefileInput.setText(name)

    #functions for analysis

    def YT_ANA(self):
        self.dialog = popup.YTpopup()

    
    def AMRVIEWER(self):
        from pymses.analysis.visualization import AMRViewer
        AMRViewer.run()
        

    
    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
   
   # MainWindow.setStyleSheet(" background-image: url(./result.jpg);")

   
    MainWindow.setWindowTitle("RamsesGui")
    MainWindow.show()
    sys.exit(app.exec_())

