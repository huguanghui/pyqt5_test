#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import time

if hasattr(sys, "frozen"):
    os.environ["PATH"] = sys._MEIPASS + ";" + os.environ["PATH"]

from PyQt5.QtCore import QThreadPool, QRunnable, pyqtSignal


class Worker(QRunnable):
    def __init__(self, task):
        super().__init__()
        self.task = task

    def run(self):
        # 执行任务
        self.task()
        time.sleep(1)


class Manager:
    def __init__(self):
        self.threadpool = QThreadPool()

    def add_task(self, task):
        worker = Worker(task)
        self.threadpool.start(worker)


if __name__ == "__main__":
    manager = Manager()
    manager.add_task(lambda: print("Task 1"))
    manager.add_task(lambda: print("Task 2"))
    manager.add_task(lambda: print("Task 3"))
    # 等待所有任务完成
    manager.threadpool.waitForDone()
