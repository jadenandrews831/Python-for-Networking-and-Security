import threading
import time

num_threads = 4

def thread_message(msg):
  global num_threads
  num_threads -= 1
  print('Message from thread %s\n' %msg)

while num_threads > 0:
  print("I am the %s thread" %num_threads)
  t = threading.Thread(target=thread_message, args=("I am the %s thread"%num_threads,))
  time.sleep(0.1)
  t.start()