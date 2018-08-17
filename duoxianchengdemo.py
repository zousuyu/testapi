# -*- coding:utf-8 -*-

import threading
import queue

q=queue.Queue()
def product():
    while True:
        for i in range(100):
            q.put(i)
            print("生产了编号为%s号的包子"%i)

def xiaofei():
    while True:
        a=q.get()
        print("吃了编号为%s号的包子"%a)

p1=threading.Thread(target=product)
# p2=threading.Thread(target=product)
x=threading.Thread(target=xiaofei)
p1.start()
# p2.start()
x.start()
p1.join()
p2.join()
x.join()

