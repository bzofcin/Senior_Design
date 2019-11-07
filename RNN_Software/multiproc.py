from multiprocessing import Process, Lock
import os

def f(l, i):
    l.acquire()
    print ('hello world', i)
    os.system('python ./P16-Deep-Learning-AZ/Deep_Learning_A_Z/P16-Recurrent-Neural-Networks/Recurrent_Neural_Networks/rnn.py')
    l.release()

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()