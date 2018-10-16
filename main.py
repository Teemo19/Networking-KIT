import rootkit,time
class device:
	#community=str(raw_input("community:"))
	community=""
	find_device=["ter len 0","show version | inc Model Number","exit"]
	switch=["terminal len 0","show run | inc snmp-server community","exit"]

def main():
	segment=str(raw_input("Network ID: "))
	port=int(raw_input("Port: "))
	user=str(raw_input("User: "))
	passwd=str(raw_input("Pass: "))
	print(rootkit._intro.output)#LOGO
	ips_port_active=rootkit._nmap(segment,port).analyze_nmap()
	telnet_con=rootkit._telnet(ips_port_active,user,passwd)
	telnet_auth=telnet_con.telnet_conection()
	result=telnet_con.write_telnet(telnet_auth,device.switch)
	configured_devices=telnet_con.analyze_snmp(result,device.community,ips_port_active)
	print(configured_devices)
	#file=open("data")
	#for i in range(len(configured_devices)):
if __name__=='__main__':
	main()
	time.sleep(20)
