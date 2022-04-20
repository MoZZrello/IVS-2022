from PyQt5 import QtWidgets
from gui import window_calc
import sys
import mathlib
from PySide2 import *

memory = []
numbers = 0
sqrt = chr(8730)

class Calculator_Window(QtWidgets.QMainWindow, window_calc):
    def __init__(self):
        global memory
        super(Calculator_Window, self).__init__()
        self.setupUi(self)
        self.show()
        self.setFixedSize(245, 495)
        self.setWindowTitle("Calculator")

        self.button_number_zero.clicked.connect(lambda: self.pushed_number("0"))
        self.button_number_one.clicked.connect(lambda: self.pushed_number("1"))
        self.button_number_two.clicked.connect(lambda: self.pushed_number("2"))
        self.button_number_three.clicked.connect(lambda: self.pushed_number("3"))
        self.button_number_four.clicked.connect(lambda: self.pushed_number("4"))
        self.button_number_five.clicked.connect(lambda: self.pushed_number("5"))
        self.button_number_six.clicked.connect(lambda: self.pushed_number("6"))
        self.button_number_seven.clicked.connect(lambda: self.pushed_number("7"))
        self.button_number_eight.clicked.connect(lambda: self.pushed_number("8"))
        self.button_number_nine.clicked.connect(lambda: self.pushed_number("9"))
        self.button_add.clicked.connect(lambda: self.pushed_math_operand("+"))
        self.button_sub.clicked.connect(lambda: self.pushed_math_operand("-"))
        self.button_multiply.clicked.connect(lambda: self.pushed_math_operand("*"))
        self.button_division.clicked.connect(lambda: self.pushed_math_operand("/"))
        self.button_exponent.clicked.connect(lambda: self.pushed_math_operand("^"))
        self.button_decimal.clicked.connect(lambda: self.pushed_math_operand("."))
        self.button_open.clicked.connect(lambda: self.pushed_math_operand("("))
        self.button_close.clicked.connect(lambda: self.pushed_math_operand(")"))
        self.button_e.clicked.connect(lambda: self.pushed_math_operand("e"))
        self.button_factorial.clicked.connect(lambda: self.pushed_math_operand("!"))
        self.button_sqrt.clicked.connect(lambda: self.pushed_math_operand(sqrt))
        self.button_equal.clicked.connect(lambda: self.equals())

        self.button_delete.clicked.connect(lambda: self.clear_last_number())
        self.button_clear_all.clicked.connect(lambda: self.clear_all())

    def mathParse(self, txt):
        tmp = ""
        parts = []
        count = 1
        for char in txt:
            if char == "0" or char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9" or char == ".":
                tmp += char
            elif char == "+" or char == "-" or char == sqrt or char == "*" or char == "/" or char == "e" or char == "!" or char == "^" or char == "(" or char == ")":
                if tmp != "":
                    parts.append(float(tmp))
                tmp = ""
                parts.append(char)
            if count == len(txt) and len(tmp) != 0:
                parts.append(float(tmp))
            count += 1

        try:
            finish = calcRec(parts)
        except ValueError:
            return "Syntax Error"

        if finish == int(finish):
            finish = int(finish)
        return str(finish)

    def equals(self):
        global memory
        global numbers
        upper_display_text = ""
        for char in memory:
            upper_display_text += char
        self.display_top.setText(upper_display_text)
        out = self.mathParse(upper_display_text)
        self.display_bottom.setText(out)
        memory.clear()
        numbers = 0

    def pushed_math_operand(self, operand):
        global numbers
        global memory
        text = self.display_bottom.text()
        memory.append(operand)
        if numbers == 0:
            self.display_bottom.setText(operand)
            numbers += 1
        else:
            self.display_bottom.setText(text + operand)
            numbers += 1

    def pushed_number(self, num):
        global numbers
        global memory
        text = self.display_bottom.text()
        memory.append(num)
        if numbers == 0:
            self.display_bottom.setText(num)
            numbers += 1
        else:
            self.display_bottom.setText(text + num)

    def clear_last_number(self):
        global numbers
        global memory
        text = ""
        text = self.display_bottom.text()
        text = text[:-1]
        memory.pop()
        self.display_bottom.setText(text)
        numbers -= 1

    def clear_all(self):
        global numbers
        global memory
        self.display_bottom.setText("0")
        memory.clear()
        numbers = 0


def calcRec(numlist):
    finish = 0
    elemCount = 0
    openPar = 0
    closePar = 0
    for part in numlist:
        if part == '(':
            openPar += 1
            lastOpenPos = elemCount
        if part == ')':
            closePar += 1
        elemCount += 1

    if closePar != openPar:
        raise ValueError("Number of brackets don't match")

    i = lastOpenPos
    del numlist[i]
    tmplist = []
    while numlist[i] != ')':
        tmplist.append(numlist[i])
        del numlist[i]
    del numlist[i]
    print(tmplist)
    numlist.insert(lastOpenPos, numCalc(tmplist))
    print(numlist)
    if len(numlist) != 1:
        calcRec(numlist)
    return numlist[0]


def numCalc(numList):
    finish = 69
    elemCount = 0
    for elem in numList:
        if elem == "+":
            if type(numList[elemCount + 1]) == float:
                finish = mathlib.add(finish, numList[elemCount + 1])
                elemCount += 2
            else:
                print("Err")
                sys.exit(1)
        elif elem == "-":
            if type(numList[elemCount + 1]) == float:
                finish = mathlib.sub(finish, numList[elemCount + 1])
                elemCount += 2
            else:
                print("Err")
                sys.exit(1)
        elif elem == "/":
            if type(numList[elemCount + 1]) == float:
                finish = mathlib.divide(finish, numList[elemCount + 1])
                elemCount += 2
            else:
                print("Err")
                sys.exit(1)
        elif elem == "*":
            if type(numList[elemCount + 1]) == float:
                finish = mathlib.multiply(finish, numList[elemCount + 1])
                elemCount += 2
            else:
                print("Err")
                sys.exit(1)
        elif elem == "^":
            if type(numList[elemCount + 1]) == float:
                finish = mathlib.exponent(finish, numList[elemCount + 1])
                elemCount += 2
            else:
                print("Err")
                sys.exit(1)
        elif elem == "!":
            if type(numList[elemCount - 1]) == float:
                if int(numList[elemCount - 1]) != numList[elemCount - 1]:
                    exit(1)
                finish = mathlib.fact(int(numList[elemCount - 1]))
                elemCount += 1
            else:
                print("Err")
                sys.exit(1)
        elif elem == sqrt:
            if type(numList[elemCount + 1]) == float:
                finish = mathlib.sqrt(numList[elemCount + 1], 2)
                elemCount += 2
            else:
                print("Err")
                sys.exit(1)
        else:
            if elemCount == 0:
                finish = numList[elemCount]
            elemCount += 1
            continue

    return finish




