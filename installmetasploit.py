import os 


print("this script will install metasploit")

os.system("figlet script by youssef")
os.system("pkg update && pkg upgrade -y && pkg install wget curl openssh git -y && pkg install git -y")
os.system("cd /data/data/com.termux/files/home")
os.system("git clone https://github.com/gushmazuko/metasploit_in_termux")
os.system("cd metasploit_in_termux")
os.system("chmod 777 *")
os.system("./metasploit.sh")
os.system("./postgresql_ctl.sh start")

print("metasploit will be started")

os.system("msfconsole")
