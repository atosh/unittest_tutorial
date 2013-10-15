# coding: utf-8
'''
Created on Oct 15, 2013

@author: toshi
'''
import unittest
from pyunit.exercise.item import Item
from pyunit.exercise.item_stock import ItemStock


class InitialState(unittest.TestCase):
    def setUp(self):
        self.book = Item('book', 3800)
        self.sut = ItemStock()
    def test_getNum_book_gets_0(self):
        self.assertEquals(self.sut.getNum(self.book), 0)
    def test_add_book_gets_1(self):
        self.sut.add(self.book)
        self.assertEquals(self.sut.getNum(self.book), 1)

class Add1State(unittest.TestCase):
    def setUp(self):
        self.book = Item('book', 3800)
        self.sut = ItemStock()
        self.sut.add(self.book)
    def test_getNum_book_gets_1(self):
        self.assertEquals(self.sut.getNum(self.book), 1)
    def test_add_book_gets_2(self):
        self.sut.add(self.book)
        self.assertEquals(self.sut.getNum(self.book), 2)
    def test_add_other_gets_1(self):
        self.sut.add(Item('bike', 57000))
        self.assertEquals(self.sut.getNum(self.book), 1)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()