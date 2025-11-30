
class DataTracker():
    def __init__(self, character):
        self.__character= character
        self.__turnsTaken = 0
        self.__ammountAttack = 0
        self.__ammountMercy = 0
        self.__totalDamageTaken = 0

    def setCharacter(self, character):
        self.__character = str(character)

    def takeTurn(self):
        self.__turnsTaken += 1

    def doAttack(self):
        self.__ammountAttack += 1

    def useMercy(self):
        self.__ammountMercy += 1

    def attacked(self, ammount):
        self.__totalDamageTaken += ammount

    def getDatas(self, character):
        self.__character = str(character)
        return [self.__character, self.__turnsTaken, self.__ammountAttack, self.__ammountMercy, self.__totalDamageTaken]

    def __str__(self):
        return f"Character: [{self.__character}], turns Taken: {self.__turnsTaken}, took {self.__totalDamageTaken} damage, ammount of mercies: {self.__ammountMercy}, ammount of attacks: {self.__ammountAttack}"