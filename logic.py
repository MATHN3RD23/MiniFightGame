from unittest import result

from PyQt6.QtWidgets import *

from gui import *
from fighter import *
import csv


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
        self.__scene = 0
        self.update("-", "PRESS TO START", "-", "Starting screen...")

    def exit_screen(self, type):
        #0 = enemy mercy, 1 = player mercy, 2 = enemy KO, 3 = player KO
        self.__scene = 99
        self.EnemyHPbar.setValue(self.enemy.get_hp())
        self.PlayerHPbar.setValue(self.player.get_hp())

        self.FirstButton.setText("SAVE DATA")
        self.SecindButton.setText("-")
        self.ThirdButton.setText("RESTART")


        if type == 0:
            self.TextLabel.setText("The player made the enemy retreat!")
        elif type == 1:
            self.TextLabel.setText("The enemy made the player retreat!")
        elif type == 2:
            self.TextLabel.setText("The enemy fainted!")
        elif type == 3:
            self.TextLabel.setText("The player fainted!")


    def saveData(self):
        with open('C:/Users/emool/OneDrive/Desktop/CS2/MiniFightGame/gameResults.csv', 'a', newline='') as output_csv_file:
            print('here in file')
            content = csv.writer(output_csv_file)

            content.writerow(["player", self.player.strGetData()])
            content.writerow(["enemy", self.enemy.strGetData()])



    def battle_screen(self):
        self.__scene = 1
        self.update("FIGHT", "ITEM", "MERCY", "CHOOSE AN ACTION!")

    def fight_screen(self):
        self.__scene = 2
        self.update("PUNCH", "KICK", "FIREBALL", "CHOOSE AN ATTACK!")

    def item_screen(self):
        self.__scene = 3
        self.update("POTION", "BERRY", "POISON", "CHOOSE AN ITEM!")

    def mercy_screen(self):
        self.__scene = 4
        self.update("'hey buddy'", "'you look good fighting'", "*do a cool dance move*", "CHOOSE AN ACTION!")

    def player_results(self, text):
        self.__scene = 5
        self.update("-", "RESULTS", "-", text)

    def enemy_attack(self):
        self.__scene = 6
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
        elif self.__scene == 99:
            self.saveData()

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
        elif self.__scene == 99:
            self.newGame()

