p = int(input('p='))
q = int(input('q='))
print('p =',p,'q =',q)
n = p*q
print('n =',n)
F=(p-1)*(q-1)
print('F =',F)
e = int(input('e='))
d = int(input('d='))
x = 10
Z = (x**e)%(n)
print(Z)
O = (Z**d)%(n)
print(O)
print('Шифруем слово crypto')
m = 'crypto'
v = len(m)
print('Длина слова:',v)
L = [3, 18, 25, 16, 20, 15 ]
# L = [int(input()) for i in range(v)]
print('Код строки:',L)
L1 = []
L2 = []
for i in L:
  L1.append((i**e)%(n))
print('Закодированная строка:',L1)
for i in L1:
   L2.append((i**d)%(n))
print('Раскодированная строка:',L2)