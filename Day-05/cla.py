#example for Command Line Argument
import sys

def add(num1,num2):
    sum = num1+num2
    return sum

num1= float(sys.argv[1])
num2= float(sys.argv[2])
operation= sys.argv[3]

if operation == "add":
    result=add(num1, num2)
    print(result)


#how to run this file
#python cla.py 10 20 add