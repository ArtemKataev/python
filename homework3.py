#HW 3 TAsk 16 
def func_16():
    n = int(input('entered quantity '))
    nums = list(map(int, input("entered the list separated by a space ").split(' ')))
    x = int(input("entered number that you want yo find "))

    count = 0
    for i in range(n):
        if nums[i] == x:
            count += 1 
    print(f' number {x} was founded in list A {count } ')        
      
# func_16

# HW 3 Task 18
def func_18():
    n = abs(int(input('entered quantity ')))
    A_entered = (input("entered the list separated by a space ").split())
    A_num = list(map(int,A_entered))
    if len(A_num) != n or n ==0:
      print("try again")
    else: 
      x = int(input("entered number that you want yo find "))
      min = abs(x -  A_num[0])
      index = 0
      for i in range(1,n):
        count = abs(x- A_num[i])
        if count < min:
            min  = count 
            index = i
    print(f'number {A_num[index]} was closed by the number {x} , {abs(x - A_num[index])}')
 
# func_18()

# HW 3 Task 20
eng = {1:'AEIOULNSTR',
      	2:'DG',
      	3:'BCMP',
      	4:'FHVWY',
      	5:'K',
      	8:'JZ',
      	10:'QZ'}
rus = {1:'АВЕИНОРСТ',
      	2:'ДКЛМПУ',
      	3:'БГЁЬЯ',
      	4:'ЙЫ',
      	5:'ЖЗХЦЧ',
      	8:'ШЭЮ',
      	10:'ФЩЪ'}
N = abs(int(input('enter 1, if will play in english, or 0, if in rus: ')))
word = input('enter number: ').upper()
if N == 1:
	print( sum([k for i in word for k, v in eng.items() if i in v]), 'points')
elif N == 0:
	print( sum([k for i in word for k, v in rus.items() if i in v]), 'points')

