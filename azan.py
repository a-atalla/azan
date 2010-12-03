# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore, QtSvg, uic
from PyQt4.phonon import Phonon
import images
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
        
        #svg widget to display qibla svg image
        self.svgwidget = QtSvg.QSvgWidget()
        #insert svg widget into main vbox before the last widget
        self.verticalLayout.insertWidget(4,self.svgwidget)
        
        self.timer = QtCore.QTimer(self)
        self.timer.start(1000)
        
        self.center()
        self.TrayIcon()
        self.displayTime()
        self.refreshWindow()
        self.connections()  
        
    def refreshWindow(self):
        settingsDialog.calculate()
        self.load_qibla()
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
        self.trayicon=QtGui.QSystemTrayIcon(QtGui.QIcon(":/images/images/kaba.png"))
        self.trayicon.setToolTip('Azan Prayer Times')

        self.traymenu=QtGui.QMenu()

        self.traymenu.addAction(self.actionShow)
        self.traymenu.addAction(self.actionStopAzan)
        self.traymenu.addAction(self.actionClose)
        self.trayicon.setContextMenu(self.traymenu)
        self.trayicon.show()
        
    def onTrayIconActivated(self, reason):
        if reason == QtGui.QSystemTrayIcon.DoubleClick:
            if self.isVisible():
                self.hide()
            else:
                self.show()


        
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
        self.connect(self.actionClose, QtCore.SIGNAL('triggered()'), self.quit_app)
        self.connect(self.actionStopAzan, QtCore.SIGNAL('triggered()'), self.stopAzan)
        
        self.connect(settingsDialog.btnPlay, QtCore.SIGNAL('clicked()'), self.playAzan)
        self.connect(settingsDialog.btnStop, QtCore.SIGNAL('clicked()'), self.stopAzan)
        self.connect(settingsDialog.btnSaveSettings, QtCore.SIGNAL('clicked()'), self.refreshWindow)
        self.connect(settingsDialog.btnSaveSettings, QtCore.SIGNAL('clicked()'), azkar.resetTiming)
        self.connect(settingsDialog.btnSaveSettings, QtCore.SIGNAL('clicked()'), azkar.location)
        
        self.trayicon.activated.connect(self.onTrayIconActivated)
    
    def qibla_svg(self,degree):
        xml='''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:xlink="http://www.w3.org/1999/xlink"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   width="400"
   height="400"
   id="svg2"
   version="1.1"
   inkscape:version="0.48.0 r9654"
   sodipodi:docname="e-kiblah.svg"
   inkscape:export-filename="/home/romanov/cadr.png"
   inkscape:export-xdpi="90"
   inkscape:export-ydpi="90">
<!-- center of rotation -->
<circle cx="200" cy="200" r="15" style="fill: black;"/>

<circle cx="200" cy="200" r="195" 
   style="stroke: brown; fill: none;stroke-width: 10"/>

<!-- non-rotated arrow -->
<g id="arrow" style="stroke: black;" transform="rotate(%f, 200, 200)">
    <line x1="200" y1="200" x2="380" y2="200"
      style="stroke-width: 10; stroke: blue;"/>
    <polygon points="380  200, 375  195, 375  205"
      style="stroke-width: 18; stroke: blue;"/>
    <text x="270" y="180" style="font-weight:bold;font-size: 20">%s °</text>
</g>



</svg>''' %(degree,str(int(degree)))
        return xml
     
    def quit_app(self):
      self.ensure_quit = True
      self.close()
      
    def load_qibla(self):
        direction = settingsDialog.qibla_direction()
        simple_qibla_xml = self.qibla_svg(0)#direction)
        qibla = QtCore.QByteArray(simple_qibla_xml)
        self.svgwidget.load(qibla)
        
    def closeEvent(self,event):
        try:
          if self.ensure_quit:
	    settingsDialog.db.close()
            del  settingsDialog.db #avoiding db reomveDatabase warning
            if settingsDialog.isVisible():
                settingsDialog.close()
        except:
            #ensure_quit isn't defined so just hide
	    self.hide()
            event.ignore()
   