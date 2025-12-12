import random
from MiniFightGame.dataTracker import DataTracker


class Fighter():
    def __init__(self, name):
        self.__minAttack = 1
        self.__maxAttack = 10
        self.__hp = 100
        self.__items = [2, 'heal potion', 3, 'berry', 1, 'poison']
        self.__attackBonus = 1
        self.__name = str(name)
        self.__mercyLevel = 0
        self.__data = DataTracker(str(self))

    def set_min_attack(self, new_value) -> None:
        self.__minAttack = new_value

    def set_max_attack(self, new_value) -> None:
        self.__maxAttack = new_value

    def take_damage(self, amount) -> None:
        self.__hp -= amount
        self.__data.attacked(amount)
        if self.__hp <= 0:
            self.__hp = 0

    def get_hp(self) -> int:
        """

        :return: hp of the fighter
        """
        return self.__hp

    def attack(self, type) -> tuple[int, str]:
        """
        method to use attack action
        :param: type = 1-3 int deciding attack
        :return: [int: how much damage was dealt, str: flavertext]
        """
        if type == 1:
            damage = int(((random.randint(self.__minAttack, self.__maxAttack)) * self.__attackBonus) - (self.__mercyLevel/10))
            self_damage = random.randint(0, 5)
            self.__hp -= self_damage
            self.__attackBonus = 1
            self.__data.doAttack()
            self.__data.takeTurn()
            self.__data.attacked(self_damage)
            return damage, f"{self.__name} did {damage} damage and took {self_damage} recoil!"

        if type == 2:
            damage = int((((random.randint(self.__minAttack, self.__maxAttack)) * self.__attackBonus) - (self.__mercyLevel / 10)) + 10)
            self_damage = random.randint(0, 5) * 2
            self.__hp -= self_damage
            self.__attackBonus = 1
            self.__data.doAttack()
            self.__data.takeTurn()
            self.__data.attacked(self_damage)
            return (damage, f"{self.__name} did {damage} damage and took {self_damage} recoil!")

        if type == 3:
            damage = int(((random.randint(self.__minAttack, self.__maxAttack)) * self.__attackBonus) - (self.__mercyLevel / 10)) * 2
            self_damage = random.randint(0, 5) * 4
            self.__hp -= self_damage
            self.__attackBonus = 1
            self.__data.doAttack()
            self.__data.takeTurn()
            self.__data.attacked(self_damage)
            return (damage, f"{self.__name} did {damage} damage and took {self_damage} recoil!")

    def use_potion(self) -> str:
        """
        method to use potion item
        :return: str: flavertext
        """
        self.__data.takeTurn()
        if self.__items[0] > 0:
            healed = random.randint(5, 20)
            self.__hp += healed
            self.__items[0] -= 1
            return f"{self.__name} healed by {healed} hp!"
        else:
            return f"{self.__name} is out of potions!"

    def use_berry(self) -> str:
        """
        method to use berry item
        :return: str: flavertext
        """
        self.__data.takeTurn()
        if self.__items[2] > 0:
            bonus = random.randint(2, 4)
            self.__attackBonus += bonus
            self.__items[2] -= 1
            return f"{self.__name}'s next attack will do {self.__attackBonus} times damage!"
        else:
            return f"{self.__name} is out of berrys!"

    def use_poison(self)-> tuple[int, str]:
        """
        method to use poison item
        :return: [int: how much damage was dealt, str: flavertext]
        """
        self.__data.takeTurn()
        if self.__items[4] > 0:
            attack = random.randint(2, 5)
            self.__attackBonus += attack
            self.__items[4] -= 1
            return attack, f"{self.__name}'s poision did {attack} damage!"
        else:
            return 0, f"{self.__name} is out of poison!"

    def mercey(self, amount) -> tuple[bool, str]:
        """
        method when using the mercy action
        :param amount: the amount of mercy
        :return: [bool: if the enemy retreats, str: flavortext]
        """
        self.__data.takeTurn()
        self.__mercyLevel += amount
        self.__data.useMercy()
        if self.__mercyLevel > 50:
            self.__mercyLevel = 51
            return True, f"{self.__name} made the enemy retreat!"
        if self.__mercyLevel > 40:
            return False, f"{self.__name} is making the enemy consider a diffrent line of work!"
        if self.__mercyLevel > 30:
            return False, f"{self.__name} is making the enemy rethink their choices!"
        if self.__mercyLevel > 10:
            return False, f"{self.__name} is making the enemy wonder why they are fighting!"
        else:
            return False, f"{self.__name} is making the enemy confused!"

    def use_random_action(self) -> list:
        """
        method to randomly choose an action, for enemy
        :return: [int: 1-mercy, 2-potion, 3-berry, 4-poison, 5-attack; return of choice]
        """
        choice = random.randint(1, 20)
        if choice <5:
            return [1, self.mercey(random.randint(1, 10))]
        if choice <8:
            return [2, self.use_potion()]
        if choice <10:
            return [3, self.use_berry()]
        if choice <11:
            return [4, self.use_poison()]
        else:
            nextchoice = random.randint(1, 3)
            if nextchoice == 1:
                return [5, self.attack(1)]
            if nextchoice == 2:
                return [5, self.attack(2)]
            if nextchoice == 3:
                return [5, self.attack(3)]

    def updateData(self) -> None:
        self.__data = str(self)

    def __str__(self) -> str:
        """

        :return: string of fighters data
        """
        return f"{self.__name}: hp: {self.__hp}, items: {self.getItems()}, mercy: {self.__mercyLevel}"

    def getItems(self) -> list:
        """

        :return: string of items
        """
        return [f"{self.__items[0]}: {self.__items[1]}", f"{self.__items[2]}: {self.__items[3]}", f"{self.__items[4]}: {self.__items[5]}"]

    def getData(self) -> list:
        return self.__data.getDatas(self)

    def strGetData(self) -> str:
        self.__data.setCharacter(self)
        return str(self.__data)

"""
#IF NEED TO TEST FIGHTER LOGIC
def main():
    f = Fighter("Cool guy")
    print(f)
    print(f.getData())
    print(f.getItems())
    print(f.use_potion())
    print(f.use_berry())
    print(f.use_poison())
    print(f.attack())
    print(f.attack())
    for i in range(0, 51, 5):
        print(f.mercey(i))
    print(f.use_poison())
    print(f.use_berry())
    print(f.use_berry())
    print(f.use_berry())
    print(f.take_damage(1))
    print(f.take_damage(20))
    print(f.attack())
    print(f)
    print(f.getItems())
    print(f.getData())
    print(f.strGetData())


main()
"""
