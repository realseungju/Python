bloods = []
count = 0
countA = 0
countB = 0
countAB = 0
countO = 0

for i in range(5):
  print('헌혈한 혈액형 기록 ',i,' 번째')
  bloods.append(input("A, B, AB, O >> "))

print('혈액형 별 헌혈 횟수')

while count < len(bloods):
  if bloods[count] == 'A':
    countA+=1
  elif bloods[count] == 'B':
    countB+=1
  elif bloods[count] == 'AB':
    countAB+=1
  elif bloods[count] == 'O':
    countO+=1
  count+=1

print('A: ',countA)
print('B: ',countB)
print('AB: ',countAB)
print('O: ',countO)