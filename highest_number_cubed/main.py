"""This is the entry point of the program."""


def highest_number_cubed(limit):
    max = 1
    index = 1
    while (index*index*index) < limit:
        max = index
        index += 1
    return max
    
