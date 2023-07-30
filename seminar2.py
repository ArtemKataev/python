from random import randint


# def weather(n):
#     if n < 1 or n > 100:
#         print("try again")
#     else:
#         max_count =0
#         count =0
#         for i in range(1, n+1):
#             next = randint(-50, 50)
#             print(next)
#             if next > 0:
#                 count += 1
#             else:
#                 if count > max_count:
#                     max_count = count
#                 count = 0
#     return max_count


# num = int(input("entered n numbers at 1 to 100: "))
# print(weather(num))

# def arbuz(n):
#     if n<1:
#         print("net arbuzov")
#     else:
#         next_n = randint(1,10)
#         print(next_n)
#         min_n =next_n
#         max_n =next_n
#         for i  in range (2, n+1):
#             next_n = randint(1,10)
#             print(next_n)
#             if next_n>max_n:
#                 max_n= next_n
#             elif next_n<min_n:
#                 min_n = next_n
#         return(min_n,max_n)

# num = int(input("entered n number"))
# print(arbuz(num))


a = 12 
b = 18
nod = 0
nok = 0

for i in range (2, min(a,b)):
    flag=False
    if a %i ==0 and b %i ==0:
        nod = i
        if flag:
            continue
        else:
            nok = i
            flag = True
print(f"nod = {nod}")
print(f"nok = {nok}")