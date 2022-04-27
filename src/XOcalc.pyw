"""
    @file main.py
    @author Marek Špirka
    @package Importujeme kalkulačku z iného súboru a používame PySide2 pre aplikáciu
"""
import sys
from calculator import Calculator_Window
from PySide2.QtWidgets import QApplication


app = QApplication(sys.argv)

calculator = Calculator_Window()
sys.exit(app.exec_())

