import multiprocessing as mp
import random
import datetime
import time

def process1():
    time.sleep(random.randint(0, 1))
    print(datetime.datetime.now().ctime())

def process2():
    time.sleep(random.randint(0, 1))
    print(datetime.datetime.now().ctime())

def process3():
    time.sleep(random.randint(0, 1))
    print(datetime.datetime.now().ctime())

if __name__ == "__main__":
    proc1 = mp.Process(target=process1)
    proc2 = mp.Process(target=process2)
    proc3 = mp.Process(target=process3)

    proc1.start()
    proc2.start()
    proc3.start()

    proc1.join()
    proc2.join()
    proc3.join()