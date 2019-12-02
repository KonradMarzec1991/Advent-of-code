"""
Advent of code DAY 2
"""


TARGET_VALUE = 19690720


def retrieve_nums(file_name):
    """
    :param file_name: text file with numbers input
    :return: list of numbers
    """
    with open(file_name) as f:
        row = f.read()

    num_list = [int(v) for v in row.split(',')]
    return num_list


def calculate_0index(num_list, noun=None, verb=None):
    """
    :param num_list: int list retrieved from text file
    :param noun: given in task num between 0 and 99
    :param verb: given in task num between 0 and 99
    :return: 0-index value of list
    """
    if noun is not None and verb is not None:
        num_list[1], num_list[2] = noun, verb
    counter = 0

    for _ in range(len(num_list) // 4):
        sublist = slice(counter*4, counter*4 + 4)
        counter += 1

        first = num_list[sublist][0]

        if first == 1:
            two_sum = num_list[num_list[sublist][1]] + num_list[num_list[sublist][2]]
            num_list[num_list[sublist][3]] = two_sum
        elif first == 2:
            two_sum = num_list[num_list[sublist][1]] * num_list[num_list[sublist][2]]
            num_list[num_list[sublist][3]] = two_sum
        else:
            break

    return num_list[0]


# Part I
# calculate_0index(retrieve_nums('day_2.txt'))


# Part II
def main():
    """
    :return: 100 * noun + verb VALUE (from task conditions)
    """
    for noun in range(100):
        for verb in range(100):

            num_list = retrieve_nums('day_2.txt')
            s_0 = calculate_0index(num_list, noun, verb)

            if s_0 == TARGET_VALUE:
                print('-'*10)
                val = 100 * noun + verb
                print(val)
                print('-'*10)


# Part II
if __name__ == '__main__':
    calculate_0index(retrieve_nums('day_2.txt'))
    main()