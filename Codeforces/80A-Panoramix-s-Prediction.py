# time limit per test2 seconds
# memory limit per test256 megabytes
# A prime number is a number which has exactly two distinct divisors: one and itself. For example, numbers 2, 7, 3 are prime, and 1, 6, 4 are not.

# The next prime number after x is the smallest prime number greater than x. For example, the next prime number after 2 is 3, and the next prime number after 3 is 5. Note that there is exactly one next prime number after each number. So 5 is not the next prime number for 2.

# One cold April morning Panoramix predicted that soon Kakofonix will break free from his straitjacket, and this will be a black day for the residents of the Gallic countryside.

# Panoramix's prophecy tells that if some day Asterix and Obelix beat exactly x Roman soldiers, where x is a prime number, and next day they beat exactly y Roman soldiers, where y is the next prime number after x, then it's time to wait for Armageddon, for nothing can shut Kakofonix up while he sings his infernal song.

# Yesterday the Gauls beat n Roman soldiers and it turned out that the number n was prime! Today their victims were a troop of m Romans (m > n). Determine whether the Gauls should wait for the black day after today's victory of Asterix and Obelix?

# Input
# The first and only input line contains two positive integers — n and m (2 ≤ n < m ≤ 50). It is guaranteed that n is prime.

# Pretests contain all the cases with restrictions 2 ≤ n < m ≤ 4.

# Output
# Print YES, if m is the next prime number after n, or NO otherwise.

# Examples
# Input
# 3 5
# Output
# YES
# Input
# 7 11
# Output
# YES
# Input
# 7 9
# Output
# NO

def isItPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n**(1/2)) + 2):
            if n % i == 0:
                return False
        return True

def isNextPrimeM(n, m):
    for i in range(n+1, m+1):
        if isItPrime(i):
            if i == m:
                return 'YES'
            else:
                return 'NO'
                
n, m = map(int, input().split())

if n == 2 and m == 3:
    print('YES')
elif n == 2 and m != 3:
    print('NO')
elif isItPrime(m) == False:
    print('NO')
else:
    print(isNextPrimeM(n, m))