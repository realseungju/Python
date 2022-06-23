from Dice import sixDice
from Dice import sortNumbers

gamer1Dice = sixDice()
gamer2Dice = sixDice()
gamer3Dice = sixDice()

for i in range(5):
  gamer1Dice.playDice()
  gamer2Dice.playDice()
  gamer3Dice.playDice()

sumGamer1 = gamer1Dice.getSum()
sumGamer2 = gamer2Dice.getSum()
sumGamer3 = gamer3Dice.getSum()

print('Gamer1 : ',gamer1Dice.getNumbers())
print('Sum of Gamer 1 : ',sumGamer1)
print('========')
print('Gamer2 : ',gamer2Dice.getNumbers())
print('Sum of Gamer 2 : ',sumGamer2)
print('========')
print('Gamer3 : ',gamer3Dice.getNumbers())
print('Sum of Gamer 3 : ',sumGamer3)
print('========')

sortedNumbers = sortNumbers(sumGamer1,sumGamer2,sumGamer3)
print("First score : ", sortedNumbers[0])
print("Second score : ",sortedNumbers[1])
print("Third Score : ",sortedNumbers[2])