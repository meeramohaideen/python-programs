num1 = int(input("starting integer "))
num2 = int(input("ending integer: "))
num3=0
for num in range(num1,num2+ 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           num3=num3+num
           
print(num3)           
