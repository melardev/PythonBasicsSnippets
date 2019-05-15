'''
Snippet on __enter__ and __exit__ which are the functions called when using with: construct
'''
import time


class Benchmark:
    def __enter__(self):
        self.start = time.time()
        self.end = 0
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        #  exc_tb is the traceback
        self.end = time.time() - self.start


with Benchmark() as benchmark:
    time.sleep(2)
    # perform some work you wanna benchmark

print(benchmark.end)
