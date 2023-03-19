#This code plots the mandelbrot set
import numpy as np
import matplotlib.pyplot as plt
res=1000
real=np.linspace(-2,2,res)
imag=np.linspace(-1,1,res)
x=[]
y=[]
cnt=0
for r in real:
    cnt+=1
    print(cnt,'/',len(real))
    for i in imag:
        c=complex(r,i) #c=/z=
        n=0
        z=0.2 #z=0/c=
        while True:
            z_sq=z**2+c
            if n>=80: #max_iter
                break
            if abs(z_sq)>=10:
                break
            n+=1
            z=z_sq
        if abs(z_sq)<=2:
            x.append(r)
            y.append(i)

plt.scatter(x,y,s=1)
plt.title(f'resolution={res}x{res}')
plt.show