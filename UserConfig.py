import os

def UserManagement():
	
	os.system("tput setaf 5")
	os.system("clear")

	print("\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("\t\t\tUSER MANAGEMENT USING TUI")
	print("\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("""Select the number to perform the task :\n
Press 01: TO LIST ALL USERS PRESENT
Press 02: TO CREATE A NEW USER	
Press 03: TO REMOVE USER
Press 04: TO LIST ALL GROUPS
Press 05: TO CREATE A GROUP
Press 06: TO CHECK DETAILS OF CURRENT USER
Press 07: TO REMOVE GROUP\n""")
	
	os.system("tput setaf 6")
	opt=int(input("Enter your Choice :"))
	if(opt==1):
		os.system("cat /etc/passwd")
	elif(opt==2):
		Uname=input("Enter Username to Create :")
		os.system("useradd {}".format(Uname))
	elif(opt==3):
		os.system("cat /etc/passwd")
		Uname=input("Enter Username to Delete :")
		os.system("userdel {}".format(Uname))
	elif(opt==4):
		os.system("cat /etc/group")
	elif(opt==5):
		gname=input("Enter Group name :")
		os.system("groupadd {}".format(gname))
	elif(opt==6):
		os.system("id")
	elif(opt==7):
		gname=input("Enter Group name to remove :")
		os.system("groupdel {}".format())
	else:
		print("!!!Please Enter a valid number !!!")

	input("\nPress Enter to Continue...")
	os.system("clear")
	os.system("tput setaf 7")


def RemoteUserManagement(IP):
	os.system("tput setaf 5")
	os.system("clear")

	print("\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("\t\t\tUSER MANAGEMENT USING TUI")
	print("\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("""Select the number to perform the task :\n
Press 01: TO LIST ALL USERS PRESENT
Press 02: TO CREATE A NEW USER	
Press 03: TO REMOVE USER
Press 04: TO LIST ALL GROUPS
Press 05: TO CREATE A GROUP
Press 06: TO CHECK DETAILS OF CURRENT USER
Press 07: TO REMOVE GROUP\n""")
	
	os.system("tput setaf 6")
	opt=int(input("Enter your Choice :"))
	if(opt==1):
		os.system("ssh root@{} cat /etc/passwd".format(IP))
	elif(opt==2):
		Uname=input("Enter Username to Create :")
		os.system("ssh root@{0} useradd {1}".format(IP, Uname))
	elif(opt==3):
		os.system("ssh root@{} cat /etc/passwd".format(IP))
		Uname=input("Enter Username to Delete :")
		os.system("ssh root@{0} userdel {1}".format(IP, Uname))
	elif(opt==4):
		os.system("ssh root@{} cat /etc/group".format(IP))
	elif(opt==5):
		gname=input("Enter Group name :")
		os.system("ssh root@{0} groupadd {1}".format(IP, gname))
	elif(opt==6):
		os.system("ssh root@{} id".format(IP))
	elif(opt==7):
		gname=input("Enter Group name to remove :")
		os.system("ssh root@{0} groupdel {1}".format(IP,gname))
	else:
		print("!!!Please Enter a valid number !!!")

	input("\nPress Enter to Continue...")
	os.system("clear")
	os.system("tput setaf 7")









