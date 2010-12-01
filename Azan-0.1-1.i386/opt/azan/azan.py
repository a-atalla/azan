import sys
from PyQt4 import QtGui, QtCore, uic
from PyQt4.phonon import Phonon

from settings import *
from azkar import *

class Azan(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        uic.loadUi("ui/MainWindow.ui", self)
        
        global settingsDialog
        settingsDialog=SettingsDialog()
        settingsDialog.database()
        settingsDialog.calculate()
        settingsDialog.getcity()
        settingsDialog.settings()
        settingsDialog.cityCoordinates()
            
        global azkar
        azkar = PopupWindow() 

        self.audioOutput = Phonon.AudioOutput(Phonon.MusicCategory, self)
        self.mediaObject = Phonon.MediaObject(self)
        self.metaInformationResolver = Phonon.MediaObject(self)
        Phonon.createPath(self.mediaObject, self.audioOutput)
        
        self.timer = QtCore.QTimer(self)
        self.timer.start(1000)
        
        self.center()
        self.TrayIcon()
        self.displayTime()
        self.refreshWindow()
        self.connections()  
    def refreshWindow(self):
        settingsDialog.calculate()
        self.lblCurrentCity.setText(settingsDialog.city)
        self.lblCurrentCountry.setText(settingsDialog.country)
        self.txtFajr.setText(settingsDialog.FajrTime)
        self.txtShrouk.setText(settingsDialog.ShroukTime)
        self.txtZuhr.setText(settingsDialog.ZuhrTime)
        self.txtAsr.setText(settingsDialog.AsrTime)
        self.txtMaghrib.setText(settingsDialog.MaghribTime)
        self.txtIshaa.setText(settingsDialog.IshaTime)
        
    def displayTime(self):
        '''Display Time in the main window ,and play sound when the time is equal of any pray
        '''
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

    def connections(self):
        self.connect(self.btnSettings, QtCore.SIGNAL('clicked()'), self.showSettings)
        self.connect(self.timer,QtCore.SIGNAL("timeout()"), self.displayTime)
        self.connect(self.btnHide, QtCore.SIGNAL('clicked()'), self.hide)
        self.connect(self.actionShow, QtCore.SIGNAL('triggered()'), self.show)
        self.connect(self.actionClose, QtCore.SIGNAL('triggered()'), self.close)
        self.connect(self.actionStopAzan, QtCore.SIGNAL('triggered()'), self.stopAzan)
        
        self.connect(settingsDialog.btnPlay, QtCore.SIGNAL('clicked()'), self.playAzan)
        self.connect(settingsDialog.btnStop, QtCore.SIGNAL('clicked()'), self.stopAzan)
        self.connect(settingsDialog.btnSaveSettings, QtCore.SIGNAL('clicked()'), self.refreshWindow)
        self.connect(settingsDialog.btnSaveSettings, QtCore.SIGNAL('clicked()'), azkar.resetTiming)
        self.connect(settingsDialog.btnSaveSettings, QtCore.SIGNAL('clicked()'), azkar.location)

        
    def closeEvent(event,self):
        settingsDialog.db.close()
        del  settingsDialog.db #avoiding db reomveDatabase warning
        if settingsDialog.isVisible():
            settingsDialog.close()

