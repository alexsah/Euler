#2520 is the smallest number that can be divided by each of the numbers
#from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all
#of the numbers from 1 to 20?

value=2000
found = False
while found == False:
        for i in range(1, 21):
                if (value%i!=0):
                        break
                if (i==20)and(value%20==0):
                        print("Value is:")
                        print(value)
                        found=True
                        break
        value+=20
