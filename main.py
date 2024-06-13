
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
        # self.pix = QBitmap("./Resources/Images/back.png")
        # print(self.pix.size())
        # self.resize(self.pix.size())
        self.setFixedSize(500, 500)
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
        # 新增：添加主题切换按钮
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

    def toggle_theme(self):
        self.is_light_theme = not self.is_light_theme
        if self.is_light_theme:
            self.setStyleSheet(self.light_theme)
        else:
            self.setStyleSheet(self.dark_theme)

    def get_button_color(self):
        if self.is_light_theme:
            return Qt.darkGray
        else:
            return Qt.black


    def drawOuterPie(self, painter):
        """
        绘制右下侧按钮
        :param painter:
        :return:
        """
        painter.save()
        # 以下绘图保存至painter的坐标系统
        # 设置标志位，判断鼠标是否进入该区域。如果进入该区域，则半径扩大
        if self.mouseRightView:
            radius1 = self.outerPieRadius + 4
        else:
            radius1 = self.outerPieRadius

        # 绘制大扇形

        rect = QtCore.QRectF(-radius1/2, -radius1/2, radius1, radius1)  # 该扇形饼圆所在的region
        pathOuterChampagnePie = QtGui.QPainterPath()  # 新建QPainterPath对象
        pathOuterChampagnePie.arcMoveTo(rect, -45)  # 画弧线的起点角度，从0°开始
        pathOuterChampagnePie.arcTo(rect, -45, 45)  # 扇形饼圆弧度为self.outerChampagnePercent * 360
        pathOuterChampagnePie.lineTo(0, 0)  # 画直线
        pathOuterChampagnePie.closeSubpath()  # 使该路径闭合
        pathOuterChampagnePie.addText(radius1 / 2 - 20 , 18, painter.font(), "2")
       
        # painter.restore()
        # 以下同理绘制小扇形
        radius = 50
        rect1 = QtCore.QRectF(-radius/2, -radius/2, radius, radius)
        pathMidPie = QtGui.QPainterPath()
        pathMidPie.arcMoveTo(rect1, -45)
        pathMidPie.arcTo(rect1, -45, 45)
        pathMidPie.lineTo(0, 0)
        pathMidPie.closeSubpath()

        # 大扇形减去小扇形，得到扇形饼圆
        self.rightBtnView = pathOuterChampagnePie.subtracted(pathMidPie)
        painter.setPen(QColor(255, 255, 255))  # 边框线条无色
        painter.setBrush(self.get_button_color())
        painter.drawPath(self.rightBtnView)
        #
        painter.restore()  # 恢复坐标系

    def drawuprightOuterPie(self, painter):
        """
        绘制右上侧按钮
        :param painter:
        :return:
        """
        painter.save()
        # 以下绘图保存至painter的坐标系统
        # 设置标志位，判断鼠标是否进入该区域。如果进入该区域，则半径扩大
        if self.mouseUpRightView:
            radius1 = self.outerPieRadius + 4
        else:
            radius1 = self.outerPieRadius

        # 绘制大扇形

        rect = QtCore.QRectF(-radius1/2, -radius1/2, radius1, radius1)  # 该扇形饼圆所在的region
        pathOuterChampagnePie = QtGui.QPainterPath()  # 新建QPainterPath对象
        pathOuterChampagnePie.arcMoveTo(rect, 0)  # 画弧线的起点角度，从0°开始
        pathOuterChampagnePie.arcTo(rect, 0, 45)  # 扇形饼圆弧度为self.outerChampagnePercent * 360
        pathOuterChampagnePie.lineTo(0, 0)  # 画直线
        pathOuterChampagnePie.closeSubpath()  # 使该路径闭合
        pathOuterChampagnePie.addText(radius1 / 2 -20, -10, painter.font(), "1")
       
        # painter.restore()
        # 以下同理绘制小扇形
        radius = 50
        rect1 = QtCore.QRectF(-radius/2, -radius/2, radius, radius)
        pathMidPie = QtGui.QPainterPath()
        pathMidPie.arcMoveTo(rect1, 0)
        pathMidPie.arcTo(rect1, 0, 45)
        pathMidPie.lineTo(0, 0)
        pathMidPie.closeSubpath()

        # 大扇形减去小扇形，得到扇形饼圆
        self.uprightBtnView = pathOuterChampagnePie.subtracted(pathMidPie)
        painter.setPen(QColor(255, 255, 255))  # 边框线条无色
        painter.setBrush(self.get_button_color())
        painter.drawPath(self.uprightBtnView)
        #
        painter.restore()  # 恢复坐标系


    def drawOuterCircle(self, painter):
        """
            绘制顶部按钮
             :param painter:
             :return:
             """
        painter.save()
        # 以下绘图保存至painter的坐标系统
        # 设置标志位，判断鼠标是否进入该区域。如果进入该区域，则半径扩大
        if self.mouseTopView:
            radius1 = self.outerPieRadius + 4
        else:
            radius1 = self.outerPieRadius

        # 绘制大扇形

        rect = QtCore.QRectF(-radius1 / 2, -radius1 / 2, radius1, radius1)  # 该扇形饼圆所在的region
        pathOuterChampagnePie = QtGui.QPainterPath()  # 新建QPainterPath对象
        pathOuterChampagnePie.arcMoveTo(rect, 45)  # 画弧线的起点角度，从0°开始
        pathOuterChampagnePie.arcTo(rect, 45, 45)  # 扇形饼圆弧度为self.outerChampagnePercent * 360
        pathOuterChampagnePie.lineTo(0, 0)  # 画直线
        pathOuterChampagnePie.closeSubpath()  # 使该路径闭合
        pathOuterChampagnePie.addText(10, -radius1 / 2 + 20, painter.font(), "8")
 
        # painter.restore()
        # 以下同理绘制小扇形
        radius = 50
        rect1 = QtCore.QRectF(-radius / 2, -radius / 2, radius, radius)
        pathMidPie = QtGui.QPainterPath()
        pathMidPie.arcMoveTo(rect1, 45)
        pathMidPie.arcTo(rect1, 45, 45)
        pathMidPie.lineTo(0, 0)
        pathMidPie.closeSubpath()

        # 大扇形减去小扇形，得到扇形饼圆
        self.topBtnView = pathOuterChampagnePie.subtracted(pathMidPie)
        painter.setPen(QColor(255, 255, 255))  # 边框线条无色
        painter.setBrush(self.get_button_color())
        painter.drawPath(self.topBtnView)
        #
        painter.restore()  # 恢复坐标系


    def drawrightOuterCircle(self, painter):
        """
            绘制顶部按钮
             :param painter:
             :return:
             """
        painter.save()
        # 以下绘图保存至painter的坐标系统
        # 设置标志位，判断鼠标是否进入该区域。如果进入该区域，则半径扩大
        if self.mouserightTopView:
            radius1 = self.outerPieRadius + 4
        else:
            radius1 = self.outerPieRadius

        # 绘制大扇形

        rect = QtCore.QRectF(-radius1 / 2, -radius1 / 2, radius1, radius1)  # 该扇形饼圆所在的region
        pathOuterChampagnePie = QtGui.QPainterPath()  # 新建QPainterPath对象
        pathOuterChampagnePie.arcMoveTo(rect, 90)  # 画弧线的起点角度，从0°开始
        pathOuterChampagnePie.arcTo(rect, 90, 45)  # 扇形饼圆弧度为self.outerChampagnePercent * 360
        pathOuterChampagnePie.lineTo(0, 0)  # 画直线
        pathOuterChampagnePie.closeSubpath()  # 使该路径闭合
        pathOuterChampagnePie.addText(-20, -radius1 / 2 + 20, painter.font(), "7")
 
        # painter.restore()
        # 以下同理绘制小扇形
        radius = 50
        rect1 = QtCore.QRectF(-radius / 2, -radius / 2, radius, radius)
        pathMidPie = QtGui.QPainterPath()
        pathMidPie.arcMoveTo(rect1, 90)
        pathMidPie.arcTo(rect1, 90, 45)
        pathMidPie.lineTo(0, 0)
        pathMidPie.closeSubpath()

        # 大扇形减去小扇形，得到扇形饼圆
        self.righttopBtnView = pathOuterChampagnePie.subtracted(pathMidPie)
        painter.setPen(QColor(255, 255, 255))  # 边框线条无色
        painter.setBrush(self.get_button_color())
        painter.drawPath(self.righttopBtnView)
        #
        painter.restore()  # 恢复坐标系


    def drawInnerPie(self, painter):
        """
             绘制左侧按钮
             :param painter:
             :return:
             """
        painter.save()
        # 以下绘图保存至painter的坐标系统
        # 设置标志位，判断鼠标是否进入该区域。如果进入该区域，则半径扩大
        if self.mouseLeftView:
            radius1 = self.outerPieRadius + 4
        else:
            radius1 = self.outerPieRadius

        # 绘制大扇形

        rect = QtCore.QRectF(-radius1 / 2, -radius1 / 2, radius1, radius1)  # 该扇形饼圆所在的region
        pathOuterChampagnePie = QtGui.QPainterPath()  # 新建QPainterPath对象
        pathOuterChampagnePie.arcMoveTo(rect, 135)  # 画弧线的起点角度，从0°开始
        pathOuterChampagnePie.arcTo(rect, 135, 45)  # 扇形饼圆弧度为self.outerChampagnePercent * 360
        pathOuterChampagnePie.lineTo(0, 0)  # 画直线
        pathOuterChampagnePie.closeSubpath()  # 使该路径闭合
        pathOuterChampagnePie.addText(-radius1 / 2 + 12, -8, painter.font(), "6")
      
        # 以下同理绘制小扇形
        radius = 50
        rect1 = QtCore.QRectF(-radius / 2, -radius / 2, radius, radius)
        pathMidPie = QtGui.QPainterPath()
        pathMidPie.arcMoveTo(rect1, 135)
        pathMidPie.arcTo(rect1, 135, 45)
        pathMidPie.lineTo(0, 0)
        pathMidPie.closeSubpath()

        # 大扇形减去小扇形，得到扇形饼圆
        self.leftBtnView = pathOuterChampagnePie.subtracted(pathMidPie)
        painter.setPen(QColor(255, 255, 255))  # 边框线条无色
        painter.setBrush(self.get_button_color())
        painter.drawPath(self.leftBtnView)
        #
        painter.restore()  # 恢复坐标系


    def drawdownInnerPie(self, painter):
        """
             绘制左侧按钮
             :param painter:
             :return:
             """
        painter.save()
        # 以下绘图保存至painter的坐标系统
        # 设置标志位，判断鼠标是否进入该区域。如果进入该区域，则半径扩大
        if self.mousedownLeftView:
            radius1 = self.outerPieRadius + 4
        else:
            radius1 = self.outerPieRadius

        # 绘制大扇形

        rect = QtCore.QRectF(-radius1 / 2, -radius1 / 2, radius1, radius1)  # 该扇形饼圆所在的region
        pathOuterChampagnePie = QtGui.QPainterPath()  # 新建QPainterPath对象
        pathOuterChampagnePie.arcMoveTo(rect, 180)  # 画弧线的起点角度，从0°开始
        pathOuterChampagnePie.arcTo(rect, 180, 45)  # 扇形饼圆弧度为self.outerChampagnePercent * 360
        pathOuterChampagnePie.lineTo(0, 0)  # 画直线
        pathOuterChampagnePie.closeSubpath()  # 使该路径闭合
        pathOuterChampagnePie.addText(-radius1 / 2 + 12, 18, painter.font(), "5")
      
        # 以下同理绘制小扇形
        radius = 50
        rect1 = QtCore.QRectF(-radius / 2, -radius / 2, radius, radius)
        pathMidPie = QtGui.QPainterPath()
        pathMidPie.arcMoveTo(rect1, 180)
        pathMidPie.arcTo(rect1, 180, 45)
        pathMidPie.lineTo(0, 0)
        pathMidPie.closeSubpath()

        # 大扇形减去小扇形，得到扇形饼圆
        self.downleftBtnView = pathOuterChampagnePie.subtracted(pathMidPie)
        painter.setPen(QColor(255, 255, 255))  # 边框线条无色
        painter.setBrush(self.get_button_color())
        painter.drawPath(self.downleftBtnView)
        #
        painter.restore()  # 恢复坐标系

    def drawBottom(self, painter):
        """
             绘制底部按钮
             :param painter:
             :return:
             """
        painter.save()
        # 以下绘图保存至painter的坐标系统
        # 设置标志位，判断鼠标是否进入该区域。如果进入该区域，则半径扩大
        if self.mouseBottomView:
            radius1 = self.outerPieRadius + 4
        else:
            radius1 = self.outerPieRadius

        # 绘制大扇形

        rect = QtCore.QRectF(-radius1 / 2, -radius1 / 2, radius1, radius1)  # 该扇形饼圆所在的region
        pathOuterChampagnePie = QtGui.QPainterPath()  # 新建QPainterPath对象
        pathOuterChampagnePie.arcMoveTo(rect, 225)  # 画弧线的起点角度，从0°开始
        pathOuterChampagnePie.arcTo(rect, 225, 45)  # 扇形饼圆弧度为self.outerChampagnePercent * 360
        pathOuterChampagnePie.lineTo(0, 0)  # 画直线
        pathOuterChampagnePie.closeSubpath()  # 使该路径闭合
        pathOuterChampagnePie.addText(-20, radius1/2-10, painter.font(), "4")

        # 以下同理绘制小扇形
        radius = 50
        rect1 = QtCore.QRectF(-radius / 2, -radius / 2, radius, radius)
        pathMidPie = QtGui.QPainterPath()
        pathMidPie.arcMoveTo(rect1, 225)
        pathMidPie.arcTo(rect1, 225, 45)
        pathMidPie.lineTo(0, 0)
        pathMidPie.closeSubpath()

        # 大扇形减去小扇形，得到扇形饼圆
        self.bottomBtnView = pathOuterChampagnePie.subtracted(pathMidPie)
        painter.setPen(QColor(255, 255, 255))  # 边框线条无色
        painter.setBrush(self.get_button_color())
        painter.drawPath(self.bottomBtnView)
        #
        painter.restore()  # 恢复坐标系

    def drawrightBottom(self, painter):
        """
             绘制底部按钮
             :param painter:
             :return:
             """
        painter.save()
        # 以下绘图保存至painter的坐标系统
        # 设置标志位，判断鼠标是否进入该区域。如果进入该区域，则半径扩大
        if self.mouseRightBottomView:
            radius1 = self.outerPieRadius + 4
        else:
            radius1 = self.outerPieRadius

        # 绘制大扇形

        rect = QtCore.QRectF(-radius1 / 2, -radius1 / 2, radius1, radius1)  # 该扇形饼圆所在的region
        pathOuterChampagnePie = QtGui.QPainterPath()  # 新建QPainterPath对象
        pathOuterChampagnePie.arcMoveTo(rect, 270)  # 画弧线的起点角度，从0°开始
        pathOuterChampagnePie.arcTo(rect, 270, 45)  # 扇形饼圆弧度为self.outerChampagnePercent * 360
        pathOuterChampagnePie.lineTo(0, 0)  # 画直线
        pathOuterChampagnePie.closeSubpath()  # 使该路径闭合
        pathOuterChampagnePie.addText(12, radius1/2-10, painter.font(), "3")

        # 以下同理绘制小扇形
        radius = 50
        rect1 = QtCore.QRectF(-radius / 2, -radius / 2, radius, radius)
        pathMidPie = QtGui.QPainterPath()
        pathMidPie.arcMoveTo(rect1, 270)
        pathMidPie.arcTo(rect1, 270, 45)
        pathMidPie.lineTo(0, 0)
        pathMidPie.closeSubpath()

        # 大扇形减去小扇形，得到扇形饼圆
        self.rightbottomBtnView = pathOuterChampagnePie.subtracted(pathMidPie)
        painter.setPen(QColor(255, 255, 255))  # 边框线条无色
        painter.setBrush(self.get_button_color())
        painter.drawPath(self.rightbottomBtnView)
        #
        painter.restore()  # 恢复坐标系

    def drawMidCircle(self, painter):
        """
        中间按钮
        :param painter:
        :return:
        """
        if self.mouseCenterView:
            radius = 40 + 4
        else:
            radius = 40
        painter.save()
        painter.setPen(QColor(255, 255, 255))  # 边框线条无色
        painter.setBrush(self.get_button_color())
        path = QtGui.QPainterPath()
        path.addEllipse(-radius/2, -radius/2, radius, radius)
        # path.addText(-5, 8, painter.font(), "0")
        painter.drawPath(path)

        # 绘制图标
        icon = QPixmap('./refresh_ico.png')
        icon_rect = icon.rect()
        icon_rect.moveCenter(QtCore.QPoint(-1, -1))  # 将图标中心移动到按钮中心
        painter.drawPixmap(icon_rect, icon)

        self.centerBtnView = path
        # painter.drawEllipse(-radius/2, -radius/2, radius, radius)
        painter.restore()
        # font = QFont()

    def paintEvent(self, event):
        # 绘制准备工作, 启用反锯齿
        painter = QtGui.QPainter(self)
        painter.setRenderHints(QtGui.QPainter.Antialiasing | QtGui.QPainter.TextAntialiasing)

        # 平移坐标中心，等比例缩放
        width = self.width()
        height = self.height()
        side = min(width, height)
        painter.translate(width / 2, height / 2)  # 坐标中心移至窗口中心位置
        painter.scale(side / 200.0, side / 200.0)  # 坐标刻度缩放为原来的（side/200）倍

        # 画圆
        self.drawOuterCircle(painter)  # 绘制顶部按钮
        self.drawrightOuterCircle(painter)
        self.drawMidCircle(painter)  # 绘制中间按钮
        self.drawOuterPie(painter)  # 绘制右侧按钮
        self.drawuprightOuterPie(painter)
        self.drawInnerPie(painter)  # 绘制左侧按钮
        self.drawdownInnerPie(painter)
        self.drawBottom(painter)  # 绘制底部按钮
        self.drawrightBottom(painter)
        # self.drawLegend(painter)  # 绘制图例
        # self.drawTitle(painter)  # 绘制左上角文字

    def mouseMoveEvent(self, event):
        print('鼠标移动')
        print(event.pos)
        # 坐标系转换，和之前painter转换坐标系相对应
        width = self.width()
        height = self.height()
        side = min(width, height)
        enterPoint = QtCore.QPoint((event.pos().x() - width / 2) / side * 250.0,
                                   (event.pos().y() - height / 2) / side * 250.0)

        # 判断鼠标是否进入，并置标志位
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

        self.update()  # 重绘

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        width = self.width()
        height = self.height()
        side = min(width, height)
        enterPoint = QtCore.QPoint((a0.pos().x() - width / 2) / side * 200.0,
                                   (a0.pos().y() - height / 2) / side * 200.0)
        # 判断鼠标是否进入，并置标志位
        if self.centerBtnView.contains(enterPoint):
            print("centerBtnView")

        if self.bottomBtnView.contains(enterPoint):
            print("bottomBtnView")

        if self.rightBtnView.contains(enterPoint):
            print('rightBtnView')

        if self.topBtnView.contains(enterPoint):
            print('topBtnView')
        
        if self.righttopBtnView.contains(enterPoint):
            print("righttopBtnView")

        if self.uprightBtnView.contains(enterPoint):
            print("uprightBtnView")

        if self.leftBtnView.contains(enterPoint):
            print('leftBtnView')
        
        if self.downleftBtnView.contains(enterPoint):
            print("downleftBtnView")
        
        if self.rightbottomBtnView.contains(enterPoint):
            print("rightbottomBtnView")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui_button = UIButton()
    ui_button.show()
    sys.exit(app.exec_())
