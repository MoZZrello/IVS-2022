from mathlib import *
import sys
numbers = sys.stdin.read().split()

N = len(numbers)
average = 0
suma = 0

for i in range(len(numbers)):
    average = add(average, int(numbers[i]))
    suma = add(suma, exponent(int(numbers[i]), 2))

if N == 0:
    print(0)
    exit()

average = multiply(N, exponent(divide(average, N), 2))
s = sqrt(divide(sub(suma, average), sub(N, 1)), 2)

print(s)