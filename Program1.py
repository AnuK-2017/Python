import random
import math

# Program1 :
# num1, num2 = input('Enter two numbers: ').split()
#
# num1 = int(num1)
# num2 = int(num2)
#
# add = num1 + num2
# diff = num1 - num2
# multi = num1 * num2
# div = num1 / num2
# mod = num1 % num2
#
# print('{} + {} = {}'.format( num1, num2, add))
# print('{} - {} = {}'.format( num1, num2, diff))
# print('{} * {} = {}'.format( num1, num2, multi))
# print('{} / {} = {}'.format( num1, num2, div))
# print('{} % {} = {}'.format( num1, num2, mod))

######################################################################################
# Program2: Convert miles to kilometers

# num1 = input('Enter miles:')
# num1 = int(num1)
#
# km = num1 * 1.6093
#
# print('{} miles equals {} kilometers'.format(num1,km))
#######################################################################################
# Program 3
# num1, oper, num2 = input('Enter the operation:').split()
#
# num1 = int(num1)
# num2 = int(num2)
#
# if oper == '+':
#     result = num1 + num2
# elif oper == '-':
#     result = num1 - num2
# elif oper == '*':
#     result = num1 * num2
# elif oper == '/':
#     result = num1 / num2
# else:
#     result = 0
#
# print('{} {} {} = {}'.format(num1, oper, num2, result))
######################################################################################
# program 4
# num1 = input('Enter your age:')
#
# num1 = int(num1)
#
# if num1 == 5:
#     print('You should be going to kindergarten')
# elif (num1 > 5) and (num1 < 17):
#     print ('You should be going to grade {}'.format(num1-5))
# elif num1 > 17:
#     print('You should be going to college')
# else:
#     print('You are a baby, stay a home and enjoy')
###########################################################################################
# program 5

# for i in range(1,21):
# for i in range(10):
#     if i % 2 != 0:
#         print(i)
# j = float(input('Enter a float:'))
#
# print("The float number is {:.2f}".format(j))
##############################################################################################
# program 6
# print a pine tree
# i = input('How tall the tree is:')
# i = int(i)
# k = 0
# #print(i)
# while i != 0:
#     for j in range(1, i):
#         print(' ',end="")
#     for l in range(1,k):
#         print('#',end="")
#         l -= 1
#     print('')
#     i -= 1
#     k += 2
#     #print(k)
#############################################################################################
# program 7: how to use exception

# while True:
#     try:
#         i = int(input("Enter some number:"))
#         break
#     except ValueError:
#         print("Enter a valid number")
#     except:
#         print("Unexpected error occurred")
#
# print(i)
###############################################################################################
# program 8: Importing decimal
# sum = 0
# sum += 0.1
# sum += 0.3
# sum -= 0.1
# print("sum=",sum)
#
# from decimal import Decimal as D
# sum = D(0)
# sum += D("0.1")
# sum += D("0.3")
# sum -= D("0.1")
# print("sum=",sum)
###################################################################################################
# program 9: Convert input string to its accronym
# Input: Random access memory  Output= RAM
# u_list = input("Enter a string:").split()
# string_out = ""
# for c in u_list:
#     string_out = string_out + c[0]
# print(string_out.upper())

####################################################################################3
# program 10: Encrypt the input

# string_in = input("Enter the string to be encrypted:")
# key = int(input("Enter the number, the letters to be shifted:"))
#
# # string_in= "AN1# u"
# string_out = ""
#
# for c in string_in:
#     if c.isalpha():
#         string_out += chr(ord(c)+key)
#         # print(string_out)
#     else:
#         string_out = string_out + c
#         # print(string_out)
# print(string_out)
#########################################################################################
# functions

# def cal(cal_string):
#     cal_list = cal_string.split()
#     num1 = cal_list[0]
#     num2 = int(cal_list[2])
#     oprtr = cal_list[1]
#     ans = int(cal_list[4])
# # or do like this: num1, oprtr , num2,equal,ans = cal_string.split()
#     if oprtr == '+':
#         cal_list[0] = str(ans - num2)
#         return cal_list
#     elif oprtr == '*':
#         cal_list[0] = str(ans/num2)
#         return cal_list
#
# input_str = input("Enter the arithmetic operation: ")
# output_str = cal(input_str)
#
# print("The answer is:", " ".join(output_str))
#
##################################################################################
# function1: print prime numbers:
# input_prime = int(input("Enter the prime number:"))
#
# def is_prime(num):
#     for i in range(2,num):
#         if num%i == 0:
#             return False
#     return True
#
# j = 0
#
# for k in range(2, input_prime-1):
#     # print(k)
#     for i in range(2, k):
#         if k%i == 0:
#             j += 1
#     if j == 0:
#         print(k)
#     j = 0
######################################################################################3
# function2: passing unknown number of arguments to function
# def addNum(*args):
#     sum = 0
#     for i in args:
#         sum += i
#
#     return sum
#
# print("Sum:",addNum(1, 2, 3, 4, 5))
########################################################################################
# Lists: program1

numList = []

for i in range(5):
    numList.append(random.randrange(1,9))

print(numList)
print(len(numList))
numList.sort()
print(numList)

numList.insert(5,10)
print(numList)
numList.remove(10)  # to remove a particular
print(numList)
numList.pop(2)      # to remove a particular index
print(numList)

evenList = [i*2 for i in range(10)]

for i in evenList:
    print(i)

##### multi dimensional list or list of list

multiList = [[0]* 10 for i in range(10)]

print(multiList)

accountSid = "AC5377adbfa1dd504e05bff3a0cbb83b59"
authToken = "557ebe1ced46b7fcfa495aac17eb77bb"

myTwilioNumber = "+17634529239"
destCellPhone = "+16512700430"