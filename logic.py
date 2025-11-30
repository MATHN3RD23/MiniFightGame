from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_gameWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__scene = "start"

  
    def starting_screen(self):
        pass

    def exit_screen(self):
        pass

    def battle_screen(self):
        pass

    def fight_screen(self):
        pass

    def item_screen(self):
        pass

    def mercy_screen(self):
        pass

    def enemy_attack(self):
        pass

