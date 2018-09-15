#!/usr/bin/env python2

import  socket,commands,time
#  we are looking for UDP (user datagram protocol )
#              ip_version4,         UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
'''
user=raw_input("enter the username\t")
password=raw_input("enter the password\t")
if user=="ashish" and password=="123":
	
	# defining ip and port below 
	ip="192.168.43.221"
	port1=7890
	port2=8888
	s.bind(("",port2))
	# defining list for 10 commands counter

	timer=[]
	while  True :
	#  taking input 
		cmd=raw_input("ashish@ash:~/Desktop$  ")
	# showing rebooting message
			if 'reboot' in cmd or 'restart' in cmd:
			print "server is rebooting in 10 seconds...cannot send the commands"
			time.sleep(10)
			s.sendto(cmd,(ip,port1)) 
	#sending command to server	
		s.sendto(cmd,(ip,port1))
			
		if  'exit' in  cmd  or  'close' in cmd:
			print commands.getoutput(cmd)
			print "closing server.."
			exit()
				
		else :
			''print commands.getoutput(cmd)''
	#receiving data from server
			server_data=s.recvfrom(20)
			server_cmd=server_data[0]
	#now printing the output of command received from server
			print commands.getoutput(server_cmd)
			timer.append(cmd)
			'#print len(timer)''
			#list will be cleara after entering 5 commands
			if  len(timer) > 5 :
				print commands.getoutput('clear')
				''#print  timer''
				for i in  range(len(timer)):
					timer.pop()
			else :
				pass


else:
	print "enter correct authentication details"
'''
def func1():
	user=raw_input("enter the username\t")
	password=raw_input("enter the password\t")
	if user=="ashish" and password=="123":
		func2()	
	else:	
		print "enter correct authentication details"
		print "do u want to continue:Y/N"
def func2():
		
	# defining ip and port below 
		ip="192.168.43.221"
		port1=7890
		port2=8888
		s.bind(("",port2))
		# defining list for 10 commands counter

		timer=[]
		while  True :
		#  taking input 
			cmd=raw_input("ashish@ash:~/Desktop$  ")
		# showing rebooting message
		        if 'reboot' in cmd or 'restart' in cmd:
				print "server is rebooting in 10 seconds...cannot send the commands"
				time.sleep(10)
				s.sendto(cmd,(ip,port1)) 
		#sending command to server	
			s.sendto(cmd,(ip,port1))
				
			if  'exit' in  cmd  or  'close' in cmd:
				print commands.getoutput(cmd)
				print "closing server.."
				exit()
					
			else :
				#print commands.getoutput(cmd)
		#receiving data from server
				server_data=s.recvfrom(20)
				server_cmd=server_data[0]
		#now printing the output of command received from server
				print commands.getoutput(server_cmd)
				timer.append(cmd)
				'''#print len(timer)'''
				#list will be cleara after entering 5 commands
				if  len(timer) > 5 :
					print commands.getoutput('clear')
					'''#print  timer'''
					for i in  range(len(timer)):
						timer.pop()
				else :
					pass		
		


	
while True:
	func1()
	
	a=raw_input()
	if a=="Y" or a=="y":	
		func1()
	else:
		exit()
		
s.close()
s.close()
