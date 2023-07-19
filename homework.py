import math
# lesson 1

a = int(input())
if(a>999 or a<100):
    print("try again")
else:
  print(a//100+a%10+a//10%10)

# lesson 2

b = int(input())
print(math.ceil(b/6) ,(math.ceil(b/6*4)) ,(math.ceil(b/6)))

# lesson 3

t =(input())
if len(t) == 6:
  l = int(t[0])+int(t[1])+int(t[2])   
  p = int(t[3])+int(t[4])+int(t[5])
  if(l == p):
    print("your ticket lucky")
  else:
    print("your ticket unlucky")
else:
  print("number incorrect")

# lesson 4 

n = int(input())
m = int(input())
k = int(input()) 
if k < m * n and (k % m == 0 or k % n == 0):
  (print("success"))
else:
  (print("try again"))