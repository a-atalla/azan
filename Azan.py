#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
from PyQt4 import QtGui, QtCore, QtSql
from PyQt4.phonon import Phonon
from prayertime import *
from Ui_MainWindow import  *
from Ui_SettingsDialog import *

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
        self.trayicon=QtGui.QSystemTrayIcon(QtGui.QIcon('icons/seccade.png'))
        self.trayicon.setToolTip('Azan Prayer Times')
        self.trayicon.show()
        #self.trayicon.setContextMenu(self.menuFile)
    def playAzan(self):
        user=os.getenv('USER')
        if  not os.path.isfile ("/home/"+user+"/.config/Azan.conf"):
            print 'play default azan'
            azanSound = '.Azan/sounds/qatami.ogg'
        else:
            print 'play custom azan'
            set = QtCore.QSettings('Azan')
            azanSound= set.value('Azan').toString()
        snd = Phonon.MediaSource(azanSound)
        self.mediaObject.clearQueue()
        self.mediaObject.setCurrentSource(snd)
        self.mediaObject.play()
    def stopAzan(self):
        self.mediaObject.stop()
    def showSettings(self):
        settings.show()
        settings.cityCoordinates()

    def connections(self):
        self.connect(self.btnSettings, QtCore.SIGNAL('clicked()'), self.showSettings)
        self.connect(self.timer,QtCore.SIGNAL("timeout()"), self.showTime)
        self.connect(self.btnHide, QtCore.SIGNAL('clicked()'), self.hide)

class Settings(QtGui.QDialog, Ui_SettingsDialog):
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
        if  not os.path.isfile ("/home/"+user+"/.config/Azan.conf"):
            #Default settings when the config file doesnot exist
            self.country ='Saudi Arabia'
            self.city = 'Makkah'
            self.longitude=39.8409
            self.latitude=21.4309
            self.timeZone=3
            self.maz='Default'
            self.seas='Winter'
            self.cal='UmmAlQuraUniv'
        else:
            set = QtCore.QSettings('Azan')
            #Get the setting from the config file
            self.country =set.value('country').toString()
            self.city = set.value('city').toString()
            self.latitude=float (set.value('latitude').toString())
            self.longitude=float (set.value('longitude').toString())
            self.timeZone=int(set.value('timezone').toString())
            self.cal=set.value('calendar').toString()
            self.maz=set.value('mazhab').toString()
            self.seas=set.value('season').toString()
        azan.lblCurrentCity.setText(self.city)
        azan.lblCurrentCountry.setText(self.country)
        if  self.cal == 'UmmAlQuraUniv':
            self.calendar=Calendar.UmmAlQuraUniv
        if self.cal == 'EgyptianGeneralAuthorityOfSurvey':
            self.calendar=Calendar.EgyptianGeneralAuthorityOfSurvey
        if self.cal == 'UnivOfIslamicSciencesKarachi':
            self.calendar=Calendar.UnivOfIslamicSciencesKarachi
        if self.cal == 'IslamicSocietyOfNorthAmerica':
            self.calendar=Calendar.IslamicSocietyOfNorthAmerica
        if self.cal == 'MuslimWorldLeague':
            self.Calendar=Calendar.MuslimWorldLeague
        ######################
        if self.maz=='Default':
            self.mazhab=Mazhab.Default
        if self.maz=='Hanfi':
            self.mazhab=Mazhab.Hanafi
        ########################
        if self.seas == 'Summer':
            self.season=Season.Summer
        if self.seas == 'Winter':
            self.season = 'Winter'
        
     def saveSettings(self):
        set = QtCore.QSettings('Azan')
        # Save the city   and country
        set.setValue('country', self.listCountries.currentItem().text())
        set.setValue('city', self.listCities.currentItem().text())
        set.setValue('longitude', self.txtLongitude.text())
        set.setValue('latitude', self.txtLatitude.text())
        set.setValue('timezone', self.txtTimeZone.text())
        if  self.rbWinter.isChecked():
            set.setValue('season', 'Winter')
        if self.rbSummer.isChecked():
            set.setValue('season', 'Summer')
        # Save the Mazhab
        if self.cboxMazhab.currentIndex() == 0:
            set.setValue('mazhab', 'Default')
        else:
            set.setValue('mazhab','Hanafi')
        # Save the calender
        if self.cboxCalendar.currentIndex() == 0:
            set.setValue('calendar', 'UmmAlQuraUniv')
        if self.cboxCalendar.currentIndex() == 1:
            set.setValue('calendar', 'EgyptianGeneralAuthorityOfSurvey')
        if self.cboxCalendar.currentIndex() == 2:
            set.setValue('calendar', 'UnivOfIslamicSciencesKarachi')
        if self.cboxCalendar.currentIndex() == 3:
            set.setValue('calendar', 'IslamicSocietyOfNorthAmerica')
        if self.cboxCalendar.currentIndex() == 4:
            set.setValue('calendar', 'MuslimWorldLeague')
       #Save the Azan sound
        if self.cboxAzanSound.currentIndex()==0:
            set.setValue('Azan', '.Azan/sounds/qatami.ogg')

       
        self.calculate()
        self.close()
        
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

def main():
    global azan, settings
    app=QtGui.QApplication(sys.argv)
    azan=Azan()
    settings=Settings()
    settings.calculate()
    azan.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
