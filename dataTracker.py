
class DataTracker():
    def __init__(self, character):
        self.__character= character
        self.__turnsTaken = 0
        self.__ammountAttack = 0
        self.__ammountMercy = 0
        self.__totalDamageTaken = 0

    def setCharacter(self, character):
        """
        method to set fighter that this tracker will use
        :param character: fighter to keep track of
        :return: none
        """
        self.__character = str(character)

    def takeTurn(self) -> None:
        self.__turnsTaken += 1

    def doAttack(self) -> None:
        self.__ammountAttack += 1

    def useMercy(self) -> None:
        self.__ammountMercy += 1

    def attacked(self, ammount) -> None:
        self.__totalDamageTaken += ammount

    def getDatas(self, character) -> list[str | int]:
        """
        method to get data in list form
        :param character: the fighter to get data from
        :return: list[character, turns Taken, amount of attacks, ammount of mercies, ammount of total damage]
        """
        self.__character = str(character)
        return [self.__character, self.__turnsTaken, self.__ammountAttack, self.__ammountMercy, self.__totalDamageTaken]

    def __str__(self) -> str:
        """
        method to return string representation of data
        :return: string representation of data
        """
        return f"Character: [{self.__character}], turns Taken: {self.__turnsTaken}, took {self.__totalDamageTaken} damage, ammount of mercies: {self.__ammountMercy}, ammount of attacks: {self.__ammountAttack}"