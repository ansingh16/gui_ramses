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

        openeditor = QtGui.QAction("&Editor",self)
        openeditor.setShortcut("Ctrl+E")
        openeditor.setStatusTip("Open the editor")
        openeditor.triggered.connect(self.editor)



        openfile = QtGui.QAction("&Open File",self)
        openfile.setShortcut("Ctrl+O")
        openfile.setStatusTip("Open File")
        openfile.triggered.connect(self.open_file)
        

        
        savefile = QtGui.QAction("&Save File",self)
        savefile.setShortcut("Ctrl+S")
        savefile.setStatusTip("Save File")
        savefile.triggered.connect(self.save_file)
        


        self.statusBar()
        
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&FILE')
        fileMenu.addAction(extractAction)
        fileMenu.addAction(openfile)
        fileMenu.addAction(savefile)


        editorMenu = mainMenu.addMenu('&Editor')
        editorMenu.addAction(openeditor)

        

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
        

        fontChoice = QtGui.QAction('Font',self)
        fontChoice.triggered.connect(self.font_choice)
        self.toolBar = self.addToolBar("Fonts")
        self.toolBar.addAction(fontChoice)
        
        
        color = QtGui.QColor(0,0,0)
        fontcolor = QtGui.QAction('Font bg color',self)
        fontcolor.triggered.connect(self.color_picker)

        self.toolBar.addAction(fontcolor)
        


        checkBox = QtGui.QCheckBox('Enlarge window',self)
        checkBox.move(300,25)
        checkBox.stateChanged.connect(self.enlarge_window)

        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(200,80,250,20)
        
        self.btn = QtGui.QPushButton("Downlod",self)
        self.btn.move(200,120)
        self.btn.clicked.connect(self.download)
        
        print(self.style().objectName())
        self.styleChoice = QtGui.QLabel("gtk+",self)
        
        combobox=QtGui.QComboBox(self)
        combobox.addItem("gtk+")
        combobox.addItem("motif")
        combobox.addItem("cde")
        combobox.addItem("Plastique")

        combobox.move(50,250)
        self.styleChoice.move(50,150)

        combobox.activated[str].connect(self.style_choice)
        

        cal = QtGui.QCalendarWidget(self)
        cal.move(500,200)
        cal.resize(200,200)



        self.show()


    def open_file(self):
        name = QtGui.QFileDialog.getOpenFileName(self,'Open File')
        file = open(name,'r')

        self.editor()

        with file:
            text= file.read()
            self.textEdit.setText(text)
        
    def save_file(self):
        name = QtGui.QFileDialog.getSaveFileName(self,'Save File')
        file = open(name,'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()
        


    def color_picker(self):
        color = QtGui.QColorDialog.getColor()
        self.styleChoice.setStyleSheet("QWidget {background-color = %s }"% color.name())

    def editor(self):
        self.textEdit = QtGui.QTextEdit()

        print "M here"
        self.setCentralWidget(self.textEdit)


    def font_choice(self):
        font, valid = QtGui.QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)


    def style_choice(self,text):
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))



    def download(self):
        self.completed = 0

        while self.completed < 100 :
            self.completed += 0.0001
            self.progress.setValue(self.completed)
            

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
