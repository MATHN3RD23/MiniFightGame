from unittest import result

from PyQt6.QtWidgets import *

from gui import *
from fighter import *

class Logic(QMainWindow, Ui_gameWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__scene = 0
        # 0 = starting, 1 = battle, 2 = attack, 3 = item, 4 = mercy, 5 = player results, 6 enemy attack, 99 = exit

        self.FirstButton.clicked.connect(self.clickedA)
        self.SecindButton.clicked.connect(self.clickedB)
        self.ThirdButton.clicked.connect(self.clickedC)
        self.player = Fighter("none")
        self.enemy = Fighter("none")
        self.starting_screen()



    def newGame(self):
        self.player = Fighter("player")
        self.enemy = Fighter("enemy")
        self.battle_screen()


    def starting_screen(self):
        self.update("-", "PRESS TO START", "-", "Starting screen...")
        self.__scene = 0

    def exit_screen(self, type):
        #0 = enemy mercy, 1 = player mercy, 2 = enemy KO, 3 = player KO
        print("here")
        self.__scene = 99
        self.FirstButton.setText("DATA SAVED")
        self.SecindButton.setText("-")
        self.ThirdButton.setText("RESTART")

        self.EnemyHPbar.setValue(self.enemy.get_hp())
        self.PlayerHPbar.setValue(self.player.get_hp())
        print("and here")
        if type == 0:
            self.TextLabel.setText("")
        elif type == 1:
            self.TextLabel.setText("")
        elif type == 2:
            self.TextLabel.setText("")
        elif type == 3:
            self.TextLabel.setText("")
        self.EnemyHPbar.setValue(self.enemy.get_hp())
        self.PlayerHPbar.setValue(self.player.get_hp())

        print("and maybe here also")


    def battle_screen(self):
        self.update("FIGHT", "ITEM", "MERCY", "CHOOSE AN ACTION!")
        self.__scene = 1

    def fight_screen(self):
        self.update("PUNCH", "KICK", "FIREBALL", "CHOOSE AN ATTACK!")
        self.__scene = 2

    def item_screen(self):
        self.update("POTION", "BERRY", "POISON", "CHOOSE AN ITEM!")
        self.__scene = 3

    def mercy_screen(self):
        self.update("'hey buddy'", "'you look good fighting'", "*do a cool dance move*", "CHOOSE AN ACTION!")
        self.__scene = 4

    def player_results(self, text):
        self.update("-", "result", "-", text)
        self.__scene = 5

    def enemy_attack(self):
        results = self.enemy.use_random_action()
        choice = results[0]
        if choice == 1:
            if results[1][0]:
                self.exit_screen(1)
            else:
                self.update("-", "RESULT", "-", results[1][1])
        elif choice == 2 or choice == 3:
            self.update("-", "RESULT", "-", results[1])
        elif choice == 4 or choice == 5:
            self.player.take_damage(results[1][0])
            self.update("-", "RESULT", "-", results[1][1])
        self.__scene = 6

    def update(self, a, b, c, text) -> None:
        """
        method to update screen
        :param a: first button text
        :param b: second button text
        :param c: third button text
        :param text: flavor text
        """


        self.FirstButton.setText(a)
        self.SecindButton.setText(b)
        self.ThirdButton.setText(c)
        self.TextLabel.setText(text)
        self.EnemyHPbar.setValue(self.enemy.get_hp())
        self.PlayerHPbar.setValue(self.player.get_hp())

        if self.player.get_hp() < 0:
            self.exit_screen(3)
        if self.enemy.get_hp() < 0:
            self.exit_screen(2)
        pass

    def clickedA(self):
        if self.__scene == 1:
            self.fight_screen()
        elif self.__scene == 2:
            result = self.player.attack(1)
            self.enemy.take_damage(result[0])
            self.player_results(result[1])
        elif self.__scene == 3:
            result = self.player.use_potion()
            self.player_results(result)
        elif self.__scene == 4:
            result = self.player.mercey(random.randint(1, 10))
            if result[0]:
                self.exit_screen(0)
            else:
                self.player_results(result[1])
        elif self.__scene == 5:
            self.enemy_attack()
        elif self.__scene == 6:
            self.battle_screen()

    def clickedB(self):
        if self.__scene == 0:
            self.newGame()
        elif self.__scene == 1:
            self.item_screen()
        elif self.__scene == 2:
            result = self.player.attack(2)
            self.enemy.take_damage(result[0])
            self.player_results(result[1])
        elif self.__scene == 3:
            result = self.player.use_berry()
            self.player_results(result)
        elif self.__scene == 4:
            result = self.player.mercey(random.randint(1, 10))
            if result[0]:
                self.exit_screen(0)
            else:
                self.player_results(result[1])
        elif self.__scene == 5:
            self.enemy_attack()
        elif self.__scene == 6:
            self.battle_screen()

    def clickedC(self):
        if self.__scene == 1:
            self.mercy_screen()
        elif self.__scene == 2:
            result = self.player.attack(3)
            self.enemy.take_damage(result[0])
            self.player_results(result[1])
        elif self.__scene == 3:
            result = self.player.use_poison()
            self.enemy.take_damage(result[0])
            self.player_results(result[1])
        elif self.__scene == 4:
            result = self.player.mercey(random.randint(1, 15))
            if result[0]:
                self.exit_screen(0)
            else:
                self.player_results(result[1])
        elif self.__scene == 5:
            self.enemy_attack()
        elif self.__scene == 6:
            self.battle_screen()

