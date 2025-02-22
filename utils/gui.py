import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self, start_processing):
        super().__init__()
        self.setWindowTitle("Голосовой Ассистент")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        layout.addWidget(self.text_area)

        self.start_button = QPushButton("Старт")
        self.start_button.clicked.connect(lambda: start_processing(self))
        layout.addWidget(self.start_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def update_text(self, text):
        self.text_area.append(text)

def run_gui(start_processing):
    app = QApplication(sys.argv)
    window = MainWindow(start_processing)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_gui(lambda window: print("Тест GUI"))
