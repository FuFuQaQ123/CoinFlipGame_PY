from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtWidgets import QPushButton# , QPropertyAnimation, QRect
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QEasingCurve, QPropertyAnimation, QRect, QTimer, QSize, QObject
from functools import partial  # 确保导入 functools 模块

from CoinFlip_PY.mypushbutton import MyPushButton
from CoinFlip_PY.subwindow import SubWindow


class CustomCentralWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        # 创建自定义按钮
        self.start_button = MyPushButton("MenuSceneStartButton.png")
        self.start_button.setParent(self)

        # 计算按钮的中心位置
        x = int(110)
        y = int(400)
        self.start_button.move(x, y)

        # 连接按钮的点击信号
        self.start_button.clicked.connect(self.on_start_button_clicked)

    def paintEvent(self, event: QtGui.QPaintEvent):
        painter = QtGui.QPainter(self)  # 创建 QPainter 对象
        pix = QtGui.QPixmap()  # 创建 QPixmap 对象

        # 绘制背景图片
        pix.load("MenuSceneBg.png")  # 加载背景图片
        painter.drawPixmap(0, 0, self.width(), self.height(), pix)  # 绘制背景图片

    def on_start_button_clicked(self):
        print("点击了开始")
        self.start_button.zoom1()
        self.start_button.zoom2()

        # 使用 QTimer 实现延时效果
        QTimer.singleShot(200, self.show_sub_window)  # 200 毫秒后显示子窗

    def show_sub_window(self):
        # 创建子窗口并显示
        self.sub_window = SubWindow()
        self.sub_window.show_main_window.connect(self.parent().show)  # 连接信号
        self.sub_window.show()

        self.parent().hide()  # 隐藏主窗口





class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # 配置主场景
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(320, 588)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Coin0001.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)

        # 创建一个自定义的中心部件
        self.centralwidget = CustomCentralWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        # 创建一个菜单栏 QMenuBar
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 26))
        self.menubar.setObjectName("menubar")

        # 创建一个菜单 QMenu，命名为 menu。
        # 创建一个菜单项动作 QAction，命名为 actionquit，并将其添加到菜单中。
        # 将菜单添加到菜单栏。
        self.menu = QtWidgets.QMenu(parent=self.menubar)
        self.menu.setObjectName("menu")

        MainWindow.setMenuBar(self.menubar)

        self.actionquit = QtWidgets.QAction(parent=MainWindow)
        self.actionquit.setObjectName("actionquit")
        self.menu.addAction(self.actionquit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 退出按钮实现
        self.actionquit.triggered.connect(MainWindow.close)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "翻金币主场景"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.actionquit.setText(_translate("MainWindow", "退出"))
# ____________________________________
# 按钮类MyPushButton


# ____________________________________
# 子窗口

