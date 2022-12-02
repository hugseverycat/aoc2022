with open('inputs/day2.txt') as f:
    lines = [line.rstrip() for line in f]

scores = {'A': 1, # rock
          'B': 2, # paper
          'C': 3, # scissors
          'X': 1, # rock
          'Y': 2, # paper
          'Z': 3} # scissors

score_p1 = 0
score_p2 = 0

win = 6
draw = 3
lose = 0
for this_game in lines:
    opponent, me = this_game.split(' ')
    x = scores[opponent] * scores[me]
    #print(x)

    # Part 1
    if x in (1, 4, 9):
        score_p1 += draw + scores[me]
    elif x == 3:
        if scores[me] == 1:
            score_p1 += win + scores[me]
        else:
            score_p1 += lose + scores[me]
    elif scores[me] > scores[opponent]:
        score_p1 += win + scores[me]
    else:
        score_p1 += lose + scores[me]


print("Part 1:", score_p1)

# wrong answers: 12950, 13058
