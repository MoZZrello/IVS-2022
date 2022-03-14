pi = float(3.14159265358979323846264338327950288419716939937510)
e = float(2.71828182845904523536028747135266249775724709369995957496696762772407663035354759457138217852516642742746639)


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def fact(num):
    f = 1
    for i in range(1, num+1):
        f = f*i
    return f


def exponent(num, exp):
    return num ** exp


def sqrt(num, root):
    return num ** (1/root)


def expe(num):
    ret = e
    for i in range(0, num-1):
        ret = e * e
    return ret


def modulo(num1, num2):
    return num1 % num2


