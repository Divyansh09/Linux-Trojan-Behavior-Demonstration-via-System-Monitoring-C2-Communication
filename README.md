# Linux Trojan Behavior Demonstration via System Monitoring & C2 Communication

**Project Overview:**
This project is a resource monitoring system developed in Python, designed to operate on Linux systems. It incorporates a Trojan horse component for educational purposes.
**Components:**
•	trojan.py: The main script that integrates the Trojan functionality into the resource monitoring system.
•	c2-server.py: The command-and-control (C2) server script that communicates with the Trojan, allowing for remote command execution.
•	memmon: A binary executable responsible for monitoring system resources.
**Functionality:**
•	Monitors system resources such as CPU and memory usage. 
•	Establishes a connection with the C2 server to receive and execute remote commands.
**Usage:**
1.	Clone the repository to your local machine.
2.	Run the memmon binary to start monitoring system resources.
3.	Launch the c2-server.py script to set up the command-and-control server.
4.	Execute the trojan.py script to initiate the Trojan's operations and connect to the C2 server.

