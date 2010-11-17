from Ui_PopupWidget import *

class PopupWidget(QtGui.QWidget, Ui_Form):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setpUi(self)
        
    def location(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width()), (screen.height()-size.height()))

azkar=PopupWidget()
azkar.show()
