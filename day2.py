with open('inputs/day2.txt') as f:
    lines = [line.rstrip() for line in f]

values = {'A': 1,  # rock
          'B': 2,  # paper
          'C': 3,  # scissors
          'X': 1,  # rock       / lose
          'Y': 2,  # paper      / draw
          'Z': 3}  # scissors   / win

score_p1 = 0
score_p2 = 0

win = 6
draw = 3
lose = 0

for this_game in lines:
    opponent, me = this_game.split(' ')

    # Part 1
    # Observation: When you subtract my value from the opponent's and modulo
    # by 3, 0 is a draw, 1 is a lose for me, and 2 is a win for me.
    x = (values[opponent] - values[me]) % 3

    if x == 0:
        score_p1 += values[me] + draw
    elif x == 1:
        score_p1 += values[me] + lose
    else:  # x == 2
        score_p1 += values[me] + win

    # Part 2
    # Observation: To win, you must be "higher" than the opponent except
    # when the opponent has 3 (scissors), you must have 1 (rock). So we can
    # model this with modulo starting at 1 instead of 0. To do this, subtract
    # 1 from the part you are modulo'ing then add 1 to the result
    y = values[me]

    if y == 2:
        score_p2 += values[opponent] + draw
    if y == 1:
        # Lose, so subtract 1 (subtract 2 total to make mod start at 1)
        z = (values[opponent] - 2) % 3 + 1
        score_p2 += z + lose
    if y == 3:
        # Win, so add 1 (add 0 total to make mod start at 1)
        z = (values[opponent]) % 3 + 1
        score_p2 += z + win

print("Part 1:", score_p1)
print("Part 2:", score_p2)

