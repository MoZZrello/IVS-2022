"""
    @file XOcalc.pyw
    @author Marek Špirka
    @brief Zapnutie celej kalkulačky
"""
import sys
from calculator import Calculator_Window
from PySide2.QtWidgets import QApplication


app = QApplication(sys.argv)

calculator = Calculator_Window()
sys.exit(app.exec_())

