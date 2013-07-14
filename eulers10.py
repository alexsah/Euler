from math import sqrt

def isprime(n):
    '''check if integer n is a prime'''
    # range starts with 2 and only needs to go up the squareroot of n
    for x in range(3, int(sqrt(n)+1), 2):
        if n % x == 0:
            return False
    return True

result = 2 #Start at 3 because 1+2 are prime
i = 3 #Start at 3 because 2 is prime

while i <= 2000000:
    if isprime(i):
        result+=i
    i+=2    #skipped 2 so all remaining primes are odd

print("Result is:")
print(result)

    
