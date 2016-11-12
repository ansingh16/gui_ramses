import sys
from PyQt4 import QtGui,QtCore

class Window(QtGui.QMainWindow):
    
    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("Mygui")

        extractAction = QtGui.QAction("&Get Out you are silly !!!!",self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip("Leave the app")
        extractAction.triggered.connect(self.close_application)

        self.statusBar()
        
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&FILE')
        fileMenu.addAction(extractAction)


        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit",self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0,100)


        extractAction = QtGui.QAction( QtGui.QIcon('todachoppa.png'),'Flee the scene',self)
        extractAction.triggered.connect(self.close_application)
        

        self.toolBar = self.addToolBar("Extraction")

        self.toolBar.addAction(extractAction)
        
        checkBox = QtGui.QCheckBox('Enlarge window',self)
        checkBox.move(100,25)
        checkBox.stateChanged.connect(self.enlarge_window)

      
        
        self.show()

    def enlarge_window(self,state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50,50,1000,500)
        else:
            self.setGeometry(50,50,500,399)

        


    def close_application(self):
        
        choice = QtGui.QMessageBox.question(self,'extract!!',"do you wanna exit?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

        if (choice == QtGui.QMessageBox.Yes):
            print "Exiting nowwwwwwww!!!!!!"
            sys.exit()
        else:
            pass
        
        

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()
