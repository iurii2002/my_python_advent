

def day6_1():
    without_repeat = []
    with open("./input/day6", "r") as inp:
        i = 0
        for character in inp.readline():
            i += 1
            if character in without_repeat:
                without_repeat = without_repeat[without_repeat.index(character) + 1:]
            without_repeat.append(character)
            if len(without_repeat) == 4:
                break

    return i


def day6_2():
    without_repeat = []
    with open("./input/day6", "r") as inp:
        i = 0
        for character in inp.readline():
            i += 1
            if character in without_repeat:
                without_repeat = without_repeat[without_repeat.index(character) + 1:]
            without_repeat.append(character)
            if len(without_repeat) == 14:
                break

    return i


if __name__ == '__main__':
    print(day6_2())
