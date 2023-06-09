import os
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from throw_in.game import Game
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
        self.game: Game = Game()
        self.game.setVisible(False)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.menu_widget)
        v_layout.addWidget(self.game)
        widget = QWidget()
        widget.setLayout(v_layout)
        self.setCentralWidget(widget)

    def start_game(self) -> None:
        self.menu_widget.setVisible(False)
        self.game.setVisible(True)
