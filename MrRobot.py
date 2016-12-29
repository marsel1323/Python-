# coding : utf-8
import os
import psutil
import sys
import shutil

# Комментарий

def duplicate_file(filename):
    if os.path.isfile(filename):
        newfile = filename + '.dupl'
        shutil.copy(filename, newfile) #copy
        if os.path.exists(newfile):
            print("File ", newfile, " has been successfully created")
            return True
        else:
            print("When copying a file had problems")
            return False

def del_duplicats(dirname):
    file_list = os.listdir(dirname)
    doubl_count = 0

    for f in file_list:
        fullname = os.path.join(dirname, f)  # \ /
        if fullname.endswith('.dupl'):
            os.remove(fullname)
            if not os.path.exists(fullname):
                doubl_count += 1
                print("File ", fullname, " has been successfully deleted")
    return doubl_count



def sys_info():
    print("Here's what I know about the system: ")
    print("Number of processors: ", psutil.cpu_count())
    print("Platform: ", sys.platform)
    print("File System Encoding: ", sys.getfilesystemencoding())
    print("The current directory: ", os.getcwd())
    print("Current user: ", os.getlogin())

def main():
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
				sys_info()
			elif do == 3:
				print(psutil.pids())
			elif do == 4:
				print("=Duplicate=")
				file_list = os.listdir()
				i = 0
				while i < len(file_list):
					duplicate_file(file_list[i])
					i += 1
			elif do == 5:
				print("=Duplicate the specified file=")
				filename = input("Enter the file name: ")
				duplicate_file(filename)

			elif do == 6:
				print("=Delete the specified file=")
				dirname = input("Enter the directory name: ")
				count = del_duplicats(dirname)
				print("--Deleting files: ", count)

			else:
				pass

		elif answer == 'N':
			print("Goodbye!")
		else:
			print("Unknown answer")
	
if __name__ == "__main__":
	main()
	
def duble_files(dirname):
	file_list = os.listdir(dirname)
	i = 0
	while i < len(file_list[i]):
		duplicate_file(file_list[i])
		i += 1