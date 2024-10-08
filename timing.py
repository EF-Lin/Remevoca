import atexit
import time


def timer():
    start_time = time.time()
    atexit.register(lambda: print(f'Run time: {time.time() - start_time:.6f}'))
