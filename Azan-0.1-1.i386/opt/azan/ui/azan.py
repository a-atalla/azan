import sys
from PyQt4 import QtGui, QtCore, uic
from PyQt4.phonon import Phonon
from settings import *

class Azan(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        uic.loadUi("ui/MainWindow.ui", self)
        global     settingsDialog
        settingsDialog=SettingsDialog()
        self.audioOutput = Phonon.AudioOutput(Phonon.MusicCategory, self)
        self.mediaObject = Phonon.MediaObject(self)
        self.metaInformationResolver = Phonon.MediaObject(self)
        Phonon.createPath(self.mediaObject, self.audioOutput)
        
        self.timer = QtCore.QTimer(self)
        self.timer.start(1000)
        self.center()
        self.TrayIcon()
        self.displayTime()
        self.connections()  
        
    def displayTime(self):
        nowTime =QtCore.QDateTime.currentDateTime().toString("h:m:s A")
        nowDate =QtCore.QDateTime.currentDateTime().toString("ddd dd MMM yyyy")
        self.lblCurrentTime.setText(nowTime)
        self.lblCurrentDate.setText(nowDate)
        if  str(nowTime) == self.txtFajr.text():
            print "it is Fajr time"
            self.playAzan()
        if  str(nowTime) == self.txtZuhr.text():
            print "it is Zuhr time"
            self.playAzan()
        if  str(nowTime) == self.txtAsr.text():
            print "it is Asr time"
            self.playAzan()
        if  str(nowTime) == self.txtMaghrib.text():
            print "it is Maghrib time"
            self.playAzan()
        if  str(nowTime) == self.txtIshaa.text():
            print "it is Ishaa time"
            self.playAzan()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

    def TrayIcon(self):
        self.trayicon=QtGui.QSystemTrayIcon(QtGui.QIcon('icons/kaba.png'))
        self.trayicon.setToolTip('Azan Prayer Times')
        self.traymenu=QtGui.QMenu()
        self.traymenu.addAction(self.actionShow)
        self.traymenu.addAction(self.actionStopAzan)
        self.traymenu.addAction(self.actionClose)
        self.trayicon.setContextMenu(self.traymenu)
        self.trayicon.show()
        
    def playAzan(self):
        settings = QtCore.QSettings('Azan')
        if  not os.path.isfile(settings.fileName()):
            azanSound = 'sounds/makka.ogg'
        else:
            azanSound= settings.value('Azan').toString()
        snd = Phonon.MediaSource(azanSound)
        self.mediaObject.clearQueue()
        self.mediaObject.setCurrentSource(snd)
        self.mediaObject.play()
        
    def stopAzan(self):
        self.mediaObject.stop()
        
    def showSettings(self):
        settingsDialog.show()
#        settingsDialog.cityCoordinates()

    def connections(self):
        self.connect(self.btnSettings, QtCore.SIGNAL('clicked()'), self.showSettings)
        self.connect(self.timer,QtCore.SIGNAL("timeout()"), self.displayTime)
        self.connect(self.btnHide, QtCore.SIGNAL('clicked()'), self.hide)
        self.connect(self.actionShow, QtCore.SIGNAL('triggered()'), self.show)
        self.connect(self.actionClose, QtCore.SIGNAL('triggered()'), self.close)
        self.connect(self.actionStopAzan, QtCore.SIGNAL('triggered()'), self.stopAzan)
        
        
        
    def closeEvent(event,self):
        settingsDialog.db.close()
        del  settingsDialog.db #avoiding db reomveDatabase warning
        if settingsDialog.isVisible():
            settingsDialog.close()
#        if  azkar.isVisible():
#            azkar.close()
