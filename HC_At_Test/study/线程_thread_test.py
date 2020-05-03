# -*-coding:utf-8-*-
import threading
def run(num):
    print(threading.currentThread().getName()+ '\n')
    print(num)

if __name__ == "__main__":
    for i in range(5):
        my_thread = threading.Thread(target=run,args=(i,))
        my_thread.start()