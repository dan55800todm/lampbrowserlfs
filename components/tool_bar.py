from PyQt6.QtWidgets import QToolBar, QLabel, QTextEdit, QLineEdit, QMenu, QToolButton, QDialog, QVBoxLayout
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon, QFont, QAction
import webbrowser
import sys

class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("About")
        self.setFixedSize(400, 200)

        self.setWindowIcon(QIcon("assets/brand/lampico.ico"))

        self.setStyleSheet("""
            QDialog {
                background-color: #282a36;
                color: #dfe0e6;
            }

            QTextEdit {
                font-size: 16px;
                color: #dfe0e6;
                background-color: #282a36;
                border: none;
            }
        """)

        layout = QVBoxLayout()

        about_text = """
        <h2>The Lamp Browser 1.4</h2>
        <p>Lamp Browser is a browser developed by dan55800todm.</p>
        <p>For more information visit: <a href='https://github.com/dan55800todm/lampbrowserlfs'>https://github.com/dan55800todm/lampbrowserlfs</a></p>
        """
        text_edit = QTextEdit()
        text_edit.setReadOnly(True)
        text_edit.setHtml(about_text)

        layout.addWidget(text_edit)
        self.setLayout(layout)

class ToolBar(QToolBar):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setMovable(False)

        self.setStyleSheet("""       
            QToolBar {
                border: none;
                background-color: #22282a;
                padding: 3px;
            }

            QToolButton {
                color: #fff;
                width: 21px;
                height: 21px;
            }

            QLineEdit,
            QToolButton:hover {
                background-color: #363b3f;
            }

            QLineEdit {
                padding-top: 2px;
                padding-right: 25px;
                padding-bottom: 2px;
                border-top-right-radius: 5px;
                border-bottom-right-radius: 5px;
                border-top-left-radius: 5px;
                border-bottom-left-radius: 5px;
                color: #fff;
            }

            QLabel#search_icon {
                margin-right: 5px;
            }
        """)

        self.setIconSize(QSize(14, 14))

        button_back = self.addAction("Back")
        button_back.setIcon(QIcon("assets/icons/arrow-left.svg"))
        button_back.setToolTip("Back")
        button_back.triggered.connect(self.parent.main.back)

        button_forward = self.addAction("Forward")
        button_forward.setIcon(QIcon("assets/icons/arrow-right.svg"))
        button_forward.setToolTip("Forward")
        button_forward.triggered.connect(self.parent.main.forward)

        button_refresh = self.addAction("Refresh")
        button_refresh.setIcon(QIcon("assets/icons/refresh.svg"))
        button_refresh.setToolTip("Refresh Page")
        button_refresh.triggered.connect(self.parent.main.reload)

        label = QLabel()
        label.setPixmap(QIcon("assets/icons/search.svg").pixmap(QSize(12, 12)))
        label.setObjectName("search_icon")
        self.addWidget(label)

        self.url_edit = QLineEdit()
        self.url_edit.returnPressed.connect(lambda: self.parent.main.navigate(self.url_edit.text()))
        self.url_edit.setPlaceholderText("Start your search using google.com or enter the site's URL...")
        self.url_edit.setFont(QFont("Poppins", 11))
        self.addWidget(self.url_edit)

        menu_icon = QIcon("assets/icons/qmenuicons/more_vert.svg")
        self.menu_button = QToolButton(self)
        self.menu_button.setIcon(menu_icon)
        self.menu_button.setToolTip("Menu")
        self.menu_button.clicked.connect(self.show_menu)
        self.menu_button.setIconSize(QSize(90, 90))
        self.addWidget(self.menu_button)

    def show_menu(self):
        try:
            menu = QMenu(self)

            new_tab_action = QAction("New Tab", self)
            about_action = QAction("About", self)
            about_action.triggered.connect(self.show_about_dialog)

            new_tab_action.triggered.connect(self.new_tab)

            menu.addAction(new_tab_action)
            menu.addSeparator()
            menu.addAction(about_action)

            source_action = QAction("Source", self)
            source_action.triggered.connect(lambda: webbrowser.open("https://github.com/dan55800todm/lampbrowserlfs"))
            menu.addAction(source_action)

            # Применяем стиль к меню
            menu.setStyleSheet("""
                QMenu {
                    background-color: #282a36;
                    color: #f8f8f2;
                    border: 1px solid #44475a;
                }

                QMenu::item {
                    background-color: transparent;
                    padding: 5px 20px;
                }

                QMenu::item:selected {
                    background-color: #44475a;
                }

                QMenu::separator {
                    height: 1px;
                    background: #44475a;
                    margin: 5px 0;
                }
            """)

            pos = self.menu_button.mapToGlobal(self.menu_button.rect().bottomLeft())
            menu.exec(pos)
        except Exception as e:
            print(f"Error displaying menu: {e}")

    def show_about_dialog(self):
        about_dialog = AboutDialog()
        about_dialog.exec()

    def new_tab(self):
        self.parent.main.add_tab()


class Main:
    def __init__(self, parent):
        self.parent = parent