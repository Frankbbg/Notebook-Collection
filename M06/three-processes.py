'''
This program uses the multiprocessing module to start three separate processes to get the time and wait a random number 
of seconds. The functions are defined, then the processes are declared with targets pointing to the functions, 
then the processes are started and joined to wait for child processes to finish.
'''

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