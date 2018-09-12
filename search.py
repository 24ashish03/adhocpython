#!/usr/bin/env  python


import webbrowser
import time
import sys


data = sys.argv[1:3]

n1 = data[0]
n2 = data[1]
 
n1,n2 = n2,n1
print "Please wait until swapping is done" 
time.sleep(2)


print n1
print n2

n3 = n1+" "+n2

webbrowser.open_new_tab('http://google.com/search?btnG=1&q=%s'%n3)

