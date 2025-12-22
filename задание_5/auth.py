import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication, QComboBox, QTableWidgetItem


class PriorityComboBox(QComboBox):
    def __init__(self, parent=None, row = 0, main_window=None):
        super().__init__(parent)
        self.row_index = row
        self.main_window = main_window
        self.addItems(['Низкий', 'Средний', 'Высокий'])
        self.currentIndexChanged.connect(self.on_priority_changed)

    def on_priority_changed(self):
        if self.main_window:
            self.main_window.ui.update_icon(self.row_index, self.currentText())


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 300)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 40, 401, 221))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(5)

        self.tableWidget.setHorizontalHeaderLabels(["", "Приоритет", "Задача"])

        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 200)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setup_priorities(self, main_window):
        self.priority_colors = {
            'Низкий': QtGui.QColor('green'),
            'Средний': QtGui.QColor('yellow'),
            'Высокий': QtGui.QColor('red')
        }

        for row in range(self.tableWidget.rowCount()):
            combo = PriorityComboBox(self.tableWidget, row, main_window)
            self.tableWidget.setCellWidget(row, 1, combo)

            self.update_icon(row, combo.currentText())


    def update_icon(self, row, priority_text):
        pixmap = QtGui.QPixmap(32, 32)
        pixmap.fill(QtGui.QColor('transparent'))

        painter = QtGui.QPainter(pixmap)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)

        color = self.priority_colors.get(priority_text, QtGui.QColor('gray'))
        painter.setBrush(QtGui.QBrush(color))
        painter.setPen(QtGui.QPen(QtGui.QColor('black'), 1))

        painter.drawEllipse(4, 4, 24, 24)
        painter.end()

        icon_item = self.tableWidget.item(row, 0)
        if icon_item is None:
            icon_item = QtWidgets.QTableWidgetItem()
            icon_item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.tableWidget.setItem(row, 0, icon_item)

        icon_item.setIcon(QtGui.QIcon(pixmap))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Задачи"))

        for row in range(self.tableWidget.rowCount()):
            self.tableWidget.setVerticalHeaderItem(row,
                                                   QtWidgets.QTableWidgetItem(str(row + 1)))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.setup_priorities(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())