
import time

print(" \x1b[4;31mWhat Text Looks Like Without Proper Imports\x1b[0m")
print(" Sleeping for 5 seconds")
print(" Then colored text will work")
#time.sleep(5)

# Default Modules
import datetime,os,sys,unittest

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
    sys.path.insert(0,'../modules/')
elif((OS_TYPE == 'windows')):
    sys.path.insert(0,'..\\classes\\')
    sys.path.insert(0,'..\\modules\\')

from constants import *
import solana

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

#outfile = open(OUTPUTS_DIR + "temp_file.txt",'w')

for value in range(0,256):
	if(value < 10):
		out_string = "  " + str(value)
	elif(value < 100):
		out_string = " " + str(value)
	else:
		out_string = str(value)
	print("\x1b[7;38;5;"+str(value)+"m"+out_string +"\x1b[0m",end=" ")
	#outfile.write(str("print("+'"'+"\x1b[7;38;5;")+str(value)+"m"+out_string +str("\x1b[0m"+'"'+")")+"\n")
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
#outfile.close()

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

print("")
##print("\x1b[7;38;5;0m  1\x1b[0m",end=" ")
##print("\x1b[7;38;5;1m  1\x1b[0m",end=" ")
##print("\x1b[7;38;5;2m  2\x1b[0m",end=" ")
##print("\x1b[7;38;5;3m  3\x1b[0m",end=" ")
##print("\x1b[7;38;5;4m  4\x1b[0m",end=" ")
##print("\x1b[7;38;5;5m  5\x1b[0m",end=" ")
##print("\x1b[7;38;5;6m  6\x1b[0m",end=" ")
##print("\x1b[7;38;5;7m  7\x1b[0m",end=" ")
##print("\x1b[7;38;5;8m  8\x1b[0m",end=" ")
##print("\x1b[7;38;5;9m  9\x1b[0m",end=" ")
##print("\x1b[7;38;5;10m 10\x1b[0m",end=" ")
##print("\x1b[7;38;5;11m 11\x1b[0m",end=" ")
##print("\x1b[7;38;5;12m 12\x1b[0m",end=" ")
##print("\x1b[7;38;5;13m 13\x1b[0m",end=" ")
##print("\x1b[7;38;5;14m 14\x1b[0m",end=" ")
##print("\x1b[7;38;5;15m 15\x1b[0m",)
print("\x1b[7;38;5;16m 16\x1b[0m",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("\x1b[7;38;5;23m 23\x1b[0m",end=" ")
print("\x1b[7;38;5;24m 24\x1b[0m",end=" ")
print("\x1b[7;38;5;25m 25\x1b[0m",end=" ")
print("\x1b[7;38;5;26m 26\x1b[0m",end=" ")
print("\x1b[7;38;5;27m 27\x1b[0m",end=" ")
print("   ",end=" ")
print("\x1b[7;38;5;29m 29\x1b[0m",end=" ")
print("\x1b[7;38;5;30m 30\x1b[0m",end=" ")
print("\x1b[7;38;5;31m 31\x1b[0m",end=" ")
print("\x1b[7;38;5;32m 32\x1b[0m",end=" ")
print("\x1b[7;38;5;33m 33\x1b[0m",end=" ")
print("   ",end=" ")
print("\x1b[7;38;5;35m 35\x1b[0m",end=" ")
print("\x1b[7;38;5;36m 36\x1b[0m",end=" ")
print("\x1b[7;38;5;37m 37\x1b[0m",end=" ")
print("\x1b[7;38;5;38m 38\x1b[0m",end=" ")
print("\x1b[7;38;5;39m 39\x1b[0m",end=" ")
print("   ",end=" ")
print("\x1b[7;38;5;41m 41\x1b[0m",end=" ")
print("\x1b[7;38;5;42m 42\x1b[0m",end=" ")
print("\x1b[7;38;5;43m 43\x1b[0m",end=" ")
print("\x1b[7;38;5;44m 44\x1b[0m",end=" ")
print("\x1b[7;38;5;45m 45\x1b[0m",end=" ")
print("   ",end=" ")
print("\x1b[7;38;5;47m 47\x1b[0m",end=" ")
print("\x1b[7;38;5;48m 48\x1b[0m",end=" ")
print("\x1b[7;38;5;49m 49\x1b[0m",end=" ")
print("\x1b[7;38;5;50m 50\x1b[0m",end=" ")
print("\x1b[7;38;5;51m 51\x1b[0m")
print("   ",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("\x1b[7;38;5;58m 58\x1b[0m",end=" ")
print("\x1b[7;38;5;59m 59\x1b[0m",end=" ")
print("\x1b[7;38;5;60m 60\x1b[0m",end=" ")
print("\x1b[7;38;5;61m 61\x1b[0m",end=" ")
print("\x1b[7;38;5;62m 62\x1b[0m",end=" ")
print("\x1b[7;38;5;63m 63\x1b[0m",end=" ")
print("\x1b[7;38;5;64m 64\x1b[0m",end=" ")
print("\x1b[7;38;5;65m 65\x1b[0m",end=" ")
print("\x1b[7;38;5;66m 66\x1b[0m",end=" ")
print("\x1b[7;38;5;67m 67\x1b[0m",end=" ")
print("\x1b[7;38;5;68m 68\x1b[0m",end=" ")
print("\x1b[7;38;5;69m 69\x1b[0m",end=" ")
print("\x1b[7;38;5;70m 70\x1b[0m",end=" ")
print("\x1b[7;38;5;71m 71\x1b[0m",end=" ")
print("\x1b[7;38;5;72m 72\x1b[0m",end=" ")
print("\x1b[7;38;5;73m 73\x1b[0m",end=" ")
print("\x1b[7;38;5;74m 74\x1b[0m",end=" ")
print("\x1b[7;38;5;75m 75\x1b[0m",end=" ")
print("\x1b[7;38;5;76m 76\x1b[0m",end=" ")
print("\x1b[7;38;5;77m 77\x1b[0m",end=" ")
print("\x1b[7;38;5;78m 78\x1b[0m",end=" ")
print("\x1b[7;38;5;79m 79\x1b[0m",end=" ")
print("\x1b[7;38;5;80m 80\x1b[0m",end=" ")
print("\x1b[7;38;5;81m 81\x1b[0m",end=" ")
print("\x1b[7;38;5;82m 82\x1b[0m",end=" ")
print("\x1b[7;38;5;83m 83\x1b[0m",end=" ")
print("\x1b[7;38;5;84m 84\x1b[0m",end=" ")
print("\x1b[7;38;5;85m 85\x1b[0m",end=" ")
print("\x1b[7;38;5;86m 86\x1b[0m",end=" ")
print("\x1b[7;38;5;87m 87\x1b[0m")
print("   ",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("\x1b[7;38;5;94m 94\x1b[0m",end=" ")
print("\x1b[7;38;5;95m 95\x1b[0m",end=" ")
print("\x1b[7;38;5;96m 96\x1b[0m",end=" ")
print("\x1b[7;38;5;97m 97\x1b[0m",end=" ")
print("\x1b[7;38;5;98m 98\x1b[0m",end=" ")
print("\x1b[7;38;5;99m 99\x1b[0m",end=" ")
print("\x1b[7;38;5;100m100\x1b[0m",end=" ")
print("\x1b[7;38;5;101m101\x1b[0m",end=" ")
print("\x1b[7;38;5;102m102\x1b[0m",end=" ")
print("\x1b[7;38;5;103m103\x1b[0m",end=" ")
print("\x1b[7;38;5;104m104\x1b[0m",end=" ")
print("\x1b[7;38;5;105m105\x1b[0m",end=" ")
print("\x1b[7;38;5;106m106\x1b[0m",end=" ")
print("\x1b[7;38;5;107m107\x1b[0m",end=" ")
print("\x1b[7;38;5;108m108\x1b[0m",end=" ")
print("\x1b[7;38;5;109m109\x1b[0m",end=" ")
print("\x1b[7;38;5;110m110\x1b[0m",end=" ")
print("\x1b[7;38;5;111m111\x1b[0m",end=" ")
print("\x1b[7;38;5;112m112\x1b[0m",end=" ")
print("\x1b[7;38;5;113m113\x1b[0m",end=" ")
print("\x1b[7;38;5;114m114\x1b[0m",end=" ")
print("\x1b[7;38;5;115m115\x1b[0m",end=" ")
print("\x1b[7;38;5;116m116\x1b[0m",end=" ")
print("\x1b[7;38;5;117m117\x1b[0m",end=" ")
print("\x1b[7;38;5;118m118\x1b[0m",end=" ")
print("\x1b[7;38;5;119m119\x1b[0m",end=" ")
print("\x1b[7;38;5;120m120\x1b[0m",end=" ")
print("\x1b[7;38;5;121m121\x1b[0m",end=" ")
print("\x1b[7;38;5;122m122\x1b[0m",end=" ")
print("\x1b[7;38;5;123m123\x1b[0m")
print("   ",end=" ")
print("\x1b[7;38;5;125m125\x1b[0m",end=" ")
print("\x1b[7;38;5;126m126\x1b[0m",end=" ")
print("\x1b[7;38;5;127m127\x1b[0m",end=" ")
print("\x1b[7;38;5;128m128\x1b[0m",end=" ")
print("\x1b[7;38;5;129m129\x1b[0m",end=" ")
print("\x1b[7;38;5;130m130\x1b[0m",end=" ")
print("\x1b[7;38;5;131m131\x1b[0m",end=" ")
print("\x1b[7;38;5;132m132\x1b[0m",end=" ")
print("\x1b[7;38;5;133m133\x1b[0m",end=" ")
print("\x1b[7;38;5;134m134\x1b[0m",end=" ")
print("\x1b[7;38;5;135m135\x1b[0m",end=" ")
print("\x1b[7;38;5;136m136\x1b[0m",end=" ")
print("\x1b[7;38;5;137m137\x1b[0m",end=" ")
print("\x1b[7;38;5;138m138\x1b[0m",end=" ")
print("\x1b[7;38;5;139m139\x1b[0m",end=" ")
print("\x1b[7;38;5;140m140\x1b[0m",end=" ")
print("\x1b[7;38;5;141m141\x1b[0m",end=" ")
print("\x1b[7;38;5;142m142\x1b[0m",end=" ")
print("\x1b[7;38;5;143m143\x1b[0m",end=" ")
print("\x1b[7;38;5;144m144\x1b[0m",end=" ")
print("\x1b[7;38;5;145m145\x1b[0m",end=" ")
print("\x1b[7;38;5;146m146\x1b[0m",end=" ")
print("\x1b[7;38;5;147m147\x1b[0m",end=" ")
print("\x1b[7;38;5;148m148\x1b[0m",end=" ")
print("\x1b[7;38;5;149m149\x1b[0m",end=" ")
print("\x1b[7;38;5;150m150\x1b[0m",end=" ")
print("\x1b[7;38;5;151m151\x1b[0m",end=" ")
print("\x1b[7;38;5;152m152\x1b[0m",end=" ")
print("\x1b[7;38;5;153m153\x1b[0m",end=" ")
print("\x1b[7;38;5;154m154\x1b[0m",end=" ")
print("\x1b[7;38;5;155m155\x1b[0m",end=" ")
print("\x1b[7;38;5;156m156\x1b[0m",end=" ")
print("\x1b[7;38;5;157m157\x1b[0m",end=" ")
print("\x1b[7;38;5;158m158\x1b[0m",end=" ")
print("\x1b[7;38;5;159m159\x1b[0m")
print("   ",end=" ")
print("\x1b[7;38;5;161m161\x1b[0m",end=" ")
print("\x1b[7;38;5;162m162\x1b[0m",end=" ")
print("\x1b[7;38;5;163m163\x1b[0m",end=" ")
print("\x1b[7;38;5;164m164\x1b[0m",end=" ")
print("\x1b[7;38;5;165m165\x1b[0m",end=" ")
print("\x1b[7;38;5;166m166\x1b[0m",end=" ")
print("\x1b[7;38;5;167m167\x1b[0m",end=" ")
print("\x1b[7;38;5;168m168\x1b[0m",end=" ")
print("\x1b[7;38;5;169m169\x1b[0m",end=" ")
print("\x1b[7;38;5;170m170\x1b[0m",end=" ")
print("\x1b[7;38;5;171m171\x1b[0m",end=" ")
print("\x1b[7;38;5;172m172\x1b[0m",end=" ")
print("\x1b[7;38;5;173m173\x1b[0m",end=" ")
print("\x1b[7;38;5;174m174\x1b[0m",end=" ")
print("\x1b[7;38;5;175m175\x1b[0m",end=" ")
print("\x1b[7;38;5;176m176\x1b[0m",end=" ")
print("\x1b[7;38;5;177m177\x1b[0m",end=" ")
print("\x1b[7;38;5;178m178\x1b[0m",end=" ")
print("\x1b[7;38;5;179m179\x1b[0m",end=" ")
print("\x1b[7;38;5;180m180\x1b[0m",end=" ")
print("\x1b[7;38;5;181m181\x1b[0m",end=" ")
print("\x1b[7;38;5;182m182\x1b[0m",end=" ")
print("\x1b[7;38;5;183m183\x1b[0m",end=" ")
print("\x1b[7;38;5;184m184\x1b[0m",end=" ")
print("\x1b[7;38;5;185m185\x1b[0m",end=" ")
print("\x1b[7;38;5;186m186\x1b[0m",end=" ")
print("\x1b[7;38;5;187m187\x1b[0m",end=" ")
print("\x1b[7;38;5;188m188\x1b[0m",end=" ")
print("\x1b[7;38;5;189m189\x1b[0m",end=" ")
print("\x1b[7;38;5;190m190\x1b[0m",end=" ")
print("\x1b[7;38;5;191m191\x1b[0m",end=" ")
print("\x1b[7;38;5;192m192\x1b[0m",end=" ")
print("\x1b[7;38;5;193m193\x1b[0m",end=" ")
print("\x1b[7;38;5;194m194\x1b[0m",end=" ")
print("\x1b[7;38;5;195m195\x1b[0m")
print("",end="    ")
print("\x1b[7;38;5;197m197\x1b[0m",end=" ")
print("\x1b[7;38;5;198m198\x1b[0m",end=" ")
print("\x1b[7;38;5;199m199\x1b[0m",end=" ")
print("\x1b[7;38;5;200m200\x1b[0m",end=" ")
print("\x1b[7;38;5;201m201\x1b[0m",end=" ")
print("   ",end=" ")
print("\x1b[7;38;5;203m203\x1b[0m",end=" ")
print("\x1b[7;38;5;204m204\x1b[0m",end=" ")
print("\x1b[7;38;5;205m205\x1b[0m",end=" ")
print("\x1b[7;38;5;206m206\x1b[0m",end=" ")
print("\x1b[7;38;5;207m207\x1b[0m",end=" ")
print("   ",end=" ")
print("\x1b[7;38;5;209m209\x1b[0m",end=" ")
print("\x1b[7;38;5;210m210\x1b[0m",end=" ")
print("\x1b[7;38;5;211m211\x1b[0m",end=" ")
print("\x1b[7;38;5;212m212\x1b[0m",end=" ")
print("\x1b[7;38;5;213m213\x1b[0m",end=" ")
print("   ",end=" ")
print("\x1b[7;38;5;215m215\x1b[0m",end=" ")
print("\x1b[7;38;5;216m216\x1b[0m",end=" ")
print("\x1b[7;38;5;217m217\x1b[0m",end=" ")
print("\x1b[7;38;5;218m218\x1b[0m",end=" ")
print("\x1b[7;38;5;219m219\x1b[0m",end=" ")
print("   ",end=" ")
print("\x1b[7;38;5;221m221\x1b[0m",end=" ")
print("\x1b[7;38;5;222m222\x1b[0m",end=" ")
print("\x1b[7;38;5;223m223\x1b[0m",end=" ")
print("\x1b[7;38;5;224m224\x1b[0m",end=" ")
print("\x1b[7;38;5;225m225\x1b[0m",end=" ")
print("   ",end=" ")
print("\x1b[7;38;5;227m227\x1b[0m",end=" ")
print("\x1b[7;38;5;228m228\x1b[0m",end=" ")
print("\x1b[7;38;5;229m229\x1b[0m",end=" ")
print("\x1b[7;38;5;230m230\x1b[0m",end=" ")
print("\x1b[7;38;5;231m231\x1b[0m")
print("   ",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("   ",end=" ")
print("   ")



print("\x1b[7;38;5;0m  0\x1b[0m")
print("Red",end="\t")
print("\x1b[7;38;5;196m196\x1b[0m",end="")
print("\x1b[7;38;5;160m160\x1b[0m",end="")
print("\x1b[7;38;5;1m  1\x1b[0m",end="")
print("\x1b[7;38;5;124m124\x1b[0m",end="")
print("\x1b[7;38;5;88m 88\x1b[0m",end="")
print("\x1b[7;38;5;52m 52\x1b[0m")

print("Green",end="\t")
print("\x1b[7;38;5;46m 46\x1b[0m",end="")
print("\x1b[7;38;5;40m 40\x1b[0m",end="")
print("\x1b[7;38;5;10m 10\x1b[0m",end="")
print("\x1b[7;38;5;34m 34\x1b[0m",end="")
print("\x1b[7;38;5;2m  2\x1b[0m",end="")
print("\x1b[7;38;5;28m 28\x1b[0m",end="")
print("\x1b[7;38;5;22m 22\x1b[0m")






print("Yellow",end="\t")
print("\x1b[7;38;5;226m226\x1b[0m",end="")
print("\x1b[7;38;5;220m220\x1b[0m",end="")
print("\x1b[7;38;5;3m  3\x1b[0m")



print("Orange",end="\t")
print("\x1b[7;38;5;202m202\x1b[0m",end="")
print("\x1b[7;38;5;208m208\x1b[0m",end="")
print("\x1b[7;38;5;214m214\x1b[0m")

print("Blue",end="\t")

print("\x1b[7;38;5;21m 21\x1b[0m",end="")
print("\x1b[7;38;5;20m 20\x1b[0m",end="")
print("\x1b[7;38;5;19m 19\x1b[0m",end="")
print("\x1b[7;38;5;18m 18\x1b[0m",end="")
print("\x1b[7;38;5;17m 17\x1b[0m")

print("Purple",end="\t")
print("\x1b[7;38;5;57m 57\x1b[0m",end="")
print("\x1b[7;38;5;56m 56\x1b[0m",end="")
print("\x1b[7;38;5;55m 55\x1b[0m",end="")
print("\x1b[7;38;5;54m 54\x1b[0m",end="")
print("\x1b[7;38;5;53m 53\x1b[0m")

print("\t",end="")
print("\x1b[7;38;5;93m 93\x1b[0m",end="")
print("\x1b[7;38;5;92m 92\x1b[0m",end="")
print("\x1b[7;38;5;91m 91\x1b[0m",end="")
print("\x1b[7;38;5;90m 90\x1b[0m",end="")
print("\x1b[7;38;5;89m 89\x1b[0m")













print("\x1b[7;38;5;4m  4\x1b[0m")
print("\x1b[7;38;5;6m  6\x1b[0m")


print("\x1b[7;38;5;9m  9\x1b[0m")

print("\x1b[7;38;5;5m  5\x1b[0m")

print("\x1b[7;38;5;11m 11\x1b[0m")
print("\x1b[7;38;5;12m 12\x1b[0m")
print("\x1b[7;38;5;13m 13\x1b[0m")
print("\x1b[7;38;5;14m 14\x1b[0m")
print("\x1b[7;38;5;15m 15\x1b[0m",end="")
print("\x1b[7;38;5;255m255\x1b[0m",end="")
print("\x1b[7;38;5;254m254\x1b[0m",end="")
print("\x1b[7;38;5;253m253\x1b[0m",end="")
print("\x1b[7;38;5;252m252\x1b[0m",end="")
print("\x1b[7;38;5;7m  7\x1b[0m",end="")
print("\x1b[7;38;5;251m251\x1b[0m",end="")
print("\x1b[7;38;5;250m250\x1b[0m",end="")
print("\x1b[7;38;5;249m249\x1b[0m",end="")
print("\x1b[7;38;5;248m248\x1b[0m",end="")
print("\x1b[7;38;5;247m247\x1b[0m",end="")
print("\x1b[7;38;5;246m246\x1b[0m",end="")
print("\x1b[7;38;5;245m245\x1b[0m",end="")
print("\x1b[7;38;5;244m244\x1b[0m",end="")
print("\x1b[7;38;5;243m243\x1b[0m",end="")
print("\x1b[7;38;5;8m  8\x1b[0m",end="")
print("\x1b[7;38;5;242m242\x1b[0m",end="")
print("\x1b[7;38;5;241m241\x1b[0m",end="")
print("\x1b[7;38;5;240m240\x1b[0m",end="")
print("\x1b[7;38;5;239m239\x1b[0m",end="")
print("\x1b[7;38;5;238m238\x1b[0m",end="")
print("\x1b[7;38;5;237m237\x1b[0m",end="")
print("\x1b[7;38;5;236m236\x1b[0m",end="")
print("\x1b[7;38;5;235m235\x1b[0m",end="")
print("\x1b[7;38;5;234m234\x1b[0m",end="")
print("\x1b[7;38;5;233m233\x1b[0m",end="")
print("\x1b[7;38;5;232m232\x1b[0m")














print("\x1b[7;38;5;16m 16\x1b[0m")

print("\x1b[7;38;5;226m226\x1b[0m")
#print("\x1b[38;2;213;117;37mwhut\x1b[0m")

#print("\x1b[0;38;2;50;198;252mBaby Blue\x1b[0m")
#print("\x1b[0;38;2;68;206;68mMiddle Green\x1b[0m")
#print("\x1b[0;38;2;255;153;51mOrange\x1b[0m")
print("\x1b[0;38;2;0;255;255mJames Favorite Color\x1b[0m" + " test " + "\x1b[0;38;2;67;114;245mNora's Favorite Color\x1b[0m")
print("\x1b[0;38;2;255;144;249mRachel's Favorite Color\x1b[0m")

print('default',end=' ')


ans = yellow.colored('the text can') + ' ' + green.colored('be') + ' ' + red.colored('whatever is needed')
ans += ' ' + tableau_10_blue.colored(' from constants file')
print(ans)

print("\x1b[4;38;5;226mTEST TEST\x1b[0m")


print("\x1b[7;38;5;202m202\x1b[0m" + "\x1b[7;38;5;208m208\x1b[0m",end="")
print("\x1b[7;38;5;214m214\x1b[0m")

os.system('cls')

ans = white.colored(' Tableau 10:') + ' '
ans += tableau_10_blue.colored('blue') + ' '
ans += tableau_10_brown.colored('brown') + ' '
ans += tableau_10_orange.colored('orange') + ' '
ans += tableau_10_pink.colored('pink') + ' '
ans += tableau_10_green.colored('green') + ' '
ans += tableau_10_grey.colored('grey') + ' '
ans += tableau_10_red.colored('red') + ' '
ans += tableau_10_yellow.colored('yellow') + ' '
ans += tableau_10_purple.colored('purple') + ' '
ans += tableau_10_teal.colored('teal') + ' '
#ans += tableau_10_.colored('')
print(ans)

ans = white.colored(' Tableau 20:') + ' '
ans += tableau_20_blue.colored('blue') + ' '
ans += tableau_20_light_green.colored('blue') + ' '
ans += tableau_20_brown.colored('blue') + ' '
ans += tableau_20_grey.colored('blue') + ' '
ans += tableau_20_light_blue.colored('blue') + ' '
ans += tableau_20_red.colored('blue') + ' '
ans += tableau_20_light_brown.colored('blue') + ' '
ans += tableau_20_yellow.colored('blue') + ' '
ans += tableau_20_orange.colored('blue') + ' '
ans += tableau_20_light_red.colored('blue') + ' '
ans += tableau_20_pink.colored('blue') + ' '
ans += tableau_20_light_yellow.colored('blue') + ' '
ans += tableau_20_light_orange.colored('blue') + ' '
ans += tableau_20_purple.colored('blue') + ' '
ans += tableau_20_light_pink.colored('blue') + ' '
ans += tableau_20_baby_blue.colored('blue') + ' '
ans += tableau_20_green.colored('blue') + ' '
ans += tableau_20_light_purple.colored('blue') + ' '
ans += tableau_20_dark_grey.colored('blue') + ' '
ans += tableau_20_light_baby_blue.colored('blue') + ' '
ans += tableau_20_blue.colored('blue') + ' '
ans += tableau_20_light_green.colored('blue') + ' '
ans += tableau_20_brown.colored('blue') + ' '
ans += tableau_20_grey.colored('blue') + ' '
ans += tableau_20_light_blue.colored('blue') + ' '
ans += tableau_20_red.colored('blue') + ' '
ans += tableau_20_light_brown.colored('blue') + ' '
ans += tableau_20_yellow.colored('blue') + ' '
ans += tableau_20_orange.colored('blue') + ' '
ans += tableau_20_light_red.colored('blue') + ' '
ans += tableau_20_pink.colored('blue') + ' '
ans += tableau_20_light_yellow.colored('blue') + ' '
ans += tableau_20_light_orange.colored('blue') + ' '
ans += tableau_20_purple.colored('blue') + ' '
ans += tableau_20_light_pink.colored('blue') + ' '
ans += tableau_20_baby_blue.colored('blue') + ' '
ans += tableau_20_green.colored('blue') + ' '
ans += tableau_20_light_purple.colored('blue') + ' '
ans += tableau_20_dark_grey.colored('blue') + ' '
ans += tableau_20_light_baby_blue.colored('blue')
print(ans)

print("\x1b[38;2;255;255;255mEND RESET\x1b[0m")



