# TASK34

# def func(a):
#   a = a.split()
#   lst = []
#   for wrd in a:
#       sum = 0
#       for i in wrd:
#           if i in 'уеыаоэяиюё':
#               sum+=1
#       lst.append(sum)
#   return len(lst) == lst.count(lst[0])

# x = "пара-ам ра-ра-авибзьцихуеуеуебмзшигмтйьха-дам"
# if func(x):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')

# TASK 36
def print_operation_table(operation, num_rows=6, num_columns=6):
    a = [[operation(i,j) for j in range(1,num_columns+1)] for i in range(1,num_rows+1)]
    for i in a:
        print(*[f"{x:>3}"for x in i])

print_operation_table(lambda x, y: x * y)