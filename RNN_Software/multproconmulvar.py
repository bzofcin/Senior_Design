from multiprocessing import Process, Lock, Array
import os
import time

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
global x
x = 0

start_time = time.time()
def f(l, i, a,x):
    while(a[x] <  19):
        l.acquire()
        a[x] = a[x]+1
        temp = "./MultiVarTestOuput/Multivarsub/" + str(a[x]) + '.txt'
        print(a[x])
        l.release()
        open(temp, 'w+')
        os.system('python ./rnnmultvar.py' + ' ' + str(a[x] - 1) + ' > ' + str(temp) )

if __name__ == '__main__':
    lock = Lock()
    arr = Array('i', range(19))

    for num in range(10):
        Process(target=f, args=(lock, num, arr,x)).start()

    print("--- %s seconds ---" % (time.time() - start_time))
