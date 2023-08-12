
                                    # TASK 26
def func_26(a,b):
    if b == 0:
      return 1
    return(a*func_26(a,b-1))
    print(func_26(a,b))

a = int(input("введите число "))
b = int(input("введите степень числа "))
print(func_26(a,b))

                                    # TASK 28
def func_28(a,b):
   if b ==0:
      return a
   return 1+func_28(a,b-1)

a = int(input("введите первое число "))
b = int(input("введите второе число "))
print(func_28(a,b))
   
