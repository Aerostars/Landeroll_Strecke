from numpy import *
from pylab import *

f=1.2           #Sicherheit gegen Stall
clmax=2.8
mue=0.6         #Reibungskoef, Gummi/runway
rho=1.225       #SL/15°C
g=9.81

S_G=linspace(0.001,0.5,200)
G_F=linspace(0,8000,200)
X,Y = meshgrid(S_G,G_F)
Z=(f**2)*(Y)/(rho*g*clmax*(X+mue))

figure().canvas.set_window_title('Lande_Rollstrecke')
levels = [0,50,100,150,200,250,300,350,400,450,500,600]
colormap =cm.get_cmap('jet', len(levels)-1)
c=colormap

c = contourf(X,Y,Z,levels,cmap=colormap,linewidth='5')
clabel(c, fontsize=10,colors='k') 
title('Landerollstrecke s[m]=f(S/G,G/F)')
xlabel('Schubumkehr S/G')
ylabel('G/F[N/m**2]')
text(0.1,1000,'clmax=%s'%clmax,color="white")
text(0.1,800,'mue=%s'%mue,color="white")
text(0.1,600,'v/vstall=%s'%f,color="white")
colorbar(c)

ylim(0,7000)
xlim(0,0.5)


grid(True)

#savefig("Contour.pdf")
show()
