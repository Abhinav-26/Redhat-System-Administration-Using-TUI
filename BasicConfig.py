import os

def Basic():
	os.system("tput setaf 6")
	os.system("clear")

	print("\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("\t\t\tBASIC CONFIGURATION USING TUI")
	print("\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("""Select the number to perform the task :\n
Press 01: TO SEE DATE & TIME	
Press 02: TO SEE SYSTEM LANGUAGE
Press 03: TO SEE SYSTEM INFO
Press 04: TO OPEN SYSTEM PREFERENCES GUI
Press 05: WORKING ON IT
Press 06: TO EXIT THE APPLICATION
\n""")
	
	opt=int(input("Enter your Choice :"))	

	if(opt==1):
		os.system("timedatectl")

	elif(opt==2):
		os.system("localectl")

	elif(opt==3):
		os.system("lshw")


	elif(opt==4):
		os.system("gnome-control-center")


	elif(opt==5):
		print("WORKING ON IT")

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


################## REMOTE SYSTEM CONFIGURATION 


def RemoteBasic(IP):
	os.system("tput setaf 6")
	os.system("clear")

	print("\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("\t\t\tBASIC CONFIGURATION USING TUI")
	print("\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("""Select the number to perform the task :\n
Press 01: TO SEE DATE & TIME	
Press 02: TO SEE SYSTEM LANGUAGE
Press 03: To VIEW SYSTEM PROFILE
Press 04: TO OPEN SYSTEM PREFERENCES GUI
Press 05: WORKING ON IT
\n""")
	
	opt=int(input("Enter your Choice :"))	

	if(opt==1):
		os.system("ssh root@{} timedatectl".format(IP))

	elif(opt==2):
		os.system("ssh root@{} localectl".format(IP))

	elif(opt==3):
		os.system("ssh root@{} lshw".format(IP))


	elif(opt==4):
		os.system("ssh root@{} gnome-control-center".format(IP))


	elif(opt==5):
		print("WORKING ON IT")

	else:
		print("\n!!! Please enter a valid number !!!\n")
	
	input("\nPress Enter to Continue...")
	os.system("clear")	
	os.system("tput setaf 7")


