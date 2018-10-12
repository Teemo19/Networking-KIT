import nmap

class _nmap:
	def __init__(self,segment,port):
		self.segment=segment
		self.port=port
		self.port_dic={22:"ssh",23:"telnet"}
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
		return self.scanned.ips

class parsing:
	def __init__(self,ips):
		self.ips=ips

	def sort_ip_range(self):
		split_ips=[self.ips[i] for i in range(len(self.ips))]
		A=[int split_ips[i][0]) for i in range(len(self.ips))]
		B=[int split_ips[i][1]) for i in range(len(self.ips))]
		C=[int split_ips[i][2]) for i in range(len(self.ips))]
		D=[int split_ips[i][3]) for i in range(len(self.ips))]
		A.sort()
		B.sort()
		C.sort()
		D.sort()
		SORTED=[str(A[i])+"."str(B[i])+"."str(C[i])+"."+str(D[i]) for i in range(len(split_ips))]
		return SORTED
