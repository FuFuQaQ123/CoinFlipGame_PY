from functools import partial

from PyQt5 import QtWidgets
from PyQt5.uic.Compiler.qtproxies import QtCore
from PyQt5.uic.properties import QtGui

from CoinFlip_PY.mypushbutton import MyPushButton
from CoinFlip_PY.playscene import PlayScene


class SubWindow(QtWidgets.QMainWindow):
    show_main_window = QtCore.pyqtSignal()  # 定义一个信号，用于通知主窗口返回

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        # 配置选择关卡场景
        self.setFixedSize(320, 588)  # 设置固定大小

        # 设置图标
        self.setWindowIcon(QtGui.QIcon("Coin0001.png"))  # 使用资源路径加载图标

        # 设置标题
        self.setWindowTitle("选择关卡场景")

        # 创建菜单栏
        bar = self.menuBar()
        self.setMenuBar(bar)

        # 创建开始菜单
        start_menu = bar.addMenu("开始")

        # 创建退出菜单项
        quit_action = start_menu.addAction("退出")

        # 点击退出，实现退出游戏
        quit_action.triggered.connect(self.close)

        # 返回按钮
        self.back_button = MyPushButton("BackButton.png", "BackButtonSelected.png")
        self.back_button.setParent(self)
        self.back_button.move(self.width() - self.back_button.width(), self.height() - self.back_button.height())

        # 连接返回按钮的点击信号
        self.back_button.clicked.connect(self.on_back_button_clicked)

        # 创建关卡按钮
        self.create_level_buttons()

    # 监听选择的关卡
    def create_level_buttons(self):
        for i in range(20):
            self.create_level_button(i)
    # ??????
    def create_level_button(self, i):
        # 创建关卡按钮
        menu_btn = MyPushButton("LevelIcon.png")
        menu_btn.setParent(self)
        menu_btn.move(25 + i % 4 * 70, 130 + i // 4 * 70)

        # 创建标签
        label = QtWidgets.QLabel(self)
        label.setFixedSize(menu_btn.width(), menu_btn.height())
        label.setText(str(i + 1))  # 显示关卡编号
        label.move(25 + i % 4 * 70, 130 + i // 4 * 70)

        # 设置标签上的文字对齐方式
        label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        # 设置让鼠标进行穿透
        label.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)

        # 监听按钮的点击事件
        menu_btn.clicked.connect(partial(self.on_level_button_clicked, i + 1))

    def on_level_button_clicked(self, level_number):
        print(f"您选择的是第 {level_number} 关")

        QtCore.QTimer.singleShot(200, lambda: self.show_game_window(level_number)) # 延时效果

    def show_game_window(self, level_number):
        # 创建游戏窗口并显示
        self.game_window = PlayScene(level_number, self)
        self.game_window.chooseSceneBack.connect(self.show)  # 连接返回信号
        self.game_window.show()
        self.hide()  # 隐藏子窗口

    def paintEvent(self, event: QtGui.QPaintEvent):
        painter = QtGui.QPainter(self)  # 创建 QPainter 对象
        pix = QtGui.QPixmap()  # 创建 QPixmap 对象

        # 绘制背景图片
        pix.load("OtherSceneBg.png")  # 加载背景图片
        painter.drawPixmap(0, 0, self.width(), self.height(), pix)  # 绘制背景图片

        # 绘制标题图片
        pix.load("Title.png")
        painter.drawPixmap(20, 30, pix.width(), pix.height(), pix)

    def on_back_button_clicked(self):
        print("点击了返回按钮")
        # 延时返回
        QtCore.QTimer.singleShot(300, self.emit_choose_scene_back)

    def emit_choose_scene_back(self):
        # 发出返回信号，通知主窗口
        self.show_main_window.emit()
        self.close() # 关闭子窗口
