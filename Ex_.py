num = 10

def varTest():
    global num
    num = 40
    print('num : ', num)

print('num : ', num)
varTest()
print('num : ', num)