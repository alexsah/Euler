#The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
#Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
import math
result = 0
for i in range(1, 1001):
        result += int(pow(i,i))
#print("The series is " + str(int(result)))
resultString=str(int(result))
condensed = resultString[-10:]
print("Last 10 chars is: " + str(condensed))
#Last 10 chars is: 9110846700
