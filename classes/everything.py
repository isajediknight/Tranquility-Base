import platform,datetime,sys

def find_all(a_str, sub):
    """
    Returns the indexes of {sub} where they were found in {a_str}.  The values
    returned from this function should be made into a list() before they can
    be easily used.
    """

    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += 1

if(sys.platform.lower().startswith('linux')):
    OS_TYPE = 'linux'
elif(sys.platform.lower().startswith('mac')):
    OS_TYPE = 'macintosh'
elif(sys.platform.lower().startswith('win')):
    OS_TYPE = 'windows'
else:
    OS_TYPE = 'invalid'

class CustomString:
    """
    Make strings great again
    """

    def __init__(self,value = ''):
        """
        Initialize with just the string
        """
        
        # Padding desired
        self.prepend_spaces_number = 0
        self.postpend_spaces_number = 0

        # Actual padding applied
        self.left_spaces = ""
        self.right_spaces = ""

        # The string
        self.value = value
        self.colored = value

        # Changes to True once colors have been set
        self.is_colored = False

        # Not sure what this is for
        self.value_spaced = value
        
        # Have pre and post spaces been added?
        self.is_spaced = False
        self.length = len(value)


    def define_color(self,name,red,green,blue,text,ansi_1='0',ansi_2='38',ansi_3='2'):
        """
        Sets the color of the text
        """
        self.colored = TextColor(name,red,green,blue,text,ansi_1,ansi_2,ansi_3)
        self.is_colored = True

    def set_pre_spaces(self,prepend_spaces):
        """
        * Will only prepend spaces for a print string.
        * Will only add spaces if the string is shorter than the prepend amount
        """
        self.prepend_spaces_number = prepend_spaces

    def set_post_spaces(self,postpend_spaces):
        """
        * Will only postpend spaces for a print string.
        * Will only add spaces if the string is shorter than the postpend amount
        """
        self.postpend_spaces_number = postpend_spaces

    def fix_spacing(self):
        """
        Puts pre and post spaces on the string
        """
        while((self.length + len(self.left_spaces)) < self.prepend_spaces_number):
            self.left_spaces += " "

        while((self.length + len(self.right_spaces)) < self.postpend_spaces_number):
            self.right_spaces += " "
        
        self.is_spaced = True

    def uncolored(self):
        """
        Return the text uncolored
        """
        return self.left_spaces + self.value + self.right_spaces

    def c(self):
        """
        Meant to be the smallest amount of text needed to print the text colored
        """
        return self.left_spaces + self.colored.__str__() + self.right_spaces

    def __str__(self):
        """
        toString() method
        """
        if(self.is_colored):
            return self.left_spaces + self.colored.__str__() + self.right_spaces
        else:
            return self.left_spaces + self.value + self.right_spaces

    def __repr__(self):
        """
        for debugging
        """
        if(self.is_colored):
            return f'CustomString(\'{self.left_spaces}\', \'{self.colored}\', \'{self.right_spaces}\')'
        else:
            return self.left_spaces + self.value + self.right_spaces

class TextColor:
    """
    Class for text color
    """

    def __init__(self,name='white',red='0',green='0',blue='0',text='replace this',ansi_1='0',ansi_2='38',ansi_3='2'):
##        self.text_affects = {}
##        self.text_affects['normal'] = ''
##        self.text_affects['bold'] = '1;'
##        self.text_affects['disabled'] = '2;'
##        self.text_affects['italic'] = '3;'
##        self.text_affects['underlined'] = '4;'
##        self.text_affects['reverse'] = '7;'
##        self.text_affects['strike through'] = '8;'
##        self.text_affects['invisible'] = '9;'
        
        self.name = name
        self.text = text
        self.ansi_1 = str(ansi_1)
        self.ansi_2 = str(ansi_2)
        self.ansi_3 = str(ansi_3)
        self.red = str(red)
        self.green = str(green)
        self.blue = str(blue)
        self.colored_without_text = '\x1b[' + self.ansi_1 + ';'+ self.ansi_2 + ';' + self.ansi_3 + ';' + self.red + ';' + self.green + ';' + self.blue +'m' + '\x1b[0m'

        self.colored = '\x1b[' + self.ansi_1 + ';'+ self.ansi_2 + ';' + self.ansi_3 + ';' + self.red + ';' + self.green + ';' + self.blue +'m' + self.text + '\x1b[0m'
        self.c = '\x1b[' + self.ansi_1 + ';'+ self.ansi_2 + ';' + self.ansi_3 + ';' + self.red + ';' + self.green + ';' + self.blue +'m' + self.text + '\x1b[0m'

    def color(self,text=''):
        return '\x1b[' + self.ansi_1 + ';'+ self.ansi_2 + ';' + self.ansi_3 + ';' + self.red + ';' + self.green + ';' + self.blue +'m' + text + '\x1b[0m'

    def __str__(self):
        return str(self.c)
