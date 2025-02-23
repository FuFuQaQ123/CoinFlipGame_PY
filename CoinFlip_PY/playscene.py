# 游戏窗口
from functools import partial

from PyQt5 import QtGui
from PyQt5.QtCore import QTimer
from PyQt5.uic.Compiler.qtproxies import QtWidgets, QtCore

from CoinFlip_PY.dataconfig import DataConfig
from CoinFlip_PY.mycoin import MyCoin
from CoinFlip_PY.mypushbutton import MyPushButton


class PlayScene(QtWidgets.QMainWindow):
    chooseSceneBack = QtCore.pyqtSignal()  # 定义一个信号，用于通知主窗口返回

    def __init__(self, level_num, parent=None):
        super().__init__(parent)
        self.level_index = level_num
        self.gameArray = [[0 for _ in range(4)] for _ in range(4)]  # 初始化 4x4 的二维数组
        self.coinBtn = [[None for _ in range(4)] for _ in range(4)]  # 初始化 4x4 的金币按钮数组
        self.isWin = False  # 是否胜利标志
        self.init_ui()

    def init_ui(self):
        # 初始化游戏场景
        self.setFixedSize(320, 588)
        self.setWindowIcon(QtGui.QIcon("Coin0001.png"))
        self.setWindowTitle("翻金币")

        # 创建菜单栏
        bar = self.menuBar()
        self.setMenuBar(bar)

        # 创建开始菜单
        start_menu = bar.addMenu("开始")

        # 创建退出菜单项
        quit_action = start_menu.addAction("退出")
        quit_action.triggered.connect(self.close)

        # 返回按钮
        self.back_button = MyPushButton("BackButton.png", "BackButtonSelected.png")
        self.back_button.setParent(self)
        self.back_button.move(self.width() - self.back_button.width(), self.height() - self.back_button.height())
        self.back_button.clicked.connect(self.on_back_button_clicked)

        # 显示当前关卡数
        self.label = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setFamily("华文新魏")  # 设置字体
        font.setPointSize(20)      # 设置字体大小
        self.label.setFont(font)
        self.label.setText(f"Level: {self.level_index}")
        self.label.setGeometry(30, self.height() - 50, 120, 50)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        # 初始化关卡数据
        self.init_level_data()

        # 显示金币背景图
        self.show_coin_background()


    def init_level_data(self):
        # 获取关卡数据
        config = DataConfig()
        level_data = config.get_level_data(self.level_index)

        if level_data:
            for i in range(4):
                for j in range(4):
                    self.gameArray[i][j] = int(level_data[i][j])
        else:
            print(f"关卡 {self.level_index} 数据未找到")


    def show_coin_background(self):
        for i in range(4):
            for j in range(4):
                # 绘制背景图片
                pix = QtGui.QPixmap("BoardNode.png")
                label = QtWidgets.QLabel(self)
                label.setPixmap(pix)
                label.setGeometry(0, 0, pix.width(), pix.height())
                label.move(57 + i * 50, 200 + j * 50)

                # 创建金币
                if self.gameArray[i][j] == 1:
                    coin_img = "Coin0001.png"  # 金币
                else:
                    coin_img = "Coin0008.png"  # 银币

                coin = MyCoin(coin_img)
                coin.setParent(self)
                coin.move(59 + i * 50, 204 + j * 50)

                # 给金币属性赋值
                coin.posX = i
                coin.posY = j
                coin.flag = self.gameArray[i][j]

                # 将金币放入二维数组以便后期维护
                self.coinBtn[i][j] = coin

                # 点击金币，翻转
                coin.clicked.connect(partial(self.on_coin_clicked, coin))

    def on_coin_clicked(self, coin):
        # 翻转金币
        coin.change_flag()
        self.gameArray[coin.posX][coin.posY] = 1 if self.gameArray[coin.posX][coin.posY] == 0 else 0

        # 翻转周围金币
        QTimer.singleShot(300, lambda: self.flip_adjacent_coins(coin))

    def flip_adjacent_coins(self, coin):
        positions = [
            (coin.posX + 1, coin.posY),  # 右侧
            (coin.posX - 1, coin.posY),  # 左侧
            (coin.posX, coin.posY + 1),  # 上侧
            (coin.posX, coin.posY - 1)   # 下侧
        ]

        for x, y in positions:
            if 0 <= x < 4 and 0 <= y < 4:
                adjacent_coin = self.coinBtn[x][y]
                adjacent_coin.change_flag()
                self.gameArray[x][y] = 1 if self.gameArray[x][y] == 0 else 0

        # 检查是否胜利
        self.check_win()

    def check_win(self):
        self.isWin = True
        for i in range(4):
            for j in range(4):
                if not self.coinBtn[i][j].flag:
                    self.isWin = False
                    break
            if not self.isWin:
                break

        if self.isWin:
            print("游戏胜利了！")
            self.show_win_animation()

    def show_win_animation(self):
        # 胜利图片
        # 创建 QLabel 用于显示图片
        self.win_label = QtWidgets.QLabel(self)  # 使用 QtWidgets.QLabel
        self.win_label.setGeometry(0, 250, self.width(), self.height() // 5)  # 设置 QLabel 的位置和大小
        self.win_label.raise_()  # 将 QLabel 置于最上层，覆盖其他控件

        # 加载图片
        pixmap = QtGui.QPixmap("LevelCompletedDialogBg.png")  # 替换为你的图片路径
        if pixmap.isNull():
            print("图片加载失败，请检查路径是否正确！")
        else:
            self.win_label.setPixmap(pixmap)  # 设置 QLabel 的图片
            self.win_label.setScaledContents(True)  # 图片会自动缩放以适应 QLabel 的大小
            self.win_label.show()  # 显式调用 show() 确保显示

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
        print("游戏点击了返回按钮")
        # 延时返回
        QTimer.singleShot(200, self.emit_choose_scene_back)

    def emit_choose_scene_back(self):
        # 发出返回信号，通知子窗口
        self.chooseSceneBack.emit()
        self.close()  # 关闭游戏窗口
