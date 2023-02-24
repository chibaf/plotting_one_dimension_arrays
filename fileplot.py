# files plot

import numpy as np
import sys
from matplotlib import pyplot as plt

nd=len(sys.argv)-1
listd=[]
for i in range(1,nd+1):
  f = open(sys.argv[i], 'r', encoding='UTF-8')
  data = [float(s.strip()) for s in f.readlines()]
  listd.append(data)
  f.close

fig,ax = plt.subplots(facecolor="w")
x=range(0,len(listd[0]))
for i in range(0,nd):
  plt.plot(x,listd[i],label=str(i+1)+" "+str(sys.argv[i+1]))
ax.legend()
plt.show()