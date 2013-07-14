from math import factorial

orig=factorial(100)
work=str((orig))
i=0
result = 0
while i < len(work):
    result+=int(work[i])
    i+=1
print(result)
