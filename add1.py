#!/usr/bin/env  python2

import  sys,time
#  taking all numbers to add 
user_data=sys.argv[1:]
sum=0
for   i   in  user_data:
	sum=sum+int(i)


print "addition of given numbers is:  ",sum
