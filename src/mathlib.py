import sys

pi = float(3.14159265358979323846264338327950288419716939937510)
e = float(2.71828182845904523536028747135266249775724709369995957496696762772407663035354759457138217852516642742746639)


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        raise ValueError('Can not divide by zero!')
    return num1 / num2


def fact(num):
    if num < 0:
        raise ValueError('Can not make a factorial from negative number!')
    elif num == 0:
        return 1
    f = 1
    for i in range(1, num+1):
        f = f*i
    return f


def exponent(num, exp):
    return num ** exp


def sqrt(num, root):
    if num < 0:
        raise ValueError('Can not do sqrt() with negative number!')
    return num ** (1/root)


def expe(num):
    return e**num


def modulo(num1, num2):
    return num1 % num2


