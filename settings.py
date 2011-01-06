# -*- coding: utf-8 -*-
import os
import sys
from prayertime import *
from PyQt4 import QtGui, QtCore, QtSql, uic
from urllib import urlopen
from mapWidget import *

class SettingsDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        uic.loadUi("ui/SettingsDialog.ui", self)
        
        global mapWidget
        mapWidget = MapWidget()
        
        self.cboxStyle.addItems(QtGui.QStyleFactory.keys())
        self.center()
        self.connections()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
    
    def database(self):
        '''Connect to Database and list the countries in the countries list box
        That will fill the Countries list box
        '''
        self.db=QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('database/CountriesDB')
        self.db.open()
        self.query=QtSql.QSqlQuery()
        self.query.exec_('SELECT countryName FROM countriesTable order by countryName asc')
        while self.query.next():
            country = self.query.value(0).toString()   
            self.listCountries.addItem(country)
        

    def  getcity(self):
        '''list the cities in its listbox for the selected country 
        That will fill the cities list box
        '''

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
        '''From the selected city This will get the city data and show them in 
        the settings form 
        '''
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
        '''This method will load the settings from config file
        if the program started for t he first time the config file will not exists
        so it will load the default settings 
        '''
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
            self.hideazkartime='20'
            self.azkarlocation='BottomRight'
            self.selectedStyle = 'BlueSky'
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
            self.selectedStyle =settings.value('style').toString()
            
            self.azkartime=settings.value('AzkarTime').toString()
            self.spinShowZekrTimer.setValue(int(self.azkartime))
            
            self.hideazkartime=settings.value('hideAzkarTime').toString()
            self.spinHideZekrTimer.setValue(int(self.hideazkartime))
            
            self.azkarlocation=settings.value('AzkarLocation').toString()
            
       
        
        
        # The following part of code will make the country and city selected in the list boxes
        for  i  in range (0, self.listCountries.count()):
            if self.listCountries.item(i).text() == self.country:
                self.listCountries.setCurrentRow(i)
        for  i  in range (0, self.listCities.count()):
            if self.listCities.item(i).text() == self.city:
                self.listCities.setCurrentRow(i)
                
        self.spinShowZekrTimer.setValue(int(self.azkartime))
        self.spinHideZekrTimer.setValue(int(self.hideazkartime))
        
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
        ########################
        if self.azkarlocation=='TopLeft':
            self.rbTopLeft.setChecked(1)
        if self.azkarlocation=='TopRight':
            self.rbTopRight.setChecked(1)
        if self.azkarlocation=='BottomLeft':
            self.rbBottomLeft.setChecked(1)
        if self.azkarlocation=='BottomRight':
            self.rbBottomRight.setChecked(1)
        
        
    def saveSettings(self):
        ''' This method will collect the various settings from the settings dialog and
        save them in  config file "Azan" for the next startup
        '''
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
        
        if int(self.spinHideZekrTimer.text() ) >0:
            settings.setValue('hideAzkarTime', self.spinHideZekrTimer.text())
        else:
            settings.setValue('hideAzkarTime', '1')
        #Save Azkar position
        if self.rbTopLeft.isChecked():
            settings.setValue('AzkarLocation', 'TopLeft')
        if self.rbTopRight.isChecked():
             settings.setValue('AzkarLocation', 'TopRight')
        if self.rbBottomLeft.isChecked():
            settings.setValue('AzkarLocation', 'BottomLeft')
        if self.rbBottomRight.isChecked():
             settings.setValue('AzkarLocation', 'BottomRight')
            
        # Save selected style
        settings.setValue('style', self.cboxStyle.currentText())
        
        self.calculate()
        
   
    def  calculate(self):
        year= int(QtCore.QDateTime.currentDateTime().toString("yyyy"))
        month=int(QtCore.QDateTime.currentDateTime().toString("MM"))
        day=int(QtCore.QDateTime.currentDateTime().toString("dd"))
        print "Today is " , day
        self.settings()
        for  i  in range (0, self.listCountries.count()):
            if self.listCountries.item(i).text() == self.country:
                self.listCountries.setCurrentRow(i)
        for  i  in range (0, self.listCities.count()):
            if self.listCities.item(i).text() == self.city:
                self.listCities.setCurrentRow(i)
        pt=Prayertime(self.longitude, self.latitude,self.timeZone, year, month, day ,self.calendar, self.mazhab, self.season)
        pt.calculate()
        self.qibla = pt.get_qibla()
        print 'Qibla Direction is ', self.qibla;
        self.FajrTime=pt.fajr_time()
        self.ShroukTime=pt.shrouk_time()
        self.ZuhrTime=pt.zuhr_time()
        self.AsrTime=pt.asr_time()
        self.MaghribTime=pt.maghrib_time()
        self.IshaTime=pt.isha_time()
        
    def qibla_direction(self):
      return self.qibla
    
    def showMap(self):
        try:
	  urlopen('http://www.google.com')
	except:
	  QtGui.QMessageBox.critical(self, u'خطأ', u'تأكد من الإتصال بالانترنت و حاول مرة أخري')
	else:
	  mapWidget.setWindowFlags(QtCore.Qt.Dialog)
	  mapWidget.webView.reload()
	  mapWidget.clearAll()
	  mapWidget.show()
	  
    def connections(self):
        self.connect(self.listCountries,QtCore.SIGNAL("itemClicked(QListWidgetItem*)"), self.getcity)
        self.connect(self.listCities,QtCore.SIGNAL("itemClicked(QListWidgetItem*)"), self.cityCoordinates)
        self.connect(self.btnSaveSettings, QtCore.SIGNAL('clicked()'), self.saveSettings)
        self.connect(self.listCountries, QtCore.SIGNAL("currentItemChanged(QListWidgetItem*,QListWidgetItem*)"), self.getcity)
        self.connect(self.btnAddNew, QtCore.SIGNAL('clicked()'), self.showMap)

def main():
    settingsDialog=settingsDialog()
    settingsDialog.database()
if __name__ == "__main__":
    main()
