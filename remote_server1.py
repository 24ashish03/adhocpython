#!/usr/bin/env python2

import  socket
import  commands
#  we are looking for UDP (user datagram protocol )
#              ip_version4,         UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# defining ip and port below 
ip="192.168.43.221"
port1=7890
port2=8888
#  binind ip and port with bind function that takes input as tuple
s.bind(("",port1))

#  rec  data from  client 
while True:
#  only  accepting  commands with  20 char 
	client_data=s.recvfrom(20)
#   only  client  data is stored
	recv_cmd=client_data[0]
#  executing  client data 
	if  'exit' in recv_cmd or 'close' in  recv_cmd :
		exit()
			
	else :
		
		s.sendto(recv_cmd,(ip,port2))
		'''#print  commands.getoutput(recv_cmd)'''
		
s.close()

