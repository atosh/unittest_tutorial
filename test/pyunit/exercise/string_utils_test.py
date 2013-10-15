# coding: utf-8
'''
Created on Oct 15, 2013

@author: toshi
'''
import unittest
from pyunit.exercise.string_utils import StringUtils

class StringUtilsTest(unittest.TestCase):

    def test_toSnakeCase_aaa(self):
        self.assertEquals(StringUtils.toSnakeCase('aaa'), 'aaa')
        
    def test_toSnakeCase_HelloWorld(self):
        self.assertEquals(StringUtils.toSnakeCase('HelloWorld'), 'hello_world')

    def test_toSnakeCase_practiceJunit(self):
        self.assertEquals(StringUtils.toSnakeCase('practiceJunit'), 'practice_junit')

if __name__ == "__main__":
    unittest.main()