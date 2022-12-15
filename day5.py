# start
#         [H]     [W] [B]
#     [D] [B]     [L] [G] [N]
# [P] [J] [T]     [M] [R] [D]
# [V] [F] [V]     [F] [Z] [B]     [C]
# [Z] [V] [S]     [G] [H] [C] [Q] [R]
# [W] [W] [L] [J] [B] [V] [P] [B] [Z]
# [D] [S] [M] [S] [Z] [W] [J] [T] [G]
# [T] [L] [Z] [R] [C] [Q] [V] [P] [H]
#  1   2   3   4   5   6   7   8   9


stack_1 = ["T", "D", "W", "Z", "V", "P"]
stack_2 = ["L", "S", "W", "V", "F", "J", "D"]
stack_3 = ["Z", "M", "L", "S", "V", "T", "B", "H"]
stack_4 = ["R", "S", "J"]
stack_5 = ["C", "Z", "B", "G", "F", "M", "L", "W"]
stack_6 = ["Q", "W", "V", "H", "Z", "R", "G", "B"]
stack_7 = ["V", "J", "P", "C", "B", "D", "N"]
stack_8 = ["P", "T", "B", "Q"]
stack_9 = ["H", "G", "Z", "R", "C"]

total_stacks =[stack_1, stack_2, stack_3, stack_4, stack_5, stack_6, stack_7, stack_8, stack_9]



def day5_1():
    with open("./input/day5", "r") as inp:
        for line in inp.readlines():
            line_split = line.split()
            amount = int(line_split[1])
            tr_from = int(line_split[3])
            tr_to = int(line_split[5])


            for i in range(0, amount):
                stack_from = total_stacks[tr_from - 1]
                element = stack_from.pop()
                stack_to = total_stacks[tr_to - 1]
                stack_to.append(element)

    result = [stack[-1:] for stack in total_stacks]
    return result


def day5_2():
    with open("./input/day5", "r") as inp:
        for line in inp.readlines():
            line_split = line.split()
            amount = int(line_split[1])
            tr_from = int(line_split[3])
            tr_to = int(line_split[5])

            stack_from = total_stacks[tr_from - 1]
            stack_to = total_stacks[tr_to - 1]

            if amount == 1:

                for i in range(0, amount):
                    element = stack_from.pop()
                    stack_to.append(element)
            else:

                reverse_moved_stack = []
                for i in range(0, amount):
                    element = stack_from.pop()
                    reverse_moved_stack.append(element)
                correct_moved_stack = reverse_moved_stack[::-1]
                for element in correct_moved_stack:
                    stack_to.append(element)

    result = [stack[-1:] for stack in total_stacks]
    result = ' '.join([' '.join(string) for string in result])
    return result


if __name__ == '__main__':
    print(day5_2())
