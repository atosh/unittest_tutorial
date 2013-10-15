# coding: utf-8
'''
Created on Oct 15, 2013

@author: toshi
'''
from multiprocessing import Process

class BackgroundTask(object):
    def __init__(self, task):
        self.task = task
    def invoke(self):
        p = Process(target=self.task)
        p.start()
