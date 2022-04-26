"""
    @brief Výpočet výběrové směrodatné odchylky
    @file profiling.py
    @author Andrea Michlíková
"""

from mathlib import *

""" Načteme čísla ze vstupu do proměnné. """
import sys
numbers = sys.stdin.read().split()

N = len(numbers)

""" Kontrola jestli byla zadaná nějaká čisla. """
if N == 0:
    print(0)
    exit()

average = 0
suma = 0

""" Sečtení všech hodnot pro výpočet průměru a výpočet sumy čtverců xi."""
for i in range(len(numbers)):
    average = add(average, int(numbers[i]))
    suma = add(suma, exponent(int(numbers[i]), 2))

""" Výpočet aritmetického průměru. """
average = multiply(N, exponent(divide(average, N), 2))

""" Dopočítání odchylky. """
s = sqrt(divide(sub(suma, average), sub(N, 1)), 2)

print(s)