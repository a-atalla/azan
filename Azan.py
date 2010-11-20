#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import random
from PyQt4 import QtGui, QtCore, QtSql
from PyQt4.phonon import Phonon
from prayertime import *
from Ui_MainWindow import  *
from Ui_SettingsDialog import *
from Ui_PopupWindow import *

class Azan(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.audioOutput = Phonon.AudioOutput(Phonon.MusicCategory, self)
        self.mediaObject = Phonon.MediaObject(self)
        self.metaInformationResolver = Phonon.MediaObject(self)
        Phonon.createPath(self.mediaObject, self.audioOutput)
        self.timer = QtCore.QTimer(self)
        self.timer.start(1000)
        self.center()
        self.TrayIcon()
        self.showTime()
        self.connections()  
        
    def showTime(self):
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
        settingsDialog.cityCoordinates()

    def connections(self):
        self.connect(self.btnSettings, QtCore.SIGNAL('clicked()'), self.showSettings)
        self.connect(self.timer,QtCore.SIGNAL("timeout()"), self.showTime)
        self.connect(self.btnHide, QtCore.SIGNAL('clicked()'), self.hide)
        self.connect(self.actionShow, QtCore.SIGNAL('triggered()'), self.show)
        self.connect(self.actionClose, QtCore.SIGNAL('triggered()'), self.close)
        self.connect(self.actionStopAzan, QtCore.SIGNAL('triggered()'), self.stopAzan)
        
    def closeEvent(event,self):
        settingsDialog.db.close()
        del  settingsDialog.db #avoiding db reomveDatabase warning
        if settingsDialog.isVisible():
            settingsDialog.close()
        if  azkar.isVisible():
            azkar.close()

class SettingsDialog(QtGui.QDialog, Ui_SettingsDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.center()
        self.database()
        self.connections()
        self.settings()
        # ####################################
        
    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
    
    def database(self):
        self.db=QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('database/CountriesDB')
        self.db.open()
        self.query=QtSql.QSqlQuery()
        self.query.exec_('SELECT countryName FROM countriesTable')
        while self.query.next():
            country = self.query.value(0).toString()   
            self.listCountries.addItem(country)

    def  getcity(self):
        self.listCities.clear()
        CurrentCountry=str((self.listCountries.currentItem()).text())
        self.query.exec_('SELECT * FROM countriesTable WHERE countryName =' +"'"+CurrentCountry+"'")
        while self.query.next():
            countryNo = self.query.value(0).toString() 
        self.query.exec_('SELECT cityName FROM citiesTable WHERE countryNO='+countryNo)
        while self.query.next():
            city= self.query.value(0).toString()   
            self.listCities.addItem(city)
    def  cityCoordinates(self):
        self.city = str(self.listCities.currentItem().text())
        self.query.exec_('SELECT longitude  FROM citiesTable WHERE cityName =' +"'"+self.city+"'")
        while self.query.next():
            self.longitude = str(float((self.query.value(0).toString()))/10000)
            self.txtLongitude.setText(self.longitude)            
        self.query.exec_('SELECT latitude  FROM citiesTable WHERE cityName =' +"'"+self.city+"'")
        while self.query.next():
            self.latitude = str(float((self.query.value(0).toString()))/10000)
            self.txtLatitude.setText(self.latitude) 
        self.query.exec_('SELECT timeZone  FROM citiesTable WHERE cityName =' +"'"+self.city+"'")
        while self.query.next():
            self.timeZone =str(int((self.query.value(0)).toString())/100)
            self.txtTimeZone.setText(self.timeZone) 
     
    def settings(self):
        user=os.getenv('USER')
        settings = QtCore.QSettings('Azan')
        if  not os.path.isfile(settings.fileName()):
            #Default settings when the config file doesnot exist
            self.country ='Saudi Arabia'
            self.city = 'Makkah'
            self.longitude=39.8409
            self.latitude=21.4309
            self.timeZone=3
            self.maz='Default'
            self.seas='Winter'
            self.cal='UmmAlQuraUniv'
            self.azan='sounds/makka.ogg'
            self.azkartime='1'
        else:
            #Get the setting from the config file
            self.country =settings.value('country').toString()
            self.city = settings.value('city').toString()
            self.latitude=float (settings.value('latitude').toString())
            self.longitude=float (settings.value('longitude').toString())
            self.timeZone=int(settings.value('timezone').toString())
            self.cal=settings.value('calendar').toString()
            self.maz=settings.value('mazhab').toString()
            self.seas=settings.value('season').toString()
            self.azan=settings.value('Azan').toString()
        azan.lblCurrentCity.setText(self.city)
        azan.lblCurrentCountry.setText(self.country)
        if  self.cal == 'UmmAlQuraUniv':
            self.calendar=Calendar.UmmAlQuraUniv
            self.cboxCalendar.setCurrentIndex(0)
        if self.cal == 'EgyptianGeneralAuthorityOfSurvey':
            self.calendar=Calendar.EgyptianGeneralAuthorityOfSurvey
            self.cboxCalendar.setCurrentIndex(1)
        if self.cal == 'UnivOfIslamicSciencesKarachi':
            self.calendar=Calendar.UnivOfIslamicSciencesKarachi
            self.cboxCalendar.setCurrentIndex(2)
        if self.cal == 'IslamicSocietyOfNorthAmerica':
            self.calendar=Calendar.IslamicSocietyOfNorthAmerica
            self.cboxCalendar.setCurrentIndex(3)
        if self.cal == 'MuslimWorldLeague':
            self.calendar=Calendar.MuslimWorldLeague
            self.cboxCalendar.setCurrentIndex(4)
        ###########################
        if  self.azan == 'sounds/qatami.ogg':
            self.cboxAzanSound.setCurrentIndex(0)
        if  self.azan == 'sounds/makka.ogg':
            self.cboxAzanSound.setCurrentIndex(1)
        if  self.azan == 'sounds/madina.ogg':
            self.cboxAzanSound.setCurrentIndex(2)
        if  self.azan == 'sounds/egypt.ogg':
            self.cboxAzanSound.setCurrentIndex(3)
       ######################
        if self.maz=='Default':
            self.mazhab=Mazhab.Default
            self.cboxMazhab.setCurrentIndex(0)
        if self.maz=='Hanafi':
            self.mazhab=Mazhab.Hanafi
            self.cboxMazhab.setCurrentIndex(1)
        ########################
        if self.seas == 'Summer':
            self.season=Season.Summer
            self.rbSummer.setChecked(1)
        if self.seas == 'Winter':
            self.season = 'Winter'
            self.rbWinter.setChecked(1)
        self.azkartime=settings.value('AzkarTime').toString()
        self.spinShowZekrTimer.setValue(int(self.azkartime))
        
        
    def saveSettings(self):
        settings = QtCore.QSettings('Azan')
        # Save the city   and country
        settings.setValue('country', self.listCountries.currentItem().text())
        settings.setValue('city', self.listCities.currentItem().text())
        settings.setValue('longitude', self.txtLongitude.text())
        settings.setValue('latitude', self.txtLatitude.text())
        settings.setValue('timezone', self.txtTimeZone.text())
        if  self.rbWinter.isChecked():
            settings.setValue('season', 'Winter')
        if self.rbSummer.isChecked():
            settings.setValue('season', 'Summer')
        # Save the Mazhab
        if self.cboxMazhab.currentIndex() == 0:
            settings.setValue('mazhab', 'Default')
        else:
            settings.setValue('mazhab','Hanafi')
        # Save the calender
        if self.cboxCalendar.currentIndex() == 0:
            settings.setValue('calendar', 'UmmAlQuraUniv')
        if self.cboxCalendar.currentIndex() == 1:
            settings.setValue('calendar', 'EgyptianGeneralAuthorityOfSurvey')
        if self.cboxCalendar.currentIndex() == 2:
            settings.setValue('calendar', 'UnivOfIslamicSciencesKarachi')
        if self.cboxCalendar.currentIndex() == 3:
            settings.setValue('calendar', 'IslamicSocietyOfNorthAmerica')
        if self.cboxCalendar.currentIndex() == 4:
            settings.setValue('calendar', 'MuslimWorldLeague')
        #Save the Azan sound
        if self.cboxAzanSound.currentIndex()==0:
            settings.setValue('Azan', 'sounds/qatami.ogg')
        if self.cboxAzanSound.currentIndex()==1:
            settings.setValue('Azan', 'sounds/makka.ogg')
        if self.cboxAzanSound.currentIndex()==2:
            settings.setValue('Azan', 'sounds/madina.ogg')
        if self.cboxAzanSound.currentIndex()==3:
            settings.setValue('Azan', 'sounds/egypt.ogg')       
        # Save the Azkar timing
        if int(self.spinShowZekrTimer.text() ) >0:
            settings.setValue('AzkarTime', self.spinShowZekrTimer.text())
        else:
            settings.setValue('AzkarTime', '1')
        self.calculate()
        
    def  calculate(self):
        year= int(QtCore.QDateTime.currentDateTime().toString("yyyy"))
        month=int(QtCore.QDateTime.currentDateTime().toString("MM"))
        day=int(QtCore.QDateTime.currentDateTime().toString("dd"))
        self.settings()
        azan.lblCurrentCity.setText(self.city)
        azan.lblCurrentCountry.setText(self.country)
        for  i  in range (0, self.listCountries.count()):
            if self.listCountries.item(i).text() == self.country:
                self.listCountries.setCurrentRow(i)
        for  i  in range (0, self.listCities.count()):
            if self.listCities.item(i).text() == self.city:
                self.listCities.setCurrentRow(i)         
        pt=Prayertime(self.longitude, self.latitude,self.timeZone, year, month, day ,self.calendar, self.mazhab, self.season)
        pt.calculate()
        print 'Qibla Direction is ', pt.get_qibla();
        azan.txtFajr.setText(pt.fajr_time())
        azan.txtShrouk.setText(pt.shrouk_time())
        azan.txtZuhr.setText(pt.zuhr_time())
        azan.txtAsr.setText(pt.asr_time())
        azan.txtMaghrib.setText(pt.maghrib_time())
        azan.txtIshaa.setText(pt.isha_time())

    def connections(self):
        self.connect(self.listCountries,QtCore.SIGNAL("itemClicked(QListWidgetItem*)"), self.getcity)
        self.connect(self.listCities,QtCore.SIGNAL("itemClicked(QListWidgetItem*)"), self.cityCoordinates)
        self.connect(self.btnSaveSettings, QtCore.SIGNAL('clicked()'), self.saveSettings)
        self.connect(self.listCountries, QtCore.SIGNAL("currentItemChanged(QListWidgetItem*,QListWidgetItem*)"), self.getcity)
        self.connect(self.btnPlay, QtCore.SIGNAL('clicked()'), azan.playAzan)
        self.connect(self.btnStop, QtCore.SIGNAL('clicked()'), azan.stopAzan)

class PopupWindow(QtGui.QWidget, Ui_Form):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Tool)  
        self.location()
        self.hideZekr()
        time =(int(settingsDialog.azkartime) * 6000)
        self.timerShowZekr = QtCore.QTimer(self)
        self.timerShowZekr.start(time)
    
        self.connections()
       
    def location(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width()), (screen.height()-size.height()))
        
    def showEvent(self, event):
        self.hideZekr()
        
        
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
            
            
    def hideZekr(self):
        self.timerHideZekr=QtCore.QTimer(self)
        self.timerHideZekr.start(2000)
        
    def connections(self):
        self.connect(self.btnClosePopup, QtCore.SIGNAL('clicked()'), self.hide)
        self.connect(self.timerShowZekr,QtCore.SIGNAL("timeout()"), self.showZekr)
        self.connect(self.timerHideZekr,QtCore.SIGNAL("timeout()"), self.hide)

def main():
    global azan, settingsDialog, azkar
    app=QtGui.QApplication(sys.argv)
    QtCore.QCoreApplication.setApplicationName('Azan')
    azan=Azan()
    azan.show()
    
    settingsDialog=SettingsDialog()
    settingsDialog.calculate()

    azkar=PopupWindow()

    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
