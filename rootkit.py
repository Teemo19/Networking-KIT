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
