from multiprocessing import Process, Lock, Array
import os
import time

global x
x = 0

start_time = time.time()
def f(l, i, a):
    while(a[x] < 10):
        l.acquire()
        a[x] = a[x]+1
        l.release()
        os.system('python ./rnnmultvar.py ' + str(a[x]))

if __name__ == '__main__':
    lock = Lock()
    arr = Array('i', range(10))

    for num in range(9):
        Process(target=f, args=(lock, num, arr)).start()

    print("--- %s seconds ---" % (time.time() - start_time))