class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year
 
    def __str__(self):
        return f'{self.__day}.{self.__month}.{self.__year}'
 
    # Comparisons are easier, when date is converted to days
    def __value(self):
        return self.__year * 360 + self.__month * 30 + self.__day
 
    # Converst days back to date
    def __to_date(self, days: int):
        months = days // 30
        years = months // 12
        days -= months * 30
        months -= years * 12
        return SimpleDate(days, months, years)
 
    def __lt__(self, other: "SimpleDate"):
        return self.__value() < other.__value()
 
    def __gt__(self, other: "SimpleDate"):
        return self.__value() > other.__value()
 
    def __eq__(self, other: "SimpleDate"):
        return self.__value() == other.__value()
        
    def __ne__(self, other: "SimpleDate"):
        return self.__value() != other.__value()
 
    def __add__(self, days_to_add: int):
        return self.__to_date(self.__value() + days_to_add)
 
    def __sub__(self, other: "SimpleDate"):
        # abs(x) returns the absolute value of x
        return abs(self.__value() - other.__value())



if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)
    d3 = SimpleDate(28, 12, 1985)

    print(d1)
    print(d2)
    print(d1 == d2)
    print(d1 != d2)
    print(d1 == d3)
    print(d1 < d2)
    print(d1 > d2)