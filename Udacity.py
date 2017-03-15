import numpy as np


scores = [3.0,1.0,0.2]


def softmax(x):
    e_x = np.exp(x) / np.sum(np.exp(x), axis=0)
    return e_x

#print softmax(scores / 10)

a = 1000000000
def addUp(x):
    b = 1000000000
    for i in xrange(1000000):
        b =x+b
    b= b-1000000000
    return b
print addUp(0.000001)
