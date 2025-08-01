"""
Section of the main window where the
match's controls will be displayed.
"""

import os
from PyQt6.QtWidgets import (
    QWidget, QPushButton, QLabel, QComboBox, QLineEdit,
    QHBoxLayout, QVBoxLayout, QGridLayout, QSizePolicy
)
from PyQt6.QtGui import QPalette, QColor, QFont, QIcon
from PyQt6.QtCore import QSize, Qt
from entities.match import Match
from main_window.widgets.log import Log

"""
██████╗░░█████╗░██████╗░░█████╗░███╗░░░███╗███████╗████████╗███████╗██████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗████╗░████║██╔════╝╚══██╔══╝██╔════╝██╔══██╗██╔════╝
██████╔╝███████║██████╔╝███████║██╔████╔██║█████╗░░░░░██║░░░█████╗░░██████╔╝╚█████╗░
██╔═══╝░██╔══██║██╔══██╗██╔══██║██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══╝░░██╔══██╗░╚═══██╗
██║░░░░░██║░░██║██║░░██║██║░░██║██║░╚═╝░██║███████╗░░░██║░░░███████╗██║░░██║██████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░
"""

class ControlParams(QWidget):
    """
    Additional window to show the robot's control parameters.
    """

    def __init__(self, context: Match, log: Log, param_list=[]):
        super().__init__()
        self.setMaximumWidth(0) # Total width of its children
        self.setMaximumHeight(0) # Total height of its children
        self.setWindowTitle("Control Parameters")
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor('#D7C3F1'))
        self.setPalette(palette)

        self.context = context
        self.log = log

        # v_layout = QVBoxLayout()
        # v_layout.addWidget(QLabel("<h3> Parâmetros do controle dos robôs </h3>", parent=self), alignment=Qt.AlignmentFlag.AlignHCenter)

        # self.setLayout(v_layout)

        # param_list = [KP, KI, KD, K_W, R_M, V_M]
        # TODO get parm_list once when comunication with NeonFC is stablished?
        # TODO change param_list to a dictionary
        if param_list:
            pid_kp = param_list[0]
            ki = param_list[1]
            kd = param_list[2]
            kw = param_list[3]
            rm = param_list[4]
            vm = param_list[5]
            uni_kp = param_list[6]
            {"pid_kp":pid_kp, "ki":ki, "kd":kd, "kw":kw, "rm":rm, "vm":vm, "uni_kp":uni_kp}
        else:
            # Default parameters:
            # TODO button to change default
            # TODO save default parameters on a file
            pid_kp = 1
            ki = 0
            kd = 0
            kw = 3.5
            rm = 0.44
            vm = 0.5
            uni_kp = 1
            self.parameters = {"pid_kp":pid_kp, "ki":ki, "kd":kd, "kw":kw, "rm":rm, "vm":vm, "uni_kp":uni_kp}
            msg = f"Parâmetros padrão:\nPID_KP={str(pid_kp)};  KI={str(ki)};  KD={str(kd)};  KW={str(kw)};  RM={str(rm)};  VM={str(vm)}; UNI_KP ={str(uni_kp)}"
            print(msg)
            self.log.add_message(msg)
            # TODO show this message on log?
            # TODO send info to Info_Api

        # Creating QLineEdits for each parameter
        self.pid_kp_line = QLineEdit()
        self.pid_kp_line.setText(str(self.parameters["pid_kp"]))
        self.pid_kp_line.setFixedWidth(60)

        self.ki_line = QLineEdit()
        self.ki_line.setText(str(self.parameters["ki"]))
        self.ki_line.setFixedWidth(60)

        self.kd_line = QLineEdit()
        self.kd_line.setText(str(self.parameters["kd"]))
        self.kd_line.setFixedWidth(60)

        self.kw_line = QLineEdit()
        self.kw_line.setText(str(self.parameters["kw"]))
        self.kw_line.setFixedWidth(60)

        self.rm_line = QLineEdit()
        self.rm_line.setText(str(self.parameters["rm"]))
        self.rm_line.setFixedWidth(60)

        self.vm_line = QLineEdit()
        self.vm_line.setText(str(self.parameters["vm"]))
        self.vm_line.setFixedWidth(60)

        self.uni_kp_line = QLineEdit()
        self.uni_kp_line.setText(str(self.parameters["uni_kp"]))
        self.uni_kp_line.setFixedWidth(60)

        v_layout = QVBoxLayout()
        v_layout.addWidget(QLabel("<h3> Parâmetros do controle dos robôs </h3>", parent=self), alignment=Qt.AlignmentFlag.AlignHCenter)

        # Display parameters in a table?
        self.params_table = QGridLayout()

        # Table labels
        self.params_table.addWidget(QLabel("PID_KP", parent=self), 0, 0, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.params_table.addWidget(QLabel("KI", parent=self), 0, 1, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.params_table.addWidget(QLabel("KD", parent=self), 0, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.params_table.addWidget(QLabel("K_W", parent=self), 0, 3, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.params_table.addWidget(QLabel("R_M", parent=self), 0, 4, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.params_table.addWidget(QLabel("V_M", parent=self), 0, 5, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.params_table.addWidget(QLabel("UNI_KP", parent=self), 0, 6, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Table values
        self.params_table.addWidget(self.pid_kp_line, 1, 0, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.params_table.addWidget(self.ki_line, 1, 1, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.params_table.addWidget(self.kd_line, 1, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.params_table.addWidget(self.kw_line, 1, 3, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.params_table.addWidget(self.rm_line, 1, 4, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.params_table.addWidget(self.vm_line, 1, 5, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.params_table.addWidget(self.uni_kp_line, 1, 6, alignment=Qt.AlignmentFlag.AlignHCenter)


        v_layout.addLayout(self.params_table)

        # Button to change values
        self.btn_change_params = QPushButton(text="Alterar parâmetros")
        self.btn_change_params.setFixedWidth(180)
        self.btn_change_params.setFixedHeight(30)
        self.btn_change_params.clicked.connect(self.changeParams)
        v_layout.addWidget(self.btn_change_params, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.setLayout(v_layout)
    
    def changeParams(self):
        pid_kp = self.pid_kp_line.text()
        ki = self.ki_line.text()
        kd = self.kd_line.text()
        kw = self.kw_line.text()
        rm = self.rm_line.text()
        vm = self.vm_line.text()
        uni_kp = self.uni_kp_line.text()

        # Validando os valores dos parametros
        # KP, KI, KD >= 0
        # KW, RM, VM > 0
        params = [pid_kp, ki, kd, kw, rm, vm, uni_kp]
        value_error = False
        for i in range(7):
            if self.is_float(params[i]):
                params[i] = float(params[i])
            else:
                value_error = True
        
        pid_kp = params[0]
        ki = params[1]
        kd = params[2]
        kw = params[3]
        rm = params[4]
        vm = params[5]
        uni_kp = params[6]
        
        if value_error:
            print("Todos os parâmetros devem conter valores numéricos.")
        else:
            if pid_kp < 0 or ki < 0 or kd < 0:
                print("PID_KP, KI e KD devem ter valores não negativos.")
            elif kw <= 0 or rm <= 0 or vm <= 0 or uni_kp < 0:
                print("K_W, R_M e V_M devem ter valores positivos. UNI_KP deve ter valor não negativo.")
            else:
                self.parameters = {"pid_kp":pid_kp, "ki":ki, "kd":kd, "kw":kw, "rm":rm, "vm":vm, "uni_kp":uni_kp}
                msg = f"Parâmetros atuais:\nPID_KP={str(pid_kp)};  KI={str(ki)};  KD={str(kd)};  KW={str(kw)};  RM={str(rm)};  VM={str(vm)}; UNI_KP = {str(uni_kp)}"
                print(msg)
                self.log.add_message(msg)
                self.context.set_control_parameters(self.parameters)
        # TODO show these messages on log
    
    def is_float(self, string):
        try:
            # Return true if float
            float(string)
            return True
        except ValueError:
            # Return False if Error
            return False

"""
░██████╗░░█████╗░███╗░░░███╗███████╗      ░█████╗░░█████╗░███╗░░██╗████████╗██████╗░░█████╗░██╗░░░░░░██████╗
██╔════╝░██╔══██╗████╗░████║██╔════╝      ██╔══██╗██╔══██╗████╗░██║╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝
██║░░██╗░███████║██╔████╔██║█████╗░░      ██║░░╚═╝██║░░██║██╔██╗██║░░░██║░░░██████╔╝██║░░██║██║░░░░░╚█████╗░
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░      ██║░░██╗██║░░██║██║╚████║░░░██║░░░██╔══██╗██║░░██║██║░░░░░░╚═══██╗
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗      ╚█████╔╝╚█████╔╝██║░╚███║░░░██║░░░██║░░██║╚█████╔╝███████╗██████╔╝
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝      ░╚════╝░░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚══════╝╚═════╝░
"""

class GameControls(QWidget):
    def __init__(self, context: Match, log: Log, parent_panel):
        super(GameControls, self).__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor('#D7C3F1'))
        self.setPalette(palette)

        self.context = context
        self.log = log
        self.parent_panel = parent_panel

        parent_width = self.parent_panel.width()
        parent_height = self.parent_panel.height()

        # Creating buttons to change color and side
        self.current_color = 'blue'
        self.current_side = 'left'

        # To add icon to the button we will use the QIcon object, which
        # gets the path to an SVG image
        self.path_to_icons = os.getcwd()+"/main_window/images/"

        self.btn_change_color = QPushButton(icon=QIcon(self.path_to_icons+"blue.svg"), text="Mudar Cor  ", parent=self)
        self.btn_change_color.clicked.connect(self.change)

        self.btn_change_side = QPushButton(icon=QIcon(self.path_to_icons+"left.svg"), text="Mudar Lado", parent=self)
        self.btn_change_side.clicked.connect(self.change)

        # Creating coach drop-down selection
        if context.coach_list:
            self.coach_list = context.coach_list
        else:
            self.coach_list = ['No coach found']
        
        if context.coach_name != None:
            self.current_coach = context.coach_name
        else:
            self.current_coach = self.coach_list[0]

        # Function to find current coach's index in coach_list
        coach_index = self.get_coach_index(self.current_coach)

        # Display this info on this gui's log section
        msg = f"Coach atual: {self.current_coach}"
        print(msg)
        self.log.add_message(msg)

        coach_section = QWidget()
        coach_section.setFixedHeight(70) 
        coach_section.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        coach_layout = QVBoxLayout()
        # coach_layout.setSpacing(0)
        lbl_coach = QLabel("Coach", parent=self)
        lbl_coach.setFont(QFont('Arial', 14))
        # coach_layout.addWidget(lbl_coach, alignment=Qt.AlignmentFlag.AlignHCenter)
        coach_layout.addWidget(lbl_coach, alignment=Qt.AlignmentFlag.AlignLeft)

        self.btn_coach = QComboBox()
        self.btn_coach.setFixedHeight(28)
        self.btn_coach.setMinimumWidth(200)
        # self.btn_coach.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        # self.btn_coach.setSizePolicy(QSizePolicy.horizontalStretch)
        self.btn_coach.addItems(self.coach_list)
        # select current coach
        self.btn_coach.setCurrentIndex(coach_index)
        self.btn_coach.activated.connect(self.select_coach)
        coach_layout.addWidget(self.btn_coach)
        coach_section.setLayout(coach_layout)

        """
        Adding parameters' window
        param_list = [pid_kp, ki, kd, kw, rm, vm, uni_kp]
        """
        params=[] # TODO receive params or get this from info object? Change it to dict?
        self.params_window = ControlParams(self.context, self.log, params)

        # Button to open parameter settings' window
        self.btn_params = QPushButton(text="Parâmetros", parent=self)
        self.btn_params.clicked.connect(self.toggle_params)

        # Goalkeeper ID selection section
        self.gk_id = self.context.gk_id
        self.lbl_gk = QLabel(("Goalkeeper ID: " + str(self.gk_id)), parent=self)
        self.lbl_gk.setFont(QFont('Arial', 14))
        self.btn_gk = QComboBox()
        self.btn_gk.setFixedHeight(28)
        self.btn_gk.setFixedWidth(70)
        # self.btn_gk.setSizePolicy(QSizePolicy.horizontalStretch)
        self.robots_ids_str = []
        for r_id in self.context.robots_ids:
            self.robots_ids_str.append(str(r_id))
        # print(self.robots_ids_str)
        self.btn_gk.addItems(self.robots_ids_str)
        # Select current gk
        # self.btn_gk.setCurrentIndex(r_index)
        self.btn_gk.activated.connect(self.select_gk)
        self.gk_section = QWidget()
        self.gk_section.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        gk_layout = QVBoxLayout()
        gk_layout.addWidget(self.lbl_gk, alignment=Qt.AlignmentFlag.AlignLeft)
        gk_layout.addWidget(self.btn_gk)
        self.gk_section.setLayout(gk_layout)

        # Adding buttons to layout
        # layout = QVBoxLayout()
        # widget_label = QLabel("Controles da partida:")
        # widget_label.setFixedHeight(int(int(parent_height/8)/1.8))
        # layout.addWidget(widget_label, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Buttons displayed in a grid
        grid = QGridLayout()
        grid.addWidget(coach_section, 0, 0, 1, 2) # row:0, column:0, spans 1 row, spans 2 columns
        grid.addWidget(self.gk_section, 1, 0)
        grid.addWidget(self.btn_params, 1, 1)
        # grid.addWidget(self.lbl_gk, 1, 1)
        # grid.addWidget(self.btn_gk, 1, 2)
        grid.addWidget(self.btn_change_side, 2, 0)
        grid.addWidget(self.btn_change_color, 2, 1)
        # grid.setColumnStretch(0, 2)
        # grid.setColumnStretch(1, 2)
        # grid.setColumnStretch(2, 2)
        # grid.setColumnStretch(3, 3)
        grid.setColumnMinimumWidth(0, 150)
        grid.setColumnMinimumWidth(1, 150)
        # grid.setRowStretch(0, 1)
        # grid.setRowStretch(1, 2)
        # grid.setRowStretch(2, 2)
        # layout.addLayout(grid, stretch=1)
        
        # self.setLayout(layout)
        self.setLayout(grid)

    def change(self):
        sender = self.sender()

        if sender is self.btn_change_color:
            if self.current_color == 'blue':
                sender.setIcon(QIcon(self.path_to_icons+"yellow.svg"))
                self.current_color = 'yellow'
                self.log.add_message("A cor do time foi alterada para: Amarelo")
            else:
                sender.setIcon(QIcon(self.path_to_icons+"blue.svg"))
                self.current_color = 'blue'
                self.log.add_message("A cor do time foi alterada para: Azul")
            self.context.set_team_color(self.current_color)
        elif sender is self.btn_change_side:
            if self.current_side == 'left':
                sender.setIcon(QIcon(self.path_to_icons+"right.svg"))
                self.current_side = 'right'
                self.log.add_message("O lado foi alterado para: Direita")
            else:
                sender.setIcon(QIcon(self.path_to_icons+"left.svg"))
                self.current_side = 'left'
                self.log.add_message("O lado foi alterado para: Esquerda")
            self.context.set_team_side(self.current_side)

    def get_coach_index(self, coach):
        for i in range(len(self.coach_list)):
            if self.coach_list[i] == coach:
                return i
        return 0
    
    def select_coach(self):
        coach_name = self.btn_coach.currentText()
        self.current_coach = coach_name
        self.context.coach_name = coach_name
        msg = f"Coach atual:\n{coach_name}"
        print(msg)
        self.log.add_message(msg)

    def toggle_params(self):
        if self.params_window.isVisible():
            self.params_window.hide()
        else:
            self.params_window.show()
    
    def select_gk(self):
        id_str = self.btn_gk.currentText()
        self.context.set_gk_id(int(id_str))

    def update_info(self, status: Match):
        coach = status.coach_name
        if coach != None and coach != self.current_coach:
            self.current_coach = coach
            msg = f"Coach atual:\n{self.current_coach}"
            print(msg)
            self.log.add_message(msg)
        
        if status.coach_list != self.coach_list:
            self.coach_list = status.coach_list
            # Repopulate coach's dropdown button
            self.btn_coach.clear()
            self.btn_coach.addItems(self.coach_list)

        coach_index = self.get_coach_index(self.current_coach)
        self.btn_coach.setCurrentIndex(coach_index)

        self.gk_id = status.gk_id
        self.lbl_gk.setText(("Goalkeeper ID: " + str(self.gk_id)))
    
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_button_sizes()
    
    def update_button_sizes(self):
        w = self.width()
        h = self.height()
        
        icon_size = QSize(int(h/6.5), int(h/6.5))
        btn_size = QSize(int(w/(8)), int(h/5))
        font_size = int(h/19)
        
        for btn in [self.btn_change_color, self.btn_change_side, self.btn_params]:
            if btn:
                btn.setIconSize(icon_size)
                btn.setMinimumSize(btn_size)
                btn.setMaximumHeight(btn_size.height())
                btn.setFont(QFont('Arial', font_size))
                btn.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
