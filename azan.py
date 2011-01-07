# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore, QtSvg, uic
from PyQt4.phonon import Phonon
import images
from settings import *
from azkar import *
from prayertime import to_hrtime

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
        
        global reportDialog
        reportDialog = ReportDialog()
        
        
        self.changeStyle(settingsDialog.selectedStyle)
        self.audioOutput = Phonon.AudioOutput(Phonon.MusicCategory, self)
        self.mediaObject = Phonon.MediaObject(self)
        self.metaInformationResolver = Phonon.MediaObject(self)
        Phonon.createPath(self.mediaObject, self.audioOutput)
        
        #svg widget to display qibla svg image
        self.svgwidget = QtSvg.QSvgWidget()
        
        #insert svg widget into main vbox before the last widget
        self.horizontalLayout_3.insertWidget(0,self.svgwidget)
        self.svgwidget.setSizePolicy(QtGui.QSizePolicy.Maximum,QtGui.QSizePolicy.Maximum)
        self.svgwidget.setMaximumSize(150,150)
        
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
        global nowTime, nowDate
        nowTime =QtCore.QTime.currentTime().toString("hh:mm:ss A")
        nowDate =QtCore.QDate.currentDate().toString("ddd dd MMM yyyy")
        self.lblCurrentTime.setText(nowTime)
        self.lblCurrentDate.setText(nowDate)

        #Calculate for the new day at 00:00:01
        if str(nowTime) == "12:00:00 AM":
            self.refreshWindow()
        # Show Tray Message befor prayer with 5 min
        if  QtCore.QTime.currentTime().secsTo(QtCore.QTime.fromString(self.txtFajr.text(), "hh:mm:ss A"))  == 300 :
            self.trayicon.showMessage(u"إستعد ", u" بقي علي صلاة الفجر أقل من ", msecs = 300000)
        if  QtCore.QTime.currentTime().secsTo(QtCore.QTime.fromString(self.txtZuhr.text(), "hh:mm:ss A"))  == 300 :
            self.trayicon.showMessage(u"إستعد ", u" بقي علي صلاة الظهر أقل من  5 دقائق", msecs = 300000)
        if  QtCore.QTime.currentTime().secsTo(QtCore.QTime.fromString(self.txtAsr.text(), "hh:mm:ss A"))  == 300 :
            self.trayicon.showMessage(u"إستعد ", u" بقي علي صلاة العصرأقل من  5 دقائق ", msecs = 300000)
        if  QtCore.QTime.currentTime().secsTo(QtCore.QTime.fromString(self.txtMaghrib.text(), "hh:mm:ss A"))  == 300 :
            self.trayicon.showMessage(u"إستعد ", u" بقي علي صلاة المغربأقل من  5 دقائق ", msecs = 300000)
        if  QtCore.QTime.currentTime().secsTo(QtCore.QTime.fromString(self.txtIshaa.text(), "hh:mm:ss A"))  == 300 :
            self.trayicon.showMessage(u"إستعد ", u" بقي علي صلاة العشاءأقل من  5 دقائق  ", msecs = 300000)
            
            
        
        
        # Play Azan and show tray message at prayer  time
        if  str(nowTime) == self.txtFajr.text():
            self.trayicon.showMessage(u"إنتبه", u"حان الآن موعداذان الفجر ", msecs = 200000)
            self.playAzan()
        
        if  str(nowTime) == self.txtZuhr.text():
            self.trayicon.showMessage(u"إنتبه", u"حان الآن موعداذان الظهر ", msecs = 200000)
            self.playAzan()
        
        if  str(nowTime) == self.txtAsr.text():
            self.trayicon.showMessage(u"إنتبه", u"حان الآن موعداذان العصر ", msecs = 200000)
            self.playAzan()
        
        if  str(nowTime) == self.txtMaghrib.text():
            self.trayicon.showMessage(u"إنتبه", u"حان الآن موعداذان المغرب ", msecs = 200000)
            self.playAzan()
        
        if  str(nowTime) == self.txtIshaa.text():
            self.trayicon.showMessage(u"إنتبه", u"حان الآن موعد أذان العشاء", msecs = 200000)
            self.playAzan()
        
        self.nextPrayer()
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
        self.connect(self.btnMonthReport, QtCore.SIGNAL('clicked()'), reportDialog.fillReport)
        self.connect(self.actionShow, QtCore.SIGNAL('triggered()'), self.show)
        self.connect(self.actionClose, QtCore.SIGNAL('triggered()'), self.quit_app)
        self.connect(self.actionStopAzan, QtCore.SIGNAL('triggered()'), self.stopAzan)
        
        self.connect(settingsDialog.btnPlay, QtCore.SIGNAL('clicked()'), self.playAzan)
        self.connect(settingsDialog.btnStop, QtCore.SIGNAL('clicked()'), self.stopAzan)
        self.connect(settingsDialog.btnSaveSettings, QtCore.SIGNAL('clicked()'), self.refreshWindow)
        self.connect(settingsDialog.btnSaveSettings, QtCore.SIGNAL('clicked()'), azkar.resetTiming)
        self.connect(settingsDialog.btnSaveSettings, QtCore.SIGNAL('clicked()'), azkar.location)
        
        self.trayicon.activated.connect(self.onTrayIconActivated)
        settingsDialog.cboxStyle.activated[str].connect(self.changeStyle)

    def blueSkyStyle(self):
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Oxygen"))
        self.setStyleSheet ('''
                                    QPushButton {
                                    color: #333;
                                    border: 2px solid #555;
                                    border-radius: 11px;
                                    padding: 5px;
                                    background: qradialgradient(cx: 0.3, cy: -0.4,
                                    fx: 0.3, fy: -0.4,
                                    radius: 1.35, stop: 0 #fff, stop: 1 #888);
                                    min-width: 80px;
                                    }
                                    QPushButton:hover {
                                    background: qradialgradient(cx: 0.3, cy: -0.4,
                                    fx: 0.3, fy: -0.4,
                                    radius: 1.35, stop: 0 #fff, stop: 1 #bbb);
                                    }
                                    QPushButton:pressed {
                                    background: qradialgradient(cx: 0.4, cy: -0.1,
                                    fx: 0.4, fy: -0.1,
                                    radius: 1.35, stop: 0 #fff, stop: 1 #ddd);
                                    }
                                    #centralwidget{
                                    color: rgb(255, 255, 255);
                                    background-image: url(:/images/images/back.png);
                                    background-image: url(:/images/images/back.png);}
                                    ''')
        settingsDialog.setStyleSheet('''  
                                    QPushButton,QToolButton {
                                    color: #333;
                                    border: 2px solid #555;
                                    border-radius: 11px;
                                    padding: 5px;
                                    background: qradialgradient(cx: 0.3, cy: -0.4,
                                    fx: 0.3, fy: -0.4,
                                    radius: 1.35, stop: 0 #fff, stop: 1 #888);
                                    min-width: 80px;
                                    }
                                    QPushButton:hover {
                                    background: qradialgradient(cx: 0.3, cy: -0.4,
                                    fx: 0.3, fy: -0.4,
                                    radius: 1.35, stop: 0 #fff, stop: 1 #bbb);
                                    }
                                    QPushButton:pressed {
                                    background: qradialgradient(cx: 0.4, cy: -0.1,
                                    fx: 0.4, fy: -0.1,
                                    radius: 1.35, stop: 0 #fff, stop: 1 #ddd);
                                    }
                                    QDialog{
                                    color: rgb(255, 255, 255);
                                    background-image: url(:/images/images/back.png);
                                    background-image: url(:/images/images/back.png);}
                                      ''') 
        azkar.setStyleSheet('''  
                                    QPushButton,QToolButton {
                                    color: #333;
                                    border: 2px solid #555;
                                    border-radius: 11px;
                                    padding: 5px;
                                    background: qradialgradient(cx: 0.3, cy: -0.4,
                                    fx: 0.3, fy: -0.4,
                                    radius: 1.35, stop: 0 #fff, stop: 1 #888);
                                    min-width: 80px;
                                    }
                                    QPushButton:hover {
                                    background: qradialgradient(cx: 0.3, cy: -0.4,
                                    fx: 0.3, fy: -0.4,
                                    radius: 1.35, stop: 0 #fff, stop: 1 #bbb);
                                    }
                                    QPushButton:pressed {
                                    background: qradialgradient(cx: 0.4, cy: -0.1,
                                    fx: 0.4, fy: -0.1,
                                    radius: 1.35, stop: 0 #fff, stop: 1 #ddd);
                                    }
                                    QWidget{
                                    color: rgb(255, 255, 255);
                                    background-image: url(:/images/images/back.png);
                                    background-image: url(:/images/images/back.png);}
                                      ''')                               
    def changeStyle(self, styleName):
        if styleName == "BlueSky":
            self.blueSkyStyle()
        else:
            self.setStyleSheet ('''  ''')
            settingsDialog.setStyleSheet('''  ''') 
            azkar.setStyleSheet(''' ''')
            QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(styleName))


    
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



<circle cx="200" cy="200" r="195" 
   style="stroke: brown; fill: none;stroke-width: 10"/>

<!-- rotated arrow -->
<g id="arrow" style="stroke: black;" transform="rotate(%f, 200, 200)">
    <line x1="200" y1="200" x2="20" y2="200"
      style="stroke-width: 10; stroke: blue;"/>
    <line x1="200" y1="200" x2="380" y2="200"
      style="stroke-width: 10; stroke: blue;"/>
    <polygon points="380  200, 375  195, 375  205"
      style="stroke-width: 18; stroke: blue;"/>
    <!-- center of rotation -->
    <circle cx="200" cy="200" r="15" style="fill: black;"/>
    <!--<text x="130" y="180" style="font-weight:bold;font-size: 20;fill: blue;">Qibla Direction</text>-->
</g>

<text x="165" y="300" style="font-weight:bold;font-size: 30">%s°</text>

<text x="200" y="50" style="font-weight:bold;fill: brown;font-size: 30">N</text>
<text x="200" y="370" style="font-weight:bold;fill: brown;font-size: 30">S</text>
<text x="350" y="200" style="font-weight:bold;fill: brown;font-size: 30">E</text>
<text x="30" y="200" style="font-weight:bold;fill: brown;font-size: 30">W</text>

</svg>''' %(degree,str(int((degree+90)*100)/100.0))
        return xml
     
    def quit_app(self):
      self.ensure_quit = True
      self.close()
    
    def svg_rotation_to_cardinal(self,degree):
      #top: north
      return degree-90
    
    def load_qibla(self):
        direction = settingsDialog.qibla_direction()
        if direction < 0 : direction += 360
        simple_qibla_xml = self.qibla_svg(self.svg_rotation_to_cardinal(direction))
        qibla = QtCore.QByteArray(simple_qibla_xml)
        self.svgwidget.load(qibla)
        
    def secs_to_hrtime(self, secs):
      return to_hrtime(secs/3600)[:-3]
    
    def nextPrayer(self):
        prayerList = [str(self.txtFajr.text()) ,  str(self.txtShrouk.text()) , str(self.txtZuhr.text()), str(self.txtAsr.text()), str(self.txtMaghrib.text()) ,  str(self.txtIshaa.text())]
        for prayer in prayerList:
            prayerIndex = prayerList.index(prayer)
            secsToNextPrayer =float  (QtCore.QTime.currentTime().secsTo(QtCore.QTime.fromString(prayer, "hh:mm:ss A")))
            if secsToNextPrayer > 0 :
                if prayerIndex == 0 :
                    self.lblNextPrayer.setText(u"الفجر")
                    self.lblPrevPrayer.setText(u"العشاء")
                    
                    timeBetweenPrayers =   (QtCore.QTime.fromString(prayerList[0] , "hh:mm:ss A").secsTo(QtCore.QTime.fromString(prayerList[5] , "hh:mm:ss A")))
                    timeBetweenPrayers = (24 * 3600 ) - timeBetweenPrayers
                    self.progressBar.setMaximum (timeBetweenPrayers)
                    self.progressBar.setValue (timeBetweenPrayers -  secsToNextPrayer)
                    self.progressBar.setFormat(u'الوقت حتي صلاة '+ self.lblNextPrayer.text() + ' ' + self.secs_to_hrtime(secsToNextPrayer))
                    
                if prayerIndex == 1 :
                    self.lblNextPrayer.setText(u"الشروق")
                    self.lblPrevPrayer.setText(u"الفجر")
                if prayerIndex == 2 :
                    self.lblNextPrayer.setText(u"الظهر")
                    self.lblPrevPrayer.setText(u"الشروق")
                if prayerIndex == 3 :
                    self.lblNextPrayer.setText(u"العصر")
                    self.lblPrevPrayer.setText(u"الظهر")
                if prayerIndex == 4 :
                    self.lblNextPrayer.setText(u"المغرب")
                    self.lblPrevPrayer.setText(u"العصر")
                if prayerIndex == 5 :
                    self.lblNextPrayer.setText(u"العشاء")
                    self.lblPrevPrayer.setText(u"المغرب")
                
                
                if prayerIndex <> 0:
                    timeBetweenPrayers = float  (QtCore.QTime.fromString(prayerList[prayerIndex-1], "hh:mm:ss A").secsTo(QtCore.QTime.fromString(prayerList[prayerIndex], "hh:mm:ss A")))
                    self.progressBar.setMaximum (timeBetweenPrayers)
                    self.progressBar.setValue (timeBetweenPrayers -  secsToNextPrayer)
                    self.progressBar.setFormat(u'الوقت حتي صلاة '+ self.lblNextPrayer.text() + ' ' + self.secs_to_hrtime(secsToNextPrayer))
		    
                break
            #If after Ishaa all the values will return negativ so we had to calculate next day fajr time
            else :
                if  prayerList.index(prayer) == 5 :
                    self.lblNextPrayer.setText(u"الفجر")
                    self.lblPrevPrayer.setText(u"العشاء")
                    timeBetweenPrayers =   (QtCore.QTime.fromString(prayerList[0] , "hh:mm:ss A").secsTo(QtCore.QTime.fromString(prayerList[5] , "hh:mm:ss A")))
                    timeBetweenPrayers = (24 * 3600 ) - timeBetweenPrayers
                    secsToNextPrayer = timeBetweenPrayers + secsToNextPrayer
            
                    self.progressBar.setMaximum (timeBetweenPrayers)
                    self.progressBar.setValue (timeBetweenPrayers -  secsToNextPrayer)
                    self.progressBar.setFormat(u'الوقت حتي صلاة '+ self.lblNextPrayer.text() + ' ' + self.secs_to_hrtime(secsToNextPrayer))
                    
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
   


class ReportDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        uic.loadUi("ui/ReportDialog.ui", self)
        
    def fillReport(self):
        year= int(QtCore.QDate.currentDate().toString("yyyy"))
        month=int(QtCore.QDate.currentDate().toString("MM"))
        Month = QtCore.QDate.currentDate().toString("MMMM")
        daysofmonth = QtCore.QDate.currentDate().daysInMonth()
        self.labelCity.setText(settingsDialog.city)
        self.labelMonth.setText(Month)
        
        day = 0
        while day < daysofmonth :
            #calculate the prayertimes for the day
            settingsDialog.settings()
            for  i  in range (0, settingsDialog.listCountries.count()):
                if settingsDialog.listCountries.item(i).text() == settingsDialog.country:
                    settingsDialog.listCountries.setCurrentRow(i)
            for  i  in range (0, settingsDialog.listCities.count()):
                if settingsDialog.listCities.item(i).text() == settingsDialog.city:
                    settingsDialog.listCities.setCurrentRow(i)
            pt=Prayertime(settingsDialog.longitude, settingsDialog.latitude,settingsDialog.timeZone, year, month, day+1 ,settingsDialog.calendar, settingsDialog.mazhab, settingsDialog.season)
            pt.calculate()
            self.tableWidget.setRowCount(daysofmonth)
            
            itemFajr = QtGui.QTableWidgetItem(pt.fajr_time())
            itemShrouk = QtGui.QTableWidgetItem(pt.shrouk_time())
            itemZuhr = QtGui.QTableWidgetItem(pt.zuhr_time())
            itemAsr = QtGui.QTableWidgetItem(pt.asr_time())
            itemMaghrib = QtGui.QTableWidgetItem(pt.maghrib_time())
            itemIshaa = QtGui.QTableWidgetItem(pt.isha_time())
            
            self.tableWidget.setItem(day, 0, itemFajr)
            self.tableWidget.setItem(day, 1, itemShrouk)
            self.tableWidget.setItem(day, 2, itemZuhr)
            self.tableWidget.setItem(day, 3, itemAsr)
            self.tableWidget.setItem(day, 4, itemMaghrib) 
            self.tableWidget.setItem(day, 5, itemIshaa)
            
            
            day = day +1
        
        
        self.show()
        
        
        
