class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        # If there is no items at all, then there is no frequency
        if not my_list:
            return None
 
        max_frequency = 0
        max_item = my_list[0]
        for element in my_list:
            if my_list.count(element) > max_frequency:
                max_frequency = my_list.count(element)
                max_item = element
 
        return max_item
 
    @classmethod
    def doubles(cls, my_list: list):
        my_set = set(my_list)
        doubles = 0
        for element in my_set:
            if my_list.count(element) >= 2:
                doubles += 1
        return doubles

if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))