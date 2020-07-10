import os
import getpass
from BasicConfig import *
from UserConfig import *
from PackageConfig import *

os.system("clear")

##################################### FOR LOGIN INTO PORTAL
print("\t\t\t\t~~~~~~~")
print("\t\t\t\t LOGIN")
print("\t\t\t\t~~~~~~~")
print("\n")
loginID = input("\t\tPlease Enter Your Username :")
loginPsd = getpass.getpass("\t\tPlease Enter Your Password :")

if(loginID=="authority" and loginPsd=="abhinav"):
	os.system("clear")
	os.system("tput setaf 7")
	print("\t\t  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	os.system("tput setaf 4")
	print("\t\t  PLEASE SELECT THE PLATFORM To PERFORM THE TASKs :")
	os.system("tput setaf 7")
	print("\t\t  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
	print("\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	os.system("tput setaf 4")
	print("\t\t\tPress 01: To Run in your Local Host")
	print("\t\t\tPress 02: To Run in Remote Machine")
	os.system("tput setaf 7")
	print("\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

	os.system("tput setaf 3")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("PRESS 0 TO EXIT THE APPLICATION")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

	os.system("tput setaf 2")
	run = int(input("Enter your Choice :"))

	if(run==0):
		print("\n")
		exit()

##################################### FOR LOCAL SYSTEM
	elif(run==1):
		os.system("clear")
		while True:
			# os.system("clear")
			os.system("tput setaf 2")
			print("\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~")
			os.system("tput setaf 3")
			print("\t\t\tWelcome to your Dashboard")
			os.system("tput setaf 2")
			print("\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~")



			print("""SELECT THE NUMBER FOR CONFIGURATION DOMAIN :\n
		Press 01: FOR BASIC CONFIGURATION
		Press 02: FOR PACKAGE MANAGEMENT
		Press 03: FOR USER MANAGEMENT
		Press 04: FOR LOG MANAGEMENT
		Press 05: FOR NETWORK MANAGEMENT
		Press 06: FOR SECURITY AND IDENTITY
		Press 07: FOR RESOURCE MANAGEMENT
		Press 08: FOR FILE SYSTEM, VOLUME AND DISKS
		Press 09: FOR DOCKER MANAGEMENT
		Press 10: FOR EXIT \n""")

			os.system("tput setaf 6")
			ch=int(input("Enter your option :"))
			os.system("tput setaf 5")

			if(ch==1):
				Basic()

			elif(ch==2):
				PkgManagement()	
				
			elif(ch==3):
				UserManagement()


			elif(ch==4):
				print("Working on it !!!")
				
			elif(ch==5):
				print("Working on it !!!")


			elif(ch==6):
				print("Working on it !!!")


			elif(ch==7):
				print("Working on it !!!")


			elif(ch==8):
				print("Working on it !!!")
								
			elif(ch==9):
				print("Working on it !!!")
	
			elif(ch==10):
				os.system("tput setaf 3")
				print("\n------------------------")
				print("Thank You For Using :)")
				print("------------------------\n")
				os.system("tput setaf 7")
				exit(0)
					
			else:
				print("!!! Enter a Valid Number !!!")
			os.system("clear")

################################## FOR REMOTE SYSTEM
		
	elif(run==2):
		IP = input("Please Enter IP Address of Remote  Machine :")
		while True:
			os.system("clear")
			os.system("tput setaf 2")
			print("\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~")
			os.system("tput setaf 3")
			print("\t\t\tWelcome to your Dashboard")
			os.system("tput setaf 2")
			print("\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~")



			print("""SELECT THE NUMBER FOR CONFIGURATION DOMAIN :\n
		Press 01: FOR BASIC CONFIGURATION
		Press 02: FOR PACKAGE MANAGEMENT
		Press 03: FOR USER MANAGEMENT
		Press 04: FOR KERNAL,BOOT & HARDWARE
		Press 05: FOR NETWORK MANAGEMENT
		Press 06: FOR SECURITY AND IDENTITY
		Press 07: FOR RESOURCE MANAGEMENT
		Press 08: FOR FILE SYSTEM, VOLUME AND DISKS
		Press 09: FOR DOCKER MANAGEMENT
		Press 10: FOR EXIT \n""")

			os.system("tput setaf 6")
			ch=int(input("Enter your option :"))
			os.system("tput setaf 5")

			if(ch==1):
				RemoteBasic(IP)

			elif(ch==2):
				RemotePkgManagement(IP)
				
			elif(ch==3):
				RemoteUserManagement(IP)


			elif(ch==4):
				print("Working on it !!!")
				
			elif(ch==5):
				print("Working on it !!!")


			elif(ch==6):
				print("Working on it !!!")


			elif(ch==7):
				print("Working on it !!!")


			elif(ch==8):
				print("Working on it !!!")
				
					
			elif(ch==9):
				os.system("tput setaf 3")
				print("\n------------------------")
				print("Thank You For Using :)")
				print("------------------------\n")
				os.system("tput setaf 7")
				exit(0)
					
			else:
				print("!!! Enter a Valid Number !!!")
			os.system("clear")	
		
	else:
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print("\nPlease Enter a valid number :(")
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



else:
	print("\n")
	print("\t\t  You are not Authorised User\n")


