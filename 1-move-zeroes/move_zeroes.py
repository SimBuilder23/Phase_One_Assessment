#!/usr/bin/env python3 

some_list = [1, 2, 3, 0, 5, 4, 32, 0, 4, 5, 0, 6, 7, 8]

def move_zeroes(some_list):
    for number in some_list:
        if number == 0:
            some_list.remove(number)
            some_list.append(0)
    return some_list

print (move_zeroes(some_list))