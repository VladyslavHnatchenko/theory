import threading
from urllib.request import urlopen


class WorkerThread(threading.Thread):
    def __init__(self, url_list, url_list_lock):
        super(WorkerThread, self).__init__()
        self.url_list = url_list
        self.url_list_lock = url_list_lock

    def run(self):
        while 1:
            next_url = self.grab_next_url()
            if next_url is None:
                break
            self.retrieve_url(next_url)

    def grab_next_url(self):
        self.url_list_lock.acquire(1)
        if len(self.url_list) < 1:
            next_url = None
        else:
            next_url = self.url_list[0]
            del self.url_list[0]
        self.url_list_lock.release()
        return next_url

    def retrieve_url(self, next_url):
        text = urlopen(next_url).read()
        print(text)
        print("############## %s #############" % next_url)


url_list = [
    "http://linux.org.ru",
    "http://kernel.org",
    "http://python.org",
]
url_list_lock = threading.Lock()
worker_thread_list = []

for x in range(0, 3):
    new_thread = WorkerThread(url_list, url_list_lock)
    worker_thread_list.append(new_thread)
    new_thread.start()

for x in range(0, 3):
    worker_thread_list[x].join()

# import sys
#
#
# word = sys.stdin.readline().rstrip()
# filename = sys.stdin.readline().rstrip()
#
# try:
#     with open(filename, "rb") as fh:
#         while True:
#             current = fh.readline()
#             if not current:
#                 break
#             if word in current:
#                 print("find: {0} {1}".format(filename, word))
# except:
#     pass
