"""
Section of the GUI where the field is displayed.
"""

from PyQt6 import QtGui
from PyQt6.QtCore import QTimerEvent
from PyQt6.QtWidgets import QLabel, QWidget
from PyQt6.QtGui import QPalette, QColor

from entities import Match

class FieldView(QWidget):
    def __init__(self, context: Match):
        super().__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor('#D7C3F1'))
        self.setPalette(palette)
        self.setMinimumWidth(400)
        QLabel("<h5>Espaço reservado<br>para o campo!</h5>", parent=self)
