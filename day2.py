our_win = {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}
score_for_shape = {"Paper": 2, "Rock": 1, "Scissors": 3}
opp_shape = {"A": "Rock", "B": "Paper", "C": "Scissors"}
our_shape = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}

# part2
should_end = {"X": 0, "Y": 3, "Z": 6}
to_lose = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}

def day2_1():
    result = 0
    with open("./input/day2", "r") as inp:
        for line in inp.readlines():
            round_res = ""
            opp = opp_shape[line.split(" ")[0].strip()]
            our = our_shape[line.split(" ")[1].strip()]
            print(opp, our)
            # draw
            if opp == our:
                round_res = "Draw"
                result += score_for_shape[our] + 3
            # we win
            elif our_win[opp] == our:
                result += score_for_shape[our] + 6
                round_res = "win"
            # we lose
            else:
                result += score_for_shape[our]
                round_res = "lose"
    return result


def day2_2():
    result = 0
    with open("./input/day2", "r") as inp:
        for line in inp.readlines():
            round_res = ""
            opp = opp_shape[line.split(" ")[0].strip()]
            sh_res = line.split(" ")[1].strip()
            if should_end[sh_res] == 0:
                # should lose
                shape = to_lose[opp]
                result += should_end[sh_res] + score_for_shape[shape]
            if should_end[sh_res] == 3:
                # should draw
                shape = opp
                result += should_end[sh_res] + score_for_shape[shape]
            if should_end[sh_res] == 6:
                # should win
                shape = our_win[opp]
                result += should_end[sh_res] + score_for_shape[shape]


    return result

if __name__ == '__main__':
    print(day2_2())
