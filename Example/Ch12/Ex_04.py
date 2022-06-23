from unittest import result
from webbrowser import get


def calculator(inputNum1, intputNum2):
  resultPlus = inputNum1 + intputNum2
  resultMinus = intputNum1 = intputNum2
  resultMulti = inputNum1 * intputNum2
  resultDivide = inputNum1 / intputNum2

  return (resultPlus,resultMinus,resultMulti,resultDivide)

getUserInput1 = int(input('정수1을 입력하세요: '))
getUserInput2 = int(input('정수2을 입력하세요: '))

resultTotal = calculator(getUserInput1,getUserInput2)
print('사칙연산 결과: ',resultTotal)