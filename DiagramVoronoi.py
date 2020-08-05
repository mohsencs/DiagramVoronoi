#sudo apt-get install python3-tk
import random;
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch



############   define m function   #################
def m(p1,p2):
    return -(p1[0][0]-p2[0][0])/(p1[1][0]-p2[1][0]);
####################################################


#######    define subtract of tow vectors   ########
def subtract(p1,p2):
    p3 = []
    p3.append([]);
    p3.append([]);
    for i in range(len(p1[0][:])):
        p3[0].append(p1[0][i] - p2[0][i]);
        p3[1].append(p1[1][i] - p2[1][i]);
    return p3;
###  define sum of power of tow on the vector  #####
def SumPow2Vector(p):
    result = 0;
    #p is similar to p = [[2][3]]
    length = len(p[:][0]);
    for i in range(length):
        result = result + (p[0][i]**2) + (p[1][i]**2) ;
    return result;
#########    define distance function    ###########
def distance(p1,p2):
    return (SumPow2Vector(subtract(p1,p2)))**(1/2);
####################################################


###########    define contact function    ##########
def contact(p1,p2,p3,p4):
    return (1/(m(p1,p2)-m(p3,p4)))*(m(p1,p2)*(p1[0][0]+p2[0][0])/2 - m(p3,p4)*(p3[0][0]+p4[0][0])/2 + (p3[1][0]+p4[1][0])/2 -(p1[1][0]+p2[1][0])/2);
####################################################


#############    define y unction     ##############
def y(x,point1,point2):
    return ( m(point1,point2)*(x -(point1[0][0]+point2[0][0])/2)+(point1[1][0]+point2[1][0])/2);
           #(m(ps(:,i),ps(:,j))*(x-(ps(1,i)+ps(1,j))/2)+(ps(2,i)+ps(2,j))/2);
####################################################

##############   sort one array   ##################
def sort(array,size):
    for i in range(size):
        for j in range(i+1,size):
            if array[0][j] < array[0][i]:
                tempx = array[0][i];
                tempy = array[1][i];
                array[0][i] = array[0][j];
                array[1][i] = array[1][j];
                array[0][j] = tempx;
                array[1][j] = tempy;
    return array;
####################################################

###############   define MLVD function    ##########
def MLVD(ps,x_min,x_max):
    n = len(a[0][:]);
    result = [];
    result.append([]);
    result.append([]);
    result.append([]);
    result.append([]);

    for i in range(n):
        for j in range(n):
            if i == j:
                continue;
            #ps_i same as ps(:,i) and ps_j same as ps(:,j)
            ps_i=[];
            ps_i.append([]);
            ps_i[0].append(ps[0][i]);
            ps_i.append([]);
            ps_i[1].append(ps[1][i]);
            ps_j=[];
            ps_j.append([]);
            ps_j[0].append(ps[0][j]);
            ps_j.append([]);
            ps_j[1].append(ps[1][j]);
            #three below line have this result: v = [[][]]
            v=[];
            v.append([]);
            v.append([]);
            for k in range(n):
                if k == i or k == j:
                    continue;
                #ps_k same as ps(:,k)
                ps_k=[];
                ps_k.append([]);
                ps_k[0].append(ps[0][k]);
                ps_k.append([]);
                ps_k[1].append(ps[1][k]);

                xc = contact(ps_i,ps_j,ps_i,ps_k);
                v[0].append(xc);#this line whit below ine are same as:v=[v [xc;y(xc)]]
                v[1].append(y(xc,ps_i,ps_j));
            
            #v=[v [x_min;y(x_min)] [x_max;y(x_max)]];???????????????????
            v[0].append(x_min);
            v[1].append(y(x_min,ps_i,ps_j));
            v[0].append(x_max);
            v[1].append(y(x_max,ps_i,ps_j));
            #sort on x
            v = sort(v,len(v[0][:]));            
            length_v = len(v[0][:]);
            for l in range(1,length_v):
                c=[];
                c.append([]);
                c.append([]);
                #c in thid step is [[][]]
                c[0].append((v[0][l-1]+v[0][l])/2);
                c[1].append((v[1][l-1]+v[1][l])/2);
                
                d1=distance(c,ps_i);
                for h in range(n):
                    if h==i or h==j:
                        continue;
                    #d2=distance(c(:,1),ps(:,h))????????????
                    ps_h = [];
                    ps_h.append([]);
                    ps_h.append([]);
                    ps_h[0].append(ps[0][h]);
                    ps_h[1].append(ps[1][h]);
                    d2 = distance(c,ps_h);
                    if d2<d1:
                        break;
                if h==n-1 and d2>d1:
                    result[0].append(v[0][l-1]);
                    result[1].append(v[0][l]);
                    result[2].append(v[1][l-1]);
                    result[3].append(v[1][l]);
    return result;
####################################################


#start program
a = [] ;
a.append([]);
a.append([]);
for i in range(2):
    for j in range(50):
        if i == 0 :
            a[i].append(random.uniform(0,5));
        else:
            a[i].append(random.uniform(0,6));
        #print('a[',i,',',j,']=',a[i][j]);

result = MLVD(a,0,5);

matplotlib.rcParams['axes.unicode_minus'] = False
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(a[0],a[1], '.')

for i in range(len(result[:][0])):
    vertices = []
    codes = []
    vertices = [(result[0][i],result[2][i]),(result[1][i],result[3][i])];
    codes = [Path.MOVETO ] + [Path.LINETO];
    vertices = np.array(vertices, float);
    path = Path(vertices, codes);
    pathpatch = PathPatch(path, facecolor='None', edgecolor='green');
    ax.add_patch(pathpatch);

ax.set_title('Diagram Voronoi');
plt.show();
