# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Thu Jun  2 21:28:29 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(672, 487)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Images/icons/chameleon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 661, 461))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.tabWidget = QtGui.QTabWidget(self.layoutWidget)
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setObjectName("tabWidget")
        self.hide = QtGui.QWidget()
        self.hide.setObjectName("hide")
        self.hideStatusLabel = QtGui.QLabel(self.hide)
        self.hideStatusLabel.setGeometry(QtCore.QRect(10, 270, 491, 17))
        self.hideStatusLabel.setStyleSheet("font: italic 11pt \"Ubuntu\";\n"
"border-color: rgb(170, 0, 0);")
        self.hideStatusLabel.setText("")
        self.hideStatusLabel.setTextFormat(QtCore.Qt.RichText)
        self.hideStatusLabel.setObjectName("hideStatusLabel")
        self.hidetoolButton = QtGui.QToolButton(self.hide)
        self.hidetoolButton.setGeometry(QtCore.QRect(540, 260, 81, 81))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Images/icons/2196503-lock-off-icon-red-isolated-on-white-background.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hidetoolButton.setIcon(icon1)
        self.hidetoolButton.setIconSize(QtCore.QSize(50, 50))
        self.hidetoolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.hidetoolButton.setAutoRaise(True)
        self.hidetoolButton.setObjectName("hidetoolButton")
        self.layoutWidget1 = QtGui.QWidget(self.hide)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 10, 621, 241))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_5 = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtGui.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fileLineEdit = QtGui.QLineEdit(self.layoutWidget1)
        self.fileLineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.fileLineEdit.setObjectName("fileLineEdit")
        self.verticalLayout_2.addWidget(self.fileLineEdit)
        self.imageFileLineEdit = QtGui.QLineEdit(self.layoutWidget1)
        self.imageFileLineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.imageFileLineEdit.setObjectName("imageFileLineEdit")
        self.verticalLayout_2.addWidget(self.imageFileLineEdit)
        self.passwordLineEdit = QtGui.QLineEdit(self.layoutWidget1)
        self.passwordLineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.passwordLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.verticalLayout_2.addWidget(self.passwordLineEdit)
        self.cpasswordLineEdit = QtGui.QLineEdit(self.layoutWidget1)
        self.cpasswordLineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.cpasswordLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.cpasswordLineEdit.setObjectName("cpasswordLineEdit")
        self.verticalLayout_2.addWidget(self.cpasswordLineEdit)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.browsePushButton = QtGui.QPushButton(self.layoutWidget1)
        self.browsePushButton.setObjectName("browsePushButton")
        self.verticalLayout_10.addWidget(self.browsePushButton)
        self.browseImagePushButton = QtGui.QPushButton(self.layoutWidget1)
        self.browseImagePushButton.setObjectName("browseImagePushButton")
        self.verticalLayout_10.addWidget(self.browseImagePushButton)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout_10, 0, 2, 1, 1)
        self.passwordLabel = QtGui.QLabel(self.layoutWidget1)
        self.passwordLabel.setText("")
        self.passwordLabel.setObjectName("passwordLabel")
        self.gridLayout.addWidget(self.passwordLabel, 1, 0, 1, 3)
        self.gridLayout_5.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.layoutWidget1)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 2, 0, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_8 = QtGui.QLabel(self.layoutWidget1)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)
        self.opimageComboBox = QtGui.QComboBox(self.layoutWidget1)
        self.opimageComboBox.setObjectName("opimageComboBox")
        self.opimageComboBox.addItem("")
        self.opimageComboBox.setItemText(0, "")
        self.opimageComboBox.addItem("")
        self.opimageComboBox.addItem("")
        self.opimageComboBox.addItem("")
        self.opimageComboBox.addItem("")
        self.gridLayout_4.addWidget(self.opimageComboBox, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 3, 0, 1, 1)
        self.tabWidget.addTab(self.hide, "")
        self.extract = QtGui.QWidget()
        self.extract.setObjectName("extract")
        self.extractToolButton = QtGui.QToolButton(self.extract)
        self.extractToolButton.setGeometry(QtCore.QRect(540, 260, 81, 81))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Images/icons/2196504-lock-on-icon-red-isolated-on-white-background.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.extractToolButton.setIcon(icon2)
        self.extractToolButton.setIconSize(QtCore.QSize(50, 50))
        self.extractToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.extractToolButton.setAutoRaise(True)
        self.extractToolButton.setObjectName("extractToolButton")
        self.extractStatusLabel = QtGui.QLabel(self.extract)
        self.extractStatusLabel.setGeometry(QtCore.QRect(30, 270, 481, 17))
        self.extractStatusLabel.setText("")
        self.extractStatusLabel.setObjectName("extractStatusLabel")
        self.layoutWidget2 = QtGui.QWidget(self.extract)
        self.layoutWidget2.setGeometry(QtCore.QRect(0, 10, 631, 211))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_8 = QtGui.QGridLayout(self.layoutWidget2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_9 = QtGui.QLabel(self.layoutWidget2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_8.addWidget(self.label_9, 0, 0, 1, 1)
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_11 = QtGui.QLabel(self.layoutWidget2)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.label_12 = QtGui.QLabel(self.layoutWidget2)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.label_13 = QtGui.QLabel(self.layoutWidget2)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(self.label_13)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.efileLineEdit = QtGui.QLineEdit(self.layoutWidget2)
        self.efileLineEdit.setObjectName("efileLineEdit")
        self.verticalLayout_4.addWidget(self.efileLineEdit)
        self.epasswordLineEdit = QtGui.QLineEdit(self.layoutWidget2)
        self.epasswordLineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.epasswordLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.epasswordLineEdit.setObjectName("epasswordLineEdit")
        self.verticalLayout_4.addWidget(self.epasswordLineEdit)
        self.ecpasswordLineEdit = QtGui.QLineEdit(self.layoutWidget2)
        self.ecpasswordLineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.ecpasswordLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.ecpasswordLineEdit.setObjectName("ecpasswordLineEdit")
        self.verticalLayout_4.addWidget(self.ecpasswordLineEdit)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 1, 1, 1)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.ebrowsePushButton = QtGui.QPushButton(self.layoutWidget2)
        self.ebrowsePushButton.setObjectName("ebrowsePushButton")
        self.verticalLayout_5.addWidget(self.ebrowsePushButton)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 2, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.epasswordLabel = QtGui.QLabel(self.layoutWidget2)
        self.epasswordLabel.setText("")
        self.epasswordLabel.setObjectName("epasswordLabel")
        self.gridLayout_7.addWidget(self.epasswordLabel, 1, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 1, 0, 1, 5)
        self.label_14 = QtGui.QLabel(self.layoutWidget2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_8.addWidget(self.label_14, 2, 0, 1, 1)
        self.label_15 = QtGui.QLabel(self.layoutWidget2)
        self.label_15.setObjectName("label_15")
        self.gridLayout_8.addWidget(self.label_15, 4, 0, 1, 1)
        self.saveasLineEdit = QtGui.QLineEdit(self.layoutWidget2)
        self.saveasLineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.saveasLineEdit.setObjectName("saveasLineEdit")
        self.gridLayout_8.addWidget(self.saveasLineEdit, 4, 2, 1, 1)
        self.saveasPushButton = QtGui.QPushButton(self.layoutWidget2)
        self.saveasPushButton.setObjectName("saveasPushButton")
        self.gridLayout_8.addWidget(self.saveasPushButton, 4, 3, 1, 1)
        self.tabWidget.addTab(self.extract, "")
        self.verticalLayout_6.addWidget(self.tabWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.helpPushButton = QtGui.QPushButton(self.layoutWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Images/icons/Help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpPushButton.setIcon(icon3)
        self.helpPushButton.setObjectName("helpPushButton")
        self.horizontalLayout.addWidget(self.helpPushButton)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.closePushButton = QtGui.QPushButton(self.layoutWidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Images/icons/CloseButton.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closePushButton.setIcon(icon4)
        self.closePushButton.setDefault(False)
        self.closePushButton.setFlat(False)
        self.closePushButton.setObjectName("closePushButton")
        self.horizontalLayout.addWidget(self.closePushButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_3.setBuddy(self.fileLineEdit)
        self.label_4.setBuddy(self.imageFileLineEdit)
        self.label_5.setBuddy(self.passwordLineEdit)
        self.label_6.setBuddy(self.cpasswordLineEdit)
        self.label_8.setBuddy(self.opimageComboBox)
        self.label_11.setBuddy(self.efileLineEdit)
        self.label_12.setBuddy(self.epasswordLineEdit)
        self.label_13.setBuddy(self.ecpasswordLineEdit)
        self.label_15.setBuddy(self.saveasLineEdit)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.closePushButton, QtCore.SIGNAL("clicked()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Camouflage Xtreme", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setStatusTip(QtGui.QApplication.translate("MainWindow", "Welcome to Camouflage Xtreme v1.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Welcome  to  <span style=\" font-weight:600;\">Camouflage Xtreme v1.0</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setStatusTip(QtGui.QApplication.translate("MainWindow", "Hide or Extract data", None, QtGui.QApplication.UnicodeUTF8))
        self.hidetoolButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Hide data in Image", None, QtGui.QApplication.UnicodeUTF8))
        self.hidetoolButton.setText(QtGui.QApplication.translate("MainWindow", "Hi&de", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Input Options</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "    File conataning data", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "    Image file for hiding data", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "    Password", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "    Confirm password", None, QtGui.QApplication.UnicodeUTF8))
        self.fileLineEdit.setToolTip(QtGui.QApplication.translate("MainWindow", "File containing data", None, QtGui.QApplication.UnicodeUTF8))
        self.imageFileLineEdit.setToolTip(QtGui.QApplication.translate("MainWindow", "Name of image file", None, QtGui.QApplication.UnicodeUTF8))
        self.imageFileLineEdit.setStatusTip(QtGui.QApplication.translate("MainWindow", "Enter name of Image file", None, QtGui.QApplication.UnicodeUTF8))
        self.passwordLineEdit.setToolTip(QtGui.QApplication.translate("MainWindow", "Enter password", None, QtGui.QApplication.UnicodeUTF8))
        self.passwordLineEdit.setStatusTip(QtGui.QApplication.translate("MainWindow", "Enter password", None, QtGui.QApplication.UnicodeUTF8))
        self.cpasswordLineEdit.setToolTip(QtGui.QApplication.translate("MainWindow", "Confirm password", None, QtGui.QApplication.UnicodeUTF8))
        self.cpasswordLineEdit.setStatusTip(QtGui.QApplication.translate("MainWindow", "Confirm password", None, QtGui.QApplication.UnicodeUTF8))
        self.browsePushButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Browse for files in system", None, QtGui.QApplication.UnicodeUTF8))
        self.browsePushButton.setStatusTip(QtGui.QApplication.translate("MainWindow", "Browse for files in system", None, QtGui.QApplication.UnicodeUTF8))
        self.browsePushButton.setText(QtGui.QApplication.translate("MainWindow", "&Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.browseImagePushButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Browse images  in system", None, QtGui.QApplication.UnicodeUTF8))
        self.browseImagePushButton.setStatusTip(QtGui.QApplication.translate("MainWindow", "Browse for Image files in system", None, QtGui.QApplication.UnicodeUTF8))
        self.browseImagePushButton.setText(QtGui.QApplication.translate("MainWindow", "Browse &Image", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Output Options</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "    Output image format", None, QtGui.QApplication.UnicodeUTF8))
        self.opimageComboBox.setToolTip(QtGui.QApplication.translate("MainWindow", "Select output file format", None, QtGui.QApplication.UnicodeUTF8))
        self.opimageComboBox.setStatusTip(QtGui.QApplication.translate("MainWindow", "Select output file format", None, QtGui.QApplication.UnicodeUTF8))
        self.opimageComboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", ".jpg", None, QtGui.QApplication.UnicodeUTF8))
        self.opimageComboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", ".png", None, QtGui.QApplication.UnicodeUTF8))
        self.opimageComboBox.setItemText(3, QtGui.QApplication.translate("MainWindow", ".bmp", None, QtGui.QApplication.UnicodeUTF8))
        self.opimageComboBox.setItemText(4, QtGui.QApplication.translate("MainWindow", ".tiff", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.hide), QtGui.QApplication.translate("MainWindow", "Hide Data", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.hide), QtGui.QApplication.translate("MainWindow", "Hide data in image", None, QtGui.QApplication.UnicodeUTF8))
        self.extractToolButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Extract data from image", None, QtGui.QApplication.UnicodeUTF8))
        self.extractToolButton.setText(QtGui.QApplication.translate("MainWindow", "&Extract", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Input Options</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "    Image file which contains data", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "    Password", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "    Confirm password", None, QtGui.QApplication.UnicodeUTF8))
        self.efileLineEdit.setToolTip(QtGui.QApplication.translate("MainWindow", "Name of file which contains data", None, QtGui.QApplication.UnicodeUTF8))
        self.efileLineEdit.setStatusTip(QtGui.QApplication.translate("MainWindow", "Enter Name of file which contains data", None, QtGui.QApplication.UnicodeUTF8))
        self.epasswordLineEdit.setToolTip(QtGui.QApplication.translate("MainWindow", "Enter Password", None, QtGui.QApplication.UnicodeUTF8))
        self.epasswordLineEdit.setStatusTip(QtGui.QApplication.translate("MainWindow", "Browse for files in system", None, QtGui.QApplication.UnicodeUTF8))
        self.ecpasswordLineEdit.setToolTip(QtGui.QApplication.translate("MainWindow", "confirm password", None, QtGui.QApplication.UnicodeUTF8))
        self.ecpasswordLineEdit.setStatusTip(QtGui.QApplication.translate("MainWindow", "Browse for files in system", None, QtGui.QApplication.UnicodeUTF8))
        self.ebrowsePushButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Browse for files inside the system", None, QtGui.QApplication.UnicodeUTF8))
        self.ebrowsePushButton.setStatusTip(QtGui.QApplication.translate("MainWindow", "Browse for files inside the system", None, QtGui.QApplication.UnicodeUTF8))
        self.ebrowsePushButton.setText(QtGui.QApplication.translate("MainWindow", "&Browse ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Output Options</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("MainWindow", "    Save output file as", None, QtGui.QApplication.UnicodeUTF8))
        self.saveasLineEdit.setToolTip(QtGui.QApplication.translate("MainWindow", "Enter output file name", None, QtGui.QApplication.UnicodeUTF8))
        self.saveasLineEdit.setStatusTip(QtGui.QApplication.translate("MainWindow", "Browse for files in system", None, QtGui.QApplication.UnicodeUTF8))
        self.saveasPushButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Save file in a folder in system", None, QtGui.QApplication.UnicodeUTF8))
        self.saveasPushButton.setStatusTip(QtGui.QApplication.translate("MainWindow", "Save file in a folder in system", None, QtGui.QApplication.UnicodeUTF8))
        self.saveasPushButton.setText(QtGui.QApplication.translate("MainWindow", "&Save file as", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.extract), QtGui.QApplication.translate("MainWindow", "Extract Data", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.extract), QtGui.QApplication.translate("MainWindow", "Extract data from a file", None, QtGui.QApplication.UnicodeUTF8))
        self.helpPushButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.helpPushButton.setStatusTip(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.helpPushButton.setText(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.closePushButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.closePushButton.setStatusTip(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.closePushButton.setText(QtGui.QApplication.translate("MainWindow", "&Close", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
