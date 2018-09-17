#!/usr/bin/env python2

import  socket,commands,time
#  we are looking for UDP (user datagram protocol )
#              ip_version4,         UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


	
# defining ip and port below 
ip="192.168.10.200"
port1=7890
port2=8888
s.bind(("",port2))
user=raw_input("enter the username\t")
password=raw_input("enter the password\t")
s.sendto(user,(ip,port1))
s.sendto(password,(ip,port1))
message=s.recvfrom(20)
if message[0]=="ok":	
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
		
				
		if  'exit' in  cmd  or  'close' in cmd:
			print commands.getoutput(cmd)
			print "closing server.."
			exit()
					
		
								
		else :
			s.sendto(cmd,(ip,port1))
		#receiving data from server
			server_data=s.recvfrom(20)
			server_cmd=server_data[0]
			if "sh: 1" in server_cmd:
			#showing alternate msg for command not not found
				print "command you entered is not correct...Please enter valid command"
			else :#printing the output of command received from server
				print server_cmd
			timer.append(cmd)
			#list will be cleara after entering 5 commands
			if  len(timer) > 5 :
				print commands.getoutput('clear')
				for i in  range(len(timer)):
					timer.pop()
			else :
				pass
			
			

else:
	print "enter correct authentication details"

		
s.close()
s.close()
