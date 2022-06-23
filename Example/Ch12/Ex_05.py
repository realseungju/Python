def checkSMSMMS(userInput):
  strLen = len(userInput)
  print('사용자 입력 문자열 길이: ',strLen)

  if(strLen <= 100):
    print('단문 메시지로 50원이 부과됩니다.')
  else:
    print('장문 메시지로 100원이 부과됩니다.')
  
inputData = input('문자열을 입력하세요: ')
checkSMSMMS(inputData)