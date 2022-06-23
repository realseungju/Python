skiList = []

def getUserInput():
  for countInput in range(repeatCount):
    print(countInput+1,'번째 스키점프 값을 입력하세요.')
    skiList.append(int(input(':')))
def printResult():
  for countResult in range(3):
    print('스키점프',countResult+1,'등은',skiList[countResult],'meter 입니다.')

repeatCount = int(input('몇 개의 데이터를 입력하시겠습니까?(3개 이상 입력): '))
getUserInput()
skiList.sort(reverse=True)
printResult()
  