import os

def PkgManagement():

	os.system("clear")
	os.system("tput setaf 2")
	print("\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	os.system("tput setaf 3")
	print("\t\t\tPACKAGE MANAGEMENT USING TUI")
	os.system("tput setaf 2")
	print("\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	os.system("tput setaf 6")
	print("""Select the number to perform the task :\n
Press 01: TO CONFIGURE YUM/DNF	
Press 02: TO INSTALL PACKAGE
Press 03: TO REMOVE PACKAGE
Press 04: TO LIST ALL PACKAGES
Press 05: TO SEARCH ANY PACKAGE
Press 06: TO EXIT\n""")
	
	opt=int(input("Enter your Choice :"))	

	if(opt==1):
		print("Working on it .... \n")		
	
	elif(opt==2):
		pkg = input("ENTER PACKAGE NAME TO INSTALL :")
		os.system("dnf install {}".format(pkg))
		print("\n")
	
	elif(opt==3):
		pkg = input("ENTER PACKAGE NAME TO REMOVE :")
		os.system("dnf remove {}".format(pkg))
		print("\n")

	elif(opt==4):
		os.system("rpm -q -a")
		print("\n")

	elif(opt==5):
		pkg = input("ENTER PACKAGE NAME TO SEARCH :")
		os.system("rpm -q {}".format(pkg))		
		print("\n")
	
	elif(opt==6):
		os.system("tput setaf 3")
		print("\n------------------------")
		print("Thank You For Using :)")
		print("------------------------\n")
		os.system("tput setaf 7")		
		exit(0)

	else:
		print("\n!!! Please enter a valid number !!!\n")
	input("\nPress Enter to Continue...")	
	os.system("clear")	
	os.system("tput setaf 7")



def RemotePkgManagement(IP):

	os.system("clear")
	os.system("tput setaf 2")
	print("\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	os.system("tput setaf 3")
	print("\t\t\tPACKAGE MANAGEMENT USING TUI")
	os.system("tput setaf 2")
	print("\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	os.system("tput setaf 6")
	print("""Select the number to perform the task :\n
Press 01: TO CONFIGURE YUM/DNF	
Press 02: TO INSTALL PACKAGE
Press 03: TO REMOVE PACKAGE
Press 04: TO LIST ALL PACKAGES
Press 05: TO SEARCH ANY PACKAGE
Press 06: TO EXIT\n""")
	
	opt=int(input("Enter your Choice :"))	

	if(opt==1):
		print("Working on it .... \n")		
	
	elif(opt==2):
		pkg = input("ENTER PACKAGE NAME TO INSTALL :")
		os.system("ssh root@{0} dnf install {1}".format(IP,pkg))
		print("\n")
	
	elif(opt==3):
		pkg = input("ENTER PACKAGE NAME TO REMOVE :")
		os.system("ssh root@{} dnf remove {}".format(IP,pkg))
		print("\n")

	elif(opt==4):
		os.system("ssh root@{} rpm -q -a".format(IP))
		print("\n")

	elif(opt==5):
		pkg = input("ENTER PACKAGE NAME TO SEARCH :")
		os.system("ssh root@{0} rpm -q {1}".format(IP, pkg))		
		print("\n")
	
	elif(opt==6):
		os.system("tput setaf 3")
		print("\n------------------------")
		print("Thank You For Using :)")
		print("------------------------\n")
		os.system("tput setaf 7")		
		exit(0)

	else:
		print("\n!!! Please enter a valid number !!!\n")
	input("\nPress Enter to Continue...")	
	os.system("clear")	
	os.system("tput setaf 7")


