#!/usr/bin/env python
from azan import *
from azkar import *

def main():
    global azan
    app=QtGui.QApplication(sys.argv)
    QtCore.QCoreApplication.setApplicationName('Azan')
    
    azan=Azan()
    azan.show()
    
    
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
