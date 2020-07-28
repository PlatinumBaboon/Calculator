import unittest
from BODMASCalculator import math


class MyTestCase(unittest.TestCase):
    def test_subtraction(self):
        data = '- 1 - 8 - 9 - 2'
        result = math(data)
        self.assertEqual(result, '-20')
        print('ok')

    def test_Bodmas(self):
        data = '20 - 2 * 8 ^ 2 / 4 + 9'
        result = math(data)
        self.assertEqual(result, '-3.0')
    def test_Multiply(self):
        data = '1 * 8 * 3'
        result = math(data)
        self.assertEqual(result, '24')

    def test_Division(self):
        data = '30 / 3 / 2 '
        result = math(data)
        self.assertEqual(result, '5.0')

    def test_Addition(self):
        data = '30 + 3 +2'
        result = math(data)
        self.assertEqual(result, '35')

    def test_Power(self):
        data = '3 ^ 2 ^2'
        result = math(data)
        self.assertEqual(result, '81.0')

    def test_Brackets(self):
        data = '(5 + (4 ^2) - 10) *(9 /(10 -7))'
        result = math(data)
        self.assertEqual(result, '33.0')

    def test_power_minus(self):
        data = '4^ - 1 + 2 ^- 1'
        result = math(data)
        self.assertEqual(result, '0.75')

    def test_plus_minus(self):
        data = '1 -+ 4 +- 6 '
        result = math(data)
        self.assertEqual(result, '-9')

    def test_minus_plus(self):
        data = '-24 + 10'
        result = math(data)
        self.assertEqual(result, '-14')

    def test_minus_plusplus(self):
        data = '-24 -- 10'
        result = math(data)
        self.assertEqual(result, '-14')

    def test_multiple_minus(self):
        data = '1 * - 6 + 3 *-4'
        result = math(data)
        self.assertEqual(result, '-18')

    def test_divide_minus(self):
        data = '24 / - 6 + 12 / -4'
        result = math(data)
        self.assertEqual(result, '-7.0')

    def test_minus_minus(self):
        data = '24 -- 6 - 12 --4'
        result = math(data)
        self.assertEqual(result, '22')

    def test_long_equation(self):
        data = '(5 +- (4 ^-1) - 10) *(9 /(-10 +7))'
        result = math(data)
        self.assertEqual(result, '15.75')
        
    def test_letters(self):
        data = 'huguhu'
        result = math(data)
        self.assertEqual(result, '')

    def test_letters_and_numbers(self):
        data = 'hug785hu'
        result = math(data)
        self.assertEqual(result, '')

    def test_letters_and_symbols(self):
        data = 'hu*g+u-hu'
        result = math(data)
        self.assertEqual(result, '')

    def test_divide_by_zero(self):
        data = '6/0'
        result = math(data)
        self.assertEqual(result, '')


if __name__ == '__main__':
    unittest.main()
