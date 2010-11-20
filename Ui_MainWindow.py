# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ahmed/Eric/azan/MainWindow.ui'
#
# Created: Sat Nov 20 01:53:58 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(417, 379)
        font = QtGui.QFont()
        font.setFamily("KacstQurn")
        font.setPointSize(11)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/kaba.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(".QWidget ,QDialog,QGroupBox {\n"
"   background-color: beige;\n"
"   font-family: KacstQurn ;\n"
"}\n"
"\n"
"/* Nice Windows-XP-style password character. */\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character: 9679;\n"
"}\n"
"\n"
"/* We provide a min-width and min-height for push buttons\n"
"   so that they look elegant regardless of the width of the text. */\n"
"QPushButton {\n"
"    background-color: palegoldenrod;\n"
"    border-width: 2px;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-radius: 5;\n"
"    padding: 3px;\n"
"    min-width: 9ex;\n"
"    min-height: 2.5ex;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: khaki;\n"
"}\n"
"\n"
"/* Increase the padding, so the text is shifted when the button is\n"
"   pressed. */\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: #d0d67c;\n"
"}\n"
"\n"
"QLabel, QAbstractButton {\n"
"    font: bold;\n"
"}\n"
"\n"
"/* Mark mandatory fields with a brownish color. */\n"
".mandatory {\n"
"    color: brown;\n"
"}\n"
"\n"
"/* Bold text on status bar looks awful. */\n"
"QStatusBar QLabel {\n"
"   font: normal;\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"    border-width: 1;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-radius: 2;\n"
"}\n"
"\n"
"QComboBox, QLineEdit, QSpinBox, QTextEdit, QListView,QProgressBar,QscrollBar {\n"
"    background-color: cornsilk;\n"
"    selection-color: #0a214c; \n"
"    selection-background-color: #C19A6B;\n"
"}\n"
"\n"
"QListView {\n"
"    show-decoration-selected: 1;\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background-color: wheat;\n"
"}\n"
"\n"
"/* We reserve 1 pixel space in padding. When we get the focus,\n"
"   we kill the padding and enlarge the border. This makes the items\n"
"   glow. */\n"
"QLineEdit, QFrame {\n"
"    border-width: 2px;\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border-color: darkkhaki;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* As mentioned above, eliminate the padding and increase the border. */\n"
"QLineEdit:focus, QFrame:focus {\n"
"    border-width: 3px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"/* A QLabel is a QFrame ... */\n"
"QLabel {\n"
"    border: none;\n"
"    padding: 0;\n"
"    background: none;\n"
"}\n"
"\n"
"/* A QToolTip is a QLabel ... */\n"
"QToolTip {\n"
"    border: 2px solid darkkhaki;\n"
"    padding: 5px;\n"
"    border-radius: 3px;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"/* Nice to have the background color change when hovered. */\n"
"QRadioButton:hover, QCheckBox:hover {\n"
"    background-color: wheat;\n"
"}\n"
"\n"
"/* Force the dialog\'s buttons to follow the Windows guidelines. */\n"
"QDialogButtonBox {\n"
"    button-layout: 0;\n"
"}\n"
"\n"
" \n"
"")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lblCurrentCity = QtGui.QLabel(self.centralwidget)
        self.lblCurrentCity.setStyleSheet("None")
        self.lblCurrentCity.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCurrentCity.setObjectName("lblCurrentCity")
        self.horizontalLayout_5.addWidget(self.lblCurrentCity)
        self.lblCurrentCountry = QtGui.QLabel(self.centralwidget)
        self.lblCurrentCountry.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCurrentCountry.setObjectName("lblCurrentCountry")
        self.horizontalLayout_5.addWidget(self.lblCurrentCountry)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.lblCurrentTime = QtGui.QLabel(self.centralwidget)
        self.lblCurrentTime.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCurrentTime.setObjectName("lblCurrentTime")
        self.horizontalLayout_4.addWidget(self.lblCurrentTime)
        self.lblCurrentDate = QtGui.QLabel(self.centralwidget)
        self.lblCurrentDate.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCurrentDate.setObjectName("lblCurrentDate")
        self.horizontalLayout_4.addWidget(self.lblCurrentDate)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.frame = QtGui.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("KacstQurn")
        self.frame.setFont(font)
        self.frame.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame.setObjectName("frame")
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.lblFajr = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.lblFajr.setFont(font)
        self.lblFajr.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFajr.setObjectName("lblFajr")
        self.gridLayout.addWidget(self.lblFajr, 0, 0, 1, 1)
        self.lblShrook = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.lblShrook.setFont(font)
        self.lblShrook.setAlignment(QtCore.Qt.AlignCenter)
        self.lblShrook.setObjectName("lblShrook")
        self.gridLayout.addWidget(self.lblShrook, 0, 1, 1, 1)
        self.lblZuhr = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.lblZuhr.setFont(font)
        self.lblZuhr.setAlignment(QtCore.Qt.AlignCenter)
        self.lblZuhr.setObjectName("lblZuhr")
        self.gridLayout.addWidget(self.lblZuhr, 0, 2, 1, 1)
        self.txtFajr = QtGui.QLineEdit(self.frame)
        self.txtFajr.setAlignment(QtCore.Qt.AlignCenter)
        self.txtFajr.setReadOnly(True)
        self.txtFajr.setObjectName("txtFajr")
        self.gridLayout.addWidget(self.txtFajr, 1, 0, 1, 1)
        self.txtShrouk = QtGui.QLineEdit(self.frame)
        self.txtShrouk.setAlignment(QtCore.Qt.AlignCenter)
        self.txtShrouk.setReadOnly(True)
        self.txtShrouk.setObjectName("txtShrouk")
        self.gridLayout.addWidget(self.txtShrouk, 1, 1, 1, 1)
        self.txtZuhr = QtGui.QLineEdit(self.frame)
        self.txtZuhr.setAlignment(QtCore.Qt.AlignCenter)
        self.txtZuhr.setReadOnly(True)
        self.txtZuhr.setObjectName("txtZuhr")
        self.gridLayout.addWidget(self.txtZuhr, 1, 2, 1, 1)
        self.lblAsr = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.lblAsr.setFont(font)
        self.lblAsr.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAsr.setObjectName("lblAsr")
        self.gridLayout.addWidget(self.lblAsr, 2, 0, 1, 1)
        self.lblMaghrib = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.lblMaghrib.setFont(font)
        self.lblMaghrib.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMaghrib.setObjectName("lblMaghrib")
        self.gridLayout.addWidget(self.lblMaghrib, 2, 1, 1, 1)
        self.lblIsha = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("KacstQurn")
        font.setPointSize(11)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.lblIsha.setFont(font)
        self.lblIsha.setStyleSheet("font: 11pt \"KacstQurn\";")
        self.lblIsha.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIsha.setObjectName("lblIsha")
        self.gridLayout.addWidget(self.lblIsha, 2, 2, 1, 1)
        self.txtAsr = QtGui.QLineEdit(self.frame)
        self.txtAsr.setAlignment(QtCore.Qt.AlignCenter)
        self.txtAsr.setReadOnly(True)
        self.txtAsr.setObjectName("txtAsr")
        self.gridLayout.addWidget(self.txtAsr, 3, 0, 1, 1)
        self.txtMaghrib = QtGui.QLineEdit(self.frame)
        self.txtMaghrib.setStyleSheet("None")
        self.txtMaghrib.setAlignment(QtCore.Qt.AlignCenter)
        self.txtMaghrib.setReadOnly(True)
        self.txtMaghrib.setObjectName("txtMaghrib")
        self.gridLayout.addWidget(self.txtMaghrib, 3, 1, 1, 1)
        self.txtIshaa = QtGui.QLineEdit(self.frame)
        self.txtIshaa.setAlignment(QtCore.Qt.AlignCenter)
        self.txtIshaa.setReadOnly(True)
        self.txtIshaa.setObjectName("txtIshaa")
        self.gridLayout.addWidget(self.txtIshaa, 3, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnHide = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.btnHide.setFont(font)
        self.btnHide.setObjectName("btnHide")
        self.horizontalLayout_2.addWidget(self.btnHide)
        self.btnSettings = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.btnSettings.setFont(font)
        self.btnSettings.setObjectName("btnSettings")
        self.horizontalLayout_2.addWidget(self.btnSettings)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 417, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.actionShow = QtGui.QAction(MainWindow)
        self.actionShow.setObjectName("actionShow")
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionStopAzan = QtGui.QAction(MainWindow)
        self.actionStopAzan.setObjectName("actionStopAzan")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Azan", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCurrentCity.setText(QtGui.QApplication.translate("MainWindow", "City", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCurrentCountry.setText(QtGui.QApplication.translate("MainWindow", "Country", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCurrentTime.setText(QtGui.QApplication.translate("MainWindow", "Time", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCurrentDate.setText(QtGui.QApplication.translate("MainWindow", "Date", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFajr.setText(QtGui.QApplication.translate("MainWindow", "الفجر", None, QtGui.QApplication.UnicodeUTF8))
        self.lblShrook.setText(QtGui.QApplication.translate("MainWindow", "الشروق", None, QtGui.QApplication.UnicodeUTF8))
        self.lblZuhr.setText(QtGui.QApplication.translate("MainWindow", "الظهر", None, QtGui.QApplication.UnicodeUTF8))
        self.lblAsr.setText(QtGui.QApplication.translate("MainWindow", "العصر", None, QtGui.QApplication.UnicodeUTF8))
        self.lblMaghrib.setText(QtGui.QApplication.translate("MainWindow", "المغرب", None, QtGui.QApplication.UnicodeUTF8))
        self.lblIsha.setText(QtGui.QApplication.translate("MainWindow", "العشاء", None, QtGui.QApplication.UnicodeUTF8))
        self.btnHide.setText(QtGui.QApplication.translate("MainWindow", "إخفاء", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSettings.setText(QtGui.QApplication.translate("MainWindow", "الأعدادات", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow.setText(QtGui.QApplication.translate("MainWindow", "إظهار", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("MainWindow", "إنهاء البرنامج", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStopAzan.setText(QtGui.QApplication.translate("MainWindow", "إيقاف صوت الأذان", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

