import random


def generate_keypair(p, q, f, n):
    # Выберите целое число e такое, чтобы e и fi были взаимно простыми
    e = random.randrange(2, f)
    # Чтобы убедиться, что e и fi являются совместимыми
    g = gcd(e, f)
    while g != 1:
        e = random.randrange(2, f)
        g = gcd(e, f)


    # алгоритм для генерации закрытого ключа
    d = inverse(e, f)

    # Возвращает пару открытых и закрытых ключей
    return ((e, n), (d, n))

def isPrime(i):
    for j in range(2, i):
        if (i % j == 0):
            return False
    return True


def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

def inverse(a, m):
    m0 = m
    y = 0
    x = 1
    if (m == 1):
        return 0
    while (a > 1):

        q = a // m
        t = m
        m = a % m
        a = t
        t = y

        y = x - q * y
        x = t

    if (x < 0):
        x = x + m0

    return x


''' Cipher текст c = m^e mod n 
Plain текст d= c^d mod n'''



def encrypt(publicKey, message):
    e, n = publicKey
    # a^b mod m
    c = [(ord(char) ** e) % n for char in message]

    return c


def decrypt(privateKey, message):

    d, n = privateKey
    #  a^b mod m
    p = [chr((char ** d) % n) for char in message]

    return ''.join(p)


while True:
    try:
        p = int(input('Введите значение простого числа p = '))
    except ValueError:
        print("Ошибка")
        continue
    if not isPrime(p):
        print("Введите простое число")
        continue
    else:
        break
while True:
    try:
        q = int(input('Введите значение простого числа q = '))
    except ValueError:
        print("ОШИБКАОШИБКАОШИБКА")
        continue
    if not isPrime(q):
        print("Введите простое число")
        continue
    else:
        break

# Calculate n=pq
n = p * q
# вычисляем fi=(p-1)(q-1)
f = (p - 1) * (q - 1)
publicKey, privateKey = generate_keypair(p, q, f, n)

# сообщение для шифрование
m = input('Введите число для шифрование m = ')
print('открытый ключ [e,n] = ', publicKey)

c = encrypt(publicKey, m)
m = decrypt(privateKey, c)

print('cipher текст = ', c)
print('закрытый ключ [d,n] = ', privateKey)
print('Plain текст после дeшифрование = ', m)