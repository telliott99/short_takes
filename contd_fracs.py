import sys
from fractions import Fraction

prog, name, reps, lead = sys.argv[:4]
lead, reps = int(lead), int(reps)
L = [Fraction(s) for s in sys.argv[4:]] 
L = L * reps
pL = []

def add_invert(n,d):
    p = 1/d
    q = n + p
    pL.append((str(d), str(p), str(n), str(q)))
    return q

def evaluate(L):
    d = L.pop()
    while L:
         n = L.pop()
         d = add_invert(n,d)
    return add_invert(lead,d)

x = evaluate(L)
print(name)
for t in pL:
    print('%10s %10s %4s %10s' % t)
print(x)
   
if name.startswith('sqrt'):
    print('%3.12f' % float(x**2))
else:
    print('%3.12f' % float(x))

