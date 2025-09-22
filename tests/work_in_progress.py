import os,sys

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

from everything import *

tracker = Benchmark()

a = CustomString("Hello World")
a.set_pre_spaces(13)
a.set_post_spaces(13)
a.define_color('Dumb',100,100,100)
a.fix_spacing()

b = CustomString("text")
b.set_pre_spaces(13)
b.set_post_spaces(13)#a.length - 1 - b.length)
b.define_color('Color B',200,50,50)
b.fix_spacing()

c = CustomString("always aligned!")
c.set_pre_spaces(13)
c.set_post_spaces(13)#a.length - 1 - c.length)
c.define_color('Color C',250,150,75)
c.fix_spacing()

d = CustomString("Baby Baluga")
d.set_pre_spaces(13)
d.set_post_spaces(13)#a.length +7 - d.length)
d.define_color('Color D',90,10,180)
d.fix_spacing()

e = CustomString("aligned!")
e.set_pre_spaces(13)
e.set_post_spaces(13)#a.length +7 - d.length)
e.define_color('Color e',75,190,30)
e.fix_spacing()

print(" Sup" + a.c() +"Hi!")
print(" Sup" + b.c() +"Hi!")
print(" Sup" + c.c() +"Hi!")
print(" Sup" + d.c() +"Hi!")
print(" Sup" + e.c() +"Hi!")
a.debug()
b.debug()
c.debug()
d.debug()
e.debug()
my_dict = {}
my_dict['a'] = 'A'
my_dict['two'] = '2'

print(a + "Why can't this work? ")
print(a + 127)
print(a + 127.001)
print(a + [1,2,3])
print(a + my_dict)
print(a + set([1,2,3,3,3,3,4,5,5,7,7]))
print("Why can't this work? "+a)
print(127+a)
print(127.001+a)
print([1,2,3]+a)
print(my_dict+a)
print(set([1,2,3,3,3,3,4,5,5,7,7])+a)
print(a)

#ans = input("5 + 5 = ")

params = Parse()
params.add_expectation('name','string',True,False)
params.add_expectation('file','file',False,False)
params.add_expectation('weekday','string',False,False)
params.add_expectation('password','string',True,True)
#parameters.add_parameter(parameter_name,parameter_type,required,hidden)

params.parse_commandline()
params.validate_requirements()

params.display_parameters()

tracker.stop()
print(tracker.human_readable_string_without_microseconds())
