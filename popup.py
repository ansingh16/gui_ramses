from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QImage
import Forms
import sys


fp = open('test.nml','w')


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
    def __init__(self):
        super(QtGui.QDialog,self).__init__()
        self.setGeometry(150,150,600,500)
        self.dialog = QtGui.QFrame()
        self.ui = Forms.Phy_Frame()
        self.ui.setupUi(self.dialog)
        self.dialog.show()
        self.ui.Save.clicked.connect(self.saving)
        self.ui.Reset.clicked.connect(self.resetting)


    def saving(self):
        choice = QtGui.QMessageBox.question(self,'extract!!',"Do you wanna save?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if (choice == QtGui.QMessageBox.Yes):
            print "Saving Physical Parameters"
            fp = open('test.nml','a')
            textlist = []
            textlist.append('&PHYSICS_PARAMS')
            if(self.ui.editcooling.text() != ''): textlist.append('cooling = ' + self.ui.editcooling.text())
            if(self.ui.edita_spec.text() != ''): textlist.append('a_spec = ' + self.ui.edita_spec.text())
            if(self.ui.editn_star.text() != ''): textlist.append('n_star = '+ self.ui.editn_star.text())          
            if(self.ui.editisothermal.text() != ''): textlist.append('isothermal = ' + self.ui.editisothermal.text())   
            if(self.ui.editreion.text() != ''): textlist.append('reion = ' + self.ui.editreion.text())
            if(self.ui.editdel_star.text() != ''): textlist.append('del_star = ' + self.ui.editdel_star.text())
            if(self.ui.editmetal.text() != ''): textlist.append('metal = ' + self.ui.editmetal.text())
            if(self.ui.editz_ave.text() != ''): textlist.append('z_ave = ' + self.ui.editz_ave.text())
            if(self.ui.editT2_star.text() != ''): textlist.append('T2_star = ' + self.ui.editT2_star.text())
            if(self.ui.edithaardt_madau.text() != ''): textlist.append('haardt_madau = ' + self.ui.edithaardt_madau.text())
            if(self.ui.editt_star.text() != ''): textlist.append('t_star = ' + self.ui.editt_star.text())
            if(self.ui.editg_star.text() != ''): textlist.append('g_star = ' + self.ui.editg_star.text())
            if(self.ui.editJ21.text() != ''): textlist.append('J21 = ' + self.ui.editJ21.text())
            if(self.ui.editeps_star.text() != ''): textlist.append('eps_star = ' + self.ui.editeps_star.text())
            if(self.ui.editeta_sn.text() != ''): textlist.append('eta_sn = ' + self.ui.editeta_sn.text())
            if(self.ui.editndebris.text() != ''): textlist.append('ndebris = ' + self.ui.editndebris.text())
            if(self.ui.editf_w.text() != ''): textlist.append('f_w = ' + self.ui.editf_w.text())
            if(self.ui.edityield.text() != ''): textlist.append('yield = ' + self.ui.edityield.text())
            if(self.ui.editf_ek.text() != ''): textlist.append('f_ek = ' + self.ui.editf_ek.text())
            if(self.ui.editr_bubble.text() != ''): textlist.append('r_bubble = ' + self.ui.editr_bubble.text())
            
            for line in textlist:
                print >>fp,line
            fp.close()
            self.accept
        
        else:
            pass
    
    def resetting(self):
        choice = QtGui.QMessageBox.question(self,'extract!!',"Do you wanna reset?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        
        if (choice == QtGui.QMessageBox.Yes):
            self.ui.editcooling.clear()
            self.ui.edita_spec.clear()
            self.ui.editn_star.clear()          
            self.ui.editisothermal.clear()   
            self.ui.editreion.clear()
            self.ui.editdel_star.clear()
            self.ui.editmetal.clear()
            self.ui.editz_ave.clear()
            self.ui.editT2_star.clear()
            self.ui.edithaardt_madau.clear()
            self.ui.editt_star.clear()
            self.ui.editg_star.clear()
            self.ui.editJ21.clear()
            self.ui.editeps_star.clear()
            self.ui.editeta_sn.clear()
            self.ui.editndebris.clear()
            self.ui.editf_w.clear()
            self.ui.edityield.clear()
            self.ui.editf_ek.clear()
            self.ui.editr_bubble.clear()
        else :
            pass

            
        
       
class AMRPopupDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(QtGui.QDialog,self).__init__()
        self.setGeometry(150,150,600,500)

        self.dialog = QtGui.QFrame()
        self.ui = Forms.AMR_Frame()
        self.ui.setupUi(self.dialog)
        self.dialog.show()
        self.ui.Save.clicked.connect(self.saving)
        self.ui.Reset.clicked.connect(self.resetting)


    def saving(self):
        choice = QtGui.QMessageBox.question(self,'extract!!',"Do you wanna save?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if (choice == QtGui.QMessageBox.Yes):
            print "Saving AMR Parameters"
            textlist = []
            textlist.append(self.ui.editlevelmin.text()) 
            textlist.append(self.ui.editngridtot.text()) 
            textlist.append(self.ui.editlevelmax.text())
            textlist.append(self.ui.editnpartmax.text())  
            textlist.append(self.ui.editngridmax.text())  
            textlist.append(self.ui.editnparttot.text())  
            textlist.append(self.ui.editnexpand.text())  
            textlist.append(self.ui.editboxlen.text())  
            for line in textlist:
                print >>fp,line
            fp.close()
        
        else:
            pass
    
    def resetting(self):
        choice = QtGui.QMessageBox.question(self,'extract!!',"Do you wanna reset?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        
        if (choice == QtGui.QMessageBox.Yes):
            self.ui.editlevelmin.clear()
            self.ui.editngridtot.clear() 
            self.ui.editlevelmax.clear()
            self.ui.editnpartmax.clear()  
            self.ui.editngridmax.clear()  
            self.ui.editnparttot.clear()  
            self.ui.editnexpand.clear()  
            self.ui.editboxlen.clear()  
            
        else :
            pass

            
        
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
        



