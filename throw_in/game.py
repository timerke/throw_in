from PyQt5.QtWidgets import QVBoxLayout, QWidget
from throw_in.graphicswidget import GraphicsWidget


class Game(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self._init_ui()

    def _init_ui(self) -> None:
        self.field: GraphicsWidget = GraphicsWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.field)
        self.setLayout(layout)
