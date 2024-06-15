from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QFont, QMouseEvent, QColor, QPixmap
from PyQt5 import QtCore, QtGui

class UIButton(QWidget):
    btn_width = 20
    btn_height = 20
    top_margin = 10
    side_margin = 10

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedSize(300, 300)  # 调整窗口大小
        self.outerPieRadius = 100

        self.mouseCenterView = False
        self.mouseBottomView = False
        self.mouseRightBottomView = False
        self.mouseRightView = False
        self.mouseUpRightView = False
        self.mouseTopView = False
        self.mouserightTopView = False
        self.mouseLeftView = False
        self.mousedownLeftView = False

        self.mouseOuterCream = False
        self.outerChampagnePercent = 90

        self.setMouseTracking(True)  # 设置鼠标自动跟踪

        # 添加主题切换按钮
        self.theme_button = QPushButton("切换主题", self)
        self.theme_button.setGeometry(10, 10, 80, 30)
        self.theme_button.clicked.connect(self.toggle_theme)

        self.light_theme = """
        QPushButton {
            background-color: lightgray;
            color: black;
        }
        """

        self.dark_theme = """
        QPushButton {
            background-color: darkgray;
            color: white;
        }
        """

        self.is_light_theme = True
        self.setStyleSheet(self.light_theme)

        self.clicked_button = None  # 用于跟踪被点击的按钮

    def toggle_theme(self):
        self.is_light_theme = not self.is_light_theme
        if self.is_light_theme:
            self.setStyleSheet(self.light_theme)
        else:
            self.setStyleSheet(self.dark_theme)

    def get_button_color(self, is_clicked):
        if self.is_light_theme:
            return Qt.darkGray if not is_clicked else Qt.red
        else:
            return Qt.black if not is_clicked else Qt.red

    def drawOuterPie(self, painter):
        painter.save()
        if self.mouseRightView:
            radius1 = self.outerPieRadius + 4
        else:
            radius1 = self.outerPieRadius

        rect = QtCore.QRectF(-radius1 / 2, -radius1 / 2, radius1, radius1)
        pathOuterChampagnePie = QtGui.QPainterPath()
        pathOuterChampagnePie.arcMoveTo(rect, -22.5)
        pathOuterChampagnePie.arcTo(rect, -22.5, 45)
        pathOuterChampagnePie.lineTo(0, 0)
        pathOuterChampagnePie.closeSubpath()
        # pathOuterChampagnePie.addText(radius1 / 2 - 20, 5, painter.font(), "2")
        radius = 50
        rect1 = QtCore.QRectF(-radius / 2, -radius / 2, radius, radius)
        pathMidPie = QtGui.QPainterPath()
        pathMidPie.arcMoveTo(rect1, -22.5)
        pathMidPie.arcTo(rect1, -22.5, 45)
        pathMidPie.lineTo(0, 0)
        pathMidPie.closeSubpath()

        self.rightBtnView = pathOuterChampagnePie.subtracted(pathMidPie)
        painter.setPen(QColor(255, 255, 255))
        painter.setBrush(self.get_button_color(self.clicked_button == 'rightBtnView'))
        painter.drawPath(self.rightBtnView)


        icon = QPixmap('./icon/ViaRight.png')
        icon_size = 18  # 设置图标大小
        scaled_icon = icon.scaled(icon_size, icon_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icon_rect = scaled_icon.rect()
        icon_rect.moveCenter(QtCore.QPoint(radius1 / 2 - 12, 0))  # 将图标中心移动到按钮中心

        # # 绘制图标
        # icon = QPixmap('./icons/refresh_ico.png')
        # icon_size = 32
        # scaled_icon = icon.scaled(icon_size, icon_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        # icon_rect = scaled_icon.rect()
        # icon_rect.moveCenter(QtCore.QPoint(radius1 / 2 - 20, 5))
        painter.drawPixmap(icon_rect, scaled_icon)

        painter.restore()



    def drawuprightOuterPie(self, painter):
        painter.save()
        if self.mouseUpRightView:
            radius1 = self.outerPieRadius + 4
        else:
            radius1 = self.outerPieRadius

        rect = QtCore.QRectF(-radius1 / 2, -radius1 / 2, radius1, radius1)
        pathOuterChampagnePie = QtGui.QPainterPath()
        pathOuterChampagnePie.arcMoveTo(rect, 22.5)
        pathOuterChampagnePie.arcTo(rect, 22.5, 45)
        pathOuterChampagnePie.lineTo(0, 0)
        pathOuterChampagnePie.closeSubpath()
        # pathOuterChampagnePie.addText(radius1 / 2 - 28, -20, painter.font(), "1")

        radius = 50
        rect1 = QtCore.QRectF(-radius / 2, -radius / 2, radius, radius)
        pathMidPie = QtGui.QPainterPath()
        pathMidPie.arcMoveTo(rect1, 22.5)
        pathMidPie.arcTo(rect1, 22.5, 45)
        pathMidPie.lineTo(0, 0)
        pathMidPie.closeSubpath()

        self.uprightBtnView = pathOuterChampagnePie.subtracted(pathMidPie)
        painter.setPen(QColor(255, 255, 255))
        painter.setBrush(self.get_button_color(self.clicked_button == 'uprightBtnView'))
        painter.drawPath(self.uprightBtnView)

        icon = QPixmap('./icon/ViaUR.png')
        icon_size = 16  # 设置图标大小
        scaled_icon = icon.scaled(icon_size, icon_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icon_rect = scaled_icon.rect()
        icon_rect.moveCenter(QtCore.QPoint(radius1 / 2 - 24, -28))  # 将图标中心移动到按钮中心
        painter.drawPixmap(icon_rect, scaled_icon)
        painter.restore()

    def drawOuterCircle(self, painter):
        painter.save()
        if self.mouseTopView:
            radius1 = self.outerPieRadius + 4
        else:
            radius1 = self.outerPieRadius

        rect = QtCore.QRectF(-radius1 / 2, -radius1 / 2, radius1, radius1)
        pathOuterChampagnePie = QtGui.QPainterPath()
        pathOuterChampagnePie.arcMoveTo(rect, 67.5)
        pathOuterChampagnePie.arcTo(rect, 67.5, 45)
        pathOuterChampagnePie.lineTo(0, 0)
        pathOuterChampagnePie.closeSubpath()
        # pathOuterChampagnePie.addText(-5, -radius1 / 2 + 20, painter.font(), "8")

        radius = 50
        rect1 = QtCore.QRectF(-radius / 2, -radius / 2, radius, radius)
        pathMidPie = QtGui.QPainterPath()
        pathMidPie.arcMoveTo(rect1, 67.5)
        pathMidPie.arcTo(rect1, 67.5, 45)
        pathMidPie.lineTo(0, 0)
        pathMidPie.closeSubpath()

        self.topBtnView = pathOuterChampagnePie.subtracted(pathMidPie)
        painter.setPen(QColor(255, 255, 255))
        painter.setBrush(self.get_button_color(self.clicked_button == 'topBtnView'))
        painter.drawPath(self.topBtnView)
        # 
        icon = QPixmap('./icon/ViaUp.png')
        icon_size = 16  # 设置图标大小
        scaled_icon = icon.scaled(icon_size, icon_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icon_rect = scaled_icon.rect()
        icon_rect.moveCenter(QtCore.QPoint(0, -radius1 / 2 + 12))  # 将图标中心移动到按钮中心
        painter.drawPixmap(icon_rect, scaled_icon)
        painter.restore()

    def drawrightOuterCircle(self, painter):
        painter.save()
        if self.mouserightTopView:
            radius1 = self.outerPieRadius + 4
        else:
            radius1 = self.outerPieRadius

        rect = QtCore.QRectF(-radius1 / 2, -radius1 / 2, radius1, radius1)
        pathOuterChampagnePie = QtGui.QPainterPath()
        pathOuterChampagnePie.arcMoveTo(rect, 112.5)
        pathOuterChampagnePie.arcTo(rect, 112.5, 45)
        pathOuterChampagnePie.lineTo(0, 0)
        pathOuterChampagnePie.closeSubpath()
        # pathOuterChampagnePie.addText(-30, -radius1 / 2 + 30, painter.font(), "7")

        radius = 50
        rect1 = QtCore.QRectF(-radius / 2, -radius / 2, radius, radius)
        pathMidPie = QtGui.QPainterPath()
        pathMidPie.arcMoveTo(rect1, 112.5)
        pathMidPie.arcTo(rect1, 112.5, 45)
        pathMidPie.lineTo(0, 0)
        pathMidPie.closeSubpath()

        self.righttopBtnView = pathOuterChampagnePie.subtracted(pathMidPie)
        painter.setPen(QColor(255, 255, 255))
        painter.setBrush(self.get_button_color(self.clicked_button == 'righttopBtnView'))
        painter.drawPath(self.righttopBtnView)

        icon = QPixmap('./icon/ViaLU.png')
        icon_size = 16  # 设置图标大小
        scaled_icon = icon.scaled(icon_size, icon_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icon_rect = scaled_icon.rect()
        icon_rect.moveCenter(QtCore.QPoint(-26, -radius1 / 2 + 24))  # 将图标中心移动到按钮中心
        painter.drawPixmap(icon_rect, scaled_icon)
        painter.restore()

    def drawInnerPie(self, painter):
        painter.save()
        if self.mouseLeftView:
            radius1 = self.outerPieRadius + 4
        else:
            radius1 = self.outerPieRadius

        rect = QtCore.QRectF(-radius1 / 2, -radius1 / 2, radius1, radius1)
        pathOuterChampagnePie = QtGui.QPainterPath()
        pathOuterChampagnePie.arcMoveTo(rect, 157.5)
        pathOuterChampagnePie.arcTo(rect, 157.5, 45)
        pathOuterChampagnePie.lineTo(0, 0)
        pathOuterChampagnePie.closeSubpath()
        # pathOuterChampagnePie.addText(-radius1 / 2 + 10, 8, painter.font(), "6")

        radius = 50
        rect1 = QtCore.QRectF(-radius / 2, -radius / 2, radius, radius)
        pathMidPie = QtGui.QPainterPath()
        pathMidPie.arcMoveTo(rect1, 157.5)
        pathMidPie.arcTo(rect1, 157.5, 45)
        pathMidPie.lineTo(0, 0)
        pathMidPie.closeSubpath()

        self.leftBtnView = pathOuterChampagnePie.subtracted(pathMidPie)
        painter.setPen(QColor(255, 255, 255))
        painter.setBrush(self.get_button_color(self.clicked_button == 'leftBtnView'))
        painter.drawPath(self.leftBtnView)

        icon = QPixmap('./icon/ViaLeft.png')
        icon_size = 16  # 设置图标大小
        scaled_icon = icon.scaled(icon_size, icon_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icon_rect = scaled_icon.rect()
        icon_rect.moveCenter(QtCore.QPoint(-radius1 / 2 + 12, 0))  # 将图标中心移动到按钮中心
        painter.drawPixmap(icon_rect, scaled_icon)
        painter.restore()

    def drawdownInnerPie(self, painter):
        painter.save()
        if self.mousedownLeftView:
            radius1 = self.outerPieRadius + 4
        else:
            radius1 = self.outerPieRadius

        rect = QtCore.QRectF(-radius1 / 2, -radius1 / 2, radius1, radius1)
        pathOuterChampagnePie = QtGui.QPainterPath()
        pathOuterChampagnePie.arcMoveTo(rect, 202.5)
        pathOuterChampagnePie.arcTo(rect, 202.5, 45)
        pathOuterChampagnePie.lineTo(0, 0)
        pathOuterChampagnePie.closeSubpath()
        # pathOuterChampagnePie.addText(-radius1 / 2 + 20, 35, painter.font(), "5")

        radius = 50
        rect1 = QtCore.QRectF(-radius / 2, -radius / 2, radius, radius)
        pathMidPie = QtGui.QPainterPath()
        pathMidPie.arcMoveTo(rect1, 202.5)
        pathMidPie.arcTo(rect1, 202.5, 45)
        pathMidPie.lineTo(0, 0)
        pathMidPie.closeSubpath()

        self.downleftBtnView = pathOuterChampagnePie.subtracted(pathMidPie)
        painter.setPen(QColor(255, 255, 255))
        painter.setBrush(self.get_button_color(self.clicked_button == 'downleftBtnView'))
        painter.drawPath(self.downleftBtnView)

        icon = QPixmap('./icon/ViaDL.png')
        icon_size = 16  # 设置图标大小
        scaled_icon = icon.scaled(icon_size, icon_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icon_rect = scaled_icon.rect()
        icon_rect.moveCenter(QtCore.QPoint(-radius1 / 2 + 24, 26))  # 将图标中心移动到按钮中心
        painter.drawPixmap(icon_rect, scaled_icon)

        painter.restore()

    def drawBottom(self, painter):
        painter.save()
        if self.mouseBottomView:
            radius1 = self.outerPieRadius + 4
        else:
            radius1 = self.outerPieRadius

        rect = QtCore.QRectF(-radius1 / 2, -radius1 / 2, radius1, radius1)
        pathOuterChampagnePie = QtGui.QPainterPath()
        pathOuterChampagnePie.arcMoveTo(rect, 247.5)
        pathOuterChampagnePie.arcTo(rect, 247.5, 45)
        pathOuterChampagnePie.lineTo(0, 0)
        pathOuterChampagnePie.closeSubpath()
        # pathOuterChampagnePie.addText(-5, radius1 / 2 - 8, painter.font(), "4")

        radius = 50
        rect1 = QtCore.QRectF(-radius / 2, -radius / 2, radius, radius)
        pathMidPie = QtGui.QPainterPath()
        pathMidPie.arcMoveTo(rect1, 247.5)
        pathMidPie.arcTo(rect1, 247.5, 45)
        pathMidPie.lineTo(0, 0)
        pathMidPie.closeSubpath()

        self.bottomBtnView = pathOuterChampagnePie.subtracted(pathMidPie)
        painter.setPen(QColor(255, 255, 255))
        painter.setBrush(self.get_button_color(self.clicked_button == 'bottomBtnView'))
        painter.drawPath(self.bottomBtnView)

        icon = QPixmap('./icon/ViaDown.png')
        icon_size = 16  # 设置图标大小
        scaled_icon = icon.scaled(icon_size, icon_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icon_rect = scaled_icon.rect()
        icon_rect.moveCenter(QtCore.QPoint(0, radius1 / 2 - 12))  # 将图标中心移动到按钮中心
        painter.drawPixmap(icon_rect, scaled_icon)
        painter.restore()

    def drawrightBottom(self, painter):
        painter.save()
        if self.mouseRightBottomView:
            radius1 = self.outerPieRadius + 4
        else:
            radius1 = self.outerPieRadius

        rect = QtCore.QRectF(-radius1 / 2, -radius1 / 2, radius1, radius1)
        pathOuterChampagnePie = QtGui.QPainterPath()
        pathOuterChampagnePie.arcMoveTo(rect, 292.5)
        pathOuterChampagnePie.arcTo(rect, 292.5, 45)
        pathOuterChampagnePie.lineTo(0, 0)
        pathOuterChampagnePie.closeSubpath()
        # pathOuterChampagnePie.addText(22, radius1 / 2 - 20, painter.font(), "3")

        radius = 50
        rect1 = QtCore.QRectF(-radius / 2, -radius / 2, radius, radius)
        pathMidPie = QtGui.QPainterPath()
        pathMidPie.arcMoveTo(rect1, 292.5)
        pathMidPie.arcTo(rect1, 292.5, 45)
        pathMidPie.lineTo(0, 0)
        pathMidPie.closeSubpath()

        self.rightbottomBtnView = pathOuterChampagnePie.subtracted(pathMidPie)
        painter.setPen(QColor(255, 255, 255))
        painter.setBrush(self.get_button_color(self.clicked_button == 'rightbottomBtnView'))
        painter.drawPath(self.rightbottomBtnView)

        icon = QPixmap('./icon/ViaRD.png')
        icon_size = 16  # 设置图标大小
        scaled_icon = icon.scaled(icon_size, icon_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icon_rect = scaled_icon.rect()
        icon_rect.moveCenter(QtCore.QPoint(24, radius1 / 2 - 24))  # 将图标中心移动到按钮中心
        painter.drawPixmap(icon_rect, scaled_icon)

        painter.restore()

    def drawMidCircle(self, painter):
        if self.mouseCenterView:
            radius = 40 + 4
        else:
            radius = 40
        painter.save()
        painter.setPen(QColor(255, 255, 255))
        painter.setBrush(self.get_button_color(self.clicked_button == 'centerBtnView'))
        path = QtGui.QPainterPath()
        path.addEllipse(-radius / 2, -radius / 2, radius, radius)
        painter.drawPath(path)
        icon = QPixmap('./icon/refresh_ico.png')
        icon_size = 18  # 设置图标大小
        scaled_icon = icon.scaled(icon_size, icon_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icon_rect = scaled_icon.rect()
        icon_rect.moveCenter(QtCore.QPoint(-1, -1))  # 将图标中心移动到按钮中心
        painter.drawPixmap(icon_rect, scaled_icon)

        self.centerBtnView = path
        painter.restore()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHints(QtGui.QPainter.Antialiasing | QtGui.QPainter.TextAntialiasing)

        width = self.width()
        height = self.height()
        side = min(width, height)
        painter.translate(width / 2, height / 2)
        painter.scale(side / 120.0, side / 120.0)

        self.drawOuterCircle(painter)
        self.drawrightOuterCircle(painter)
        self.drawMidCircle(painter)
        self.drawOuterPie(painter)
        self.drawuprightOuterPie(painter)
        self.drawInnerPie(painter)
        self.drawdownInnerPie(painter)
        self.drawBottom(painter)
        self.drawrightBottom(painter)

    def mouseMoveEvent(self, event):
        width = self.width()
        height = self.height()
        side = min(width, height)
        enterPoint = QtCore.QPoint((event.pos().x() - width / 2) / side * 120.0,
                                   (event.pos().y() - height / 2) / side * 120.0)

        if self.centerBtnView.contains(enterPoint):
            self.mouseCenterView = True
        else:
            self.mouseCenterView = False

        if self.bottomBtnView.contains(enterPoint):
            self.mouseBottomView = True
        else:
            self.mouseBottomView = False

        if self.rightBtnView.contains(enterPoint):
            self.mouseRightView = True
        else:
            self.mouseRightView = False

        if self.topBtnView.contains(enterPoint):
            self.mouseTopView = True
        else:
            self.mouseTopView = False

        if self.righttopBtnView.contains(enterPoint):
            self.mouserightTopView = True
        else:
            self.mouserightTopView = False

        if self.uprightBtnView.contains(enterPoint):
            self.mouseUpRightView = True
        else:
            self.mouseUpRightView = False

        if self.leftBtnView.contains(enterPoint):
            self.mouseLeftView = True
        else:
            self.mouseLeftView = False

        if self.downleftBtnView.contains(enterPoint):
            self.mousedownLeftView = True
        else:
            self.mousedownLeftView = False

        if self.rightbottomBtnView.contains(enterPoint):
            self.mouseRightBottomView = True
        else:
            self.mouseRightBottomView = False

        self.update()

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        width = self.width()
        height = self.height()
        side = min(width, height)
        enterPoint = QtCore.QPoint((a0.pos().x() - width / 2) / side * 100.0,
                                   (a0.pos().y() - height / 2) / side * 100.0)
        self.clicked_button = None

        if self.centerBtnView.contains(enterPoint):
            self.clicked_button = 'centerBtnView'
            print("centerBtnView")

        if self.bottomBtnView.contains(enterPoint):
            self.clicked_button = 'bottomBtnView'
            print("bottomBtnView")

        if self.rightBtnView.contains(enterPoint):
            self.clicked_button = 'rightBtnView'
            print('rightBtnView')

        if self.topBtnView.contains(enterPoint):
            self.clicked_button = 'topBtnView'
            print('topBtnView')

        if self.righttopBtnView.contains(enterPoint):
            self.clicked_button = 'righttopBtnView'
            print("righttopBtnView")

        if self.uprightBtnView.contains(enterPoint):
            self.clicked_button = 'uprightBtnView'
            print("uprightBtnView")

        if self.leftBtnView.contains(enterPoint):
            self.clicked_button = 'leftBtnView'
            print('leftBtnView')

        if self.downleftBtnView.contains(enterPoint):
            self.clicked_button = 'downleftBtnView'
            print("downleftBtnView")

        if self.rightbottomBtnView.contains(enterPoint):
            self.clicked_button = 'rightbottomBtnView'
            print("rightbottomBtnView")

        self.update()

    def mouseReleaseEvent(self, event):
        self.clicked_button = None
        self.update()

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui_button = UIButton()
    ui_button.show()
    sys.exit(app.exec_())
