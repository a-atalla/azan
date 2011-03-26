# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtSql, QtCore, QtGui, QtWebKit, uic
from urllib2 import urlopen
from xml.dom import minidom
from math import fabs

class MapWidget(QtGui.QWidget):

    def __init__(self,  parent = None):
        QtGui.QWidget.__init__(self,  parent)
        uic.loadUi("ui/MapWidget.ui", self)
        #self.setWindowModality(QtCore.Qt.WindowModal)
        QtWebKit.QWebSettings.globalSettings().setAttribute(QtWebKit.QWebSettings.JavascriptEnabled, True)
        
        self.connect(self.txtAddress, QtCore.SIGNAL("textChanged(QString)"), self.setBtnAddState)
        self.progressBar.connect(self.webView, QtCore.SIGNAL('loadProgress(int)'), self.progressBar.setValue)
        self.progressBar.connect(self.webView, QtCore.SIGNAL('loadFinished(bool)'), self.progressBar.hide)
        self.progressBar.connect(self.webView, QtCore.SIGNAL('loadStarted()'), self.progressBar.show)
        self.webView.load(QtCore.QUrl('html/reverse_geocoder.html'))
        self.frame = self.webView.page().mainFrame()
        self.connect(self.btnAdd, QtCore.SIGNAL('clicked()'), self.addNew)
        self.connect(self.frame, QtCore.SIGNAL('javaScriptWindowObjectCleared()'), self.attachWidget)
        
    def attachWidget(self):
        self.frame.addToJavaScriptWindowObject('mapWidget', self)
        
    def clearAll(self):
        self.webView.reload()
        for lineEdit in self.findChildren(QtGui.QLineEdit):
            lineEdit.clear()
        for spinBox in self.findChildren(QtGui.QSpinBox):
            lineEdit.clear()
        
    def setBtnAddState(self, text):
        if text.isEmpty():
            self.btnAdd.setEnabled(False)
        else:
            self.btnAdd.setEnabled(True)
            
    def addNew(self):
        self.countryNO = 0
        self.query=QtSql.QSqlQuery()
        self.query.exec_('SELECT countryNO FROM countriesTable where countryName = '+"'"+self.country+"'")
        while self.query.next(): self.countryNO = self.query.value(0).toInt()[0]
        
        if self.countryNO == 0:
            #TODO: reconstruct db with an auto increment data type
            #Or use ORM ie..elixir
            self.query.exec_("SELECT max(countryNO) FROM countriesTable")
            while self.query.next(): self.countryNO = self.query.value(0).toInt()[0] + 1
            self.query.exec_("INSERT into countriesTable values(%i, '%s')") % (self.countryNO,  self.country)
        else:
            self.query.exec_("SELECT cityNO FROM citiesTable where cityName = '" + self.city + "'")
            while self.query.next():
                QtGui.QMessageBox.critical(self,  u'خطأ',  u'المدينة موجودة بقاعدة البيانات')
                return
                
        self.query.exec_("SELECT max(cityNO) FROM citiesTable")
        while self.query.next(): 
            self.cityNO = self.query.value(0).toInt()[0] + 1
            #for o in (self.cityNO,  self.countryNO,  self.city,  self.state,  self.latitude*1000,  self.longitude*1000,  self.gmt*100,  self.daylight):
            #   print type(o)
            self.query.prepare("INSERT into citiesTable  values(?, ?, ?, ?, ?, ?, ?, ?)")
            self.query.addBindValue(self.cityNO)
            self.query.addBindValue(self.countryNO)
            self.query.addBindValue(self.city)
            self.query.addBindValue(self.state)
            self.query.addBindValue(self.latitude*10000)
            self.query.addBindValue(self.longitude*10000)
            self.query.addBindValue(self.gmt*100)
            self.query.addBindValue(self.daylight)
            self.query.exec_()

        QtGui.QMessageBox.information(self,  u'إضافة',  u'تم إضافة المدينة بنجاح')

    #implemented in java script => html/map_locator.js : getTimezone()
    def getTimezone(self,lat, lon):
        url = "http://ws.geonames.org/timezone?lat=%s&lng=%s"  %(str(lat), str(lon))
        xml = urlopen(url).read()
        
        timezone = minidom.parseString(xml).firstChild.getElementsByTagName("timezone")[0]
        self.gmt = float(timezone.getElementsByTagName("gmtOffset")[0].firstChild.data)
        
        dst = timezone.getElementsByTagName("dstOffset")[0].firstChild.data
        raw = timezone.getElementsByTagName("rawOffset")[0].firstChild.data
        
        self.daylight = fabs(float(dst) - float(self.gmt))
    
    @QtCore.pyqtSlot()
    def fill_location_data(self):
        self.txtAddress.setText(self.frame.evaluateJavaScript('getMapAddress();').toString())
        if self.txtAddress.text().isEmpty(): return
        address_data = self.txtAddress.text().split(',')
        #FIXME get time zone, daylight and address components right way
        if len(address_data) == 1:
            self.country = address_data[0]
            self.city = ''
            self.btnAdd.setEnabled(False)
        elif len(address_data) == 2:
            self.state, self.country = address_data
            self.city = self.state
        elif len(address_data) > 2:
            self.city = address_data[0]
            self.state, self.country = address_data[-2:]
            self.city += ' -- State: (%s)' % str(self.state).strip()
            
        self.country = str(self.country).lstrip()
        self.longitude = self.frame.evaluateJavaScript('getMapLongitude();').toFloat()[0]
        self.latitude = self.frame.evaluateJavaScript('getMapLatitude();').toFloat()[0]
                
        self.txtCity.setText(self.city)
        self.txtCountry.setText(self.country)
        self.txtLongitude.setText(str(self.longitude))
        self.txtLatitude.setText(str(self.latitude))
        
        self.getTimezone(self.latitude,  self.longitude)
        #self.gmt = self.frame.evaluateJavaScript('getGmt();').toFloat()
        #self.daylight = self.frame.evaluateJavaScript('getDaylight();').toFloat()
        self.spinTimezone.setValue(self.gmt)
        self.spinDaylight.setValue(self.daylight)

       
      
    
    
def main():
    app = QtGui.QApplication(sys.argv)
    
    mapWidget = MapWidget()
    mapWidget.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
