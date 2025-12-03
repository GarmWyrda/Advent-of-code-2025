import time
start_time = time.time()

dial = 50
answer = 0

with open('day01/input01a.txt', 'r') as file:
    for line in file:
        if (line[0] == "L"):
            dial = (dial - int(line[1:]))%100
        else:
            dial = (dial + int(line[1:]))%100
        if dial == 0:
            answer += 1

print(answer)
print("--- %s seconds ---" % (time.time() - start_time))