# files plot

import numpy as np
import sys
import matplotlib.pyplot as plt

nd=len(sys.argv)-1

print(nd)

listd=[]
for i in range(1,nd+1):
  f = open(sys.argv[i], 'r', encoding='UTF-8')
  data = [float(s.strip()) for s in f.readlines()]
  listd.append(data)
  f.close
x=range(0,len(listd[0]))
for i in range(0,nd):
  plt.plot(x,listd[i])
plt.pause(1)