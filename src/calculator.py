"""
    @file calculator.py
    @author Richard Harman, Marek Špirka
"""

""" @package Použivame PYQT5 pre výzor, našu matematickú knižnicu a naše gui"""
from PyQt5 import QtWidgets
from gui import window_calc
import mathlib
from PySide2 import *

memory = []
numbers = 0
sqrt = chr(8730)
pars = False
eq = False

class Calculator_Window(QtWidgets.QMainWindow, window_calc):
    """
        @class Okno aplikácie kalkulačky so sovjimi funkciami a mapovaním tlačidiel a výpisov
    """
    """
        @param self
        @brief Inicializuje okno a namapuje tlačidlá a výpisy
    """
    def __init__(self):
        global memory
        super(Calculator_Window, self).__init__()
        self.setupUi(self)
        self.show()
        self.setFixedSize(245, 495)
        self.setWindowTitle("XOcalc")
        self.setWindowIcon(QtGui.QIcon('calculator_logo.png'))

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

    """ 
        @params self, txt
        @brief rozseká input string na časti (čísla a znamienka) a uloží ich do poľa, následne zavolá počítanie
        @see calcRec
        @see numCalc
        @return výsledok výpočtu
    """
    def mathParse(self, txt):
        tmp = ""
        parts = []
        count = 1
        for char in txt:
            if char == "0" or char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9" or char == ".":
                tmp += char
            elif char == "+" or char == "-" or char == sqrt or char == "*" or char == "/" or char == "e" or char == "!" or char == "^" or char == "(" or char == ")":
                if tmp != "":
                    try:
                        parts.append(float(tmp))
                    except ValueError:
                        return "Syntax Error"
                tmp = ""
                parts.append(char)
            if count == len(txt) and len(tmp) != 0:
                try:
                    parts.append(float(tmp))
                except ValueError:
                    return "Syntax Error"
            count += 1

        try:
            finish = calcRec(parts)
        except ValueError:
            return "Math Error"
        except SyntaxError:
            return "Syntax Error"

        return str(finish)

    """ 
        @params self
        @brief Pri stlačení tlačidla '=' spustí výpoČet a zapíše následne výsledok
    """
    def equals(self):
        global memory
        global numbers
        global eq
        eq = True
        upper_display_text = ""
        for char in memory:
            upper_display_text += char
        self.display_top.setText(upper_display_text)
        out = self.mathParse(upper_display_text)
        self.display_bottom.setText(out)
        memory.clear()
        numbers = 0

    """ 
        @params self, operand
        @brief Pri stlačení tlačidla nejakého operandu, ho pripíše na obrazovku a uloží do pamäte
    """
    def pushed_math_operand(self, operand):
        global numbers
        global memory
        global eq
        text = self.display_bottom.text()
        if text == "Math Error" or text == "Syntax Error":
            text = ""
        if eq:
            if 'E' in text:
                text = str(float(text))
            if 'e' in text:
                text = "{:.9f}".format(float(text))
            if len(text) > 1 or int(text) != 0:
                if numbers == 0:
                    memory.append(text)
                    numbers += 1
                memory.append(operand)
                self.display_bottom.setText(text + operand)
            else:
                memory.append(operand)
                self.display_bottom.setText(operand)
            numbers += 1
        elif numbers == 0:
            memory.append(operand)
            self.display_bottom.setText(operand)
            numbers += 1
        else:
            memory.append(operand)
            self.display_bottom.setText(text + operand)
            numbers += 1

    """ 
        @params self, num
        @brief Pri stlačení tlačidla nejakého čísla, ho pripíše na obrazovku a uloží do pamäte
    """
    def pushed_number(self, num):
        global numbers
        global memory
        text = self.display_bottom.text()
        if text == "Math Error" or text == "Syntax Error":
            text = ""
        memory.append(num)
        if numbers == 0:
            self.display_bottom.setText(num)
            numbers += 1
        else:
            self.display_bottom.setText(text + num)

    """ 
        @params self
        @brief Odstráni posledný znak zo zápisu aj pamäte
    """
    def clear_last_number(self):
        global numbers
        global memory
        text = ""
        text = self.display_bottom.text()
        text = text[:-1]
        if len(memory) > 0:
            memory.pop()
            numbers -= 1
        else:
            numbers += 1
        self.display_bottom.setText(text)
        memory.append(text)

    """ 
        @params self
        @brief Vyprázdni pamäť
    """
    def clear_all(self):
        global numbers
        global memory
        self.display_bottom.setText("0")
        memory.clear()
        numbers = 0


""" 
    @params numlist
    @brief Rozdelí príklady na podpríklady na základe zátvoriek. Tieto podpríklady pošle následne do numCalc
    @see numCalc
    @return Výsledok výpočtu
"""
def calcRec(numlist):
    global pars
    finish = 0
    elemCount = 0
    openPar = 0
    closePar = 0
    tmplist = []
    for part in numlist:
        if part == '(':
            openPar += 1
            lastOpenPos = elemCount
            if type(numlist[elemCount-1]) == float:
                numlist.insert(elemCount, "*")
                calcRec(numlist)
                openPar = 0
                closePar = 0
                break
        if part == ')':
            closePar += 1
        elemCount += 1

    if closePar != openPar:
        raise SyntaxError

    if openPar != 0:
        pars = True
        i = lastOpenPos
        del numlist[i]
        while numlist[i] != ')':
            tmplist.append(numlist[i])
            del numlist[i]
        del numlist[i]
        numlist.insert(lastOpenPos, numCalc(tmplist))
    else:
        tmplist = numlist
        numlist = []
        numlist.insert(0, numCalc(tmplist))

    if len(numlist) != 1:
        calcRec(numlist)

    if numlist[0] == int(numlist[0]):
        numlist[0] = int(numlist[0])
    if len(str(numlist[0])) > 7:
        numlist[0] = "{:.2E}".format(numlist[0])
    elif numlist[0] < 0.001 and numlist[0] > -0.001:
        numlist[0] = "{:.2E}".format(numlist[0])
    else:
        numlist[0] = round(numlist[0], 4)
    return numlist[0]


""" 
    @params numlist
    @brief Vypočíta príklad podľa dôležitosti operandu. najprv '^,!,sqrt', potom '*,/' a nakoniec '+,-'
    @return Výsledok medzivýpočtu
"""
def numCalc(numList):
    elemCount = 0
    tmp = 0
    for elem in numList:
        if elem == "^":
            if type(numList[elemCount + 1]) == float:
                if elemCount - 1 > -1:
                    tmp = mathlib.exponent(numList[elemCount-1], numList[elemCount + 1])
                    del numList[elemCount - 1]
                    del numList[elemCount - 1]
                    del numList[elemCount - 1]
                else:
                    raise SyntaxError
                numList.insert(elemCount - 1, tmp)
                numCalc(numList)
            else:
                raise SyntaxError
        elif elem == "!":
            if type(numList[elemCount - 1]) == float:
                if int(numList[elemCount - 1]) != numList[elemCount - 1]:
                    raise ValueError
                if elemCount - 1 > -1:
                    tmp = mathlib.fact(int(numList[elemCount - 1]))
                    del numList[elemCount - 1]
                    del numList[elemCount - 1]
                else:
                    raise SyntaxError
                numList.insert(elemCount-1, tmp)
                numCalc(numList)
            else:
                raise SyntaxError
        elif elem == sqrt:
            if type(numList[elemCount + 1]) == float:
                if elemCount - 1 > -1:
                    if type(numList[elemCount - 1]) == float:
                        tmp = mathlib.sqrt(numList[elemCount + 1], numList[elemCount - 1])
                        del numList[elemCount - 1]
                        del numList[elemCount - 1]
                        del numList[elemCount - 1]
                    else:
                        tmp = mathlib.sqrt(numList[elemCount + 1], 2)
                        del numList[elemCount]
                        del numList[elemCount]
                elif elemCount == 0:
                    tmp = mathlib.sqrt(numList[elemCount + 1], 2)
                    del numList[elemCount]
                    del numList[elemCount]
                else:
                    raise SyntaxError
                numList.insert(elemCount, tmp)
                numCalc(numList)
            else:
                raise SyntaxError
        else:
            elemCount += 1
            continue

    elemCount = 0
    for elem in numList:
        if elem == "/":
            if type(numList[elemCount + 1]) == float:
                if elemCount - 1 > -1:
                    tmp = mathlib.divide(numList[elemCount - 1], numList[elemCount + 1])
                    del numList[elemCount - 1]
                    del numList[elemCount - 1]
                    del numList[elemCount - 1]
                else:
                    raise SyntaxError
                numList.insert(elemCount - 1, tmp)
                numCalc(numList)
            else:
                raise SyntaxError
        elif elem == "*":
            if type(numList[elemCount + 1]) == float:
                if elemCount - 1 > -1:
                    tmp = mathlib.multiply(numList[elemCount - 1], numList[elemCount + 1])
                    del numList[elemCount - 1]
                    del numList[elemCount - 1]
                    del numList[elemCount - 1]
                else:
                    raise SyntaxError
                numList.insert(elemCount - 1, tmp)
                numCalc(numList)
            else:
                raise SyntaxError
        else:
            elemCount += 1
            continue

    elemCount = 0
    for elem in numList:
        if elem == "+":
            if type(numList[elemCount + 1]) == float:
                if elemCount-1 > -1:
                    tmp = mathlib.add(numList[elemCount - 1], numList[elemCount + 1])
                    del numList[elemCount - 1]
                    del numList[elemCount - 1]
                    del numList[elemCount - 1]
                    numList.insert(elemCount - 1, tmp)
                else:
                    tmp = mathlib.add(0, numList[elemCount + 1])
                    del numList[elemCount]
                    del numList[elemCount]
                    numList.insert(elemCount, tmp)
                numCalc(numList)
            else:
                raise SyntaxError
        elif elem == "-":
            if type(numList[elemCount + 1]) == float:
                if elemCount - 1 > -1:
                    tmp = mathlib.sub(numList[elemCount - 1], numList[elemCount + 1])
                    del numList[elemCount - 1]
                    del numList[elemCount - 1]
                    del numList[elemCount - 1]
                    numList.insert(elemCount - 1, tmp)
                else:
                    tmp = mathlib.sub(0, numList[elemCount + 1])
                    del numList[elemCount]
                    del numList[elemCount]
                    numList.insert(elemCount, tmp)
                numCalc(numList)
            else:
                raise SyntaxError
        else:
            elemCount += 1
            continue

    print(numList, "vysledok")
    return numList[0]



