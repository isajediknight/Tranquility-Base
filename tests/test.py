
print("\x1b[4;31mWhat Text Looks Like Without Proper Imports\x1b[0m")

# Default Modules
import datetime,time,os,sys,unittest

if(sys.platform.lower().startswith('linux')):
    OS_TYPE = 'linux'
elif(sys.platform.lower().startswith('mac')):
    OS_TYPE = 'macintosh'
elif(sys.platform.lower().startswith('win')):
    OS_TYPE = 'windows'
else:
    OS_TYPE = 'invalid'

# Get our current directory
OUTPUT_FILE_DIRECTORY = os.getcwd()

def find_all(a_str, sub):
    """
    Returns the indexes of {sub} where they were found in {a_str}.  The values
    returned from this function should be made into a list() before they can
    be easily used.
    Last Update: 03/01/2017
    By: LB023593
    """

    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += 1

# Create variables for all the paths
if((OS_TYPE == 'windows')):
    # Clear Screen Windows
    os.system('cls')
    directories = list(find_all(OUTPUT_FILE_DIRECTORY,'\\'))
    OUTPUTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\outputs\\'
    INPUTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\inputs\\'
    SCRIPTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\scripts\\'
    MODULES_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\modules\\'
    CLASSES_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\classes\\'
elif((OS_TYPE == 'linux') or (OS_TYPE == 'macintosh')):
    # Clear Screen Linux / Mac
    os.system('clear')
    directories = list(find_all(OUTPUT_FILE_DIRECTORY,'/'))
    OUTPUTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/outputs/'
    INPUTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/inputs/'
    SCRIPTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/scripts/'
    MODULES_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/modules/'
    CLASSES_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/classes/'

# OS Compatibility for importing Class Files
if((OS_TYPE == 'linux')):
    sys.path.insert(0,'../classes/')
elif((OS_TYPE == 'windows')):
    sys.path.insert(0,'..\\classes\\')

#print("\x1b[38;0;93mhello world\x1b[0m")
#print("\x1b[38;1;93mhello world\x1b[0m")
#print("\x1b[38;2;93mhello world\x1b[0m")
#print("\x1b[38;3;93mhello world\x1b[0m")
#print("\x1b[38;4;93mhello world\x1b[0m")
    
###print("\x1b[38;5;93mhello world\x1b[0m")
    
#print("\x1b[38;6;93mhello world\x1b[0m")
#print("\x1b[38;7;93mhello world\x1b[0m")
#print("\x1b[38;8;93mhello world\x1b[0m")
#print("\x1b[38;9;93mhello world\x1b[0m")

print("\x1b[38;5;15mNormal\x1b[0m",end="")
print("\t\t",end="")
raw_string = "\x1b[38;5;15m\x1b[0m"
for char in raw_string:
    print(char,end="")
print("")
for value in range(0,256):
	if(value < 10):
		out_string = "  " + str(value)
	elif(value < 100):
		out_string = " " + str(value)
	else:
		out_string = str(value)
	print("\x1b[38;5;"+str(value)+"m"+out_string +"\x1b[0m",end=" ")
	if(value == 15):
		print("")
	if(value == 51):
		print("")
	if(value == 87):
		print("")
	if(value == 123):
		print("")
	if(value == 159):
		print("")
	if(value == 195):
		print("")
	if(value == 231):
		print("")

print("")
print("")

print("\x1b[138;5;4m  4\x1b[0m",end=" ")
print("\x1b[138;5;7m  7\x1b[0m",end=" ")
print("\x1b[138;5;41m 41\x1b[0m",end=" ")
print("\x1b[138;5;42m 42\x1b[0m",end=" ")
print("\x1b[138;5;43m 43\x1b[0m",end=" ")
print("\x1b[138;5;44m 44\x1b[0m",end=" ")
print("\x1b[138;5;45m 45\x1b[0m",end=" ")
print("\x1b[138;5;46m 46\x1b[0m",end=" ")
print("\x1b[138;5;47m 47\x1b[0m",end=" ")
print("\x1b[138;5;100m100\x1b[0m",end=" ")
print("\x1b[138;5;101m101\x1b[0m",end=" ")
print("\x1b[138;5;102m102\x1b[0m",end=" ")
print("\x1b[138;5;103m103\x1b[0m",end=" ")
print("\x1b[138;5;104m104\x1b[0m",end=" ")
print("\x1b[138;5;105m105\x1b[0m",end=" ")
print("\x1b[138;5;106m106\x1b[0m",end=" ")
print("\x1b[138;5;107m107\x1b[0m",end=" ")
print("")
print("")

##for value in range(0,256):
##	if(value < 10):
##		out_string = "  " + str(value)
##	elif(value < 100):
##		out_string = " " + str(value)
##	else:
##		out_string = str(value)
##	print("\x1b[138;5;"+str(value)+"m"+out_string +"\x1b[0m",end=" ")
##	if(value == 15):
##		print("")
##	if(value == 51):
##		print("")
##	if(value == 87):
##		print("")
##	if(value == 123):
##		print("")
##	if(value == 159):
##		print("")
##	if(value == 195):
##		print("")
##	if(value == 231):
##		print("")
##
##print("")
##print("")

for value in range(0,256):
	if(value < 10):
		out_string = "  " + str(value)
	elif(value < 100):
		out_string = " " + str(value)
	else:
		out_string = str(value)
	print("\x1b[4;38;5;"+str(value)+"m"+out_string +"\x1b[0m",end=" ")
	if(value == 15):
		print("")
	if(value == 51):
		print("")
	if(value == 87):
		print("")
	if(value == 123):
		print("")
	if(value == 159):
		print("")
	if(value == 195):
		print("")
	if(value == 231):
		print("")

print("")
print("")

for value in range(0,256):
	if(value < 10):
		out_string = "  " + str(value)
	elif(value < 100):
		out_string = " " + str(value)
	else:
		out_string = str(value)
	print("\x1b[7;38;5;"+str(value)+"m"+out_string +"\x1b[0m",end=" ")
	if(value == 15):
		print("")
	if(value == 51):
		print("")
	if(value == 87):
		print("")
	if(value == 123):
		print("")
	if(value == 159):
		print("")
	if(value == 195):
		print("")
	if(value == 231):
		print("")

print("")
print("")

##for value in range(0,256):
##	if(value < 10):
##		out_string = "  " + str(value)
##	elif(value < 100):
##		out_string = " " + str(value)
##	else:
##		out_string = str(value)
##	print("\x1b[8;38;5;"+str(value)+"m"+out_string +"\x1b[0m",end=" ")
##	if(value == 15):
##		print("")
##	if(value == 51):
##		print("")
##	if(value == 87):
##		print("")
##	if(value == 123):
##		print("")
##	if(value == 159):
##		print("")
##	if(value == 195):
##		print("")
##	if(value == 231):
##		print("")
##print("")
##print("")
