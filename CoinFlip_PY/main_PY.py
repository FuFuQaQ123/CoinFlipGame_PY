import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets

from CoinFlip.mainscene import Ui_MainWindow

# 主方法，程序从此处启动PyQt设计的窗体
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
