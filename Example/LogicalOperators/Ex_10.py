passengerHeight = int(input('탑승자의 키를 입력하세요>> '))

limitLow = 120
limitHigh = 190

checkHeight = (limitLow<passengerHeight) and (limitHigh>passengerHeight)

print("탑승 가능 여부는 ", checkHeight, " 입니다.")
