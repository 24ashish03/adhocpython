#!/usr/bin/env python2

import  socket
import  commands
#  we are looking for UDP (user datagram protocol )
#              ip_version4,         UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# defining ip and port below 
ip="192.168.10.200"
port1=7890
port2=8888
#  binind ip and port with bind function that takes input as tuple
s.bind(("",port1))
username=s.recvfrom(20)
passwordr=s.recvfrom(20)
if username[0]=="ashish"and passwordr[0]=="123":
	s.sendto("ok",(ip,port2))
	#  receive  data from  client 
	while True:
	#  only  accepting  commands with  20 char 
		client_data=s.recvfrom(20)
	#   only  client  data is stored
		recv_cmd=client_data[0]
	#  executing  client data 
		if  'exit' in recv_cmd or 'close' in  recv_cmd :
			exit()
				
		else :
			
			s.sendto(commands.getoutput(recv_cmd),(ip,port2))
			print  commands.getoutput(recv_cmd)
else:
	print "enter vaalid username and password"		
s.close()
