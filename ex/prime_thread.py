from threading import Thread
import threading
import math


class PrimeThread(Thread):
    def __init__(self, num, file):
        Thread.__init__(self)
        self.num = num
        self.file = file

    def run(self):
        for n in range(2, math.ceil(math.sqrt(self.num))):
            if self.num % n == 0:
                f.write(f"{self.num} is not a prime number!\n")
                break
        else:
            f.write(f"{self.num} is a prime number!\n")


f = open("prime.txt", "wt")
nums = [393939393, 12121212121, 29292939327, 38433828283, 62551414124111]
for n in nums:
    t = PrimeThread(n, f)
    t.start()

# Wait until all thread are done before closing file

ct = threading.current_thread()
for t in threading.enumerate():
    if ct != t:
       t.join()  # wait until thread is terminated

f.close()