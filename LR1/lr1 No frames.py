# -*- coding: utf-8 -*-
# LR 1 no frames
import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

N = 30  # Number of abonents
p = 0.001  # p of message
collisions = 0
passed = 0
pColl = []
px=[]

def gen(p):
    frame = np.random.binomial(1, p, N).tolist()
    return frame


def reset():
    global collisions, passed
    collisions, passed = 0, 0


def Simulation():
    simLen = 500  # sinulation lenght
    reset()
    tempCollisions =0
    global collisions, passed, pColl
    for i in range(simLen):
        if (sum(gen(p))) > 1:
            collisions += 1
    pColl.append(collisions / simLen)

for i in range(190):
    p+=1/200
    px.append(p)
    Simulation()
    if pColl[-1] == 1.0: break

plt.plot(px,pColl)
plt.show()
#Simulation()
#print(pColl)
#print(gen(1))