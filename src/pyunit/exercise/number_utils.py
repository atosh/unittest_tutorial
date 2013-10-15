# coding: utf-8
'''
Created on Oct 15, 2013

@author: toshi
'''

class NumberUtils(object):
    @classmethod
    def isEven(self, x):
        if not isinstance(x, int):
            raise TypeError('%s is not int type.' % x)
        return x % 2 == 0
