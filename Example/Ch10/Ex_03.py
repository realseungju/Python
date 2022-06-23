fruits = ('사과','포도','수박','참외','배','자두','복숭아','바나나','포도')

for index, item in enumerate(fruits):
  if index % 2 == 1:
    print(index, ':' ,item)