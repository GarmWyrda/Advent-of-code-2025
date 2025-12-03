dial = 50
answer = 0

with open('input01.txt', 'r') as file:
    for line in file:
        if (line[0] == "L"):
            dial = (dial - int(line[1:]))%100
        else:
            dial = (dial + int(line[1:]))%100
        if dial == 0:
            answer += 1

print(answer)