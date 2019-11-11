
import threading

print(threading.current_thread())
print(threading.active_count())

for t in threading.enumerate():
    print(t)

