skiList = []

def getUserInput():
  print(countIntput+1,'번째 스키점프 값을 입력하세요.')
  skiList.append(int(input(':')))
  skiList.sort(reverse=True)
def printResult():
  print('스키점프',countResult+1,'등은',skiList[countResult],'meter 입니다.')

for countIntput in range(0,10):
  getUserInput()
for countResult in range(0,3):
  printResult()
  