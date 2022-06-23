import turtle
t = turtle.Turtle()
t.shape('turtle')

while(1): # 무한 반복
  t.reset() # 거북이 초기화
  choice = input("그리실 도형을 입력해주세요 >> ")
  if choice == '종료': # 종료가 입력되면 반복문을 나가서 종료
    break

  if choice == '사각형': # 사각형은 가로 세로가 있음
    width = int(input('가로의 길이를 입력해주세요 >> '))
    height = int(input('세로의 길이를 입력해주세요 >> '))
  else:
    length = int(input('길이를 입력해주세요 >> '))

  if choice == '사각형': # 사각형 입력 받음
    for i in range(0,2):
      t.forward(width)
      t.right(90)
      t.forward(height)
      t.right(90)
  elif choice == '정삼각형': # 정삼각형 입력 받음
    for i in range(0,3):
      t.right(120)
      t.forward(length)
  elif choice == '원': # 원 입력 받음
    t.circle(length)
  elif choice == '정오각형': # 정오각형 입력 받음
    for i in range(0,5):
      t.right(72)
      t.forward(length)
  else:
    print("해당되는 입력 명령이 없거나 잘못 입력하셨습니다.") # 조건을 만족하지 않을 때

