from fractions import Fraction

N = 3

def f(x):
    h = Fraction(1,2)
    return h * (x + N/x)

def g(x,y):
    return (x*y + N)/(x + y)
    
nL = (5,7,12,14,19,26,45,52,71,97,168)
dL = (3,4,7,8,11,15,26,30,41,56,97)

R = range(len(nL))
for i in R:
    x = Fraction(nL[i],dL[i])
    print(x,f(x))

print()

for i in R[:-1]:
    j = i+1
    x = Fraction(nL[j],dL[j])
    y = Fraction(nL[i],dL[i])
    print(x,y,g(x,y))
        
'''
worked by accident! (to find 265/153)

> python3 guess_sqrt.py 
5/3 26/15
7/4 97/56
12/7 97/56
7/4 97/56
19/11 362/209
26/15 1351/780
45/26 1351/780
26/15 1351/780
71/41 5042/2911
97/56 18817/10864
168/97 18817/10864

7/4 5/3 71/41
12/7 7/4 168/97
7/4 12/7 168/97
19/11 7/4 265/153
26/15 19/11 989/571
45/26 26/15 2340/1351
26/15 45/26 2340/1351
71/41 26/15 3691/2131
97/56 71/41 13775/7953
168/97 97/56 32592/18817
>
'''