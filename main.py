import rootkit
class device:
	data=["terminal len 0"]

def main():
	segment=str(raw_input("Network ID: "))
	port=int(raw_input("Port: "))
	user=str(raw_input("User: "))
	passwd=str(raw_input("Pass: "))
	ips_port_active=rootkit._nmap(segment,port).analyze_nmap()
	print(ips_port_active)
	telnet_con=rootkit._telnet(ips_port_active,user,passwd).telnet_conection()
	print(telnet_con)
	input("stop telnet_con")

if __name__=='__main__':
	main()
