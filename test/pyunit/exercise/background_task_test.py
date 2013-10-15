# coding: utf-8
'''
Created on Oct 16, 2013

@author: toshi
'''
import unittest
from multiprocessing import Queue, current_process, Pipe
import time
from pyunit.exercise.background_task import BackgroundTask


class BackgroundTaskTest(unittest.TestCase):
    def test_invoke_runs_another_thread(self):
        q = Queue()
        parent, child = Pipe()
        def task():
            q.put(current_process().name)
            time.sleep(1)
            child.send(1)
        sut = BackgroundTask(task)
        sut.invoke()
        parent.recv()
        self.assertNotEquals(q.get(), current_process().name)


if __name__ == "__main__":
    unittest.main()