import rootkit

def main():
	segment=str(raw_input("Network ID: "))
	port=str(raw_input("Port: "))
	user=(raw_input("User: "))
	passwd=(raw_input("Pass: "))
	ips_port_active=rootkit.libnmap._nmap(segment,port).analyze_nmap()
	telnet_con=rootkit.libtelnet._telnet(ips_port_active,user,passwd,device.data)
	telnet_auth=telnet.con.telnet_conection()

if name__=='__main__':
	main()
