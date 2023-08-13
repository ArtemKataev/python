#  TASK 1
a = int(input("введите первый элемент прогрессии "))
d = int(input("введите разность "))
n = int(input("введите количество элементов "))

for i in range(n):
  print(a+i*d)

# TASK 2

lst_1 = [1,2,3,4,5,6,7,8,9,10]
lst_2 = []
max = int(input("enter max "))
min = int(input("enter min "))
for i in range(len(lst_1)):
  if min <= lst_1[i]  <=max:
    lst_2.append(i)

print(lst_2)