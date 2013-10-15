# coding: utf-8
'''
Created on Oct 15, 2013

@author: toshi
'''

class Calculator(object):
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y == 0:
            raise ValueError('divide by zero.')
        return float(x) / float(y)