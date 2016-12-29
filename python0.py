# coding : utf-8
import os, psutil, sys, shutil

# Комментарий

print("Perfect python program")
print("Hi, fool")
name = input("Your name:")

print(name, ", Welcome to Python World!")


answer = ''
# PEP-8
while answer != 'q':
	answer = input ("Let's work? (Y/N/q)")
	if answer == 'Y':
		print("Excelent, master")
		print("I can:")
		print("  [1] - List of files")
		print("  [2] - System Information")
		print("  [3] - List of processes")
		print("  [4] - Duplicate files in the current directory")
		print("  [5] - Duplicate the specified file")
		print("  [6] - Delete the specified file")
		
		do = int(input("Enter the number of actions:"))
		
		if do == 1:
			print(os.listdir())
		elif do == 2:
			print("Here's what I know about the system: ")
			print("Number of processors: ", psutil.cpu_count())
			print("Platform: ", sys.platform)
			print("File System Encoding: ", sys.getfilesystemencoding())
			print("The current directory: ", os.getcwd())
			print("Current user: ", os.getlogin())
		elif do == 3:
			print(psutil.pids())
		elif do == 4:
			print("=Duplicate=")
			file_list = os.listdir()
			i = 0
			while i < len(file_list):
				if os.path.isfile(file_list[i]):
					newfile = file_list[i] + '.dupl'				
					shutil.copy(file_list[i], newfile) #copy
				i += 1
		elif do == 5:
			print("=Duplicate the specified file=")
			filename = input("Enter the file name: ")
			if os.path.isfile(filename):
				newfile = filename + '.dupl'				
				shutil.copy(filename, newfile) #copy	
		elif do == 6:
			print("=Delete the specified file=")
			dirname = input("Enter the directory name: ")
			file_list = os.listdir(dirname)
			i = 0
			while i < len(file_list):
				fullname = os.path.join(dirname, file_list[i]) # \ /
				if fullname.endswith('.dupl'):
					os.remove(fullname)					
				i += 1
		else:
			pass
			
	elif answer == 'N':
		print("Goodbye!")
	else:
		print("Unknown")
	