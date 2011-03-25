# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtSql, QtCore, QtGui, QtWebKit, uic
      
class MapWidget(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        uic.loadUi("ui/MapWidget.ui", self)
        QtWebKit.QWebSettings.globalSettings().setAttribute(QtWebKit.QWebSettings.JavascriptEnabled, True)
        
        self.connect(self.txtAddress, QtCore.SIGNAL("textChanged(QString)"), self.setBtnAddState)
        self.progressBar.connect(self.webView, QtCore.SIGNAL('loadProgress(int)'), self.progressBar.setValue)
        self.progressBar.connect(self.webView, QtCore.SIGNAL('loadFinished(bool)'), self.progressBar.hide)
        self.progressBar.connect(self.webView, QtCore.SIGNAL('loadStarted()'), self.progressBar.show)
        self.webView.load(QtCore.QUrl('html/reverse_geocoder.html'))
        self.frame = self.webView.page().currentFrame()
        #better way with a signal (emitted with a slot), and embedded qobject?
        #self.frame.addToJavaScriptWindowObject('mapObj', self) #or a custom object
        
        self.timer = QtCore.QTimer()
        self.connect(self.timer,QtCore.SIGNAL("timeout()"), self.fill_location_data)
        self.connect(self.btnAdd, QtCore.SIGNAL("clicked()"), self.addNew)
        self.timer.start()
        
    
    def clearAll(self):
        for lineEdit in self.findChildren(QtGui.QLineEdit):
	  lineEdit.clear()
        
    def setBtnAddState(self, text):
        if text.isEmpty():
	  self.btnAdd.setEnabled(False)
	else:
	  self.btnAdd.setEnabled(True)
	  
    def addNew(self):
        self.query=QtSql.QSqlQuery()
        self.query.exec_('SELECT countryName FROM countriesTable where countryName == '+"'"+self.country+"'")
        ##
        
    def fill_location_data(self):
        self.txtAddress.setText(self.frame.evaluateJavaScript('getMapAddress();').toString())
        if self.txtAddress.text().isEmpty(): return
        address_data = self.txtAddress.text().split(',')
        #get address data
        #http://maps.googleapis.com/maps/api/geocode/output?address=address&sensor=true_or_false
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
	
	self.longitude = self.frame.evaluateJavaScript('getMapLongitude();').toString()
	self.latitude = self.frame.evaluateJavaScript('getMapLatitude();').toString()
	
        self.txtCity.setText(self.city)
        self.txtCountry.setText(self.country)
        self.txtLongitude.setText(self.longitude)
        self.txtLatitude.setText(self.latitude)
    
    
def main():
    app = QtGui.QApplication(sys.argv)
    
    mapWidget = MapWidget()
    mapWidget.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()