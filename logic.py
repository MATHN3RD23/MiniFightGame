from unittest import result

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import *

from gui import *
from fighter import *
import csv

"""
NOTE: the images used are implemented with absolute path and may need re-worked with implementing
lines of occurance:
35, 40, 45, 50, 55, 60; 67, 72, 77, 82, 87, 92
"""


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
        self.TextLabel.setWordWrap(True)

        #the following section: setting up scenes with all the images for the graphics

        self.player_basic = QGraphicsScene(0, 0, 250, 250)
        pixmap_one = QPixmap("C:/Users/emool/OneDrive/Desktop/CS2/MiniFightGame/pBasic.png")
        pixmap_pBasic_item = self.player_basic.addPixmap(pixmap_one)
        pixmap_pBasic_item.setPos(0, 0)

        self.player_attack = QGraphicsScene(0, 0, 250, 250)
        pixmap_two = QPixmap("C:/Users/emool/OneDrive/Desktop/CS2/MiniFightGame/pAttack.png")
        pixmap_pAttack_item = self.player_attack.addPixmap(pixmap_two)
        pixmap_pAttack_item.setPos(0, 0)

        self.player_faint = QGraphicsScene(0, 0, 250, 250)
        pixmap_three = QPixmap("C:/Users/emool/OneDrive/Desktop/CS2/MiniFightGame/pfainted.png")
        pixmap_pFaint_item = self.player_faint.addPixmap(pixmap_three)
        pixmap_pFaint_item.setPos(0, 0)

        self.player_item = QGraphicsScene(0, 0, 250, 250)
        pixmap_four = QPixmap("C:/Users/emool/OneDrive/Desktop/CS2/MiniFightGame/pItem.png")
        pixmap_pItem_item = self.player_item.addPixmap(pixmap_four)
        pixmap_pItem_item.setPos(0, 0)

        self.player_mercy = QGraphicsScene(0, 0, 250, 250)
        pixmap_five = QPixmap("C:/Users/emool/OneDrive/Desktop/CS2/MiniFightGame/pMercy.png")
        pixmap_pMercy_item = self.player_mercy.addPixmap(pixmap_five)
        pixmap_pMercy_item.setPos(0, 0)

        self.player_retreat = QGraphicsScene(0, 0, 250, 250)
        pixmap_six = QPixmap("C:/Users/emool/OneDrive/Desktop/CS2/MiniFightGame/pRetreat.png")
        pixmap_pRetreat_item = self.player_retreat.addPixmap(pixmap_six)
        pixmap_pRetreat_item.setPos(0, 0)



        self.enemy_basic = QGraphicsScene(0, 0, 250, 250)
        pixmap_seven = QPixmap("C:/Users/emool/OneDrive/Desktop/CS2/MiniFightGame/eBasic.png")
        pixmap_eBasic_item = self.enemy_basic.addPixmap(pixmap_seven)
        pixmap_eBasic_item.setPos(0, 0)

        self.enemy_attacking = QGraphicsScene(0, 0, 250, 250)
        pixmap_eight = QPixmap("C:/Users/emool/OneDrive/Desktop/CS2/MiniFightGame/eAttack.png")
        pixmap_eAttack_item = self.enemy_attacking.addPixmap(pixmap_eight)
        pixmap_eAttack_item.setPos(0, 0)

        self.enemy_faint = QGraphicsScene(0, 0, 250, 250)
        pixmap_nine = QPixmap("C:/Users/emool/OneDrive/Desktop/CS2/MiniFightGame/eFainted.png")
        pixmap_eFaint_item = self.enemy_faint.addPixmap(pixmap_nine)
        pixmap_eFaint_item.setPos(0, 0)

        self.enemy_item = QGraphicsScene(0, 0, 250, 250)
        pixmap_ten = QPixmap("C:/Users/emool/OneDrive/Desktop/CS2/MiniFightGame/eitem.png")
        pixmap_eItem_item = self.enemy_item.addPixmap(pixmap_ten)
        pixmap_eItem_item.setPos(0, 0)

        self.enemy_mercy = QGraphicsScene(0, 0, 250, 250)
        pixmap_eleven = QPixmap("C:/Users/emool/OneDrive/Desktop/CS2/MiniFightGame/eMercy.png")
        pixmap_eMercy_item = self.enemy_mercy.addPixmap(pixmap_eleven)
        pixmap_eMercy_item.setPos(0, 0)

        self.enemy_reteat = QGraphicsScene(0, 0, 250, 250)
        pixmap_tweleve = QPixmap("C:/Users/emool/OneDrive/Desktop/CS2/MiniFightGame/eRetreat.png")
        pixmap_eRetreat_item = self.enemy_reteat.addPixmap(pixmap_tweleve)
        pixmap_eRetreat_item.setPos(0, 0)



    def newGame(self) -> None:
        self.player = Fighter("player")
        self.enemy = Fighter("enemy")
        self.playerGraphic.setScene(self.player_basic)
        self.EnemyGraphic.setScene(self.enemy_basic)
        self.battle_screen()


    def starting_screen(self) -> None:
        self.__scene = 0
        self.update("-", "PRESS TO START", "-", "Starting screen...")

    def exit_screen(self, type) -> None:
        """
        method to end the current game
        :param type: int telling which ending was recived
        """
        #0 = enemy mercy, 1 = player mercy, 2 = enemy KO, 3 = player KO
        self.__scene = 99
        self.EnemyHPbar.setValue(self.enemy.get_hp())
        self.PlayerHPbar.setValue(self.player.get_hp())

        self.FirstButton.setText("SAVE DATA")
        self.SecindButton.setText("-")
        self.ThirdButton.setText("RESTART")


        if type == 0:
            self.TextLabel.setText("The player made the enemy retreat!")
            self.playerGraphic.setScene(self.player_basic)
            self.EnemyGraphic.setScene(self.enemy_reteat)
        elif type == 1:
            self.TextLabel.setText("The enemy made the player retreat!")
            self.playerGraphic.setScene(self.player_retreat)
            self.EnemyGraphic.setScene(self.enemy_basic)
        elif type == 2:
            self.TextLabel.setText("The enemy fainted!")
            self.playerGraphic.setScene(self.player_basic)
            self.EnemyGraphic.setScene(self.enemy_faint)
        elif type == 3:
            self.TextLabel.setText("The player fainted!")
            self.playerGraphic.setScene(self.player_faint)
            self.EnemyGraphic.setScene(self.enemy_basic)


    def saveData(self) -> None:
        with open('C:/Users/emool/OneDrive/Desktop/CS2/MiniFightGame/gameResults.csv', 'a', newline='') as output_csv_file:
            print('here in file')
            content = csv.writer(output_csv_file)

            content.writerow(["player", self.player.strGetData()])
            content.writerow(["enemy", self.enemy.strGetData()])



    def battle_screen(self) -> None:
        self.playerGraphic.setScene(self.player_basic)
        self.EnemyGraphic.setScene(self.enemy_basic)
        self.__scene = 1
        self.update("FIGHT", "ITEM", "MERCY", "CHOOSE AN ACTION!")

    def fight_screen(self) -> None:
        self.playerGraphic.setScene(self.player_basic)
        self.EnemyGraphic.setScene(self.enemy_basic)
        self.__scene = 2
        self.update("PUNCH", "KICK", "FIREBALL", "CHOOSE AN ATTACK!")

    def item_screen(self) -> None:
        self.playerGraphic.setScene(self.player_basic)
        self.EnemyGraphic.setScene(self.enemy_basic)
        self.__scene = 3
        self.update("POTION", "BERRY", "POISON", "CHOOSE AN ITEM!")

    def mercy_screen(self) -> None:
        self.playerGraphic.setScene(self.player_basic)
        self.EnemyGraphic.setScene(self.enemy_basic)
        self.__scene = 4
        self.update("'hey buddy'", "'you look good fighting'", "*do a cool dance move*", "CHOOSE AN ACTION!")

    def player_results(self, text) -> None:
        self.EnemyGraphic.setScene(self.enemy_basic)
        self.__scene = 5
        self.update("-", "RESULTS", "-", text)

    def enemy_attack(self) -> None:
        """
        method to have the enemy randomly attack
        """
        self.playerGraphic.setScene(self.player_basic)
        self.__scene = 6
        results = self.enemy.use_random_action()
        choice = results[0]
        if choice == 1:
            if results[1][0]:
                self.exit_screen(1)
            else:
                self.update("-", "USED MERCY", "-", results[1][1])
                self.EnemyGraphic.setScene(self.enemy_mercy)
        elif choice == 2 or choice == 3:
            self.update("-", "USED NON LETHAL ITEM", "-", results[1])
            self.EnemyGraphic.setScene(self.enemy_item)
        elif choice == 4 or choice == 5:
            self.player.take_damage(results[1][0])
            self.update("-", "DEALT DAMAGE", "-", results[1][1])
            self.EnemyGraphic.setScene(self.enemy_item)
            if choice == 5:
                self.EnemyGraphic.setScene(self.enemy_attacking)


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

    def clickedA(self)-> None:
        """
        method for clicking the first button
        """
        if self.__scene == 1:
            self.fight_screen()
        elif self.__scene == 2:
            result = self.player.attack(1)
            self.playerGraphic.setScene(self.player_attack)
            self.enemy.take_damage(result[0])
            self.player_results(result[1])
        elif self.__scene == 3:
            result = self.player.use_potion()
            self.playerGraphic.setScene(self.player_item)
            self.player_results(result)
        elif self.__scene == 4:
            self.playerGraphic.setScene(self.player_mercy)
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

    def clickedB(self)-> None:
        """
        method for clicking the second button
        """
        if self.__scene == 0:
            self.newGame()
        elif self.__scene == 1:
            self.item_screen()
        elif self.__scene == 2:
            result = self.player.attack(2)
            self.playerGraphic.setScene(self.player_attack)
            self.enemy.take_damage(result[0])
            self.player_results(result[1])
        elif self.__scene == 3:
            self.playerGraphic.setScene(self.player_item)
            result = self.player.use_berry()
            self.player_results(result)
        elif self.__scene == 4:
            self.playerGraphic.setScene(self.player_mercy)
            result = self.player.mercey(random.randint(1, 10))
            if result[0]:
                self.exit_screen(0)
            else:
                self.player_results(result[1])
        elif self.__scene == 5:
            self.enemy_attack()
        elif self.__scene == 6:
            self.battle_screen()

    def clickedC(self)-> None:
        """
        method for clicking the third button
        """
        if self.__scene == 1:
            self.mercy_screen()
        elif self.__scene == 2:
            result = self.player.attack(3)
            self.playerGraphic.setScene(self.player_attack)
            self.enemy.take_damage(result[0])
            self.player_results(result[1])
        elif self.__scene == 3:
            self.playerGraphic.setScene(self.player_item)
            result = self.player.use_poison()
            self.enemy.take_damage(result[0])
            self.player_results(result[1])
        elif self.__scene == 4:
            self.playerGraphic.setScene(self.player_mercy)
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

