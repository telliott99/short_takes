n = 5
s = 6
cot = 3**0.5
csc = 2

for i in range(n):
    Co = s/cot
    Ci = s/csc
    print(i + 1, '%3.6f' % Co, '%3.6f' % Ci)
    cot = cot + csc
    csc = (1 + cot**2)**0.5
    s *= 2
 