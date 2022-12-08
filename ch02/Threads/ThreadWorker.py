import threading
class ThreadWorker(threading.Thread):
  def __init__(self):
    super().__init__()
  def run(self):
    for i in range(10):
      print(i)

