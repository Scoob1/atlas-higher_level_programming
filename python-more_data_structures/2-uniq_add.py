#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_sum = 0
    for i in range(len(my_list)):
        unique = True
        for j in range(i + 1, len(my_list)):
            if my_list[i] == my_list[j]:
                unique = False
                break
        if unique:
            unique_sum += my_list[i]
    return unique_sum
