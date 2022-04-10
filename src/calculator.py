from PyQt5 import QtWidgets
from gui import window_calc
import sys
from PySide2 import *


class Calculator_Window(QtWidgets.QMainWindow, window_calc):
    def __init__(self):
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
        self.button_sqrt.clicked.connect(lambda: self.pushed_math_operand((chr(8730))))

        self.button_delete.clicked.connect(lambda: self.clear_last_number)
        self.button_delete.clicked.connect(lambda: self.clear_all)

    def pushed_math_operand(self, operand):
        text = self.display_bottom.text()
        self.display_bottom.setText(text+operand)

    def pushed_number(self, num):
        text = self.display_bottom.text()
        self.display_bottom.setText(text+num)

    def clear_last_number(self):
        self.display_bottom.setText("")

    def clear_all(self):
        self.display_bottom.setText("")




