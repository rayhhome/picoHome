import math
from Crypto.Util.number import inverse, long_to_bytes

N = int(input("Please input your N:"))
sqN = math.ceil(math.sqrt(N))

p = 0
q = 0

res = input("Do you want to input p and q?(y/n):")
if(res == "y"):
    p = int(input("Please input your p:"))
    q = int(input("Please input your q:"))
else:
    for i in range(2,sqN):
        if (N % i == 0):
            p = 1
            q = N // i
            print("Your p and q are: ", p, "and", q)

t = (q - 1) * (p - 1)
e = int(input("Please input your e:"))

d = pow(e, -1, t)

print("Your d is:", d)

C = int(input("Please input your C:"))

M = pow(C, d, N)

print("Your M is:", long_to_bytes(M))

print("Program stopped.")

