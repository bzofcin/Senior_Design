from multiprocessing import Process, Lock, Array
import os
import DirectoryInfo as di

global x
x = 0

def f(l, i, a, t):

    while a[x] < t:
        l.acquire()
        a[x] = a[x]+1
        l.release()
        os.system('python ./MetaData.py ' + str(a[x]) + ' ' + str(25) + ' ' + str(30))


if __name__ == '__main__':
    lock = Lock()
    Stock_Dir = "./Test_Stock/"
    Directory = "Processed_Data"
    Stocks = os.listdir(Stock_Dir)
    StockNum = len(Stocks)
    arr = Array('i', range(-1, StockNum))
    di.CreateDir(Directory)
    for num in range(StockNum):
        Process(target=f, args=(lock, num, arr, StockNum-1)).start()