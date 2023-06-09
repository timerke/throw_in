from PyQt5.QtCore import pyqtSlot, Qt, QTimer
from PyQt5.QtGui import QBrush, QColor, QResizeEvent
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QSizePolicy


class GraphicsWidget(QGraphicsView):

    def __init__(self) -> None:
        super().__init__()
        self._timer: QTimer = QTimer()
        self._timer.setInterval(50)
        self._timer.setSingleShot(True)
        self._timer.timeout.connect(self.draw_scene)

        self._init_ui()
        self._timer.start()
        self.show()

    def _init_ui(self) -> None:
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))

        self.screen: QGraphicsScene = QGraphicsScene()
        self.screen.setBackgroundBrush(QBrush(QColor("white")))
        self.setScene(self.screen)

    @pyqtSlot()
    def draw_scene(self) -> None:
        self.screen.setSceneRect(0, 0, self.width(), self.height())

    def resizeEvent(self, event: QResizeEvent) -> None:
        self._timer.start()
        super().resizeEvent(event)
