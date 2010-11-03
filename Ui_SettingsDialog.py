# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ahmed/Eric/Azan/SettingsDialog.ui'
#
# Created: Mon Nov  1 09:48:30 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(507, 452)
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
"QPushButton , QToolButton {\n"
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
        self.stackedWidget = QtGui.QStackedWidget(SettingsDialog)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidgetPage1 = QtGui.QWidget()
        self.stackedWidgetPage1.setObjectName("stackedWidgetPage1")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.stackedWidgetPage1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.listCountries = QtGui.QListWidget(self.stackedWidgetPage1)
        self.listCountries.setObjectName("listCountries")
        self.horizontalLayout_10.addWidget(self.listCountries)
        self.listCities = QtGui.QListWidget(self.stackedWidgetPage1)
        self.listCities.setObjectName("listCities")
        self.horizontalLayout_10.addWidget(self.listCities)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupBox_2 = QtGui.QGroupBox(self.stackedWidgetPage1)
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
        self.groupBox = QtGui.QGroupBox(self.stackedWidgetPage1)
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
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.line = QtGui.QFrame(self.stackedWidgetPage1)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.cboxMazhab = QtGui.QComboBox(self.stackedWidgetPage1)
        self.cboxMazhab.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.cboxMazhab.setObjectName("cboxMazhab")
        self.cboxMazhab.addItem("")
        self.cboxMazhab.addItem("")
        self.horizontalLayout_8.addWidget(self.cboxMazhab)
        self.label_4 = QtGui.QLabel(self.stackedWidgetPage1)
        self.label_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem6)
        self.cboxCalendar = QtGui.QComboBox(self.stackedWidgetPage1)
        self.cboxCalendar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.cboxCalendar.setObjectName("cboxCalendar")
        self.cboxCalendar.addItem("")
        self.cboxCalendar.addItem("")
        self.cboxCalendar.addItem("")
        self.cboxCalendar.addItem("")
        self.cboxCalendar.addItem("")
        self.horizontalLayout_9.addWidget(self.cboxCalendar)
        self.label_5 = QtGui.QLabel(self.stackedWidgetPage1)
        self.label_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.stackedWidget.addWidget(self.stackedWidgetPage1)
        self.stackedWidgetPage2 = QtGui.QWidget()
        self.stackedWidgetPage2.setObjectName("stackedWidgetPage2")
        self.gridLayout = QtGui.QGridLayout(self.stackedWidgetPage2)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_2 = QtGui.QFrame(self.stackedWidgetPage2)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.layoutWidget = QtGui.QWidget(self.frame_2)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 20, 242, 33))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.btnStop = QtGui.QToolButton(self.layoutWidget)
        self.btnStop.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/media-playback-pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStop.setIcon(icon)
        self.btnStop.setObjectName("btnStop")
        self.horizontalLayout_12.addWidget(self.btnStop)
        self.btnPlay = QtGui.QToolButton(self.layoutWidget)
        self.btnPlay.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/media-playback-start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPlay.setIcon(icon1)
        self.btnPlay.setObjectName("btnPlay")
        self.horizontalLayout_12.addWidget(self.btnPlay)
        self.cboxAzanSound = QtGui.QComboBox(self.layoutWidget)
        self.cboxAzanSound.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.cboxAzanSound.setObjectName("cboxAzanSound")
        self.cboxAzanSound.addItem("")
        self.cboxAzanSound.addItem("")
        self.cboxAzanSound.addItem("")
        self.cboxAzanSound.addItem("")
        self.horizontalLayout_12.addWidget(self.cboxAzanSound)
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_12.addWidget(self.label_6)
        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)
        self.stackedWidget.addWidget(self.stackedWidgetPage2)
        self.horizontalLayout_11.addWidget(self.stackedWidget)
        self.frame = QtGui.QFrame(SettingsDialog)
        self.frame.setMinimumSize(QtCore.QSize(120, 0))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnCitySettings = QtGui.QPushButton(self.frame)
        self.btnCitySettings.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/kubbetussahra_128x128x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCitySettings.setIcon(icon2)
        self.btnCitySettings.setIconSize(QtCore.QSize(56, 56))
        self.btnCitySettings.setFlat(True)
        self.btnCitySettings.setObjectName("btnCitySettings")
        self.verticalLayout.addWidget(self.btnCitySettings)
        self.btnAzanSettings = QtGui.QPushButton(self.frame)
        self.btnAzanSettings.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/preferences-desktop-sound.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAzanSettings.setIcon(icon3)
        self.btnAzanSettings.setIconSize(QtCore.QSize(56, 56))
        self.btnAzanSettings.setFlat(True)
        self.btnAzanSettings.setObjectName("btnAzanSettings")
        self.verticalLayout.addWidget(self.btnAzanSettings)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout_11.addWidget(self.frame)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtGui.QPushButton(SettingsDialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.btnSaveSettings = QtGui.QPushButton(SettingsDialog)
        self.btnSaveSettings.setObjectName("btnSaveSettings")
        self.horizontalLayout_2.addWidget(self.btnSaveSettings)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.retranslateUi(SettingsDialog)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.btnCitySettings, QtCore.SIGNAL("clicked()"), self.stackedWidgetPage1.show)
        QtCore.QObject.connect(self.btnAzanSettings, QtCore.SIGNAL("clicked()"), self.stackedWidgetPage1.hide)
        QtCore.QObject.connect(self.btnCitySettings, QtCore.SIGNAL("clicked()"), self.stackedWidgetPage2.hide)
        QtCore.QObject.connect(self.btnAzanSettings, QtCore.SIGNAL("clicked()"), self.stackedWidgetPage2.show)
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
        self.cboxAzanSound.setItemText(0, QtGui.QApplication.translate("SettingsDialog", "ناصر القطامي", None, QtGui.QApplication.UnicodeUTF8))
        self.cboxAzanSound.setItemText(1, QtGui.QApplication.translate("SettingsDialog", "المسجد الحرام", None, QtGui.QApplication.UnicodeUTF8))
        self.cboxAzanSound.setItemText(2, QtGui.QApplication.translate("SettingsDialog", "المسجد النبوي", None, QtGui.QApplication.UnicodeUTF8))
        self.cboxAzanSound.setItemText(3, QtGui.QApplication.translate("SettingsDialog", " المسجد الأقصي", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("SettingsDialog", "صوت الأذان", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCitySettings.setToolTip(QtGui.QApplication.translate("SettingsDialog", "أعدادات المدينة", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAzanSettings.setToolTip(QtGui.QApplication.translate("SettingsDialog", "إعدادات التذكير", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("SettingsDialog", "إلغاء", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSaveSettings.setText(QtGui.QApplication.translate("SettingsDialog", "حفظ  ", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SettingsDialog = QtGui.QDialog()
    ui = Ui_SettingsDialog()
    ui.setupUi(SettingsDialog)
    SettingsDialog.show()
    sys.exit(app.exec_())

