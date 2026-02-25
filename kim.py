# ==================== 2 ====================
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (not (not w or (x == y)) and (not z or x)) == 1:
                    print(x, y, z, w)
# ==================== 5 ====================
def to_3(m):
    s = ''
    while m > 0:
        s = str(m % 3) + s
        m = m // 3
    return s

q = []
for n in range(1, 300):
    b = to_3(n)
    if n % 3 == 0:
        b += b[-2:]
    else:
        b +=to_3(n % 3 * 5)
    r = int(b, 3)
    
    if r > 150:
        q.append(r)
print(min(q))
# ==================== 8 ====================
n = 1
l_n = 0

for a in 'АКОРСТ':
    for b in 'АКОРСТ':
        for c in 'АКОРСТ':
            for d in 'АКОРСТ':
                for e in 'АКОРСТ':
                        w = a + b + c + d + e
                        
                        if n % 2 != 0 and w[0] not in 'А' and w.count('С') == 1:
                            l_n = n
                        n += 1
                        
print(l_n)
# ==================== 13 ====================
from ipaddress import *
net = ip_network("205.99.68.249/255.255.248.0", 0)
print(net[-1])
