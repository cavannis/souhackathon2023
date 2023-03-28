import time

class Slowprinter:
    def __init__(self, delay=0.1):
        self.delay = delay
    
    def slow_print(self, text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(self.delay)
        print()
