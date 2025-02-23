# 金币类
from PyQt5.QtCore import QSize, QTimer
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QPushButton


class MyCoin(QPushButton):
    def __init__(self, btn_img):
        super().__init__()
        self.init_ui(btn_img)

        # 初始化定时器
        self.timer1 = QTimer(self)
        self.timer2 = QTimer(self)

        # 初始化翻转动画的参数
        self.min = 1
        self.max = 8
        self.isAnimation = False
        self.flag = True  # 默认为正面

        # 连接定时器信号
        self.timer1.timeout.connect(self.flip_to_back)
        self.timer2.timeout.connect(self.flip_to_front)

    def init_ui(self, btn_img):
        # 加载图片
        pix = QPixmap(btn_img)
        if pix.isNull():
            print(f"图片 {btn_img} 加载失败")
            return

        # 设置按钮固定大小
        self.setFixedSize(pix.width(), pix.height())

        # 设置不规则图片样式
        self.setStyleSheet("QPushButton{border:0px;}")

        # 设置图标
        self.setIcon(QIcon(pix))

        # 设置图标大小
        self.setIconSize(QSize(pix.width(), pix.height()))

    def flip_to_back(self):
        # 正面翻反面
        pix = QPixmap(f"Coin000{self.min}")
        if not pix.isNull():
            self.setFixedSize(pix.width(), pix.height())
            self.setStyleSheet("QPushButton{border:0px;}")
            self.setIcon(QIcon(pix))
            self.setIconSize(QSize(pix.width(), pix.height()))

        self.min += 1
        if self.min > self.max:
            self.min = 1
            self.isAnimation = False
            self.timer1.stop()

    def flip_to_front(self):
        # 反面翻正面
        pix = QPixmap(f"Coin000{self.max}")
        if not pix.isNull():
            self.setFixedSize(pix.width(), pix.height())
            self.setStyleSheet("QPushButton{border:0px;}")
            self.setIcon(QIcon(pix))
            self.setIconSize(QSize(pix.width(), pix.height()))

        self.max -= 1
        if self.max < self.min:
            self.max = 8
            self.isAnimation = False
            self.timer2.stop()

    def change_flag(self):
        if self.isAnimation:
            return

        if self.flag:
            # 开始正面翻反面的定时器
            self.timer1.start(30)
            self.flag = False
        else:
            # 开始反面翻正面的定时器
            self.timer2.start(30)
            self.flag = True

    # 停止标识
    # def mousePressEvent(self, event):
    #     if self.isAnimation or self.isWin:
    #         return
    #     super().mousePressEvent(event)