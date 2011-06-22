#!/usr/bin/python -W
# -*- coding: utf-8 -*-
# Author: Antonio P. Diaz <emperor.cu@gmail.com>
# License: GPLv3

import sys
from PyQt4 import QtCore, QtGui
import ui_kpymirror

class Main(QtGui.QMainWindow):
    def __init__(self):
        
        QtGui.QMainWindow.__init__(self)
       
        self.ui = ui_kpymirror.Ui_MainWindow()
        self.ui.setupUi(self)
        
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move ((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

        self.connect(self.ui.pushButton_quit, QtCore.SIGNAL("clicked()"), QtGui.qApp, QtCore.SLOT("quit()"))
        self.connect(self.ui.checkBox_proxy, QtCore.SIGNAL("clicked()"), self.set_proxy)
        
    def set_proxy(self):
        if self.ui.checkBox_proxy.isChecked() is True:
            self.ui.lineEdit_host.setEnabled(True)
            self.ui.lineEdit_port.setEnabled(True)
            self.ui.lineEdit_username.setEnabled(True)
            self.ui.lineEdit_password.setEnabled(True)
        else:
            self.ui.lineEdit_host.setEnabled(False)
            self.ui.lineEdit_port.setEnabled(False)
            self.ui.lineEdit_username.setEnabled(False)
            self.ui.lineEdit_password.setEnabled(False)
            
def main():
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()