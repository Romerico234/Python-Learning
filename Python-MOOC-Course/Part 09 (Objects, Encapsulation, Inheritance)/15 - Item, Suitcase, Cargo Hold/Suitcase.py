import Item

class Suitcase:
    def __init__(self, max_weight):
        self.__max_weight = max_weight
        self.__count = 0
        self.__total_weight = 0
        self.__suitcase = []

    def add_item(self, item: Item):
        if self.__total_weight + item.weight() <= self.__max_weight:
            self.__count += 1
            self.__total_weight += item.weight()
            self.__suitcase.append(item)
        
    def __str__(self):
        if self.__count == 1:
            return f'{self.__count} item ({self.__total_weight} kg)'
        else:
            return f'{self.__count} items ({self.__total_weight} kg)'
        
    def print_items(self):
        for item in self.__suitcase:
            print(item)
    
    def weight(self):
        return self.__total_weight
    
    def heaviest_item(self):
        if not self.__suitcase:
            return None
        
        heaviest = 0
        heaviest_item = None
        for item in self.__suitcase:
            if item.weight() >= heaviest:
                heaviest = item.weight()
                heaviest_item = item
                
        return heaviest_item

