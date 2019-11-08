from multiprocessing import Process, Lock, Array
import os

global x
x = 0


def f(l, i, a):
    while(a[x] < 97):
        l.acquire()
        a[x] = a[x]+1
        l.release()
        os.system('python ./rnn.py ' + str(a[x]))

if __name__ == '__main__':
    lock = Lock()
    arr = Array('i', range(97))

    for num in range(10):
        Process(target=f, args=(lock, num, arr)).start()