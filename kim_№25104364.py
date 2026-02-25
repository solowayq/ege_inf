# ========== КИМ № 25104364 / БР № 2832503195017 ==========

# Задание 2 (№23186)
'''
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((not x or y) and z and not w) == 1:
                    print(x, y, z, w)
'''

# Задание 5 (№23189)
'''
for n in range(1, 1000000):
    r = bin(n)[2:]
    
    if n % 3 == 0:
        r += r[-3:]
    else:
        r += bin((n % 3) * 3)[2:]

    q = int(r, 2)
    if q < 130:
        print(n)
'''

# Задание 7 (№23191)
'''
r = (1920 * 1080 * 23 * 120 - 1280 * 1024 * 21 * 120) / 8 / 1024; print(r)
'''

# Задание 8 (№23192)
'''
numb = 1
last_num = 0

for a in 'ЕИОРТЯ':
    for b in 'ЕИОРТЯ':
        for c in 'ЕИОРТЯ':
            for d in 'ЕИОРТЯ':
                for e in 'ЕИОРТЯ':
                    for f in 'ЕИОРТЯ':
                        word = a + b + c + d + e + f
                        
                        if numb % 2 != 0 and word[0] not in 'ТРЯ' and word.count('И') >= 2:
                            last_num = numb
                            
                        numb += 1

print(last_num)
'''

# Задание 9 (№23193)
'''
f = open('9_23193.txt')
stroka = 1
for el in f:
    a = list(map(int, el.split()))
    n1 = [x for x in a if a.count(x) > 1]
    n2 = [x for x in a if a.count(x) == 1]
    if len(n1) == 3 and n1[0] > (sum(n2) / len(n2)):
        print(stroka)
    stroka += 1
f.close
'''

# Задание 11 (№23195)
'''
from math import *
for A in range(1, 1000):
    i = ceil(log2(A))
    V1 = ceil((172 * i) / 8)
    if V1 * 356_984 >= 54 * 2 ** 20:
        print(A)
        break
'''

# Задание 13 (№23197)
'''
from ipaddress import *
net = ip_network("45.172.106.203/255.255.252.0", 0)
print(net[-2])
'''

# Задание 14 (№23198)
'''
def to_9(n):
    s = ""
    while n > 0:
        s += str(n % 9)
        n //= 9
    return s[::-1]

for x in range(1, 3001):
    k = 9 ** 150 + 9 ** 30 - x
    if to_9(k).count("0") == 122:
        print(x)
        break
'''

# Задание 15 (№23199)
'''
def f(x, y, A):
    n1 = x * y > A
    n2 = x > y
    n3 = 11 > x
    return n1 or n2 or n3 

for A in range(1, 1000):
    t = all(f(x, y, A) for x in range(1, 1000)
        for y in range(1, 1000))
    if t == True:
        print(A, t)
'''

# Задание 16 (№23200)
'''
import sys
sys.setrecursionlimit(25000)

def f(n):
    if n < 10:
        return n
    return 3 * n + f(n - 3)
print((f(6250) + 2 * f(6244)) / f(6238))
'''




























