from Item import Item
from Suitcase import Suitcase 

class CargoHold:
    def __init__(self, max_weight):
        self.__max_weight = max_weight
        self.__count = 0
        self.__total_weight = 0
        self.__cargo = []
    
    def add_suitcase(self, suitcase: Suitcase):
        if self.__total_weight + suitcase.weight() <= self.__max_weight:
            self.__count += 1
            self.__total_weight += suitcase.weight()
            self.__cargo.append(suitcase)

    def __str__(self):
        if self.__count == 1:
            return f'{self.__count} suitcase, space for {self.__max_weight - self.__total_weight} kg'
        else:
            return f'{self.__count} suitcases, space for {self.__max_weight - self.__total_weight} kg'
    
    def print_items(self):
        for item in self.__cargo:
            item.print_items()