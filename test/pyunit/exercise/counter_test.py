# coding: utf-8
'''
Created on Oct 15, 2013

@author: toshi
'''
import unittest
from pyunit.exercise.counter import Counter

class InitialState(unittest.TestCase):
    def setUp(self):
        self.sut = Counter()
    def test_increment_1(self):
        self.assertEquals(self.sut.increment(), 1)

class FirstState(unittest.TestCase):
    def setUp(self):
        self.sut = Counter()
        self.sut.increment()
    def test_increment_2(self):
        self.assertEquals(self.sut.increment(), 2)

class FiftiethState(unittest.TestCase):
    def setUp(self):
        self.sut = Counter()
        for _ in range(50): self.sut.increment()
    def test_increment_51(self):
        self.assertEquals(self.sut.increment(), 51)


if __name__ == "__main__":
    unittest.main()