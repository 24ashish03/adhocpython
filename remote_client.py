#!/usr/bin/env python2

import  socket,commands,time
#  we are looking for UDP (user datagram protocol )
#              ip_version4,         UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# defining ip and port below 
ip="192.168.43.221"
port=7890

# defining list for 10 commands counter
timer=[]
while  True :
#  taking input 
	cmd=raw_input("ashish@ash:~/Desktop$  ")
# showing rebooting message	
	if 'reboot' in cmd or 'restart' in cmd:
		print "server is rebooting in 10 seconds...cannot send the commands"
		time.sleep(10)
		s.sendto(cmd,(ip,port)) 
#sending data to server	
	s.sendto(cmd,(ip,port))
	
	if  'exit' in  cmd  or  'close' in cmd:
		print commands.getoutput(cmd)
		print "closing server.."
		exit()
		
	else :
		print commands.getoutput(cmd)
		timer.append(cmd)
		print len(timer)
		#list will be cleara after entering 5 commands
		if  len(timer) > 5 :
			print commands.getoutput('clear')
			print  timer
			for i in  range(len(timer)):
				timer.pop()
		else :
			pass

s.close()
