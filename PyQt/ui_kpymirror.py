# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtUI/pymirror.ui'
#
# Created: Thu Feb 10 13:23:18 2011
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(411, 296)
        MainWindow.setCursor(QtCore.Qt.PointingHandCursor)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox_protocol = QtGui.QComboBox(self.centralwidget)
        self.comboBox_protocol.setGeometry(QtCore.QRect(83, 10, 70, 25))
        self.comboBox_protocol.setCursor(QtCore.Qt.PointingHandCursor)
        self.comboBox_protocol.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.comboBox_protocol.setObjectName("comboBox_protocol")
        self.comboBox_protocol.addItem("")
        self.comboBox_protocol.addItem("")
        self.comboBox_folder = QtGui.QComboBox(self.centralwidget)
        self.comboBox_folder.setGeometry(QtCore.QRect(83, 57, 70, 25))
        self.comboBox_folder.setCursor(QtCore.Qt.PointingHandCursor)
        self.comboBox_folder.setWhatsThis("")
        self.comboBox_folder.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.comboBox_folder.setEditable(False)
        self.comboBox_folder.setObjectName("comboBox_folder")
        self.comboBox_distro = QtGui.QComboBox(self.centralwidget)
        self.comboBox_distro.setGeometry(QtCore.QRect(250, 10, 111, 25))
        self.comboBox_distro.setCursor(QtCore.Qt.PointingHandCursor)
        self.comboBox_distro.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.comboBox_distro.setObjectName("comboBox_distro")
        self.comboBox_distro.addItem("")
        self.comboBox_distro.addItem("")
        self.comboBox_distro.addItem("")
        self.comboBox_distro.addItem("")
        self.comboBox_branch = QtGui.QComboBox(self.centralwidget)
        self.comboBox_branch.setEnabled(True)
        self.comboBox_branch.setGeometry(QtCore.QRect(250, 34, 141, 25))
        self.comboBox_branch.setCursor(QtCore.Qt.PointingHandCursor)
        self.comboBox_branch.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.comboBox_branch.setEditable(False)
        self.comboBox_branch.setObjectName("comboBox_branch")
        self.comboBox_branch.addItem("")
        self.comboBox_branch.addItem("")
        self.comboBox_branch.addItem("")
        self.lineEdit_origin = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_origin.setGeometry(QtCore.QRect(83, 33, 113, 25))
        self.lineEdit_origin.setCursor(QtCore.Qt.PointingHandCursor)
        self.lineEdit_origin.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lineEdit_origin.setObjectName("lineEdit_origin")
        self.lineEdit_host = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_host.setEnabled(False)
        self.lineEdit_host.setGeometry(QtCore.QRect(70, 152, 113, 25))
        self.lineEdit_host.setCursor(QtCore.Qt.PointingHandCursor)
        self.lineEdit_host.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lineEdit_host.setObjectName("lineEdit_host")
        self.lineEdit_port = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_port.setEnabled(False)
        self.lineEdit_port.setGeometry(QtCore.QRect(70, 176, 51, 25))
        self.lineEdit_port.setCursor(QtCore.Qt.PointingHandCursor)
        self.lineEdit_port.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.lineEdit_username = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_username.setEnabled(False)
        self.lineEdit_username.setGeometry(QtCore.QRect(256, 151, 113, 25))
        self.lineEdit_username.setCursor(QtCore.Qt.PointingHandCursor)
        self.lineEdit_username.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_password = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_password.setEnabled(False)
        self.lineEdit_password.setGeometry(QtCore.QRect(256, 175, 113, 25))
        self.lineEdit_password.setCursor(QtCore.Qt.PointingHandCursor)
        self.lineEdit_password.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lineEdit_password.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.pushButton_accept = QtGui.QPushButton(self.centralwidget)
        self.pushButton_accept.setGeometry(QtCore.QRect(92, 256, 105, 24))
        self.pushButton_accept.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton_accept.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pushButton_accept.setObjectName("pushButton_accept")
        self.pushButton_quit = QtGui.QPushButton(self.centralwidget)
        self.pushButton_quit.setGeometry(QtCore.QRect(212, 256, 105, 24))
        self.pushButton_quit.setCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton_quit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(40, 236, 331, 20))
        self.progressBar.setCursor(QtCore.Qt.PointingHandCursor)
        self.progressBar.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_protocol = QtGui.QLabel(self.centralwidget)
        self.label_protocol.setGeometry(QtCore.QRect(25, 14, 57, 15))
        self.label_protocol.setCursor(QtCore.Qt.PointingHandCursor)
        self.label_protocol.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_protocol.setObjectName("label_protocol")
        self.label_origin = QtGui.QLabel(self.centralwidget)
        self.label_origin.setGeometry(QtCore.QRect(40, 37, 41, 16))
        self.label_origin.setCursor(QtCore.Qt.PointingHandCursor)
        self.label_origin.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_origin.setObjectName("label_origin")
        self.label_path2save = QtGui.QLabel(self.centralwidget)
        self.label_path2save.setGeometry(QtCore.QRect(3, 59, 81, 20))
        self.label_path2save.setCursor(QtCore.Qt.PointingHandCursor)
        self.label_path2save.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_path2save.setObjectName("label_path2save")
        self.label_host = QtGui.QLabel(self.centralwidget)
        self.label_host.setGeometry(QtCore.QRect(43, 156, 31, 16))
        self.label_host.setCursor(QtCore.Qt.PointingHandCursor)
        self.label_host.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_host.setObjectName("label_host")
        self.label_port = QtGui.QLabel(self.centralwidget)
        self.label_port.setGeometry(QtCore.QRect(46, 181, 31, 16))
        self.label_port.setCursor(QtCore.Qt.PointingHandCursor)
        self.label_port.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_port.setObjectName("label_port")
        self.label_username = QtGui.QLabel(self.centralwidget)
        self.label_username.setGeometry(QtCore.QRect(193, 153, 71, 20))
        self.label_username.setCursor(QtCore.Qt.PointingHandCursor)
        self.label_username.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_username.setObjectName("label_username")
        self.label_password = QtGui.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(198, 178, 61, 16))
        self.label_password.setCursor(QtCore.Qt.PointingHandCursor)
        self.label_password.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_password.setObjectName("label_password")
        self.label_distro = QtGui.QLabel(self.centralwidget)
        self.label_distro.setGeometry(QtCore.QRect(211, 14, 41, 16))
        self.label_distro.setCursor(QtCore.Qt.PointingHandCursor)
        self.label_distro.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_distro.setObjectName("label_distro")
        self.label_branch = QtGui.QLabel(self.centralwidget)
        self.label_branch.setGeometry(QtCore.QRect(205, 39, 51, 16))
        self.label_branch.setCursor(QtCore.Qt.PointingHandCursor)
        self.label_branch.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_branch.setObjectName("label_branch")
        self.label_section = QtGui.QLabel(self.centralwidget)
        self.label_section.setGeometry(QtCore.QRect(202, 62, 51, 16))
        self.label_section.setCursor(QtCore.Qt.PointingHandCursor)
        self.label_section.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_section.setObjectName("label_section")
        self.checkBox_main = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_main.setEnabled(True)
        self.checkBox_main.setGeometry(QtCore.QRect(250, 60, 88, 23))
        self.checkBox_main.setCursor(QtCore.Qt.PointingHandCursor)
        self.checkBox_main.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.checkBox_main.setObjectName("checkBox_main")
        self.checkBox_contrib = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_contrib.setEnabled(True)
        self.checkBox_contrib.setGeometry(QtCore.QRect(250, 80, 88, 23))
        self.checkBox_contrib.setCursor(QtCore.Qt.PointingHandCursor)
        self.checkBox_contrib.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.checkBox_contrib.setObjectName("checkBox_contrib")
        self.checkBox_nonfree = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_nonfree.setEnabled(True)
        self.checkBox_nonfree.setGeometry(QtCore.QRect(250, 101, 88, 23))
        self.checkBox_nonfree.setCursor(QtCore.Qt.PointingHandCursor)
        self.checkBox_nonfree.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.checkBox_nonfree.setObjectName("checkBox_nonfree")
        self.checkBox_proxy = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_proxy.setGeometry(QtCore.QRect(70, 126, 121, 23))
        self.checkBox_proxy.setObjectName("checkBox_proxy")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "KPyMirror", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_protocol.setItemText(0, QtGui.QApplication.translate("MainWindow", "http", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_protocol.setItemText(1, QtGui.QApplication.translate("MainWindow", "ftp", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_distro.setItemText(0, QtGui.QApplication.translate("MainWindow", "stable", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_distro.setItemText(1, QtGui.QApplication.translate("MainWindow", "testing", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_distro.setItemText(2, QtGui.QApplication.translate("MainWindow", "unstable", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_distro.setItemText(3, QtGui.QApplication.translate("MainWindow", "experimental", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_branch.setItemText(0, QtGui.QApplication.translate("MainWindow", "debian", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_branch.setItemText(1, QtGui.QApplication.translate("MainWindow", "debian-security", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_branch.setItemText(2, QtGui.QApplication.translate("MainWindow", "debian-multimedia", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_origin.setText(QtGui.QApplication.translate("MainWindow", "ftp.debian.org", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_accept.setText(QtGui.QApplication.translate("MainWindow", "Accept", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_quit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_protocol.setText(QtGui.QApplication.translate("MainWindow", "Protocol", None, QtGui.QApplication.UnicodeUTF8))
        self.label_origin.setText(QtGui.QApplication.translate("MainWindow", "Origin", None, QtGui.QApplication.UnicodeUTF8))
        self.label_path2save.setText(QtGui.QApplication.translate("MainWindow", "Path to save", None, QtGui.QApplication.UnicodeUTF8))
        self.label_host.setText(QtGui.QApplication.translate("MainWindow", "Host", None, QtGui.QApplication.UnicodeUTF8))
        self.label_port.setText(QtGui.QApplication.translate("MainWindow", "Port", None, QtGui.QApplication.UnicodeUTF8))
        self.label_username.setText(QtGui.QApplication.translate("MainWindow", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.label_password.setText(QtGui.QApplication.translate("MainWindow", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.label_distro.setText(QtGui.QApplication.translate("MainWindow", "Distro", None, QtGui.QApplication.UnicodeUTF8))
        self.label_branch.setText(QtGui.QApplication.translate("MainWindow", "Branch", None, QtGui.QApplication.UnicodeUTF8))
        self.label_section.setText(QtGui.QApplication.translate("MainWindow", "Section", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_main.setText(QtGui.QApplication.translate("MainWindow", "main", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_contrib.setText(QtGui.QApplication.translate("MainWindow", "contrib", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_nonfree.setText(QtGui.QApplication.translate("MainWindow", "non-free", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_proxy.setText(QtGui.QApplication.translate("MainWindow", "Activate Proxy", None, QtGui.QApplication.UnicodeUTF8))

