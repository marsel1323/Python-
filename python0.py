# coding : utf-8
import os, psutil, sys

# Комментарий

print("Perfect python program")
print("Hi, fool")
name = input("Your name:")

print(name, ", Welcome to Python World!")

answer = input ("Let's work? (Y/N)")

# PEP-8
if answer == 'Y':
	print("Excelent, master")
	print("I can:")
	print("  [1] - List of files")
	print("  [2] - System Information")
	print("  [3] - List of processes")
	
	do = int(input("Enter the number of actions:"))
	
	if do == 1:
		print(os.listdir())
	elif do == 2:
		pass
	elif do == 3:
		print(psutil.pids()
	else:
		pass
		
elif answer == 'N':
	print("Goodbye!")
else:
	print("Unknown")
	