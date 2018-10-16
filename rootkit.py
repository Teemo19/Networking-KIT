import nmap,time,threading,sys
from telnetlib import Telnet


class _intro:
	SH_YELLOW = "\033[33m" if "win" not in sys.platform else ""
	SH_GREEN = "\033[92m" if "win" not in sys.platform else ""
	output = SH_YELLOW + """
	_______________________________________
	   _____           	    __
	   |____  |\ | |\  /|  |__|
 	   _____| | \| | \/ |  |

              CONFIGURATOR V.1.0.0
	_______________________________________
	""" +SH_YELLOW

class _nmap:
	def __init__(self,segment,port):
		self.segment=segment
		self.port=port
		self.port_dict={22:"ssh",23:"telnet"}
		self.scanned_ips=[]

	def scan_segment(self):
		return nmap.PortScanner().scan(self.segment,str(self.port))

	def analyze_nmap(self):
		nmap_data=_nmap.scan_segment(self)
		for host in nmap_data["scan"]:
			if(nmap_data["scan"][host]["status"]["state"]=="up"):
				if (nmap_data["scan"][host]["tcp"][self.port]["name"]==self.port_dict[self.port]):
					if (nmap_data["scan"][host]["tcp"][self.port]["cpe"]=="cpe:/o:cisco:ios"):
						self.scanned_ips.append(host)
		return _parsing(self.scanned_ips).sort_ip_range()

class _parsing:
	def __init__(self,ips):
		self.ips=ips

	def sort_ip_range(self):
		print("ordenando ips..")
		split_ips=[self.ips[i].split(".") for i in range(len(self.ips))]
		A=[int(split_ips[i][0]) for i in range(len(self.ips))]
		B=[int(split_ips[i][1]) for i in range(len(self.ips))]
		C=[int(split_ips[i][2]) for i in range(len(self.ips))]
		D=[int(split_ips[i][3]) for i in range(len(self.ips))]
		A.sort()
		B.sort()
		C.sort()
		D.sort()
		SORTED=[str(A[i])+"."+str(B[i])+"."+str(C[i])+"."+str(D[i]) for i in range(len(split_ips))]
		return SORTED

	def sort_ip_plus_values(self,data):
		print("ordenando datos..")
		output=[]
		for i in range(len(self.ips)):
			for j in range(len(data)):
				if(self.ips[i]==data[j][0]):
					output.append(data[j])
		return output


class _telnet:
	def __init__(self,ips,user,passwd):
		self.ips=ips
		self.user=user
		self.passwd=passwd

	def invoke_shell(self,tn):
		read=str(tn.read_some())
		while(1): #receive data until finish loading
			try:
				read+=str(tn.read_some())
			except:
				break
		if(read.find("Username: ")>=0 or read.find("Password:")>=0):
			tn.write(self.user+"\n")
			time.sleep(0.1)
			read_pwd=tn.read_some()
			if(read_pwd.find("Password:")>=0):
				tn.write(self.passwd+"\n")
				time.sleep(0.1)
				read_login=tn.read_some()
		try:
			if(read_login.find("#")>=0):
				return tn
			else:
				if(read_login.find(">")>=0):
					tn.write("ena\n")
					time.sleep(0.1)
					tn.write(self.passwd+"\n")
					time.sleep(0.1)
					read_login=tn.read_some()
					if(read_login.find("#")>=0):
						return tn
		except:
			return None

	def telnet_autorization(self,ip,output):
		try:
			telnet_client=Telnet(ip,23,10)
			remote_conn=_telnet.invoke_shell(self,telnet_client)
			output.append([ip,remote_conn])
		except:
			output.append([ip,None])

	def telnet_conection(self):
		Threads=[]
		output=[]
		for i in range(len(self.ips)):
			t=threading.Thread(target=_telnet.telnet_autorization,args=(self,self.ips[i],output,))
			Threads.append(t)
			Threads[i].start()
		Threads=[Threads[i].join() for i in range(len(self.ips))]
		return output

	def write_telnet_work(self,telnet_autorization,data,output):
		ip=telnet_autorization[0]
		remote_conn=telnet_autorization[1]
		if(remote_conn!=None):
			for i in range(len(data)):
				remote_conn.write(data[i]+"\n")
				time.sleep(0.1)
			result=""
			while(result.find("exit")<0):
				try:
					result+=remote_conn.read_some()
					time.sleep(0.1)
				except:
					pass
			output.append([ip,result])
		else:
			output.append(ip,remote_conn)

	def write_telnet(self,telnet_autorization,data):
		output=[]
		Threads=[]
		for i in range(len(telnet_autorization)):
			t=threading.Thread(target=_telnet.write_telnet_work,args=(self,telnet_autorization[i],data,output,))
			Threads.append(t)
			Threads[i].start()
		Threads=[Threads[i].join() for i in range(len(telnet_autorization))]
		return output

	def analyze_snmp(self,result,community,ip_range):
		yes=[]
		no=[]
		output=[]
		for i in range(len(result)):
			ip=result[i][0]
			data=result[i][1]
			res=(data[data.find("show run | inc snmp-server community"):len(data)])
			if(res.find("snmp-server community "+community+" RO")>=0):
				yes.append([ip,True])
			else:
				no.append([ip,False])
				if(data==None):
					no.append([ip,False])
		output.extend(yes)
		output.extend(no)
		output=_parsing(ip_range).sort_ip_plus_values(output)
		return output
"""
class excel:
	def __init__(self):

	def 
"""
