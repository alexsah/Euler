result=0
last=1
current=1
next=0
i=1
while current < 4000000:
        
        # i += 1
        # print(i)
        if current%2==0:
                result += current
        next = last + current
        last = current
        current = next

        

print (result)
