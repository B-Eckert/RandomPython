import threading
import time
# This is just to provide as an example of how multithreading works and to teach me a few things about multithreading in Python

class SharedResourceObject:
    def __init__(self, value, value2):
        self.value = value
        self.value2 = value2
    def change(self, newValue):
        self.value = newValue
    def changeTwo(self, newValue2):
        self.value2 = newValue2
    def get(self):
        return self.value
    def getTwo(self):
        return self.value2
shared_resource = SharedResourceObject("Hello", "World")
lock = threading.Lock()
lock2 = threading.Lock()
def print_x():
    print("x1")
    with lock:
        time.sleep(1)
        shared_resource.change("x")
        print("resource changed to x")
    print("x2")
def print_y():
    print("y1")
    with lock:
        shared_resource.change("y")
        print("resource changed to y")
    print("y2")
def write_z():
    print("z1")
    with lock2:
        time.sleep(0.5)
        shared_resource.changeTwo("z")
        print("resource2 changed to z")
    print("z2")
def write_a():
    print("a1")
    with lock2:
        shared_resource.changeTwo("a")
        print("resource2 changed to a")
    print("a2")
t1 = threading.Thread(target=print_x)
t2 = threading.Thread(target=print_y)
t3 = threading.Thread(target=write_z)
t4 = threading.Thread(target=write_a)

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()
print("Done:", shared_resource.get(), "and", shared_resource.getTwo())