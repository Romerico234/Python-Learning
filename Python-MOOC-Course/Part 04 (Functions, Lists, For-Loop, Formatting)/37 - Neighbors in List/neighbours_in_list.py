def longest_series_of_neighbours(my_list: list):
    count = 0
    longest_count = 0

    for i in range(1, len(my_list)):
        if abs(my_list[i] - my_list[i-1]) == 1:
            count += 1
        else:
            count = 0

        if count > longest_count:
            longest_count = count

    return longest_count + 1

if __name__ == "__main__":
    my_list = [0, 2, 4, 5, 6, 7, 10, 11, 12, 100, 101]
    print(longest_series_of_neighbours(my_list))
