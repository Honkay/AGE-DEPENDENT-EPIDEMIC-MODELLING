import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
#KUWAIT
# SAME PROCEDURE IS REPEATED FOR CAMEROON AND FRANCE BY JUST CHANGING THE PARAMETERS
def
model1(x,t):
a1=2.1
a2=2.3
a3=0.7
a5=0.765
a6=0.678
a7=1.7
a8=0.003
a9=0.45
a10=0.33
a11=0.9
a12=0.54
a13=0.3
a15=0.38
a16=0.65
a17=0.62
a18=0.28
a19=0.0025
a20=0.002
a21=0.74
a22=0.8
a23=0.0021
a24=0.19
S1=x[0]
S2=x[1]
I1=x[2]
I2=x[3]
G1=x[4]
G2=x[5]
R1=x[6]
R2=x[7]
ds1dt=a1*(S1+G1+R1)+a2*(S2+G2+R2)-(a3+a5+a6+a7*(I1+I2))*S1
ds2dt=a3*S1-a8*S2-(a9+a10+a11*(I1+I2))*S2
di1dt=a7*(I1+I2)*S1-(a12+a13)*I1
di2dt=a11*(I1+I2)*S2+a12*I1-a15*I2-a19*I2
dg1dt=a13*I1+a16*S1-(a5+a17+a18)*G1
dg2dt=a15*I2+a16*G1+a9*S2-(a21+a20+a24)*G2
dr1dt=a17*G1+a6*S1-a22*R1
dr2dt=a21*G2+a10*S2+a22*R1-a23*R2
return[ds1dt,ds2dt,di1dt,di2dt,dg1dt,dg2dt,dr1dt,dr2dt]
x0=[4413099,51422,65,194,20,17,30,73]
t=np.linspace(0,10,1000)
x=odeint(model1,x0,t)
s11=x[:,0]
s12=x[:,1]
i11=x[:,2]
i12=x[:,3]
g11=x[:,4]
g12=x[:,5]
r11=x[:,6]
r12=x[:,7]
plt.plot(t,i11,'r-',label='$I_{1}$ Kuwait')
plt.plot(t,i12,'b--',label='$I_{2}$ Kuwait')
plt.xlabel('t')
plt.ylabel('$I_{1}$ and $I_{2}$ ')
plt.legend()
plt.plot(t,g11,'r-',label='$G_{1}$ Kuwait')
plt.plot(t,g12,'b--',label='$G_{2}$ Kuwait')
plt.xlabel('t')
plt.ylabel('$G_{1}$ and $G_{2}$ ')
plt.legend()
plt.plot(t,r11,'r-',label='$R_{1}$ Kuwait')
plt.plot(t,r12,'b--',label='$R_{2}$ Kuwait')
plt.xlabel('t')
plt.ylabel('$R_{1}$ and $R_{2}$ ')
plt.legend()