import random
from PyQt4 import QtGui, QtCore, QtSql, uic
from settings import *


class PopupWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        uic.loadUi("ui/PopupWindow.ui", self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.Popup)  
        global settingsDialog
        settingsDialog=SettingsDialog()
        settingsDialog.settings()
        self.location()
        self.startTiming()
        self.connections()
       
    def location(self):
        print 'relocate azkar'
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        settingsDialog.settings()
        if settingsDialog.azkarlocation == 'TopLeft':
            self.move(0, 0)
        if settingsDialog.azkarlocation == 'TopRight':
            self.move((screen.width()-size.width()), 0)
        if settingsDialog.azkarlocation == 'BottomLeft':
            self.move(0,(screen.height()-size.height()))
        if settingsDialog.azkarlocation == 'BottomRight':
            self.move((screen.width()-size.width()), (screen.height()-size.height()))
        
    def showEvent(self, event):
        hideTime =(int(settingsDialog.hideazkartime) * 1000)
        self.timerHideZekr.start(hideTime)
        
    def startTiming(self):
        print 'Timing is started'
        global  timerHideZekr , timerShowZekr
        self.timerHideZekr=QtCore.QTimer(self)
        hideTime =(int(settingsDialog.hideazkartime) * 1000)
        self.timerHideZekr.start(hideTime)
        
        showTime =(int(settingsDialog.azkartime) * 60000)+hideTime
        self.timerShowZekr = QtCore.QTimer(self)
        self.timerShowZekr.stop()
        self.timerShowZekr.start(showTime)
    
    def resetTiming(self):
        print 'reset timer'
        self.timerShowZekr.stop()
        self.timerHideZekr.stop()
        hideTime =(int(settingsDialog.hideazkartime) * 1000)
        self.timerHideZekr.start(hideTime)
        
        showTime =(int(settingsDialog.azkartime) * 60000)+hideTime
        self.timerShowZekr.start(showTime)
        self.timerShowZekr.stop()
        self.timerShowZekr.start(showTime)
        
   
    def showZekr(self):
        i=random.randint(0, 24)
        azkarList=[]
        self.query=QtSql.QSqlQuery()
        self.query.exec_('SELECT zekr FROM azkar')
        while self.query.next():
            zekr = self.query.value(0).toString()   
            azkarList.append(zekr)
        self.txtPopup.setText(azkarList[i])
        self.show()
        
    def connections(self):
        self.connect(self.btnClosePopup, QtCore.SIGNAL('clicked()'), self.hide)
        self.connect(self.timerShowZekr,QtCore.SIGNAL("timeout()"), self.showZekr)
        self.connect(self.timerHideZekr,QtCore.SIGNAL("timeout()"), self.hide)

