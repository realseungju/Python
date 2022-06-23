import turtle
t = turtle.Turtle()
t.shape('turtle')

def turtlePrint(angle): # 사용자로부터 입력을 받아 처리하는 turtlePrint 함수
  if angle == 0: # 원은 각이 없음
    print("각이 없으므로 원을 그리겠습니다.")
    radius = int(input("반지름의 길이 >> "))
    t.circle(radius)
  elif angle >= 3 : # 각이 3개 이상
    length = int(input("각 변의 길이 >> "))
    for i in range(angle):
      t.forward(length)
      t.right(360//angle)
  else:
    print("에러! 도형의 각은 0 또는 3이상을 입력해주세요.") 
    # 조건을 만족하지 않을 때

print("도형의 각은 0 또는 3 이상의 정수를 입력해주세요.")

while(1): # 무한 반복
  t.reset() # 거북이 초기화
  choice = input("그리실 도형의 각 수를 입력해주세요 (0은 원) >> ")
  if choice == '종료': # 종료가 입력되면 반복문을 나가서 종료
    break

  angle = int(choice) # 입력 받은 값을 정수형으로 변환하여 angle에 저장
  turtlePrint(angle)