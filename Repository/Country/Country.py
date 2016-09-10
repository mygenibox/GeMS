# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Country.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1200, 700)
        MainWindow.setMouseTracking(True)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.webView = QtWebKit.QWebView(self.centralwidget)
        self.webView.setGeometry(QtCore.QRect(410, 40, 514, 551))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("http://www.openstreetmap.org/")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(560, 0, 211, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Sans Typewriter"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.calendarWidget = QtGui.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(930, 40, 251, 171))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.webView_2 = QtWebKit.QWebView(self.centralwidget)
        self.webView_2.setGeometry(QtCore.QRect(930, 220, 251, 371))
        self.webView_2.setUrl(QtCore.QUrl(_fromUtf8("http://exchange.genibox.net/")))
        self.webView_2.setObjectName(_fromUtf8("webView_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuCore = QtGui.QMenu(self.menubar)
        self.menuCore.setObjectName(_fromUtf8("menuCore"))
        self.menuCountry = QtGui.QMenu(self.menubar)
        self.menuCountry.setObjectName(_fromUtf8("menuCountry"))
        self.menuDownload_GEMS = QtGui.QMenu(self.menubar)
        self.menuDownload_GEMS.setObjectName(_fromUtf8("menuDownload_GEMS"))
        self.menuAndroid = QtGui.QMenu(self.menuDownload_GEMS)
        self.menuAndroid.setObjectName(_fromUtf8("menuAndroid"))
        self.menuIPhone = QtGui.QMenu(self.menuDownload_GEMS)
        self.menuIPhone.setObjectName(_fromUtf8("menuIPhone"))
        self.menuUtility = QtGui.QMenu(self.menubar)
        self.menuUtility.setObjectName(_fromUtf8("menuUtility"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionMalaysia = QtGui.QAction(MainWindow)
        self.actionMalaysia.setObjectName(_fromUtf8("actionMalaysia"))
        self.actionSingapore = QtGui.QAction(MainWindow)
        self.actionSingapore.setObjectName(_fromUtf8("actionSingapore"))
        self.actionIndonesia = QtGui.QAction(MainWindow)
        self.actionIndonesia.setObjectName(_fromUtf8("actionIndonesia"))
        self.actionThailand = QtGui.QAction(MainWindow)
        self.actionThailand.setObjectName(_fromUtf8("actionThailand"))
        self.actionLogin = QtGui.QAction(MainWindow)
        self.actionLogin.setObjectName(_fromUtf8("actionLogin"))
        self.actionReset = QtGui.QAction(MainWindow)
        self.actionReset.setObjectName(_fromUtf8("actionReset"))
        self.actionUpload_Data = QtGui.QAction(MainWindow)
        self.actionUpload_Data.setObjectName(_fromUtf8("actionUpload_Data"))
        self.actionUnited_States = QtGui.QAction(MainWindow)
        self.actionUnited_States.setObjectName(_fromUtf8("actionUnited_States"))
        self.actionUnited_Kingdom = QtGui.QAction(MainWindow)
        self.actionUnited_Kingdom.setObjectName(_fromUtf8("actionUnited_Kingdom"))
        self.actionJapan = QtGui.QAction(MainWindow)
        self.actionJapan.setObjectName(_fromUtf8("actionJapan"))
        self.actionPhiliphines = QtGui.QAction(MainWindow)
        self.actionPhiliphines.setObjectName(_fromUtf8("actionPhiliphines"))
        self.actionIreland = QtGui.QAction(MainWindow)
        self.actionIreland.setObjectName(_fromUtf8("actionIreland"))
        self.actionAustralia = QtGui.QAction(MainWindow)
        self.actionAustralia.setObjectName(_fromUtf8("actionAustralia"))
        self.actionWindows_8_Mobile = QtGui.QAction(MainWindow)
        self.actionWindows_8_Mobile.setObjectName(_fromUtf8("actionWindows_8_Mobile"))
        self.actionSamsung = QtGui.QAction(MainWindow)
        self.actionSamsung.setObjectName(_fromUtf8("actionSamsung"))
        self.actionWindows_8_Desktop = QtGui.QAction(MainWindow)
        self.actionWindows_8_Desktop.setObjectName(_fromUtf8("actionWindows_8_Desktop"))
        self.actionWindows_10 = QtGui.QAction(MainWindow)
        self.actionWindows_10.setObjectName(_fromUtf8("actionWindows_10"))
        self.actionSamsung_2 = QtGui.QAction(MainWindow)
        self.actionSamsung_2.setObjectName(_fromUtf8("actionSamsung_2"))
        self.actionLatest_Version_2 = QtGui.QAction(MainWindow)
        self.actionLatest_Version_2.setObjectName(_fromUtf8("actionLatest_Version_2"))
        self.actionPrevious_Version = QtGui.QAction(MainWindow)
        self.actionPrevious_Version.setObjectName(_fromUtf8("actionPrevious_Version"))
        self.actionLatest_Version = QtGui.QAction(MainWindow)
        self.actionLatest_Version.setObjectName(_fromUtf8("actionLatest_Version"))
        self.actionPrevious_Version_2 = QtGui.QAction(MainWindow)
        self.actionPrevious_Version_2.setObjectName(_fromUtf8("actionPrevious_Version_2"))
        self.actionFtp = QtGui.QAction(MainWindow)
        self.actionFtp.setObjectName(_fromUtf8("actionFtp"))
        self.actionWeb = QtGui.QAction(MainWindow)
        self.actionWeb.setObjectName(_fromUtf8("actionWeb"))
        self.actionLoad = QtGui.QAction(MainWindow)
        self.actionLoad.setObjectName(_fromUtf8("actionLoad"))
        self.actionEnergy = QtGui.QAction(MainWindow)
        self.actionEnergy.setObjectName(_fromUtf8("actionEnergy"))
        self.actionWater = QtGui.QAction(MainWindow)
        self.actionWater.setObjectName(_fromUtf8("actionWater"))
        self.actionServer = QtGui.QAction(MainWindow)
        self.actionServer.setObjectName(_fromUtf8("actionServer"))
        self.menuCore.addAction(self.actionLogin)
        self.menuCore.addAction(self.actionReset)
        self.menuCore.addAction(self.actionUpload_Data)
        self.menuCountry.addAction(self.actionLoad)
        self.menuAndroid.addAction(self.actionLatest_Version_2)
        self.menuAndroid.addAction(self.actionPrevious_Version)
        self.menuIPhone.addAction(self.actionLatest_Version)
        self.menuIPhone.addAction(self.actionPrevious_Version_2)
        self.menuDownload_GEMS.addAction(self.menuAndroid.menuAction())
        self.menuDownload_GEMS.addAction(self.menuIPhone.menuAction())
        self.menuDownload_GEMS.addAction(self.actionWindows_8_Mobile)
        self.menuDownload_GEMS.addAction(self.actionWindows_8_Desktop)
        self.menuDownload_GEMS.addAction(self.actionWindows_10)
        self.menuDownload_GEMS.addAction(self.actionSamsung_2)
        self.menuDownload_GEMS.addAction(self.actionServer)
        self.menuUtility.addAction(self.actionEnergy)
        self.menuUtility.addAction(self.actionWater)
        self.menubar.addAction(self.menuCore.menuAction())
        self.menubar.addAction(self.menuCountry.menuAction())
        self.menubar.addAction(self.menuDownload_GEMS.menuAction())
        self.menubar.addAction(self.menuUtility.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "GEMS by GENiBOX", "GENiBOX Energy Monitoring System"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Sans Typewriter\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">Malaysia - </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400;\">Johor Bahru 80350</span></p></body></html>", None))
        self.menuCore.setTitle(_translate("MainWindow", "CoreMain", None))
        self.menuCountry.setTitle(_translate("MainWindow", "Country", None))
        self.menuDownload_GEMS.setTitle(_translate("MainWindow", "Download", None))
        self.menuAndroid.setTitle(_translate("MainWindow", "Android", None))
        self.menuIPhone.setTitle(_translate("MainWindow", "iPhone", None))
        self.menuUtility.setTitle(_translate("MainWindow", "Utility", None))
        self.actionMalaysia.setText(_translate("MainWindow", "Malaysia", None))
        self.actionSingapore.setText(_translate("MainWindow", "Singapore", None))
        self.actionIndonesia.setText(_translate("MainWindow", "Indonesia", None))
        self.actionThailand.setText(_translate("MainWindow", "Thailand", None))
        self.actionLogin.setText(_translate("MainWindow", "Login", None))
        self.actionReset.setText(_translate("MainWindow", "Reset", None))
        self.actionUpload_Data.setText(_translate("MainWindow", "Upload Data", None))
        self.actionUnited_States.setText(_translate("MainWindow", "United States", None))
        self.actionUnited_Kingdom.setText(_translate("MainWindow", "United Kingdom", None))
        self.actionJapan.setText(_translate("MainWindow", "Japan", None))
        self.actionPhiliphines.setText(_translate("MainWindow", "Philipines", None))
        self.actionIreland.setText(_translate("MainWindow", "Ireland", None))
        self.actionAustralia.setText(_translate("MainWindow", "Australia", None))
        self.actionWindows_8_Mobile.setText(_translate("MainWindow", "Windows 8 Mobile", None))
        self.actionSamsung.setText(_translate("MainWindow", "Samsung", None))
        self.actionWindows_8_Desktop.setText(_translate("MainWindow", "Windows 8 Desktop", None))
        self.actionWindows_10.setText(_translate("MainWindow", "Windows 10", None))
        self.actionSamsung_2.setText(_translate("MainWindow", "Samsung", None))
        self.actionLatest_Version_2.setText(_translate("MainWindow", "Latest Version", None))
        self.actionPrevious_Version.setText(_translate("MainWindow", "Previous Version", None))
        self.actionLatest_Version.setText(_translate("MainWindow", "Latest Version", None))
        self.actionPrevious_Version_2.setText(_translate("MainWindow", "Previous Version", None))
        self.actionFtp.setText(_translate("MainWindow", "Ftp", None))
        self.actionWeb.setText(_translate("MainWindow", "Web Login", None))
        self.actionLoad.setText(_translate("MainWindow", "Load", None))
        self.actionEnergy.setText(_translate("MainWindow", "Energy", None))
        self.actionWater.setText(_translate("MainWindow", "Water", None))
        self.actionServer.setText(_translate("MainWindow", "Server", None))

from PyQt4 import QtWebKit

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)

        self.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

