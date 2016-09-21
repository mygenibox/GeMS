#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2010 Hans-Peter Jansen <hpj@urpla.net>.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:LGPL$
## Commercial Usage
## Licensees holding valid Qt Commercial licenses may use this file in
## accordance with the Qt Commercial License Agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and Nokia.
##
## GNU Lesser General Public License Usage
## Alternatively, this file may be used under the terms of the GNU Lesser
## General Public License version 2.1 as published by the Free Software
## Foundation and appearing in the file LICENSE.LGPL included in the
## packaging of this file.  Please review the following information to
## ensure the GNU Lesser General Public License version 2.1 requirements
## will be met: http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
##
## In addition, as a special exception, Nokia gives you certain additional
## rights.  These rights are described in the Nokia Qt LGPL Exception
## version 1.1, included in the file LGPL_EXCEPTION.txt in this package.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 3.0 as published by the Free Software
## Foundation and appearing in the file LICENSE.GPL included in the
## packaging of this file.  Please review the following information to
## ensure the GNU General Public License version 3.0 requirements will be
## met: http://www.gnu.org/copyleft/gpl.html.
##
## If you have questions regarding the use of this file, please contact
## Nokia at qt-info@nokia.com.
## $QT_END_LICENSE$
##
#############################################################################

#For GeMS User Interface sample here we use Lightmaps

import sip
sip.setapi('QVariant', 2)

import sys
import math

from PyQt4 import QtCore, QtGui, QtNetwork


WINCE = sys.platform.startswith('wince')
SYMBIAN = sys.platform.startswith('symbian')
X11 = hasattr(QtGui.QApplication, 'x11EventFilter')

HOLD_TIME = 701

MAX_MAGNIFIER = 229

TDIM = 256


class Point(QtCore.QPoint):
    """QPoint, that is fully qualified as a dict key"""
    def __init__(self, *par):
        if par:
            super(Point, self).__init__(*par)
        else:
            super(Point, self).__init__()

    def __hash__(self):
        return self.x() * 17 ^ self.y()

    def __repr__(self):
        return "Point(%s, %s)" % (self.x(), self.y())


def tileForCoordinate(lat, lng, zoom):
    zn = float(1 << zoom)
    tx = float(lng + 180.0) / 360.0
    ty = (1.0 - math.log(math.tan(lat * math.pi / 180.0) +
          1.0 / math.cos(lat * math.pi / 180.0)) / math.pi) / 2.0

    return QtCore.QPointF(tx * zn, ty * zn)


def longitudeFromTile(tx, zoom):
    zn = float(1 << zoom)
    lat = tx / zn * 360.0 - 180.0

    return lat


def latitudeFromTile(ty, zoom):
    zn = float(1 << zoom)
    n = math.pi - 2 * math.pi * ty / zn
    lng = 180.0 / math.pi * math.atan(0.5 * (math.exp(n) - math.exp(-n)))

    return lng


class SlippyMap(QtCore.QObject):

    updated = QtCore.pyqtSignal(QtCore.QRect)

    def __init__(self, parent=None):
        super(SlippyMap, self).__init__(parent)

        self._offset = QtCore.QPoint()
        self._tilesRect = QtCore.QRect()
        self._tilePixmaps = {} # Point(x, y) to QPixmap mapping
        self._manager = QtNetwork.QNetworkAccessManager()
        self._url = QtCore.QUrl()
        # public vars
        self.width = 400
        self.height = 300
        self.zoom = 15
        self.latitude = 59.9138204
        self.longitude = 10.7387413

        self._emptyTile = QtGui.QPixmap(TDIM, TDIM)
        self._emptyTile.fill(QtCore.Qt.lightGray)

        cache = QtNetwork.QNetworkDiskCache()
        cache.setCacheDirectory(
            QtGui.QDesktopServices.storageLocation
                (QtGui.QDesktopServices.CacheLocation))
        self._manager.setCache(cache)
        self._manager.finished.connect(self.handleNetworkData)

    def invalidate(self):
        if self.width <= 0 or self.height <= 0:
            return

        ct = tileForCoordinate(self.latitude, self.longitude, self.zoom)
        tx = ct.x()
        ty = ct.y()

        # top-left corner of the center tile
        xp = int(self.width / 2 - (tx - math.floor(tx)) * TDIM)
        yp = int(self.height / 2 - (ty - math.floor(ty)) * TDIM)

        # first tile vertical and horizontal
        xa = (xp + TDIM - 1) / TDIM
        ya = (yp + TDIM - 1) / TDIM
        xs = int(tx) - xa
        ys = int(ty) - ya

        # offset for top-left tile
        self._offset = QtCore.QPoint(xp - xa * TDIM, yp - ya * TDIM)

        # last tile vertical and horizontal
        xe = int(tx) + (self.width - xp - 1) / TDIM
        ye = int(ty) + (self.height - yp - 1) / TDIM

        # build a rect
        self._tilesRect = QtCore.QRect(xs, ys, xe - xs + 1, ye - ys + 1)

        if self._url.isEmpty():
            self.download()

        self.updated.emit(QtCore.QRect(0, 0, self.width, self.height))

    def render(self, p, rect):
        for x in range(self._tilesRect.width()):
            for y in range(self._tilesRect.height()):
                tp = Point(x + self._tilesRect.left(), y + self._tilesRect.top())
                box = QtCore.QRect(self.tileRect(tp))
                if rect.intersects(box):
                    p.drawPixmap(box, self._tilePixmaps.get(tp, self._emptyTile))
   
    def pan(self, delta):
        dx = QtCore.QPointF(delta) / float(TDIM)
        center = tileForCoordinate(self.latitude, self.longitude, self.zoom) - dx
        self.latitude = latitudeFromTile(center.y(), self.zoom)
        self.longitude = longitudeFromTile(center.x(), self.zoom)
        self.invalidate()

    # slots
    def handleNetworkData(self, reply):
        img = QtGui.QImage()
        tp = Point(reply.request().attribute(QtNetwork.QNetworkRequest.User))
        url = reply.url()
        if not reply.error():
            if img.load(reply, None):
                self._tilePixmaps[tp] = QtGui.QPixmap.fromImage(img)
        reply.deleteLater()
        self.updated.emit(self.tileRect(tp))

        # purge unused tiles
        bound = self._tilesRect.adjusted(-2, -2, 2, 2)
        for tp in list(self._tilePixmaps.keys()):
            if not bound.contains(tp):
                del self._tilePixmaps[tp]
        self.download()

    def download(self):
        grab = None
        for x in range(self._tilesRect.width()):
            for y in range(self._tilesRect.height()):
                tp = Point(self._tilesRect.topLeft() + QtCore.QPoint(x, y))
                if tp not in self._tilePixmaps:
                    grab = QtCore.QPoint(tp)
                    break

        if grab is None:
            self._url = QtCore.QUrl()
            return

        path = 'http://tile.openstreetmap.org/%d/%d/%d.png' % (self.zoom, grab.x(), grab.y())
        self._url = QtCore.QUrl(path)
        request = QtNetwork.QNetworkRequest()
        request.setUrl(self._url)
        request.setRawHeader('User-Agent', 'Nokia (PyQt) Graphics Dojo 1.0')
        request.setAttribute(QtNetwork.QNetworkRequest.User, grab)
        self._manager.get(request)

    def tileRect(self, tp):
        t = tp - self._tilesRect.topLeft()
        x = t.x() * TDIM + self._offset.x()
        y = t.y() * TDIM + self._offset.y()

        return QtCore.QRect(x, y, TDIM, TDIM)


class LightMaps(QtGui.QWidget):
    def __init__(self, parent = None):
        super(LightMaps, self).__init__(parent)

        self.pressed = False
        self.snapped = False
        self.zoomed = False
        self.invert = False
        self._normalMap = SlippyMap(self)
        self._largeMap = SlippyMap(self)
        self.pressPos = QtCore.QPoint()
        self.dragPos = QtCore.QPoint()
        self.tapTimer = QtCore.QBasicTimer()
        self.zoomPixmap = QtGui.QPixmap()
        self.maskPixmap = QtGui.QPixmap()
        self._normalMap.updated.connect(self.updateMap)
        self._largeMap.updated.connect(self.update)
 
    def setCenter(self, lat, lng):
        self._normalMap.latitude = lat
        self._normalMap.longitude = lng
        self._normalMap.invalidate()
        self._largeMap.invalidate()

    # slots
    def toggleNightMode(self):
        self.invert = not self.invert
        self.update()
 
    def updateMap(self, r):
        self.update(r)

    def activateZoom(self):
        self.zoomed = True
        self.tapTimer.stop()
        self._largeMap.zoom = self._normalMap.zoom + 1
        self._largeMap.width = self._normalMap.width * 2
        self._largeMap.height = self._normalMap.height * 2
        self._largeMap.latitude = self._normalMap.latitude
        self._largeMap.longitude = self._normalMap.longitude
        self._largeMap.invalidate()
        self.update()
 
    def resizeEvent(self, event):
        self._normalMap.width = self.width()
        self._normalMap.height = self.height()
        self._normalMap.invalidate()
        self._largeMap.width = self._normalMap.width * 2
        self._largeMap.height = self._normalMap.height * 2
        self._largeMap.invalidate()

    def paintEvent(self, event):
        p = QtGui.QPainter()
        p.begin(self)
        self._normalMap.render(p, event.rect())
        p.setPen(QtCore.Qt.black)

        if SYMBIAN:
            font = p.font()
            font.setPixelSize(13)
            p.setFont(font)

        p.drawText(self.rect(), QtCore.Qt.AlignBottom | QtCore.Qt.TextWordWrap,
                   "Map Loading...")
        p.end()

        if self.zoomed:
            dim = min(self.width(), self.height())
            magnifierSize = min(MAX_MAGNIFIER, dim * 2 / 3)
            radius = magnifierSize / 2
            ring = radius - 15
            box = QtCore.QSize(magnifierSize, magnifierSize)

            # reupdate our mask
            if self.maskPixmap.size() != box:
                self.maskPixmap = QtGui.QPixmap(box)
                self.maskPixmap.fill(QtCore.Qt.transparent)
                g = QtGui.QRadialGradient()
                g.setCenter(radius, radius)
                g.setFocalPoint(radius, radius)
                g.setRadius(radius)
                g.setColorAt(1.0, QtGui.QColor(255, 255, 255, 0))
                g.setColorAt(0.5, QtGui.QColor(128, 128, 128, 255))
                mask = QtGui.QPainter(self.maskPixmap)
                mask.setRenderHint(QtGui.QPainter.Antialiasing)
                mask.setCompositionMode(QtGui.QPainter.CompositionMode_Source)
                mask.setBrush(g)
                mask.setPen(QtCore.Qt.NoPen)
                mask.drawRect(self.maskPixmap.rect())
                mask.setBrush(QtGui.QColor(QtCore.Qt.transparent))
                mask.drawEllipse(g.center(), ring, ring)
                mask.end()

            center = self.dragPos - QtCore.QPoint(0, radius)
            center += QtCore.QPoint(0, radius / 2)
            corner = center - QtCore.QPoint(radius, radius)
            xy = center * 2 - QtCore.QPoint(radius, radius)
            # only set the dimension to the magnified portion
            if self.zoomPixmap.size() != box:
                self.zoomPixmap = QtGui.QPixmap(box)
                self.zoomPixmap.fill(QtCore.Qt.lightGray)
    
            if True:
                p = QtGui.QPainter(self.zoomPixmap)
                p.translate(-xy)
                self._largeMap.render(p, QtCore.QRect(xy, box))
                p.end()

            clipPath = QtGui.QPainterPath()
            clipPath.addEllipse(QtCore.QPointF(center), ring, ring)
            p = QtGui.QPainter(self)
            p.setRenderHint(QtGui.QPainter.Antialiasing)
            p.setClipPath(clipPath)
            p.drawPixmap(corner, self.zoomPixmap)
            p.setClipping(False)
            p.drawPixmap(corner, self.maskPixmap)
            p.setPen(QtCore.Qt.gray)
            p.drawPath(clipPath)

        if self.invert:
            p = QtGui.QPainter(self)
            p.setCompositionMode(QtGui.QPainter.CompositionMode_Difference)
            p.fillRect(event.rect(), QtCore.Qt.white)
            p.end()

    def timerEvent(self, event):
        if not self.zoomed:
            self.activateZoom()

        self.update()
 
    def mousePressEvent(self, event):
        if event.buttons() != QtCore.Qt.LeftButton:
            return

        self.pressed = self.snapped = True
        self.pressPos = self.dragPos = event.pos()
        self.tapTimer.stop()
        self.tapTimer.start(HOLD_TIME, self)

    def mouseMoveEvent(self, event):
        if not event.buttons():
            return

        if not self.zoomed:
            if not self.pressed or not self.snapped:
                delta = event.pos() - self.pressPos
                self.pressPos = event.pos()
                self._normalMap.pan(delta)
                return
            else:
                threshold = 10
                delta = event.pos() - self.pressPos
                if self.snapped:
                    self.snapped &= delta.x() < threshold
                    self.snapped &= delta.y() < threshold
                    self.snapped &= delta.x() > -threshold
                    self.snapped &= delta.y() > -threshold

                if not self.snapped:
                    self.tapTimer.stop()

        else:
            self.dragPos = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        self.zoomed = False
        self.update()
 
    def keyPressEvent(self, event):
        if not self.zoomed:
            if event.key() == QtCore.Qt.Key_Left:
                self._normalMap.pan(QtCore.QPoint(20, 0))
            if event.key() == QtCore.Qt.Key_Right:
                self._normalMap.pan(QtCore.QPoint(-20, 0))
            if event.key() == QtCore.Qt.Key_Up:
                self._normalMap.pan(QtCore.QPoint(0, 20))
            if event.key() == QtCore.Qt.Key_Down:
                self._normalMap.pan(QtCore.QPoint(0, -20))
            if event.key() == QtCore.Qt.Key_Z or event.key() == QtCore.Qt.Key_Select:
                self.dragPos = QtCore.QPoint(self.width() / 2, self.height() / 2)
                self.activateZoom()
        else:
            if event.key() == QtCore.Qt.Key_Z or event.key() == QtCore.Qt.Key_Select:
                self.zoomed = False
                self.update()

            delta = QtCore.QPoint(0, 0)
            if event.key() == QtCore.Qt.Key_Left:
                delta = QtCore.QPoint(-15, 0)
            if event.key() == QtCore.Qt.Key_Right:
                delta = QtCore.QPoint(15, 0)
            if event.key() == QtCore.Qt.Key_Up:
                delta = QtCore.QPoint(0, -15)
            if event.key() == QtCore.Qt.Key_Down:
                delta = QtCore.QPoint(0, 15)
            if delta != QtCore.QPoint(0, 0):
                self.dragPos += delta
                self.update()


class MapZoom(QtGui.QMainWindow):
    def __init__(self):
        super(MapZoom, self).__init__(None)

        self.map_ = LightMaps(self)
        self.setCentralWidget(self.map_)
        self.map_.setFocus()
        self.africaAction = QtGui.QAction("&Africa", self)
        self.australiaAction = QtGui.QAction("&Australia", self)
        self.bruneiAction = QtGui.QAction("&Brunei", self)
        self.canadaAction = QtGui.QAction("&Canada", self)
        self.chinaAction = QtGui.QAction("&China", self)
        self.denmarkAction = QtGui.QAction("&Denmark", self)
        self.franceAction = QtGui.QAction("&France", self)
        self.germanyAction = QtGui.QAction("&Germany", self)
        self.ghanaAction = QtGui.QAction("&Ghana", self)
        self.indiaAction = QtGui.QAction("&India", self)
        self.indonesiaAction = QtGui.QAction("&Indonesia", self)
        self.irelandAction = QtGui.QAction("&Ireland", self)
        self.malaysiaAction = QtGui.QAction("&Malaysia", self)
        self.myanmarAction = QtGui.QAction("&Myanmar", self)
        self.newzealandAction = QtGui.QAction("&New Zealand", self)
        self.philippinesAction = QtGui.QAction("&Philippines", self)
        self.russiaAction = QtGui.QAction("&Russia", self)
        self.singaporeAction = QtGui.QAction("&Singapore", self)
        self.switzerlandAction = QtGui.QAction("&Switzerland", self)
        self.taiwanAction = QtGui.QAction("&Taiwan", self)
        self.unitedKingdomAction = QtGui.QAction("&United Kingdom", self)
        self.unitedStatesAction = QtGui.QAction("&United States", self)
        self.vietnamAction = QtGui.QAction("&Vietnam", self)
        self.africaAction.triggered.connect(self.chooseAfrica)
        self.australiaAction.triggered.connect(self.chooseAustralia)
        self.bruneiAction.triggered.connect(self.chooseBrunei)
        self.canadaAction.triggered.connect(self.chooseCanada)
        self.chinaAction.triggered.connect(self.chooseChina)
        self.denmarkAction.triggered.connect(self.chooseDenmark)
        self.franceAction.triggered.connect(self.chooseFrance)
        self.germanyAction.triggered.connect(self.chooseGermany)
        self.ghanaAction.triggered.connect(self.chooseGhana)
        self.indiaAction.triggered.connect(self.chooseIndia)
        self.indonesiaAction.triggered.connect(self.chooseIndonesia)
        self.irelandAction.triggered.connect(self.chooseIreland)
        self.malaysiaAction.triggered.connect(self.chooseMalaysia)
        self.myanmarAction.triggered.connect(self.chooseMyanmar)
        self.newzealandAction.triggered.connect(self.chooseNewZealand)
        self.philippinesAction.triggered.connect(self.choosePhilippines)
        self.russiaAction.triggered.connect(self.chooseRussia)
        self.singaporeAction.triggered.connect(self.chooseSingapore)
        self.switzerlandAction.triggered.connect(self.chooseSwitzerland)
        self.taiwanAction.triggered.connect(self.chooseTaiwan)
        self.unitedKingdomAction.triggered.connect(self.chooseUnitedKingdom)
        self.unitedStatesAction.triggered.connect(self.chooseUnitedStates)
        self.vietnamAction.triggered.connect(self.chooseVietnam)
        self.loginAction = QtGui.QAction("&Login", self)
        self.resetAction = QtGui.QAction("&Reset", self)
        self.upload_dataAction = QtGui.QAction("&Upload Data", self)
        self.loadMapAction = QtGui.QAction("&Load Map", self)
        self.windows_8_mobileAction = QtGui.QAction("&Windows 8 Mobile", self)
        self.windows_8_desktopAction = QtGui.QAction("&Windows 8 Desktop", self)
        self.windows_10_mobileAction = QtGui.QAction("&Windows 10 Mobile", self)
        self.windows_10_desktopAction = QtGui.QAction("&Windows 10 Desktop", self)
        self.samsung_storeAction = QtGui.QAction("&Samsung Store", self)
        self.androidAction = QtGui.QAction("&Android", self)
        self.iPhoneAction = QtGui.QAction("&iPhone", self)
        self.solarOffGridAction = QtGui.QAction("&Solar Off Grid", self)
        self.solarGridTiedAction = QtGui.QAction("&Solar Grid Tied", self)
        self.waterAction = QtGui.QAction("&Water", self)

        if SYMBIAN or WINCE:
            self.menuBar().addAction(self.africaAction)
            self.menuBar().addAction(self.australiaAction)
            self.menuBar().addAction(self.bruneiAction)
            self.menuBar().addAction(self.canadaAction)
            self.menuBar().addAction(self.chinaAction)
            self.menuBar().addAction(self.denmarkAction)
            self.menuBar().addAction(self.franceAction)
            self.menuBar().addAction(self.germanyAction)
            self.menuBar().addAction(self.ghanaAction)
            self.menuBar().addAction(self.indiaAction)
            self.menuBar().addAction(self.indonesiaAction)
            self.menuBar().addAction(self.irelandAction)
            self.menuBar().addAction(self.malaysiaAction)
            self.menuBar().addAction(self.myanmarAction)
            self.menuBar().addAction(self.newzealandAction)
            self.menuBar().addAction(self.philippinesAction)
            self.menuBar().addAction(self.russiaAction)
            self.menuBar().addAction(self.singaporeAction)
            self.menuBar().addAction(self.switzerlandAction)
            self.menuBar().addAction(self.taiwanAction)
            self.menuBar().addAction(self.unitedKingdomAction)
            self.menuBar().addAction(self.unitedStatesAction)
            self.menuBar().addAction(self.vietnamAction)

        else:
            menu = self.menuBar().addMenu("&Country")
            menu.addAction(self.africaAction)
            menu.addAction(self.australiaAction)
            menu.addAction(self.bruneiAction)
            menu.addAction(self.canadaAction)
            menu.addAction(self.chinaAction)
            menu.addAction(self.denmarkAction)
            menu.addAction(self.franceAction)
            menu.addAction(self.germanyAction)
            menu.addAction(self.ghanaAction)
            menu.addAction(self.indiaAction)
            menu.addAction(self.indonesiaAction)
            menu.addAction(self.irelandAction)
            menu.addAction(self.malaysiaAction)
            menu.addAction(self.myanmarAction)
            menu.addAction(self.newzealandAction)
            menu.addAction(self.philippinesAction)
            menu.addAction(self.russiaAction)
            menu.addAction(self.singaporeAction)
            menu.addAction(self.switzerlandAction)
            menu.addAction(self.taiwanAction)
            menu.addAction(self.unitedKingdomAction)
            menu.addAction(self.unitedStatesAction)
            menu.addAction(self.vietnamAction)
            menu.addSeparator()
            menu = self.menuBar().addMenu("&Core")
            menu.addAction(self.loginAction)
            menu.addAction(self.resetAction)
            menu.addAction(self.upload_dataAction)
            menu = self.menuBar().addMenu("&Country")
            menu.addAction(self.loadMapAction)
            menu = self.menuBar().addMenu("&Download")
            menu.addAction(self.windows_8_mobileAction)
            menu.addAction(self.windows_8_desktopAction)
            menu.addAction(self.windows_10_mobileAction)
            menu.addAction(self.windows_10_desktopAction)
            menu.addAction(self.samsung_storeAction)
            menu.addAction(self.androidAction)
            menu.addAction(self.iPhoneAction)
            menu = self.menuBar().addMenu("&Utility")
            menu.addAction(self.solarOffGridAction)
            menu.addAction(self.solarGridTiedAction)
            menu.addAction(self.waterAction)
            
                        

        QtCore.QTimer.singleShot(0, self.delayedInit)
 
    # slots
    def delayedInit(self):
        if SYMBIAN:
            qt_SetDefaultIap()

    def chooseAfrica(self):
        self.map_.setCenter(59.9138204, 10.7387413)

    def chooseAustralia(self):
        self.map_.setCenter(59.9138204, 10.7387413)

    def chooseBrunei(self):
        self.map_.setCenter(52.52958999943302, 13.383053541183472)

    def chooseCanada(self):
        self.map_.setCenter(59.9138204, 10.7387413)

    def chooseChina(self):
        self.map_.setCenter(59.9138204, 10.7387413)

    def chooseDenmark(self):
        self.map_.setCenter(59.9138204, 10.7387413)

    def chooseFrance(self):
        self.map_.setCenter(59.9138204, 10.7387413)

    def chooseGermany(self):
        self.map_.setCenter(59.9138204, 10.7387413)

    def chooseGhana(self):
        self.map_.setCenter(59.9138204, 10.7387413)

    def chooseIndia(self):
        self.map_.setCenter(59.9138204, 10.7387413)

    def chooseIndonesia(self):
        self.map_.setCenter(-6.211544, 106.845172)

    def chooseIreland(self):
        self.map_.setCenter(59.9138204, 10.7387413)

    def chooseMalaysia(self):
        self.map_.setCenter(59.9138204, 10.7387413)
        
    def chooseMyanmar(self):
        self.map_.setCenter(59.9138204, 10.7387413)

    def chooseNewZealand(self):
        self.map_.setCenter(52.52958999943302, 13.383053541183472)

    def choosePhilippines(self):
        self.map_.setCenter(-6.211544, 106.845172)

    def chooseRussia(self):
        self.map_.setCenter(59.9138204, 10.7387413)

    def chooseSingapore(self):
        self.map_.setCenter(59.9138204, 10.7387413)

    def chooseSwitzerland(self):
        self.map_.setCenter(59.9138204, 10.7387413)

    def chooseTaiwan(self):
        self.map_.setCenter(59.9138204, 10.7387413)

    def chooseUnitedKingdom(self):
        self.map_.setCenter(59.9138204, 10.7387413)

    def chooseUnitedStates(self):
        self.map_.setCenter(59.9138204, 10.7387413)

    def chooseVietnam(self):
        self.map_.setCenter(59.9138204, 10.7387413)

if __name__ == '__main__':
    if X11:
        QtGui.QApplication.setGraphicsSystem('raster')

    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('LightMaps')
    w = MapZoom()
    w.setWindowTitle("GeMS by GENiBOX - powered by OpenStreetMap")

    if SYMBIAN or WINCE:
        w.showMaximized()
    else:
        w.resize(600, 450)

    w.show()
    sys.exit(app.exec_())
