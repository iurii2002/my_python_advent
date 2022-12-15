import string


def day3_1():
    result = 0
    with open("./input/day3", "r") as inp:
        for line in inp.readlines():
            duplicate = ""
            leng = len(line.strip())
            middle = leng//2
            first = line[:middle].strip()
            second = line[middle:].strip()

            list_of_items = {}

            for item in first:
                list_of_items[item] = 1
            for item in second:
                if item in list_of_items:
                    duplicate = item
            if duplicate.islower():
                current = string.ascii_lowercase.index(duplicate) + 1
                result += current
            if duplicate.isupper():
                current = string.ascii_lowercase.index(duplicate.lower()) + 27
                result += current

    return result




def day3_2():
    priority = {}
    p = 1
    for c in 'abcdefghijklmnopqrstuvwxyz':
        priority[c] = p
        p += 1
    for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        priority[c] = p
        p += 1


    result = 0
    with open("./input/day3", "r") as inp:
        i = 0
        elf_groups = []
        elf_group = []
        for line in inp.readlines():
            elf_group.append(line.strip())
            i += 1
            if i % 3 == 0:
                elf_groups.append(elf_group)
                elf_group = []
        for elf_g in elf_groups:
            print(elf_g)
            items_dict = {}

            elf_1 = set(elf_g[0])
            elf_2 = set(elf_g[1])
            elf_3 = set(elf_g[2])

            inter = elf_1 & elf_2 & elf_3
            print(inter)

            result += priority[inter.pop()]

            # for item in elf_1:
            #     if item not in items_dict.keys():
            #         items_dict[item] = 1
            #
            # for item in elf_2:
            #     if item in items_dict.keys():
            #         items_dict[item] = 2
            #
            # for item in elf_3:
            #     if item in items_dict.keys():
            #         if items_dict[item] == 2:
            #             badge = item
            #             print(badge, items_dict)
            #             if badge.islower():
            #                 current = string.ascii_lowercase.index(badge) + 1
            #                 result += current
            #             if badge.isupper():
            #                 current = string.ascii_lowercase.index(badge.lower()) + 27
            #                 result += current
            #             print(current, result)

    return result


if __name__ == '__main__':
    print(day3_2())
