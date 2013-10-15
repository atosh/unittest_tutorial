# coding: utf-8
'''
Created on Oct 15, 2013

@author: toshi
'''
import unittest
from pyunit.exercise.calculator import Calculator

class CalculatorTest(unittest.TestCase):

    def test_multiply_3_4(self):
        sut = Calculator()
        expected = 12
        actual = sut.multiply(3, 4)
        self.assertEquals(actual, expected)

    def test_multiply_5_7(self):
        sut = Calculator()
        expected = 35
        actual = sut.multiply(5, 7)
        self.assertEquals(actual, expected)

    def test_divide_3_2(self):
        sut = Calculator()
        expected = 1.5
        actual= sut.divide(3, 2)
        self.assertAlmostEquals(actual, expected)
        
    def test_divide_5_0(self):
        with self.assertRaises(ValueError):
            sut = Calculator()
            sut.divide(5, 0)

if __name__ == '__main__':
    unittest.main()