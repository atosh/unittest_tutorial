# coding: utf-8
'''
Created on Oct 15, 2013

@author: toshi
'''

class ItemStock(object):
    def __init__(self):
        self.values = {}
    def add(self, item):
        self.values = self._add(item, self.values)
    def _add(self, item, values):
        num = self._getNum(item, values)
        values[item.name] = num + 1
        return values
    def getNum(self, item):
        return self._getNum(item, self.values)
    def _getNum(self, item, values):
        return values.get(item.name) or 0
