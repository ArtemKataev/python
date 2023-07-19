import math

# n= 700
# m= 750
# a = int(math.ceil(m/n))

# print(a)


# class claSs():
#     class_a = int(input())
#     class_b = int(input())
#     class_c = int(input())

#     p1 = int(class_a/2)+(class_a % 2)
#     p2 = int(class_b/2)+(class_b% 2)
#     p3 = int(class_c/2)+(class_c % 2)
#     print(p1+p2+p3)

# claSs()


# def train():
#     i = int(input())
#     j = int(input())

#     if( i == j):
#         print("no")
#     else:
#         print(i+j-1)

# train()

# def year():
#     a = int(input())
#     if(a%4==0 and a%100!=0 or a%400==0 ):
#         print("yes")
#     else:
#         print("no")


# year()

king_v = int(input())
king_g = int(input())

next_turn_v = int(input())
next_turn_g = int(input())


def checkInput(king_v, king_g, next_turn_v, next_turn_g):
    if (king_v in range(1, 9) and 
       king_g in range(1, 9) and
       next_turn_v in range(1, 9) and
       next_turn_g in range(1, 9)):
        return True
    else: return False


def chess(king_v, king_g, next_turn_v, next_turn_g):

    if (checkInput(king_v, king_g, next_turn_v, next_turn_g)):
        if (abs(next_turn_v - king_v) <= 1 and abs(next_turn_g - king_g) <= 1):
            print("yes, king can ")
        else:
            print("you r wrong because need to teach rules")
    else:
        print("you r wrong because your math skills equal 0")

checkInput(king_v, king_g, next_turn_v, next_turn_g)
chess(king_v, king_g, next_turn_v, next_turn_g)
# ffffff