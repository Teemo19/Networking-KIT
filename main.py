import time,sys,serial,paramiko,telnetlib
print("Starting Program")

def cnxn_serial():
	try:
		puerto='COM1'
		ser= serial.Serial(puerto,9600,timeout=0)
		time.sleep(1)
		return ser
	except:
		print("Puerto: {} no encontrado".format(puerto))
		input("\n Por favor conecta el puerto {} ".format(puerto))
		cnxn_serial()

def write_config(ser,array_config):
		for i in range(len(array_config)):
			ser.write(array_config[i]+"\n")

def serial_work(initial_config):
	try:
		ser=cnxn_serial()
		write_config(ser,initial_config)
		time.sleep(1)
		if(ser.inWaiting()>0):
			data=ser.read()
			print(data)
	except(KeyboardInterrupt):
		print("Exiting Program")
	except:
		print("Error Occurs, Exiting Program")
	finally:
		if(cnxn_serial()>0):
			ser.close()
		pass	
def telnet_conn():
	HOST =''
	user=''
	passwd=''
	tn=telnetlib.Telnet(HOST)
	tn.read_until("User:")
	tn.write(user+"\n")
	tn.read_until("Password:")
	tn.write(passwd+"\n")
	return tn

def telnet_work(initial_config):
	tn=telnet_conn()
	write_config(tn,initial_config)
	print(tn.read_all())
	#tn.close()

def ssh_conn():
	HOST =""
	user=""
	passwd=""
	ssh_client=paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=HOST,username=user,password=passwd)
	print("Successful connection "+HOST)
	shell=ssh_client.invoke_shell()
	time.sleep(1)
	shell.send(user+"\n")
	shell.send(passwd+"\n")
	return shell

def ssh_work(initial_config):
	ssh=ssh_conn()
	last=time.time()
	for i in range(len(initial_config)):
		ssh.send(initial_config[i]+"\n")
		time.sleep(0.1)
	print(time.time()-last)
	time.sleep(2)
	print(ssh.recv(65535))
	ssh.close()

class WLC:
	enable_telnet=["config network telnet enable","save config","y"]
	disable_telnet=["config network telnet disable","save config","y"]


def main():

	#serial_work(initial_config) #FALTA PROBAR
	ssh_work(WLC.disable_telnet) #TRABAJANDO AL 100
	#telnet_work(initial_config) #FALTA TERMINAR 


if __name__=='__main__':
	main()