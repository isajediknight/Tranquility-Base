
# Default Modules
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
    directories = list(find_all(OUTPUT_FILE_DIRECTORY,'\\'))
    OUTPUTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\outputs\\'
    INPUTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\inputs\\'
    SCRIPTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\scripts\\'
    MODULES_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\modules\\'
    CLASSES_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\classes\\'
elif((OS_TYPE == 'linux') or (OS_TYPE == 'macintosh')):
    # Clear Screen Linux / Mac
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

from advanced_colors import AdvancedColor
from classic_colors import ClassicColor

yellow = ClassicColor('yellow','38;5;226m')

green = ClassicColor('green','38;5;46m')

red = AdvancedColor('red','214','39','40','0','38','2')

white = AdvancedColor('white',255,255,255,0,38,2)

tableau_10_blue = AdvancedColor('Tableau 10 Blue',31,119,180,0,38,2)
tableau_10_brown = AdvancedColor('Tableau 10 Brown',140,86,75,0,38,2)
tableau_10_orange = AdvancedColor('Tableau 10 Orange',255,127,14,0,38,2)
tableau_10_pink = AdvancedColor('Tableau 10 Pink',227,119,194,0,38,2)
tableau_10_green = AdvancedColor('Tableau 10 Green',44,160,44,0,38,2)
tableau_10_grey = AdvancedColor('Tableau 10 Grey',127,127,127,0,38,2)
tableau_10_red = AdvancedColor('Tableau 10 Red',214,39,40,0,38,2)
tableau_10_yellow = AdvancedColor('Tableau 10 Yellow',188,189,34,0,38,2)
tableau_10_purple = AdvancedColor('Tableau 10 Purple',148,103,189,0,38,2)
tableau_10_teal = AdvancedColor('Tableau 10 Teal',23,190,207,0,38,2)
tableau_20_blue = AdvancedColor('Tableau 20 Blue',31,119,180,0,38,2)
tableau_20_light_green = AdvancedColor('Tableau 20 Light Green',152,223,138,0,38,2)
tableau_20_brown = AdvancedColor('Tableau 20 Brown',140,86,75,0,38,2)
tableau_20_grey = AdvancedColor('Tableau 20 Grey',199,199,199,0,38,2)
tableau_20_light_blue = AdvancedColor('Tableau 20 Light Blue',174,199,232,0,38,2)
tableau_20_red = AdvancedColor('Tableau 20 Red',214,39,40,0,38,2)
tableau_20_light_brown = AdvancedColor('Tableau 20 Light Brown',196,156,148,0,38,2)
tableau_20_yellow = AdvancedColor('Tableau 20 Yellow',188,189,34,0,38,2)
tableau_20_orange = AdvancedColor('Tableau 20 Orange',255,127,14,0,38,2)
tableau_20_light_red = AdvancedColor('Tableau 20 Light Red',255,152,150,0,38,2)
tableau_20_pink = AdvancedColor('Tableau 20 Pink',227,119,194,0,38,2)
tableau_20_light_yellow = AdvancedColor('Tableau 20 Light Yellow',219,219,141,0,38,2)
tableau_20_light_orange = AdvancedColor('Tableau 20 Light Orange',255,187,120,0,38,2)
tableau_20_purple = AdvancedColor('Tableau 20 Purple',148,103,189,0,38,2)
tableau_20_light_pink = AdvancedColor('Tableau 20 Light Pink',247,182,210,0,38,2)
tableau_20_baby_blue = AdvancedColor('Tableau 20 Baby Blue',23,190,207,0,38,2)
tableau_20_green = AdvancedColor('Tableau 20 Green',44,160,44,0,38,2)
tableau_20_light_purple = AdvancedColor('Tableau 20 Light Purple',197,176,213,0,38,2)
tableau_20_dark_grey = AdvancedColor('Tableau 20 Dark Grey',127,127,127,0,38,2)
tableau_20_light_baby_blue = AdvancedColor('Tableau 20 Light Baby Blue',158,218,229,0,38,2)
##tableau_10_ = AdvancedColor('Tableau 10 ',,0,38,2)
##tableau_10_ = AdvancedColor('Tableau 10 ',,0,38,2)
##tableau_10_ = AdvancedColor('Tableau 10 ',,0,38,2)
##tableau_10_ = AdvancedColor('Tableau 10 ',,0,38,2)
##tableau_10_ = AdvancedColor('Tableau 10 ',,0,38,2)



#https://graf1x.com/wp-content/uploads/2017/06/list-of-colors-and-color-names.jpg
#https://unix.stackexchange.com/questions/269077/tput-setaf-color-table-how-to-determine-color-codes/269085#269085
#https://goodsciencing.com/covid/athletes-suffer-cardiac-arrest-die-after-covid-shot/

