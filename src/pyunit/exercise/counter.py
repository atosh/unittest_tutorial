# coding: utf-8
'''
Created on Oct 15, 2013

@author: toshi
'''

class Counter(object):
    def __init__(self):
        self.count = 0
        
    def increment(self):
        self.count += 1
        return self.count