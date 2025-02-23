from PyQt5.QtCore import QEasingCurve, QRect, QPropertyAnimation
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QPushButton


class MyPushButton(QPushButton):
    def __init__(self, normal_img, press_img=""):
        super().__init__()
        self.normalImgPath = normal_img
        self.pressImgPath = press_img
        self.init_ui()

    def init_ui(self):
        # 加载正常状态的图片
        pix = QPixmap(self.normalImgPath)
        if pix.isNull():
            print("图片加载失败，请检查路径是否正确！")
            return

        # 设置按钮固定大小
        self.setFixedSize(pix.width(), pix.height())

        # 设置不规则图片样式
        self.setStyleSheet("QPushButton{border:0px;}")

        # 将 QPixmap 转换为 QIcon
        icon = QIcon(pix)
        self.setIcon(icon)

        # 设置图标大小
        self.setIconSize(pix.size())

    def zoom1(self):
        # 创建动态对象
        animation = QPropertyAnimation(self, b"geometry")
        animation.setDuration(200)  # 设置动画时间间隔
        animation.setStartValue(QRect(self.x(), self.y()  + 10, self.width(), self.height())) # 起始位置
        animation.setEndValue(QRect(self.x(), self.y(), self.width(), self.height())) # 结束位置
        animation.setEasingCurve(QEasingCurve.OutBounce)  # 设置弹跳曲线
        animation.start() # 执行动画

    def zoom2(self):
        # 创建动态对象
        animation = QPropertyAnimation(self, b"geometry")
        animation.setDuration(200)  # 设置动画时间间隔
        animation.setStartValue(QRect(self.x(), self.y()  - 10, self.width(), self.height()))
        animation.setEndValue(QRect(self.x(), self.y(), self.width(), self.height()))
        animation.setEasingCurve(QEasingCurve.OutBounce)  # 设置弹跳曲线
        animation.start()

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        if self.pressImgPath:
            pix = QPixmap(self.pressImgPath)
            if not pix.isNull():
                icon = QIcon(pix)
                self.setIcon(icon)
        self.zoom1()

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        pix = QPixmap(self.normalImgPath)
        if not pix.isNull():
            icon = QIcon(pix)
            self.setIcon(icon)
        self.zoom2()
