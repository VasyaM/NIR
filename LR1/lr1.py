# -*- coding: utf-8 -*-
# LR 1
import random
import numpy as np
import  matplotlib
import matplotlib.pyplot as plt
N = 20  # Number of abonents
p = 0.01  # p of message

FN = 200  # number of frames
Slots = np.zeros(N)  # slots in frame


Buf = np.zeros(N)  # message buffer
FrameTimer = [[] * 1 for i in range(N)]


SrT = 0  # average time

MsgIn = 0
ServNum = 0  # messages served
BufNum = 0  # messages buffered
def reset():
    global Slots, Buf, FrameTimer, SrT, ServNum, BufNum, MsgIn
    Slots = np.zeros(N)  # slots in frame

    Buf = np.zeros(N)  # message buffer
    FrameTimer = [[] * 1 for i in range(N)]

    SrT = 0  # average time
    MsgIn = 0
    ServNum = 0  # messages served
    BufNum = 0  # messages buffered

def gen(p):
    frame = np.random.binomial(1, p, (N, N)).tolist()
    return frame


def TakeFromBuffer():
    slots = np.zeros(N)
    for i in range(N):
        if Buf[i] > 0:
            Buf[i] -= 1
            slots[i] = 1
            global SrT
            SrT+= FrameTimer[i][0]
            FrameTimer[i].pop(0)
    return slots
def AddTime(timer):
    for i in range(len(timer)):
        for j in range(len(timer[i])):
            timer[i][j]+=1
    return timer
def Simulate():
    global FrameTimer,ServNum,BufNum,Buf,p,MsgIn,SrT
    for i in range(FN):

        FrameTimer = AddTime(FrameTimer)
        frame = gen(p)
        MsgIn +=sum(sum(frame,[]))
#        print(frame)
#        print("--- Frame ", i,"---")
#        print("Buffer before", Buf)
        Slots = np.zeros(N)
        Slots = TakeFromBuffer()
#        print("Slots", Slots)
#        print("Buffer after", Buf)
        # print(frame)
        for j in range(N):
            if Slots[j] == 0 and frame[j][j] == 1:
                frame[j][j] = 0
                # print(j,frame[j])
                Slots[j]=1
                ServNum += 1
            BufNum += sum(frame[j])
            ServNum += sum(Slots)
            for k in range(N):
                if frame[j][k] >0:
                    FrameTimer[k].append(1)
            Buf = np.add(Buf, frame[j])
        #print("Frame",frame)
#        print("frtime",FrameTimer)
#        print("Buffer End",Buf, "\n ------------")


#    print("Messages served",ServNum)
#    print("Messages buffered", BufNum)
#    print("Messages Left in buffer",sum(Buf))
#    print("messages total", MsgIn, ServNum)
#    print(SrT/FN)
    SrT+= sum(sum(FrameTimer,[]))
    out = SrT/MsgIn
    #print(out)
    return out
SrtList =[]
px=[]
for i in range(9):
    p+=(1/N)/9
    print(i,'/10')
    px.append(p)
    reset()
    SrtList.append(Simulate())
print(p)
print(SrtList)
plt.plot(px,SrtList)
plt.show()

