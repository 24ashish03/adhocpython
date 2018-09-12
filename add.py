#!/usr/bin/env  python2

import  sys
#  only  picking  first  two arguments 
data=sys.argv[1:3]
#  now  seperating each arg into two variables 
n1=data[0]
n2=data[1]

'''
#  taking user input 
#  raw_input  convert data into string  always 
n1=raw_input("enter  first  number :  ")
n2=raw_input("enter  second  number :  ")
'''
#adding numbers but we need to typecast  from string to int 
sum=int(n1)+int(n2)
print "sum of input numbers is ",sum
