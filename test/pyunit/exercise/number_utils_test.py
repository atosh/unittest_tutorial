# coding: utf-8
'''
Created on Oct 15, 2013

@author: toshi
'''
import unittest
from pyunit.exercise.number_utils import NumberUtils


class Test(unittest.TestCase):
    def test_isEven_10_gets_True(self):
        self.assertEquals(NumberUtils.isEven(10), True)

    def test_isEven_7_gets_False(self):
        self.assertEquals(NumberUtils.isEven(7), False)

if __name__ == "__main__":
    unittest.main()