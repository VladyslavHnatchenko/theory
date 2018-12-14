import multiprocessing
import threading
from multiprocessing import Queue


class Worker(threading.Thread):

    def __init__(self, work_queue, word):
        super(Worker, self).__init__()
        self.work_queue = work_queue
        self.word = word

    def run(self):
        try:
            filename = self.work_queue.get()
            self.process(filename)
        finally:
            pass

    def process(self, filename):
        previous = ''
        current = True
        with open(filename, "rb") as fh:
            while current:
                current = fh.readline()
                if not current:
                    break
                current = current.decode("utf8", "ignore")
                if self.word in current:
                    print("find {0}: {1}".format(self.word, filename))
                previous = current


word = "import"
file_list = ["./file_1.py", "./file_2.py", "./file_3.py"]
work_queue = multiprocessing.Queue()

for filename in file_list:
    work_queue.put(filename)

for i in range(3):
    worker = Worker(work_queue, word)
    worker.start()


# import threading
# import time
#
#
# class ClockThread(threading.Thread):
#     def __init__(self, interval):
#         threading.Thread.__init__(self)
#         self.daemon = True
#         self.interval = interval
#
#     def run(self):
#         while True:
#             print("The tim is %s" % time.ctime())
#             time.sleep(self.interval)
#
#
# t = ClockThread(15)
# t.start()

# import threading
# import time
#
#
# def clock(interval):
#     while True:
#         print("The time is %s" % time.ctime())
#         time.sleep(interval)
#
#
# t = threading.Thread(target=clock, args=(15,))
# t.daemon = True
# t.start()

# import os
# import subprocess
# import sys
#
#
# child = os.path.join(os.path.dirname(__file__), "./child.py")
# word = "word"
# file = ["./parent.py,", "./child.py"]
#
# pipes = []
# for i in range(0, 2):
#     command = [sys.executable, child]
#     pipe = subprocess.Popen(command, stdin=subprocess.PIPE)
#     pipes.append(pipe)
#     pipe.stdin.write(word.encode("utf8") + b"\n")
#     pipe.stdin.write(file[i].encode("utf8") + b"\n")
#     pipe.stdin.close()
#
# while pipes:
#     pipe = pipes.pop()
#     pipe.wait()
