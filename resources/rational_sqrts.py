m = 2
N = 500

# pre-compute squares
D = dict()
for n in range(2,2*N):
    D[n] = n**2

for d in range(3, N):
    n = m
    # guaranteed to happen
    while D[n] < 3 * D[d]:
        n += 1
    m = n-1  # adjust start
    
    low = D[n-1]
    hi = D[n]
 
    target = 3*(D[d])
    low_delta = target - low
    hi_delta = hi - target
    
    if low_delta < 7:
        print('low : %d %3d %3d' % (low_delta,n-1,d))
    elif hi_delta < 7:
        print('high: %d %3d %3d' % (hi_delta,n,d))

'''
> python3 rational_sqrts.py 
low : 2   5   3
high: 1   7   4
high: 6   9   5
low : 3  12   7
high: 4  14   8
low : 2  19  11
high: 1  26  15
high: 6  33  19
low : 3  45  26
high: 4  52  30
low : 2  71  41
high: 1  97  56
high: 6 123  71
low : 3 168  97
high: 4 194 112
low : 2 265 153
high: 1 362 209
high: 6 459 265
low : 3 627 362
high: 4 724 418
> 
'''