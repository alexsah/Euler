def isprime(n):
    '''check if integer n is a prime'''
    if n==1:
            return False
    # range starts with 2 and only needs to go up the squareroot of n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

current = 1

while current < 10000000:
    if isprime(current):
        if 600851475143%current==0:
                print(current)
    current += 1
    
