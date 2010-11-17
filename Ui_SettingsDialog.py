# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ahmed/Eric/azan/SettingsDialog.ui'
#
# Created: Wed Nov 17 18:14:52 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(456, 497)
        SettingsDialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        SettingsDialog.setStyleSheet(".QWidget ,QDialog,QGroupBox {\n"
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
"QPushButton,QToolButton {\n"
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
"QComboBox, QLineEdit, QSpinBox, QTextEdit, QListView,QProgressBar {\n"
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
        SettingsDialog.setModal(False)
        self.verticalLayout_5 = QtGui.QVBoxLayout(SettingsDialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.tabWidget = QtGui.QTabWidget(SettingsDialog)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(32, 32))
        self.tabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidgetPage1 = QtGui.QWidget()
        self.tabWidgetPage1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
        self.verticalLayout = QtGui.QVBoxLayout(self.tabWidgetPage1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.listCountries = QtGui.QListWidget(self.tabWidgetPage1)
        self.listCountries.setObjectName("listCountries")
        self.horizontalLayout_10.addWidget(self.listCountries)
        self.listCities = QtGui.QListWidget(self.tabWidgetPage1)
        self.listCities.setObjectName("listCities")
        self.horizontalLayout_10.addWidget(self.listCities)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupBox_2 = QtGui.QGroupBox(self.tabWidgetPage1)
        self.groupBox_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.rbWinter = QtGui.QRadioButton(self.groupBox_2)
        self.rbWinter.setChecked(True)
        self.rbWinter.setObjectName("rbWinter")
        self.horizontalLayout_5.addWidget(self.rbWinter)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.rbSummer = QtGui.QRadioButton(self.groupBox_2)
        self.rbSummer.setObjectName("rbSummer")
        self.horizontalLayout_6.addWidget(self.rbSummer)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(self.tabWidgetPage1)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.txtLongitude = QtGui.QLineEdit(self.groupBox)
        self.txtLongitude.setObjectName("txtLongitude")
        self.horizontalLayout_3.addWidget(self.txtLongitude)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txtLatitude = QtGui.QLineEdit(self.groupBox)
        self.txtLatitude.setObjectName("txtLatitude")
        self.horizontalLayout.addWidget(self.txtLatitude)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.txtTimeZone = QtGui.QLineEdit(self.groupBox)
        self.txtTimeZone.setObjectName("txtTimeZone")
        self.horizontalLayout_4.addWidget(self.txtTimeZone)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7.addWidget(self.groupBox)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.cboxMazhab = QtGui.QComboBox(self.tabWidgetPage1)
        self.cboxMazhab.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.cboxMazhab.setObjectName("cboxMazhab")
        self.cboxMazhab.addItem("")
        self.cboxMazhab.addItem("")
        self.horizontalLayout_8.addWidget(self.cboxMazhab)
        self.label_4 = QtGui.QLabel(self.tabWidgetPage1)
        self.label_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem6)
        self.cboxCalendar = QtGui.QComboBox(self.tabWidgetPage1)
        self.cboxCalendar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.cboxCalendar.setObjectName("cboxCalendar")
        self.cboxCalendar.addItem("")
        self.cboxCalendar.addItem("")
        self.cboxCalendar.addItem("")
        self.cboxCalendar.addItem("")
        self.cboxCalendar.addItem("")
        self.horizontalLayout_9.addWidget(self.cboxCalendar)
        self.label_5 = QtGui.QLabel(self.tabWidgetPage1)
        self.label_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/kubbetussahra_128x128x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabWidgetPage1, icon, "")
        self.tabWidgetPage2 = QtGui.QWidget()
        self.tabWidgetPage2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidgetPage2.setObjectName("tabWidgetPage2")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tabWidgetPage2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem7)
        self.label_7 = QtGui.QLabel(self.tabWidgetPage2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_13.addWidget(self.label_7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.btnStop = QtGui.QToolButton(self.tabWidgetPage2)
        self.btnStop.setMinimumSize(QtCore.QSize(37, 18))
        self.btnStop.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/media-playback-pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStop.setIcon(icon1)
        self.btnStop.setObjectName("btnStop")
        self.horizontalLayout_12.addWidget(self.btnStop)
        self.btnPlay = QtGui.QToolButton(self.tabWidgetPage2)
        self.btnPlay.setMinimumSize(QtCore.QSize(37, 18))
        self.btnPlay.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/media-playback-start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPlay.setIcon(icon2)
        self.btnPlay.setObjectName("btnPlay")
        self.horizontalLayout_12.addWidget(self.btnPlay)
        self.cboxAzanSound = QtGui.QComboBox(self.tabWidgetPage2)
        self.cboxAzanSound.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.cboxAzanSound.setObjectName("cboxAzanSound")
        self.cboxAzanSound.addItem("")
        self.cboxAzanSound.addItem("")
        self.cboxAzanSound.addItem("")
        self.cboxAzanSound.addItem("")
        self.horizontalLayout_12.addWidget(self.cboxAzanSound)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.line = QtGui.QFrame(self.tabWidgetPage2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_8 = QtGui.QLabel(self.tabWidgetPage2)
        self.label_8.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_14.addWidget(self.label_8)
        self.spinShowZekrTimer = QtGui.QSpinBox(self.tabWidgetPage2)
        self.spinShowZekrTimer.setObjectName("spinShowZekrTimer")
        self.horizontalLayout_14.addWidget(self.spinShowZekrTimer)
        self.label_6 = QtGui.QLabel(self.tabWidgetPage2)
        self.label_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_14.addWidget(self.label_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_14)
        spacerItem8 = QtGui.QSpacerItem(20, 344, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem8)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/preferences-desktop-sound.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabWidgetPage2, icon3, "")
        self.horizontalLayout_11.addWidget(self.tabWidget)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtGui.QPushButton(SettingsDialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.btnSaveSettings = QtGui.QPushButton(SettingsDialog)
        self.btnSaveSettings.setObjectName("btnSaveSettings")
        self.horizontalLayout_2.addWidget(self.btnSaveSettings)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.retranslateUi(SettingsDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), SettingsDialog.close)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QtGui.QApplication.translate("SettingsDialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("SettingsDialog", "التوقيت", None, QtGui.QApplication.UnicodeUTF8))
        self.rbWinter.setText(QtGui.QApplication.translate("SettingsDialog", "شتوي", None, QtGui.QApplication.UnicodeUTF8))
        self.rbSummer.setText(QtGui.QApplication.translate("SettingsDialog", "صيفي", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("SettingsDialog", "بيانات المدينة", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SettingsDialog", "خط الطول", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SettingsDialog", "خط العرض", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("SettingsDialog", "فرق التوقيت عن جرينتش", None, QtGui.QApplication.UnicodeUTF8))
        self.cboxMazhab.setItemText(0, QtGui.QApplication.translate("SettingsDialog", "الشافعي,المالكي,الحنبلي", None, QtGui.QApplication.UnicodeUTF8))
        self.cboxMazhab.setItemText(1, QtGui.QApplication.translate("SettingsDialog", "الحنفي", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("SettingsDialog", "المذهب", None, QtGui.QApplication.UnicodeUTF8))
        self.cboxCalendar.setItemText(0, QtGui.QApplication.translate("SettingsDialog", "جامعة أم القري", None, QtGui.QApplication.UnicodeUTF8))
        self.cboxCalendar.setItemText(1, QtGui.QApplication.translate("SettingsDialog", "الهيئة  المصرية للمساحة", None, QtGui.QApplication.UnicodeUTF8))
        self.cboxCalendar.setItemText(2, QtGui.QApplication.translate("SettingsDialog", "جامعة العلوم الأسلامية بكراتشي", None, QtGui.QApplication.UnicodeUTF8))
        self.cboxCalendar.setItemText(3, QtGui.QApplication.translate("SettingsDialog", "الأتحاد الأسلامي بأمريكا الشمالية", None, QtGui.QApplication.UnicodeUTF8))
        self.cboxCalendar.setItemText(4, QtGui.QApplication.translate("SettingsDialog", "رابطة العالم الأسلامي", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("SettingsDialog", "التقويم", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), QtGui.QApplication.translate("SettingsDialog", "إعدادات المدينة", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("SettingsDialog", "صوت الأذان", None, QtGui.QApplication.UnicodeUTF8))
        self.cboxAzanSound.setItemText(0, QtGui.QApplication.translate("SettingsDialog", "مصر- ناصر القطامي", None, QtGui.QApplication.UnicodeUTF8))
        self.cboxAzanSound.setItemText(1, QtGui.QApplication.translate("SettingsDialog", "المسجد الحرام", None, QtGui.QApplication.UnicodeUTF8))
        self.cboxAzanSound.setItemText(2, QtGui.QApplication.translate("SettingsDialog", "المسجد النبوي", None, QtGui.QApplication.UnicodeUTF8))
        self.cboxAzanSound.setItemText(3, QtGui.QApplication.translate("SettingsDialog", "مصر - عبدالباسط عبد الصمد", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("SettingsDialog", "دقيقة", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("SettingsDialog", "إظهار الأذكار كل ", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), QtGui.QApplication.translate("SettingsDialog", "إعدادات الأذان", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("SettingsDialog", "إغلاق", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSaveSettings.setText(QtGui.QApplication.translate("SettingsDialog", "حفظ  ", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SettingsDialog = QtGui.QDialog()
    ui = Ui_SettingsDialog()
    ui.setupUi(SettingsDialog)
    SettingsDialog.show()
    sys.exit(app.exec_())

