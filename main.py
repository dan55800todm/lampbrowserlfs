#BASED ON HUEMULBROWSER! (https://github.com/MasterKrab/huemul-browser?tab=readme-ov-file)
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFontDatabase, QIcon
from components.tool_bar import ToolBar
from components.main import Main
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The Lamp Browser 1.5")
        self.setWindowIcon(QIcon("assets/brand/lampico.ico"))

        self.setMinimumSize(800, 600)

        self.setWindowState(Qt.WindowState.WindowMaximized)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #282a36;
                color: #fff;
                border: none;
            }
        """)

        self.main = Main(self)

        self.tool_bar = ToolBar(self)
        self.addToolBar(self.tool_bar)

        self.setCentralWidget(self.main)

        self.main.add_tab()


app = QApplication(sys.argv)
QFontDatabase.addApplicationFont("assets/fonts/poppins/poppins-v19-latin-500.ttf")
QFontDatabase.addApplicationFont("assets/fonts/poppins/poppins-v19-latin-600.ttf")
QFontDatabase.addApplicationFont("assets/fonts/poppins/poppins-v19-latin-700.ttf")
QFontDatabase.addApplicationFont("assets/fonts/poppins/poppins-v19-latin-regular.ttf")
window = MainWindow()
window.show()

sys.exit(app.exec())
