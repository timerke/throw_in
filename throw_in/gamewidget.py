from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget
from throw_in.graphicswidget import GraphicsWidget


class GameWidget(QWidget):

    HORIZONTAL_CELLS: int = 50
    VERTICAL_CELLS: int = 50
    stop_signal: pyqtSignal = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self._init_ui()

    def _init_ui(self) -> None:
        self.graphics_widget: GraphicsWidget = GraphicsWidget()
        self.button_stop: QPushButton = QPushButton("Stop")
        self.button_stop.clicked.connect(self.stop_game)

        layout = QVBoxLayout()
        layout.addWidget(self.graphics_widget)
        layout.addWidget(self.button_stop, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

    @pyqtSlot()
    def stop_game(self) -> None:
        self.stop_signal.emit()
