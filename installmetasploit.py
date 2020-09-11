import os 


print("this script will install metasploit")

os.system("figlet script by youssef")
print("this will take some time")
os.system("pkg update && pkg upgrade -y && pkg install wget curl openssh git -y && pkg install git -y")
os.system("wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh && chmod +x metasploit.sh")
os.system("wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/postgresql_ctl.sh")
os.system("bash metasploit.sh && bash postgresql_ctl.sh start")
print("metasploit will be started")

os.system("msfconsole")
