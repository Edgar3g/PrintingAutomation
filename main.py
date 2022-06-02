from logging import error
import os
import win32api
import win32print

print("\n\n\t\tWelcome to PRINTER AUTOMATIONS \n\n\n")

"""
Set the print to use!
"""
printers = win32print.EnumPrinters(2)  # look for printers in my computer

# choose the 1 of printers to use
print("Choose a Printer:\n")

for printer in printers:
    print (printer)
selectedPrinter = int(input("\n\nPrinter number: "))

myPrinter = printers[selectedPrinter -1] 
print(f'\nDo tou select ==>  {myPrinter}')
win32print.SetDefaultPrinter(myPrinter[2])

# get the files location
filesDir = input("\nEnter the complete folder location of the files:")

# select and print the files
filesToPrint = os.listdir(filesDir)

try:
    for _file in filesToPrint:
        win32api.ShellExecute(0, "print", filesDir +"\\"+_file, None,".", 0)
except error:
    print(error)