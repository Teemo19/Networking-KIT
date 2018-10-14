import rootkit

def main():
	segment=str(raw_input("Network ID: "))
	port=int(raw_input("Port: "))
	user=str(raw_input("User: "))
	passwd=str(raw_input("Pass: "))
	ips_port_active=rootkit._nmap(segment,port).analyze_nmap()
	raw_input("stop")
	telnet_con=rootkit._telnet(ips_port_active,user,passwd,device.data)
	telnet_auth=telnet.con.telnet_conection()

if __name__=='__main__':
	main()
