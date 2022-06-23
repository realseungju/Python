skiList = []
for countIntput in range(0,10):
  print(countIntput+1,'번째 스키점프 값을 입력하세요.')
  skiList.append(int(input(':')))
  skiList.sort(reverse=True)

for countResult in range(0,3):
  print('스키점프',countResult+1,'등은',skiList[countResult],'meter 입니다.')
  