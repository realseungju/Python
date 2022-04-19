remainBread = int(input('남은 빵 수를 입력하세요 >> '))
totalCost = int(input('남은 빵의 총 가격을 입력하세요 >> '))
numOfBuyer = int(input('구매자 수를 입력하세요 >> '))

limitBread = 5
limitCost = 10000
limitBuyer = 2

soldOut = (limitBread>=remainBread) or (limitCost>totalCost) or (limitBuyer==numOfBuyer)

print("완판 여부는 ", soldOut , " 입니다.")