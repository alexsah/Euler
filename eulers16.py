#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2^1000?

power = str(pow(2,1000))

powerLength = len(power)
i=0
sum=0
while i < powerLength:
    sum += int(power[i])
    i+=1

print(sum)
#Ans 1366
