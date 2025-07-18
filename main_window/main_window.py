"""
Main window using PyQt6.
Sections: field graphics, game controls and settings,
game informations and robots informations,
log and game mode selection.
"""

import math
import typing
import os
from PyQt6.QtWidgets import (
    QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QGridLayout, QSizePolicy
)
from PyQt6.QtGui import QFont, QIcon, QPalette, QColor
from PyQt6.QtCore import Qt, QTimerEvent
from entities import Match
from main_window.widgets import *

class SSLPanel(QWidget):
    context: Match = None
    updatable_components = []

    def __init__(self, context: Match, s_width, s_height):
        super(SSLPanel, self).__init__()

        self.context = context
        self.screen_width = s_width
        self.screen_height = s_height

        # Organizing the layout
        # Vertical layout divided into top section
        # for controls and a bottom section for the
        # field visualization and informations.
        window_layout = QVBoxLayout()
        
        # Log widget displaying errors and warning messages
        self.log_widget = Log()
        # self.log_widget.add_message("")

        # Height of the top widgets
        h = int(self.screen_height/10)
        
        # Adding game status widget
        self.game_status_widget = GameStatus(self.context, self.log_widget, self)
        self.game_status_widget.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed))
        self.game_status_widget.setFixedHeight(int(h*0.6))
        # self.updatable_components.append(self.game_status_widget)
        
        # Adding game controls widget
        self.game_controls_widget = GameControls(self.context, self.log_widget, self)
        self.game_controls_widget.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed))
        self.game_controls_widget.setFixedHeight(int(h*2.45))
        self.updatable_components.append(self.game_controls_widget)

        # Adding game fouls section
        self.fouls_widget = Fouls(self.context, self.log_widget, self)
        self.fouls_widget.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed))
        self.fouls_widget.setFixedHeight(int(h*1.8))

        # Top section with buttons
        top_h_layout = QHBoxLayout()
        top_v_layout = QVBoxLayout()

        top_v_layout.addWidget(self.fouls_widget)
        top_v_layout.addWidget(self.game_status_widget)

        top_h_layout.addLayout(top_v_layout, stretch=2)
        top_h_layout.addWidget(self.game_controls_widget, stretch=1)
        window_layout.addLayout(top_h_layout)

        # Lower section with field visualization,
        # robot informations, game informations and fouls
        bottom_h_layout = QHBoxLayout()
        self.field_vis = FieldView(self.context)
        bottom_h_layout.addWidget(self.field_vis, stretch=1)

        # GUI mode and NeonFC informations displayed
        # in a grid (10 rows, 6 columns)
        grid = QGridLayout()
        grid.setContentsMargins(0,0,0,0)

        # Widget to select goalkeeper by robot_id
        # self.gk_widget = GoalkeeperID(self.context, self.log_widget)
        # self.updatable_components.append(self.gk_widget)

        # grid.addWidget(self.gk_widget, 0, 3, 1, 3) # starts at row:0, column:3, spans 1 row, spans 3 columns

        # Widget to choose game mode
        self.mode_widget = GameMode(self.context, self.log_widget)
        grid.addWidget(self.mode_widget, 0, 3, 1, 3) # starts at row:0, column:3, spans 1 row, spans 3 columns

        # NeonFC's informations
        self.game_info_widget = GameInfo()
        grid.addWidget(self.game_info_widget, 1, 3, 4, 3)
        self.updatable_components.append(self.game_info_widget)

        # Add log widget to grid
        grid.addWidget(self.log_widget, 5, 3, 5, 3)

        # Robots' informations section
        self.robots_widget = RobotsInfo(self.context)
        grid.addWidget(self.robots_widget, 0, 0, 10, 3)
        self.updatable_components.append(self.robots_widget)

        # Adding grid on a widget for better control of its alignment
        grid_widget = QWidget()
        grid_widget.setLayout(grid)

        bottom_h_layout.addWidget(grid_widget, alignment=Qt.AlignmentFlag.AlignRight)
        window_layout.addLayout(bottom_h_layout)

        self.setLayout(window_layout)

        # Creates the timer that refreshes interface components periodically
        self.startTimer(math.ceil(100 / 3))

        # Creates the timer that refreshes interface components periodically
        self.startTimer(math.ceil(100 / 3))

    def timerEvent(self, event: typing.Optional['QTimerEvent']) -> None:
        for component in self.updatable_components:
            component.update_info(self.context)

class MainWindow(QMainWindow):
    def __init__(self, context: Match, s_width = 1200, s_height = 900):
        # Create application's GUI
        super(MainWindow, self).__init__()
        self.setWindowTitle("Neon SSL")

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#F9F9F9"))
        self.setPalette(palette)

        self.path_to_icons = os.getcwd()+"/main_window/images/"
        icon = QIcon(self.path_to_icons+"neon_green_logo.png")
        self.setWindowIcon(icon)

        self.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))

        # Puts the given match as context for interface display sync
        self.context = context

        self.screen_width = s_width
        self.screen_height = s_height

        self.window_width = 1000
        self.window_height = 800
        self.setGeometry(100, 100, int(self.screen_width/2), int(self.screen_height/2))
        self.setFont(QFont('Arial', 15))

        # Parent widget to hold all widgets on the main screen
        self.main_widget = SSLPanel(self.context, self.screen_width, self.screen_height)

        self.setCentralWidget(self.main_widget)
