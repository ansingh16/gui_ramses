from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QImage
import Forms
import sys
import YT_Dialog

fp = open('RAMSES_GUI.nml','w')


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
        self.dialog = QtGui.QDialog()
        self.ui = Forms.Phy_Dialog()
        self.ui.setupUi(self.dialog)
        self.ui.Save.clicked.connect(self.saving)
        self.ui.Reset.clicked.connect(self.resetting)
        self.dialog.show()

       

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
            #fp.close()
            self.dialog.accept()
                
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

        self.dialog = QtGui.QDialog()
        self.ui = Forms.AMR_Dialog()
        self.ui.setupUi(self.dialog)
        
        self.ui.Save.clicked.connect(self.saving)
        self.ui.Reset.clicked.connect(self.resetting)

        self.dialog.show()

    def saving(self):
        choice = QtGui.QMessageBox.question(self,'extract!!',"Do you wanna save?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if (choice == QtGui.QMessageBox.Yes):
            print "Saving AMR Parameters"
            textlist = []
            textlist.append('&AMR_PARAMS')
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
            #fp.close()
            self.dialog.accept()
                
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

        self.dialog = QtGui.QDialog()
        self.ui = Forms.Init_Dialog()
        self.ui.setupUi(self.dialog)
        self.ui.Save.clicked.connect(self.saving)
        self.ui.Reset.clicked.connect(self.resetting)
        self.dialog.show()
        

    def saving(self):
        choice = QtGui.QMessageBox.question(self,'extract!!',"Do you wanna save?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if (choice == QtGui.QMessageBox.Yes):
            print "Saving INIT Parameters"
            textlist = []
            textlist.append('&INIT_PARAMS')
            textlist.append('nregion= ' + self.ui.editnregion.text())
            textlist.append('length_x= ' + self.ui.editlength_x.text())
            textlist.append( 'region_type= ' + self.ui.editregion_type.text())
            textlist.append( 'length_y= ' + self.ui.editlength_y.text())
            textlist.append('x_center= ' + self.ui.editx_center.text())
            textlist.append('length_z= ' + self.ui.editlength_z.text())
            textlist.append('y_center= ' + self.ui.edity_center.text())
            textlist.append('exp_region= ' + self.ui.editexp_region.text())
            textlist.append('z_center= ' + self.ui.editz_center.text())
            textlist.append('filetype= ' + self.ui.editfiletype.text())
            textlist.append('d_region= ' + self.ui.editd_region.text())
            textlist.append('aexp_ini= ' + self.ui.editaexp_ini.text())
            textlist.append('u_region= ' + self.ui.editu_region.text())
            textlist.append('multiple= ' + self.ui.editmultiple.text())
            textlist.append('w_region= ' + self.ui.editw_region.text())
            textlist.append('initfile= ' +self.ui.editinitfile.text())
            textlist.append('p_region= ' +self.ui.editp_region.text())

            for line in textlist:
                print >>fp,line
            #fp.close()
            self.dialog.accept()
                
        else:
            pass
            
    def resetting(self):
        choice = QtGui.QMessageBox.question(self,'extract!!',"Do you wanna reset?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        
        if (choice == QtGui.QMessageBox.Yes):
            
            self.ui.editnregion.clear()
            self.ui.editlength_x.clear()
            self.ui.editregion_type.clear()
            self.ui.editlength_y.clear()
            self.ui.editx_center.clear()
            self.ui.editlength_z.clear()
            self.ui.edity_center.clear()
            self.ui.editexp_region.clear()
            self.ui.editz_center.clear()
            self.ui.editfiletype.clear()
            self.ui.editd_region.clear()
            self.ui.editaexp_ini.clear()
            self.ui.editu_region.clear()
            self.ui.editmultiple.clear()
            self.ui.editw_region.clear()
            self.ui.editinitfile.clear()
            self.ui.editp_region.clear()
            
        else :
            pass



    

        
class OutputPopupDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(QtGui.QDialog,self).__init__()
        self.setGeometry(150,150,600,500)

        self.dialog = QtGui.QDialog()
        self.ui = Forms.Output_Dialog()
        self.ui.setupUi(self.dialog)

        self.ui.Save.clicked.connect(self.saving)
        self.ui.Reset.clicked.connect(self.resetting)
        self.dialog.show()
        

    
    def saving(self):
        choice = QtGui.QMessageBox.question(self,'extract!!',"Do you wanna save?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if (choice == QtGui.QMessageBox.Yes):
            print "Saving OUT Parameters"
            textlist = []
            textlist.append('&OUT_PARAMS')
            textlist.append(self.ui.edittend.text())
            textlist.append(self.ui.editnoutput.text())
            textlist.append(self.ui.editdelta_tout_2.text())
            textlist.append(self.ui.edittout.text())
            textlist.append(self.ui.editaend.text())
            textlist.append(self.ui.editdelta_tout.text())
            textlist.append(self.ui.editfoutput.text())

            for line in textlist:
                print >>fp,line
            #fp.close()
            self.dialog.accept()
                
        else:
            pass
            
    def resetting(self):
        choice = QtGui.QMessageBox.question(self,'extract!!',"Do you wanna reset?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        
        if (choice == QtGui.QMessageBox.Yes):
            self.ui.edittend.clear()
            self.ui.editnoutput.clear()
            self.ui.editdelta_tout_2.clear()
            self.ui.edittout.clear()
            self.ui.editaend.clear()
            self.ui.editdelta_tout.clear()
            self.ui.editfoutput.clear()

        else :
            pass



class BoundaryPopupDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(QtGui.QDialog,self).__init__()
        self.setGeometry(150,150,600,500)

        self.dialog = QtGui.QDialog()
        self.ui = Forms.Boundary_Dialog()
        self.ui.setupUi(self.dialog)
        self.ui.Save.clicked.connect(self.saving)
        self.ui.Reset.clicked.connect(self.resetting)

        self.dialog.show()
        
          
    def saving(self):
        choice = QtGui.QMessageBox.question(self,'extract!!',"Do you wanna save?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if (choice == QtGui.QMessageBox.Yes):
            print "Saving BOUNDARY Parameters"
            textlist = []
            textlist.append('&BOUNDARY_PARAMS')
            textlist.append('nboundary= '  + self.ui.editnboundary.text())
            textlist.append('ibound_min= ' + self.ui.editibound_min.text())
            textlist.append('bound_type= ' + self.ui.editbound_type.text())
            textlist.append('jbound_min= ' + self.ui.editjbound_min.text())
            textlist.append('d_bound= ' + self.ui.editd_bound.text())
            textlist.append('kbound_min= ' + self.ui.editkbound_min.text())
            textlist.append('u_bound= '  + self.ui.editu_bound.text())
            textlist.append('ibound_max= ' + self.ui.editibound_max.text())
            textlist.append('v_bound= '  + self.ui.editv_bound.text())
            textlist.append('jbound_max= ' + self.ui.editjbound_max.text())
            textlist.append('w_bound= '  + self.ui.editw_bound.text())
            textlist.append('kbound_max= '  + self.ui.editkbound_max.text())
            textlist.append('p_bound= '  + self.ui.editp_bound.text())
            

            for line in textlist:
                print >>fp,line
            #fp.close()
            self.dialog.accept()
                
        else:
            pass
            
    def resetting(self):
        choice = QtGui.QMessageBox.question(self,'extract!!',"Do you wanna reset?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        
        if (choice == QtGui.QMessageBox.Yes):
            self.ui.editnboundary.clear()
            self.ui.editibound_min.clear()
            self.ui.editbound_type.clear()
            self.ui.editjbound_min.clear()
            self.ui.editd_bound.clear()
            self.ui.editkbound_min.clear()
            self.ui.editu_bound.clear()
            self.ui.editibound_max.clear()
            self.ui.editv_bound.clear()
            self.ui.editjbound_max.clear()
            self.ui.editw_bound.clear()
            self.ui.editkbound_max.clear()
            self.ui.editp_bound.clear()
            
        else :
            pass




class GlobalPopupDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(QtGui.QDialog,self).__init__()
        self.setGeometry(150,150,600,500)

        self.dialog = QtGui.QDialog()
        self.ui = Forms.Global_Dialog()
        self.ui.setupUi(self.dialog)
        self.ui.Save.clicked.connect(self.saving)
        self.ui.Reset.clicked.connect(self.resetting)

        self.dialog.show()
        
    def saving(self):
        choice = QtGui.QMessageBox.question(self,'extract!!',"Do you wanna save?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if (choice == QtGui.QMessageBox.Yes):
            print "Saving RUN Parameters"
            textlist = []
            textlist.append('&RUN_PARAMS')
            textlist.append('hydro= '  + self.ui.edithydro.text())
            textlist.append('nrestart= ' + self.ui.editnrestart.text())
            textlist.append('nstepmax= '  + self.ui.editnstepmax.text())
            textlist.append('cosmo= '  + self.ui.editcosmo.text())
            textlist.append('nremap= '  + self.ui.editnremap.text())
            textlist.append('pic= '  + self.ui.editpic.text())
            textlist.append('poisson= '  + self.ui.editpoisson.text())
            textlist.append('ncontrol= ' + self.ui.editncontrol.text())
            textlist.append('nsubcycle= ' + self.ui.editnsubcycle.text())
            textlist.append('verbose= ' + self.ui.editverbose.text())
            textlist.append('ordering= ' + self.ui.editordering.text())
            

            for line in textlist:
                print >>fp,line
            #fp.close()
            self.dialog.accept()
                
        else:
            pass
            
    def resetting(self):
        choice = QtGui.QMessageBox.question(self,'extract!!',"Do you wanna reset?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if (choice == QtGui.QMessageBox.Yes):
            self.ui.edithydro.clear()
            self.ui.editnrestart.clear()
            self.ui.editnstepmax.clear()
            self.ui.editcosmo.clear()
            self.ui.editnremap.clear()
            self.ui.editpic.clear()
            self.ui.editpoisson.clear()
            self.ui.editncontrol.clear()
            self.ui.editnsubcycle.clear()
            self.ui.editverbose.clear()
            self.ui.editordering.clear()
            
        else :
            pass




class HydroPopupDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(QtGui.QDialog,self).__init__()
        self.setGeometry(150,150,600,500)
        self.dialog = QtGui.QDialog()
        self.ui = Forms.Hydro_Dialog()
        self.ui.setupUi(self.dialog)
        self.ui.Save.clicked.connect(self.saving)
        self.ui.Reset.clicked.connect(self.resetting)
        self.dialog.show()

    def saving(self):
        choice = QtGui.QMessageBox.question(self,'extract!!',"Do you wanna save?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if (choice == QtGui.QMessageBox.Yes):
            print "Saving HYDRO Parameters"
            textlist = []
            textlist.append('&HYDRO_PARAMS')
            textlist.append('smallc= ' + self.ui.editsmallc.text())
            textlist.append('riemann2d= ' + self.ui.editriemann2d.text())
            textlist.append('gamma= ' + self.ui.editgamma.text())
            textlist.append('slope_type= ' + self.ui.editslope_type.text())
            textlist.append('courant_factor= ' + self.ui.editcourant_factor.text())
            textlist.append('smallr= ' + self.ui.editsmallr.text())
            textlist.append('niter_riemann= ' + self.ui.editniter_riemann.text())
            textlist.append('riemann= ' + self.ui.editriemann.text())
            textlist.append('pressure_fix= ' + self.ui.editpressure_fix.text()) 
            
            for line in textlist:
                print >>fp,line
            #fp.close()
            self.dialog.accept()
                
        else:
            pass
            
    def resetting(self):
        choice = QtGui.QMessageBox.question(self,'extract!!',"Do you wanna reset?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if (choice == QtGui.QMessageBox.Yes):

            self.ui.editsmallc.clean()
            self.ui.editriemann2d.clean()
            self.ui.editgamma.clean()
            self.ui.editslope_type.clean()
            self.ui.editcourant_factor.clean()
            self.ui.editsmallr.clean()
            self.ui.editniter_riemann.clean()
            self.ui.editriemann.clean()
            self.ui.editpressure_fix.clean() 
            
        else :
            pass


        
class RefinePopupDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(QtGui.QDialog,self).__init__()
        self.setGeometry(150,150,600,500)

        self.dialog = QtGui.QDialog()
        self.ui = Forms.Refine_Dialog()
        self.ui.setupUi(self.dialog)
        self.ui.Save.clicked.connect(self.saving)
        self.ui.Reset.clicked.connect(self.resetting)
        self.dialog.show()


    def saving(self):
        choice = QtGui.QMessageBox.question(self,'extract!!',"Do you wanna save?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if (choice == QtGui.QMessageBox.Yes):
            print "Saving REFINE Parameters"
            textlist = []
            textlist.append('&REFINE_PARAMS')
            textlist.append('mass_sph= '  + self.ui.editmass_sph.text())
            textlist.append('floor_d= '  + self.ui.editfloor_d.text())
            textlist.append('err_grad_d= '  + self.ui.editerr_grad_d.text())
            textlist.append('m_refine= '  + self.ui.editm_refine.text())
            textlist.append('floor_u= '  + self.ui.editfloor_u.text())
            textlist.append('err_grad_u= '  + self.ui.editerr_grad_u.text())
            textlist.append('jeans_refine= '  + self.ui.editjeans_refine.text())
            textlist.append('floor_p= '  + self.ui.editfloor_p.text())
            textlist.append('err_grad_p= ' + self.ui.editerr_grad_p.text())
            textlist.append('x_refine= '  + self.ui.editx_refine.text())
            textlist.append('r_refine= '  + self.ui.editr_refine.text())
            textlist.append('exp_refine= '  + self.ui.editexp_refine.text())
            textlist.append('y_refine= '  + self.ui.edity_refine.text())
            textlist.append('a_refine_2= '  + self.ui.edita_refine_2.text())
            textlist.append('interpol_var= '  + self.ui.editinterpol_var.text())
            textlist.append('z_refine= '  + self.ui.editz_refine.text())
            textlist.append('b_refine= '  + self.ui.editb_refine.text())
            textlist.append('interpol_type= '  + self.ui.editinterpol_type.text())

            for line in textlist:
                print >>fp,line
            #fp.close()
            self.dialog.accept()
                
        else:
            pass
            
    def resetting(self):
        choice = QtGui.QMessageBox.question(self,'extract!!',"Do you wanna reset?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if (choice == QtGui.QMessageBox.Yes):

             self.ui.editmass_sph.clear()
             self.ui.editfloor_d.clear()
             self.ui.editerr_grad_d.clear()
             self.ui.editm_refine.clear()
             self.ui.editfloor_u.clear()
             self.ui.editerr_grad_u.clear()
             self.ui.editjeans_refine.clear()
             self.ui.editfloor_p.clear()
             self.ui.editerr_grad_p.clear()
             self.ui.editx_refine.clear()
             self.ui.editr_refine.clear()
             self.ui.editexp_refine.clear()
             self.ui.edity_refine.clear()
             self.ui.edita_refine_2.clear()
             self.ui.editinterpol_var.clear()
             self.ui.editz_refine.clear()
             self.ui.editb_refine.clear()
             self.ui.editinterpol_type.clear()
             
    
        else :
            pass



        
class PoissonPopupDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(QtGui.QDialog,self).__init__()
        self.setGeometry(150,150,600,500)

        self.dialog = QtGui.QDialog()
        self.ui = Forms.Poisson_Dialog()
        self.ui.setupUi(self.dialog)
        self.ui.Save.clicked.connect(self.saving)
        self.ui.Reset.clicked.connect(self.resetting)
        self.dialog.show()

    def saving(self):
        choice = QtGui.QMessageBox.question(self,'extract!!',"Do you wanna save?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if (choice == QtGui.QMessageBox.Yes):
            print "Saving POISSON Parameters"
            textlist = []
            textlist.append('&POISSON_PARAMS')
            textlist.append('gravity_type= '  + self.ui.editgravity_type.text())
            textlist.append('cg_levelmin= '  + self.ui.editcg_levelmin.text())
            textlist.append('epsilon= '  + self.ui.editepsilon.text())
            textlist.append('cic_levelmax= '  + self.ui.editcic_levelmax.text())
            textlist.append('gravity_params= '  + self.ui.editgravity_params.text())
            
            for line in textlist:
                print >>fp,line
            #fp.close()
            self.dialog.accept()
                
        else:
            pass
            
    def resetting(self):
        choice = QtGui.QMessageBox.question(self,'extract!!',"Do you wanna reset?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if (choice == QtGui.QMessageBox.Yes):

            self.ui.editgravity_type.clear()
            self.ui.editcg_levelmin.clear()
            self.ui.editepsilon.clear()
            self.ui.editcic_levelmax.clear()
            self.ui.editgravity_params.clear()
            
        else :
            pass

        


class YTpopup(QtGui.QDialog):
    def __init__(self, parent=None):
        super(QtGui.QDialog,self).__init__()
        self.setGeometry(150,150,784,621)

        self.dialog = QtGui.QDialog()
        self.ui = YT_Dialog(self.dialog)
        self.ui.setupUi(self.dialog)

        self.dialog.show()
