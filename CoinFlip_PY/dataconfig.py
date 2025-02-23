# 数据类
from PyQt5.QtCore import QObject


class DataConfig(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mData = {}  # 使用 Python 的 dict 存储关卡数据
        self.init_data()

    def init_data(self):
        # 关卡 1
        array1 = [
            [1, 1, 1, 1],
            [1, 1, 0, 1],
            [1, 0, 0, 0],
            [1, 1, 0, 1]
        ]
        self.mData[1] = array1


        array2 = [
            [1, 0, 1, 1],
            [0, 0, 1, 1],
            [1, 1, 0, 0],
            [1, 1, 0, 1]
        ]
        self.mData[2] = array2


        array3 = [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]
        ]
        self.mData[3] = array3


        array4 = [
            [0, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 0, 1, 1],
            [1, 1, 1, 1]
        ]
        self.mData[4] = array4


        array5 = [
            [1, 0, 0, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 0, 0, 1]
        ]
        self.mData[5] = array5


        array6 = [
            [1, 0, 0, 1],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [1, 0, 0, 1]
        ]
        self.mData[6] = array6


        array7 = [
            [0, 1, 1, 1],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 0]
        ]
        self.mData[7] = array7


        array8 = [
            [0, 1, 0, 1],
            [1, 0, 0, 0],
            [0, 0, 0, 1],
            [1, 0, 1, 0]
        ]
        self.mData[8] = array8


        array9 = [
            [1, 0, 1, 0],
            [1, 0, 1, 0],
            [0, 0, 1, 0],
            [1, 0, 0, 1]
        ]
        self.mData[9] = array9


        array10 = [
            [1, 0, 1, 1],
            [1, 1, 0, 0],
            [0, 0, 1, 1],
            [1, 1, 0, 1]
        ]
        self.mData[10] = array10


        array11 = [
            [0, 1, 1, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [0, 1, 1, 0]
        ]
        self.mData[11] = array11


        array12 = [
            [0, 1, 1, 0],
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 0]
        ]
        self.mData[12] = array12


        array13 = [
            [0, 1, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 1, 1, 0]
        ]
        self.mData[13] = array13


        array14 = [
            [1, 0, 1, 1],
            [0, 1, 0, 1],
            [1, 0, 1, 0],
            [1, 1, 0, 1]
        ]
        self.mData[14] = array14


        array15 = [
            [0, 1, 0, 1],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [0, 1, 0, 1]
        ]
        self.mData[15] = array15


        array16 = [
            [0, 1, 1, 0],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [0, 1, 1, 0]
        ]
        self.mData[16] = array16


        array17 = [
            [0, 1, 1, 1],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [1, 1, 1, 0]
        ]
        self.mData[17] = array17


        array18 = [
            [0, 0, 0, 1],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [1, 0, 0, 0]
        ]
        self.mData[18] = array18


        array19 = [
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 0]
        ]
        self.mData[19] = array19


        array20 = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.mData[20] = array20

    def get_level_data(self, level):
        """根据关卡号获取数据"""
        return self.mData.get(level)

