def checkSMSMMS(userInput):
  strLen = len(userInput)
  print('����� �Է� ���ڿ� ����: ',strLen)

  if(strLen <= 100):
    print('�ܹ� �޽����� 50���� �ΰ��˴ϴ�.')
  else:
    print('�幮 �޽����� 100���� �ΰ��˴ϴ�.')
  
inputData = input('���ڿ��� �Է��ϼ���: ')
checkSMSMMS(inputData)