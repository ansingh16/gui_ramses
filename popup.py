from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QImage
import Forms


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



                   
class PhyPopupDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(QtGui.QDialog,self).__init__()
        self.setGeometry(150,150,600,500)

        self.dialog = QtGui.QFrame()
        ui = Forms.Phy_Frame()
        ui.setupUi(self.dialog)
        self.dialog.show()


class AMRPopupDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(QtGui.QDialog,self).__init__()
        self.setGeometry(150,150,600,500)

        self.dialog = QtGui.QFrame()
        ui = Forms.AMR_Frame()
        ui.setupUi(self.dialog)
        self.dialog.show()
        
class InitPopupDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(QtGui.QDialog,self).__init__()
        self.setGeometry(150,150,600,500)

        self.dialog = QtGui.QFrame()
        ui = Forms.Init_Frame()
        ui.setupUi(self.dialog)
        self.dialog.show()
        
        
class OutputPopupDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(QtGui.QDialog,self).__init__()
        self.setGeometry(150,150,600,500)

        self.dialog = QtGui.QFrame()
        ui = Forms.Output_Frame()
        ui.setupUi(self.dialog)
        self.dialog.show()
        

class BoundaryPopupDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(QtGui.QDialog,self).__init__()
        self.setGeometry(150,150,600,500)

        self.dialog = QtGui.QFrame()
        ui = Forms.Boundary_Frame()
        ui.setupUi(self.dialog)
        self.dialog.show()
        

class GlobalPopupDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(QtGui.QDialog,self).__init__()
        self.setGeometry(150,150,600,500)

        self.dialog = QtGui.QFrame()
        ui = Forms.Global_Frame()
        ui.setupUi(self.dialog)
        self.dialog.show()
        

class HydroPopupDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(QtGui.QDialog,self).__init__()
        self.setGeometry(150,150,600,500)

        self.dialog = QtGui.QFrame()
        ui = Forms.Hydro_Frame()
        ui.setupUi(self.dialog)
        self.dialog.show()
        
class RefinePopupDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(QtGui.QDialog,self).__init__()
        self.setGeometry(150,150,600,500)

        self.dialog = QtGui.QFrame()
        ui = Forms.Refine_Frame()
        ui.setupUi(self.dialog)
        self.dialog.show()
        
class PoissonPopupDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(QtGui.QDialog,self).__init__()
        self.setGeometry(150,150,600,500)

        self.dialog = QtGui.QFrame()
        ui = Forms.Poisson_Frame()
        ui.setupUi(self.dialog)
        self.dialog.show()
        

