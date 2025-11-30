import random

class Fighter():
    def __init__(self, name):
        self.__minAttack = 1
        self.__maxAttack = 10
        self.__hp = 100
        self.__items = [2, 'heal potion', 3, 'berry', 1, 'poison']
        self.__attackBonus = 1
        self.__name = str(name)
        self.__mercyLevel = 0

    def set_min_attack(self, new_value):
        self.__minAttack = new_value

    def set_max_attack(self, new_value):
        self.__maxAttack = new_value

    def take_damage(self, amount):
        self.__hp -= amount

    def attack(self) -> tuple[int, str]:
        damage = ((random.randint(self.__minAttack, self.__maxAttack)) * self.__attackBonus) - (self.__mercyLevel/2)
        self_damage = random.randint(0, 5)
        self.__hp -= self_damage
        self.__attackBonus = 1
        return (damage, f"{self.__name} did {damage} damage and took {self_damage} recoil!")

    def use_potion(self) -> str:
        if self.__items[0] > 0:
            healed = random.randint(5, 20)
            self.__hp += healed
            return f"{self.__name} healed by {healed} hp!"
        else:
            return f"{self.__name} is out of potions!"

    def use_berry(self) -> str:
        if self.__items[2] > 0:
            bonus = random.randint(2, 5)
            self.__attackBonus += bonus
            return f"{self.__name}'s next attack will do {self.__attackBonus} times damage!"
        else:
            return f"{self.__name} is out of berrys!"

    def use_poison(self)-> tuple[int, str]:
        if self.__items[4] > 0:
            attack = random.randint(2, 5)
            self.__attackBonus += attack
            return attack, f"{self.__name}'s poision did {attack} damage!"
        else:
            return 0, f"{self.__name} is out of poison!"

    def mercey(self, amount) -> tuple[bool, str]:
        self.__mercyLevel += amount
        if self.__mercyLevel > 50
            return True, f"{self.__name} made the enemy retreat!"
        if self.__mercyLevel > 40:
            return False, f"{self.__name} is making the enemy consider a diffrent line of work!"
        if self.__mercyLevel > 30:
            return False, f"{self.__name} is making the enemy rethink their choices!"
        if self.__mercyLevel > 10:
            return False, f"{self.__name} is making the enemy wonder why they are fighting!"
        else:
            return False, f"{self.__name} is making the enemy confused!"

