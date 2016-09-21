# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gems_webbrowse.ui'
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
        MainWindow.resize(1202, 700)
        MainWindow.setMouseTracking(True)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setProperty("WebTemp", QtCore.QUrl(_fromUtf8("http://openstreetmap.org")))
        self.Form = QtGui.QWidget(MainWindow)
        self.Form.setObjectName(_fromUtf8("Form"))
        self.frame = QtGui.QFrame(self.Form)
        self.frame.setGeometry(QtCore.QRect(0, 10, 1201, 651))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.webView = QtWebKit.QWebView(self.frame)
        self.webView.setGeometry(QtCore.QRect(430, 80, 431, 201))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("http://www.solrenview.com/cgi-bin/cgihandler.cgi?&view=0,0,247,0&cond=site_ID=591&mode=2&pvi_IDs=1092,1093,1709%27,%27gwin%27,2.0")))
        self.webView.setRenderHints(QtGui.QPainter.HighQualityAntialiasing|QtGui.QPainter.SmoothPixmapTransform|QtGui.QPainter.TextAntialiasing)
        self.webView.setObjectName(_fromUtf8("webView"))
        self.webView_2 = QtWebKit.QWebView(self.frame)
        self.webView_2.setGeometry(QtCore.QRect(420, 280, 441, 191))
        self.webView_2.setUrl(QtCore.QUrl(_fromUtf8("http://www.solrenview.com/cgi-bin/cgihandler.cgi?&view=0,0,247,0&cond=site_ID=591&mode=2&pvi_IDs=1450,1088%27,%27gwin%27,2.0")))
        self.webView_2.setObjectName(_fromUtf8("webView_2"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(230, 40, 531, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.textEdit = QtGui.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(40, 80, 391, 461))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit_2 = QtGui.QTextEdit(self.frame)
        self.textEdit_2.setGeometry(QtCore.QRect(430, 470, 431, 171))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        MainWindow.setCentralWidget(self.Form)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1202, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuCore = QtGui.QMenu(self.menubar)
        self.menuCore.setObjectName(_fromUtf8("menuCore"))
        self.menuCountry = QtGui.QMenu(self.menubar)
        self.menuCountry.setObjectName(_fromUtf8("menuCountry"))
        self.menuDownload = QtGui.QMenu(self.menubar)
        self.menuDownload.setObjectName(_fromUtf8("menuDownload"))
        self.menuAndroid = QtGui.QMenu(self.menuDownload)
        self.menuAndroid.setObjectName(_fromUtf8("menuAndroid"))
        self.menuIPhone = QtGui.QMenu(self.menuDownload)
        self.menuIPhone.setObjectName(_fromUtf8("menuIPhone"))
        self.menuUtility = QtGui.QMenu(self.menubar)
        self.menuUtility.setObjectName(_fromUtf8("menuUtility"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionLogin = QtGui.QAction(MainWindow)
        self.actionLogin.setMenuRole(QtGui.QAction.PreferencesRole)
        self.actionLogin.setSoftKeyRole(QtGui.QAction.PositiveSoftKey)
        self.actionLogin.setObjectName(_fromUtf8("actionLogin"))
        self.actionReset = QtGui.QAction(MainWindow)
        self.actionReset.setObjectName(_fromUtf8("actionReset"))
        self.actionUpload_Data = QtGui.QAction(MainWindow)
        self.actionUpload_Data.setObjectName(_fromUtf8("actionUpload_Data"))
        self.actionWindows_8_Mobile = QtGui.QAction(MainWindow)
        self.actionWindows_8_Mobile.setObjectName(_fromUtf8("actionWindows_8_Mobile"))
        self.actionWindows_8_Desktop = QtGui.QAction(MainWindow)
        self.actionWindows_8_Desktop.setObjectName(_fromUtf8("actionWindows_8_Desktop"))
        self.actionWindows_10 = QtGui.QAction(MainWindow)
        self.actionWindows_10.setObjectName(_fromUtf8("actionWindows_10"))
        self.actionSamsung_2 = QtGui.QAction(MainWindow)
        self.actionSamsung_2.setObjectName(_fromUtf8("actionSamsung_2"))
        self.actionLatest_Version = QtGui.QAction(MainWindow)
        self.actionLatest_Version.setObjectName(_fromUtf8("actionLatest_Version"))
        self.actionPrevious_Version = QtGui.QAction(MainWindow)
        self.actionPrevious_Version.setObjectName(_fromUtf8("actionPrevious_Version"))
        self.actionLatest_Version_2 = QtGui.QAction(MainWindow)
        self.actionLatest_Version_2.setObjectName(_fromUtf8("actionLatest_Version_2"))
        self.actionPrevious_Version_2 = QtGui.QAction(MainWindow)
        self.actionPrevious_Version_2.setObjectName(_fromUtf8("actionPrevious_Version_2"))
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
        self.menuAndroid.addAction(self.actionLatest_Version)
        self.menuAndroid.addAction(self.actionPrevious_Version)
        self.menuIPhone.addAction(self.actionLatest_Version_2)
        self.menuIPhone.addAction(self.actionPrevious_Version_2)
        self.menuDownload.addAction(self.menuAndroid.menuAction())
        self.menuDownload.addAction(self.menuIPhone.menuAction())
        self.menuDownload.addAction(self.actionWindows_8_Mobile)
        self.menuDownload.addAction(self.actionWindows_8_Desktop)
        self.menuDownload.addAction(self.actionWindows_10)
        self.menuDownload.addAction(self.actionSamsung_2)
        self.menuDownload.addAction(self.actionServer)
        self.menuUtility.addAction(self.actionEnergy)
        self.menuUtility.addAction(self.actionWater)
        self.menubar.addAction(self.menuCore.menuAction())
        self.menubar.addAction(self.menuCountry.menuAction())
        self.menubar.addAction(self.menuDownload.menuAction())
        self.menubar.addAction(self.menuUtility.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "GEMS by GENiBOX", "GENiBOX Energy Monitoring System"))
        self.label.setText(_translate("MainWindow", "Waubay - Sand Lake Drive. Columbia, SD 57433, United States of America", None))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" width=\"48%\" cellspacing=\"2\" cellpadding=\"0\" bgcolor=\"#ffffff\">\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"site_info_tip\"></a><span style=\" font-family:\'Arial\'; font-size:8pt; font-weight:600;\">S</span><span style=\" font-family:\'Arial\'; font-size:8pt; font-weight:600;\">ystem Info</span></p></td>\n"
"<td colspan=\"3\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt;\"> </span></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt; font-weight:600;\">Location</span></p></td>\n"
"<td colspan=\"3\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt;\">Sand Lake Drive., Columbia, SD 57433</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt; font-weight:600;\">Monitoring Started</span></p></td>\n"
"<td colspan=\"3\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt;\">Wed Mar 9, 2011</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt; font-weight:600;\">Installer</span></p></td>\n"
"<td colspan=\"3\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt;\">CEI</span></p></td></tr>\n"
"<tr>\n"
"<td colspan=\"4\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt;\"> </span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f0f0f0\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt; font-weight:600; background-color:#f0f0f0;\">Inverter Models</span></p></td>\n"
"<td bgcolor=\"#f0f0f0\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt; font-weight:600; background-color:#f0f0f0;\">Inverter WAC</span></p></td>\n"
"<td bgcolor=\"#f0f0f0\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt; font-weight:600; background-color:#f0f0f0;\">Qty.</span></p></td>\n"
"<td bgcolor=\"#f0f0f0\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt; font-weight:600; background-color:#f0f0f0;\">Total Capacity (WAC)</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt;\">Solectria PVI 5300</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt;\">5300</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt;\">3</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt;\">15900</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt;\">Solectria PVI 3000</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt;\">3000</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt;\">2</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt;\">6000</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f0f0f0\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt; font-weight:600; background-color:#f0f0f0;\">Solar Modules</span></p></td>\n"
"<td bgcolor=\"#f0f0f0\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt; font-weight:600; background-color:#f0f0f0;\">Module WDC</span></p></td>\n"
"<td bgcolor=\"#f0f0f0\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt; font-weight:600; background-color:#f0f0f0;\">Qty.</span></p></td>\n"
"<td bgcolor=\"#f0f0f0\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt; font-weight:600; background-color:#f0f0f0;\">Total Capacity (WDC)</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt;\">Sharp 240</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt;\">240</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt;\">85</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt;\">20400</span></p></td></tr></table></body></html>", None))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" align=\"center\" width=\"350\" cellspacing=\"2\" cellpadding=\"0\" bgcolor=\"#ffffff\">\n"
"<tr>\n"
"<td colspan=\"3\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt; font-weight:600; color:#a52a2a;\">Online</span><span style=\" font-family:\'Arial\'; font-size:8pt; color:#a52a2a;\"> </span><span style=\" font-family:\'Arial\'; font-size:8pt; font-style:italic; color:#a52a2a;\">[ last update: </span><span style=\" font-family:\'Arial\'; font-size:8pt; font-weight:600; font-style:italic; color:#a52a2a;\">Wed Sep 21, 2016 5:28 pm CDT</span><span style=\" font-family:\'Arial\'; font-size:8pt; font-style:italic; color:#a52a2a;\"> ]</span></p></td>\n"
"<td></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt; font-weight:600; font-style:italic; color:#4b4b4b;\"> System Status,  Inverter-Direct :</span></p></td>\n"
"<td colspan=\"2\" bgcolor=\"#00ff00\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"StatusBox\"></a><span style=\" font-family:\'Arial\'; font-size:8pt; font-weight:600;\">A</span><span style=\" font-family:\'Arial\'; font-size:8pt; font-weight:600;\">ctive</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt;\"> </span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt;\"> </span><span style=\" font-family:\'Arial\'; font-size:8pt; font-weight:600; font-style:italic; color:#4b4b4b;\">Energy Generated Today:</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt; font-weight:600;\">53</span></p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt;\">kWh</span></p></td>\n"
"<td></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt;\"> </span><span style=\" font-family:\'Arial\'; font-size:8pt; font-weight:600; font-style:italic; color:#4b4b4b;\">Lifetime Energy Generated:</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt; font-weight:600;\">180180</span></p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt;\">kWh</span></p></td>\n"
"<td></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt; font-weight:600; font-style:italic; color:#4b4b4b;\"> Lifetime CO</span><span style=\" font-family:\'Arial\'; font-size:8pt; font-weight:600; font-style:italic; color:#4b4b4b; vertical-align:sub;\">2</span><span style=\" font-family:\'Arial\'; font-size:8pt; font-weight:600; font-style:italic; color:#4b4b4b;\"> Emission Offset:</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt; font-weight:600;\">225225</span></p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt;\">lbs</span></p></td>\n"
"<td></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt; font-weight:600; font-style:italic; color:#4b4b4b;\"> System AC Power Now:</span></p></td>\n"
"<td>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt; font-weight:600;\">877</span></p></td>\n"
"<td>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:8pt;\">W</span></p></td>\n"
"<td></td></tr></table></body></html>", None))
        self.menuCore.setTitle(_translate("MainWindow", "CoreMain", None))
        self.menuCountry.setTitle(_translate("MainWindow", "Country", None))
        self.menuDownload.setTitle(_translate("MainWindow", "Download", None))
        self.menuAndroid.setTitle(_translate("MainWindow", "Android", None))
        self.menuIPhone.setTitle(_translate("MainWindow", "iPhone", None))
        self.menuUtility.setTitle(_translate("MainWindow", "Utility", None))
        self.actionLogin.setText(_translate("MainWindow", "Login", None))
        self.actionReset.setText(_translate("MainWindow", "Reset", None))
        self.actionUpload_Data.setText(_translate("MainWindow", "Upload Data", None))
        self.actionWindows_8_Mobile.setText(_translate("MainWindow", "Windows 8 Mobile", None))
        self.actionWindows_8_Desktop.setText(_translate("MainWindow", "Windows 8 Desktop", None))
        self.actionWindows_10.setText(_translate("MainWindow", "Windows 10", None))
        self.actionSamsung_2.setText(_translate("MainWindow", "Samsung", None))
        self.actionLatest_Version.setText(_translate("MainWindow", "Latest Version", None))
        self.actionLatest_Version.setToolTip(_translate("MainWindow", "Latest Version", None))
        self.actionPrevious_Version.setText(_translate("MainWindow", "Previous Version", None))
        self.actionLatest_Version_2.setText(_translate("MainWindow", "Latest Version", None))
        self.actionPrevious_Version_2.setText(_translate("MainWindow", "Previous Version", None))
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

