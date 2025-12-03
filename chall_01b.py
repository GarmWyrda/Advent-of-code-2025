dial = 50
answer = 0

with open('input01b.txt', 'r') as file:
     for line in file:
          a = int(line[1:])
          if (a > 100):
               answer +=(a//100)
          if (line[0] == "L"):
               if a%100 > dial and dial != 0:
                    answer += 1
               dial = (dial - a)%100
          else:
               if a%100 > (100 - dial):
                    answer += 1
               dial = (dial + a)%100
          if dial == 0:
               if a%100 != 0:
                    answer += 1

print(answer)