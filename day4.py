

def day4_1():
    result = 0
    with open("./input/day4", "r") as inp:
        result = 0
        for line in inp.readlines():
            first_elf = line.split(",")[0].strip()
            second_elf = line.split(",")[1].strip()
            first_elf = (int(first_elf.split("-")[0]), int(first_elf.split("-")[1]))
            second_elf = (int(second_elf.split("-")[0]), int(second_elf.split("-")[1]))
            if second_elf[0] <= first_elf[0] <= second_elf[1]:
                result += 1
            else:
                if first_elf[0] <= second_elf[0] <= first_elf[1]:
                    result += 1
                else:
                    if second_elf[0] <= first_elf[1] <= second_elf[1]:
                        result += 1
                    else:
                        if first_elf[0] <= second_elf[1] <= first_elf[1]:
                            result += 1

    return result


def day4_2():
    pass

if __name__ == '__main__':
    print(day4_1())
