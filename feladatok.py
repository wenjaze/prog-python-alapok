# 1.  String Reverser
# U've given a string as an input
# write code in python that prints
# the input string reverse.
# bonus : Do it in 1 line.
# example input : Hello
# example output : olleH

def reverseString():
    inputString = input("string:")
    reversedString = ""
    
    return reversedString

print(reverseString())

# 2. Prime-check
# Given a number,
# check if the numbers are primes.
# 1. example input : 7
# 1. example output : True
# 2. example input : 10
# 2. example output : False
# bonus : if not prime return dividers instead.

def primeCheck():
    nr = int(input("number:"))

# 3. ----------------------
# 
    
    

print(primeCheck())



# Solutions : 
# 1. ---------------------------
# reversedString = ''.join([inputString[i] for i in range(len(inputString)-1,-1,-1)])



# 2. ---------------------------
# simple : 
# k = [i for i in range(1,nr+1) if (nr%i==0)]
# return (len(k) ==2)

# 2. ---------------------------
# bonus :
# nr_dividers = []
#     for i in range(1,nr+1):
#         if (nr%i==0):
#             nr_dividers.append(i)
#     if len(nr_dividers) == 2:
#         return True
#     else:
#         return [i for i in nr_dividers if (i != 1 and i != nr)]