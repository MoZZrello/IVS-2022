import unittest
import random
import mathlib
import numpy

iterate = 10


class CalcTest(unittest.TestCase):

    def test_ADD(self):
        for i in range(iterate):
            with self.subTest(i=i):
                a, b = randomNumbers(-9999, 9999)
                c = a+b
                self.assertEqual(mathlib.add(a, b), c)

    def test_SUB(self):
        for i in range(iterate):
            with self.subTest(i=i):
                a, b = randomNumbers(-9999, 9999)
                c = a-b
                self.assertEqual(mathlib.sub(a, b), c)

    def test_MULTIPLY(self):
        for i in range(iterate):
            with self.subTest(i=i):
                a, b = randomNumbers(-9999, 9999)
                c = a*b
                self.assertEqual(mathlib.multiply(a, b), c)

    def test_DIVIDE(self):
        for i in range(iterate):
            with self.subTest(i=i):
                a, b = randomNumbers(-9999, 9999)
                c = a/b
                self.assertEqual(mathlib.divide(a, b), c)

        with self.assertRaises(ValueError):
            mathlib.divide(10, 0)

    def test_FACTORIAL(self):
        for i in range(iterate):
            with self.subTest(i=i):
                a, b = randomNumbers(0, 100)
                c = numpy.math.factorial(a)
                self.assertEqual(mathlib.fact(a), c)
        for i in range(iterate):
            with self.subTest(i=i):
                a, b = randomNumbers(-9999, -1)
                with self.assertRaises(ValueError):
                    mathlib.fact(a)

    def test_EXPONENT(self):
        for i in range(iterate):
            with self.subTest(i=i):
                a, b = randomNumbers(-99, 99)
                c = a**b
                self.assertEqual(mathlib.exponent(a, b), c)

    def test_SQRT(self):
        for i in range(iterate):
            with self.subTest(i=i):
                a, b = randomNumbers(0, 9999)
                c = numpy.math.sqrt(a)
                self.assertEqual(mathlib.sqrt(a, 2), c)
        for i in range(iterate):
            with self.subTest(i=i):
                a, b = randomNumbers(-9999, -1)
                with self.assertRaises(ValueError):
                    mathlib.sqrt(a, 2)

    def test_expe(self):
        for i in range(iterate):
            with self.subTest(i=i):
                a, b = randomNumbers(-10, 10)
                c = numpy.math.exp(a)
                self.assertEqual(round(mathlib.expe(a), 3), round(c, 3))

    def test_modulo(self):
        for i in range(iterate):
            with self.subTest(i=i):
                a, b = randomNumbers(-9999, 9999)
                c = a % b
                self.assertEqual(mathlib.modulo(a, b), c)


def randomNumbers(num1, num2):
    a = random.randint(num1, num2)
    b = random.randint(num1, num2)
    return a, b


if __name__ == '__main__':
    unittest.main()
