import os
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from throw_in.gamewidget import GameWidget
from throw_in.menuwidget import MenuWidget
from version import VERSION


class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self._dir_media: str = "media"
        self._init_ui()

    def _init_ui(self) -> None:
        self.setWindowTitle(f"ThrowIn v{VERSION}")
        self.setWindowIcon(QIcon(os.path.join(self._dir_media, "throw.png")))

        self.menu_widget: MenuWidget = MenuWidget(self._dir_media, VERSION)
        self.menu_widget.exit_signal.connect(self.close)
        self.menu_widget.start_signal.connect(self.start_game)
        self.game_widget: GameWidget = GameWidget()
        self.game_widget.stop_signal.connect(lambda: self.show_menu(True))

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.menu_widget)
        v_layout.addWidget(self.game_widget)
        widget = QWidget()
        widget.setLayout(v_layout)
        self.setCentralWidget(widget)
        self.show_menu(True)

    def start_game(self) -> None:
        self.show_menu(False)

    @pyqtSlot()
    def show_menu(self, show: bool) -> None:
        self.game_widget.setVisible(not show)
        self.menu_widget.setVisible(show)
