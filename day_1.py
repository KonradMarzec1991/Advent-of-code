"""
Advent of code DAY 1
"""

import math


def sum_fuel():
    """
    Part I - straight fuel calc
    :return: fuel number
    """
    fuel = 0

    with open('day_1.txt') as f:
        for num in f.readlines():
            fuel += int(num) // 3 - 2
    return fuel


if __name__ == '__main__':
    sum_fuel()