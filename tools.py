# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tools.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(241, 185)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 241, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tools"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Welcome to SteamBSD!</p><p>Technologies: <a href=\"https://docs.google.com/presentation/d/1FAQ8LqB_AtzgqjF6cK0pd4v8m-KjH4zwaMpp4Ds9-8Y/edit#slide=id.p\"><span style=\" text-decoration: underline; color:#0986d3;\">Info</span></a></p><p>List of games: <a href=\"https://docs.google.com/spreadsheets/d/1AodDt2fc7-rSmd_75vFLc_eCpmRnfiAtIfnrGtpcbmY/edit?usp=sharing\"><span style=\" text-decoration: underline; color:#0986d3;\">Library</span></a></p><p>Documentation: <a href=\"https://docs.google.com/document/d/1N6Z1mbL61G-uK1dgLHT2EJDaNrh9RiaDlk25l4BeIFE/edit\"><span style=\" text-decoration: underline; color:#0986d3;\">Manual</span></a></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
