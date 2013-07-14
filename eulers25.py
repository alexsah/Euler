#What is the first term in the Fibonacci sequence to contain 1000 digits?

i=2
last=1
current=1
next=0
fibonacciLength = 0
while fibonacciLength < 1000:
        next = last + current
        last = current
        current = next
        i+=1
        fibonacciLength=len(str(current))
print("The F value is: " + str(i))
print("The current value is: " + str(current))
