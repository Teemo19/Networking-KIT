import rootkit
class device:
	data=["terminal len 0","exit"]

def main():
	segment=str(raw_input("Network ID: "))
	port=int(raw_input("Port: "))
	user=str(raw_input("User: "))
	passwd=str(raw_input("Pass: "))
	ips_port_active=rootkit._nmap(segment,port).analyze_nmap()
	telnet_con=rootkit._telnet(ips_port_active,user,passwd)
	telnet_auth=telnet_con.telnet_conection()
	result=telnet_con.write_telnet(telnet_auth,device.data)
	print(result)
	input("stop result")

if __name__=='__main__':
	main()
