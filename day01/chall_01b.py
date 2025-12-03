import time
start_time = time.time()

dial = 50
answer = 0

with open('day01/input01b.txt', 'r') as file:
     for line in file:
          a = int(line[1:])
          if (a > 100):                                            # On retire les révolutions qui servent à rien
               answer +=(a//100)
          if (line[0] == "L"):                                        
               if a%100 > dial and dial != 0:                      # là on s'interesse aux cas "chiants" (si on commence à 0) et de la dernière "révolution"
                    answer += 1
               dial = (dial - a)%100
          else:
               if a%100 > (100 - dial):                            # même chose qu'au dessus mais plus simple car si on commence à 0 on rentre jamais dedans donc pas besoin de le gérer
                    answer += 1
               dial = (dial + a)%100
          if dial == 0:
               if a%100 != 0:
                    answer += 1

print(answer)
print("--- %s seconds ---" % (time.time() - start_time))