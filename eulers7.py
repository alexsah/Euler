def isprime(n):
    '''check if integer n is a prime'''
    if n==1:
            return False
    # range starts with 2 and only needs to go up the squareroot of n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

count = 0
i = 1

while i > 0:
    if isprime(i):
        count+=1
        if (count==10001):
                print("The 100001st prime number is:")
                print (i)
                break
    i+=1

    
