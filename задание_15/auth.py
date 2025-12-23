import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class ToastWidget(QLabel):

    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.setText(text)
        self.setFixedSize(200, 60)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Уведомления")
        self.setGeometry(100, 100, 600, 400)

        # Кнопка для демонстрации
        btn = QPushButton("Показать уведомление", self)
        btn.clicked.connect(self.show_toast)
        btn.setGeometry(200, 150, 200, 50)


        # Переменная для хранения текущего уведомления
        self.current_toast = None

    def show_toast(self):
        """Показать уведомление"""
        # Закрываем предыдущее уведомление, если есть
        if self.current_toast:
            self.current_toast.close()

        # Создаем новое уведомление
        toast = ToastWidget("Запись удалена!", self)

        # Размещаем в правом нижнем углу
        toast.move(
            self.width() - toast.width() - 20,
            self.height() - toast.height() - 40
        )

        toast.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())