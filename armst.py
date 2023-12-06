n = int(input("Enter the number: "))
s = n 
b = len(str(n))
sum1 = 0
while n != 0:
    a = n % 10
    sum1 = sum1+(a**b)
    n = n//10
if s == sum1:
    print("The given number", s, "is armstrong number")
else:
    print("The given number", s, "is not armstrong number")
