#random triangle code thingy cool shape
import numpy as np
import matplotlib.pyplot as plt
import random as r

#triangle coordinates

corners_x=[0,0.5,1]
corners_y=[0,1,0]
#(0,0)   - A
#(0.5,1) - B
#(1,0)   - C

x=[0,0.5,1]
y=[0,1,0]
#plt.scatter(x,y)

#start at point B
nu_point=[0.5,0]
for i in range(10**5):
    index=r.randint(0,2)
    #x-coordinate calculation
    nu_x=np.mean([nu_point[0],corners_x[index]])

    #same for y!!
    nu_y=np.mean([nu_point[1],corners_y[index]])
    
    #record the new point coordinates
    nu_point[0]=nu_x
    nu_point[1]=nu_y
    
    #also append to big x/y arrays to plot at the end :)
    x.append(nu_x)
    y.append(nu_y)
plt.scatter(x,y,s=0.01)
