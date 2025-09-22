import platform,datetime,sys,os,getpass

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

    def __init__(self,value):
        """
        Initialize with just the string
        """
        
        # Padding desired
        self.prepend_spaces_number = 0
        self.postpend_spaces_number = 0

        # Actual padding applied
        self.left_spaces = ""
        self.right_spaces = ""

        self.name = ''

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

    def define_color_replace_text(self,name,red,green,blue,text,ansi_1='0',ansi_2='38',ansi_3='2'):
        """
        Sets the color of the text
        """
        self.name = name
        self.colored = TextColor(name,red,green,blue,text,ansi_1,ansi_2,ansi_3)
        self.is_colored = True

    def define_color(self,name,red,green,blue,ansi_1='0',ansi_2='38',ansi_3='2'):
        """
        Sets the color of the text
        """
        self.colored = TextColor(name,red,green,blue,self.value,ansi_1,ansi_2,ansi_3)
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

        while((self.length + len(self.right_spaces)) < (self.postpend_spaces_number + self.length + len(self.left_spaces))):
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

    def __add__(self,other):
        """
        + method
        """

        if isinstance(other, CustomString):
            # Concatenate with another MyCustomString instance
            if(self.is_colored and other.is_colored):
                return str(self.left_spaces + self.colored.__str__() + self.right_spaces) + str(other.left_spaces + other.colored.__str__() + other.right_spaces)
            elif(self.is_colored and not other.is_colored):
                return str(self.left_spaces + self.colored.__str__() + self.right_spaces) + str(other.left_spaces + other.value + other.right_spaces)
            elif(not self.is_colored and other.is_colored):
                return str(self.left_spaces + self.value + self.right_spaces) + str(other.left_spaces + other.colored.__str__() + other.right_spaces)
            else:
                return str(self.left_spaces + self.value + self.right_spaces) + str(other.left_spaces + other.value + other.right_spaces)
        elif isinstance(other, str):
            # Concatenate with a standard string
            if(self.is_colored):
                return str(self.left_spaces + self.colored.__str__() + self.right_spaces) + other
            else:
                return str(self.left_spaces + self.value + self.right_spaces) + other
        elif isinstance(other, int):
            # Concatenate with a standard int
            if(self.is_colored):
                return str(self.left_spaces + self.colored.__str__() + self.right_spaces) + str(other)
            else:
                return str(self.left_spaces + self.value + self.right_spaces) + str(other)
        elif isinstance(other, float):
            # Concatenate with a standard float
            if(self.is_colored):
                return str(self.left_spaces + self.colored.__str__() + self.right_spaces) + str(other)
            else:
                return str(self.left_spaces + self.value + self.right_spaces) + str(other)
        elif isinstance(other, list):
            # Concatenate with a standard float
            if(self.is_colored):
                temp = "[ "
                for i in other:
                    temp += str(i) + ", "
                temp = temp[:-2]
                temp += " ]"
                return str(self.left_spaces + self.colored.__str__() + self.right_spaces) + temp
            else:
                return str(self.left_spaces + self.value + self.right_spaces) + str(other)
        elif isinstance(other, tuple):
            # Concatenate with a standard float
            if(self.is_colored):
                temp = "( "
                for i in other:
                    temp += str(i) + ", "
                temp = temp[:-2]
                temp += " )"
                return str(self.left_spaces + self.colored.__str__() + self.right_spaces) + temp
            else:
                return str(self.left_spaces + self.value + self.right_spaces) + str(other)
        elif isinstance(other, set):
            # Concatenate with a standard float
            if(self.is_colored):
                temp = "[ "
                other = list(other)
                for i in other:
                    temp += str(i) + ", "
                temp = temp[:-2]
                temp += " ]"
                return str(self.left_spaces + self.colored.__str__() + self.right_spaces) + temp
            else:
                return str(self.left_spaces + self.value + self.right_spaces) + str(other)
        elif isinstance(other, dict):
            # Concatenate with a standard float
            if(self.is_colored):
                temp = "{"
                for key in list(other.keys()):
                    temp += " [" +str(key)+":"+str(other[key]) + "],"
                temp = temp[:-2]
                temp += "] }"
                return str(self.left_spaces + self.colored.__str__() + self.right_spaces) + temp
            else:
                return str(self.left_spaces + self.value + self.right_spaces) + str(other)
        else:
            # Handle other types or raise an error
            return NotImplemented  # Indicate that this operation is not supported

    def __radd__(self,other):
        """
        + method
        """
        if isinstance(other, CustomString):
            # Concatenate with another MyCustomString instance
            if(self.is_colored and other.is_colored):
                return str(other.left_spaces + other.colored.__str__() + other.right_spaces) + str(self.left_spaces + self.colored.__str__() + self.right_spaces)
            elif(self.is_colored and not other.is_colored):
                return str(other.left_spaces + other.value + other.right_spaces) + str(self.left_spaces + self.colored.__str__() + self.right_spaces)
            elif(not self.is_colored and other.is_colored):
                return str(other.left_spaces + other.colored.__str__() + other.right_spaces) + str(self.left_spaces + self.value + self.right_spaces)
            else:
                return str(other.left_spaces + other.value + other.right_spaces) + str(self.left_spaces + self.value + self.right_spaces)
        elif isinstance(other, str):
            # Concatenate with a standard string
            if(self.is_colored):
                return other + str(self.left_spaces + self.colored.__str__() + self.right_spaces)
            else:
                return other + str(self.left_spaces + self.value + self.right_spaces)
        elif isinstance(other, int):
            # Concatenate with a standard int
            if(self.is_colored):
                return str(other) + str(self.left_spaces + self.colored.__str__() + self.right_spaces)
            else:
                return str(other) + str(self.left_spaces + self.value + self.right_spaces)
        elif isinstance(other, float):
            # Concatenate with a standard float
            if(self.is_colored):
                return str(other) + str(self.left_spaces + self.colored.__str__() + self.right_spaces)
            else:
                return str(other) + str(self.left_spaces + self.value + self.right_spaces)
        elif isinstance(other, list):
            # Concatenate with a standard float
            temp = "[ "
            for i in other:
                temp += str(i) + ", "
            temp = temp[:-2]
            temp += " ]"
            if(self.is_colored):
                return temp + str(self.left_spaces + self.colored.__str__() + self.right_spaces)
            else:
                return str(other) + str(self.left_spaces + self.value + self.right_spaces)
        elif isinstance(other, tuple):
            # Concatenate with a standard float
            temp = "( "
            for i in other:
                temp += str(i) + ", "
            temp = temp[:-2]
            temp += " )"
            if(self.is_colored):
                return temp + str(self.left_spaces + self.colored.__str__() + self.right_spaces)
            else:
                return str(other) + str(self.left_spaces + self.value + self.right_spaces)
        elif isinstance(other, set):
            # Concatenate with a standard float
            temp = "[ "
            other = list(other)
            for i in other:
                temp += str(i) + ", "
            temp = temp[:-2]
            temp += " ]"
            if(self.is_colored):
                return temp + str(self.left_spaces + self.colored.__str__() + self.right_spaces)
            else:
                return str(other) + str(self.left_spaces + self.value + self.right_spaces)
        elif isinstance(other, dict):
            # Concatenate with a standard float
            temp = "{"
            for key in list(other.keys()):
                temp += " [" +str(key)+":"+str(other[key]) + "],"
            temp = temp[:-2]
            temp += "] }"
            if(self.is_colored):
                return temp + str(self.left_spaces + self.colored.__str__() + self.right_spaces)
            else:
                return str(other) + str(self.left_spaces + self.value + self.right_spaces)
        else:
            # Handle other types or raise an error
            return NotImplemented  # Indicate that this operation is not supported

    def __repr__(self):
        """
        for debugging
        """
        if(self.is_colored):
            return f'CustomString(\'{self.left_spaces}\', \'{self.colored}\', \'{self.right_spaces}\')'
        else:
            return self.left_spaces + self.value + self.right_spaces

    def debug(self):
        """
        Print Info
        """
        output = self.c()+"\t"
        red_color = CustomString('Red')
        red_color.define_color('red',self.colored.red,0,0)
        red_number = CustomString(str(self.colored.red))
        red_number.set_pre_spaces(3)
        red_number.fix_spacing()
        green_color = CustomString('Green')
        green_color.define_color('green',0,self.colored.green,0)
        green_number = CustomString(str(self.colored.green))
        green_number.set_pre_spaces(3)
        green_number.fix_spacing()
        blue_color = CustomString('Blue')
        blue_color.define_color('blue',0,0,self.colored.blue)
        blue_number = CustomString(str(self.colored.green))
        blue_number.set_pre_spaces(3)
        blue_number.fix_spacing()
        output += red_color.c()+" "+red_number.c()+"\t"+green_color.c()+" "+green_number.c()+" "+blue_color.c()+" "+blue_number.c()
        print(output)

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

class Benchmark:
    def __init__(self):
        # Start the clock
        self.begin_time = datetime.datetime.now()

        # Weeks
        self.weeks = 0
        self.weeks_text = ''

        # Days
        self.days = 0
        self.days_text = ''

        # Hours
        self.hours = 0
        self.hours_text = ''

        # Minutes
        self.minutes = 0
        self.minutes_text = ''

        # Seconds
        self.seconds = 0
        self.seconds_text = ''

        # Microseconds
        self.microseconds = 0
        self.microseconds_text = 'Microseconds'

        # Total Seconds
        self.total_seconds = 0

        # Did we ever stop the counter?
        self.counter_reset = 0

        # Tracks if we are running or not
        self.boolean_running = True

    def reset(self):
        """
        Resets all the counters
        """
        # Start the clock
        self.begin_time = datetime.datetime.now()

        # Weeks
        self.weeks = 0
        self.weeks_text = ''

        # Days
        self.days = 0
        self.days_text = ''

        # Hours
        self.hours = 0
        self.hours_text = ''

        # Minutes
        self.minutes = 0
        self.minutes_text = ''

        # Seconds
        self.seconds = 0
        self.seconds_text = ''

        # Microseconds
        self.microseconds = 0
        self.microseconds_text = 'Microseconds'

        # Total Seconds
        self.total_seconds = 0

        # Track we reset
        self.counter_reset += 1

        self.boolean_running = True

    def stop(self):
        """
        Stop the benchmark and calculate all the runtime
        """

        # Stop the clock
        self.end_time = datetime.datetime.now()
        self.boolean_running = False
        self.total_seconds = (self.end_time - self.begin_time).seconds
        self.microseconds = (self.end_time - self.begin_time).microseconds

        ans = ''

        # I didn't want changes to total_seconds affecting seconds
        # There has to be a better way to do this
        counter = 0
        while (counter < self.total_seconds):
            counter += 1

        # Makes it it's own number
        convert_seconds = counter

        # Weeks
        weeks = int(convert_seconds // 604800)
        if (weeks == 0):
            pass
        elif (weeks == 1):
            ans += str(weeks) + ' Week '
            self.weeks_text = 'Week'
        else:
            ans += str(weeks) + ' Weeks '
            self.weeks_text = 'Weeks'
        self.set_weeks(weeks)

        convert_seconds = convert_seconds - (weeks * 604800)

        # Days
        days = int(convert_seconds // 86400)
        if (days == 0):
            pass
        elif (days == 1):
            ans += str(days) + ' Day '
            self.days_text = 'Day'
        else:
            ans += str(days) + ' Days '
            self.days_text = 'Days'
        self.set_days(days)

        convert_seconds = convert_seconds - (days * 86400)

        # Hours
        hours = int(convert_seconds // 3600)
        if (hours == 0):
            pass
        elif (hours == 1):
            ans += str(hours) + ' Hour '
            self.hours_text = 'Hour'
        else:
            ans += str(hours) + ' Hours '
            self.hours_text = 'Hours'
        self.set_hours(hours)

        convert_seconds = convert_seconds - (hours * 3600)

        # Minutes
        minutes = int(convert_seconds // 60)
        if (minutes == 0):
            pass
        elif (minutes == 1):
            ans += str(minutes) + ' Minute '
            self.minutes_text = 'Minute'
        else:
            ans += str(minutes) + ' Minutes '
            self.minutes_text = 'Minutes'
        self.set_minutes(minutes)

        convert_seconds = int(convert_seconds - (minutes * 60))

        # Seconds
        if (convert_seconds == 0):
            pass
        elif (convert_seconds == 1):
            ans += str(convert_seconds) + ' Second '
            self.seconds_text = 'Second'
        else:
            ans += str(convert_seconds) + ' Seconds '
            self.seconds_text = 'Seconds'
        self.set_seconds(convert_seconds)

        # Microseconds
        if (self.microseconds == 0):
            pass
        elif (self.microseconds == 1):
            ans += str(self.microseconds) + ' Microsecond'
            self.microseconds_text = 'Microsecond'
        else:
            ans += str(self.microseconds) + ' Microseconds'
            self.microseconds_text = 'Microseconds'

    def end(self):
        """
        Stop the benchmark and calculate all the runtime
        """

        # Stop the clock
        self.end_time = datetime.datetime.now()
        self.boolean_running = False
        self.total_seconds = (self.end_time - self.begin_time).seconds
        self.microseconds = (self.end_time - self.begin_time).microseconds

        ans = ''

        # I didn't want changes to total_seconds affecting seconds
        # There has to be a better way to do this
        counter = 0
        while (counter < self.total_seconds):
            counter += 1

        # Makes it it's own number
        convert_seconds = counter

        # Weeks
        weeks = int(convert_seconds // 604800)
        if (weeks == 0):
            pass
        elif (weeks == 1):
            ans += str(weeks) + ' Week '
            self.weeks_text = 'Week'
        else:
            ans += str(weeks) + ' Weeks '
            self.weeks_text = 'Weeks'
        self.set_weeks(weeks)

        convert_seconds = convert_seconds - (weeks * 604800)

        # Days
        days = int(convert_seconds // 86400)
        if (days == 0):
            pass
        elif (days == 1):
            ans += str(days) + ' Day '
            self.days_text = 'Day'
        else:
            ans += str(days) + ' Days '
            self.days_text = 'Days'
        self.set_days(days)

        convert_seconds = convert_seconds - (days * 86400)

        # Hours
        hours = int(convert_seconds // 3600)
        if (hours == 0):
            pass
        elif (hours == 1):
            ans += str(hours) + ' Hour '
            self.hours_text = 'Hour'
        else:
            ans += str(hours) + ' Hours '
            self.hours_text = 'Hours'
        self.set_hours(hours)

        convert_seconds = convert_seconds - (hours * 3600)

        # Minutes
        minutes = int(convert_seconds // 60)
        if (minutes == 0):
            pass
        elif (minutes == 1):
            ans += str(minutes) + ' Minute '
            self.minutes_text = 'Minute'
        else:
            ans += str(minutes) + ' Minutes '
            self.minutes_text = 'Minutes'
        self.set_minutes(minutes)

        convert_seconds = int(convert_seconds - (minutes * 60))

        # Seconds
        if (convert_seconds == 0):
            pass
        elif (convert_seconds == 1):
            ans += str(convert_seconds) + ' Second '
            self.seconds_text = 'Second'
        else:
            ans += str(convert_seconds) + ' Seconds '
            self.seconds_text = 'Seconds'
        self.set_seconds(convert_seconds)

        # Microseconds
        if (self.microseconds == 0):
            pass
        elif (self.microseconds == 1):
            ans += str(self.microseconds) + ' Microsecond'
            self.microseconds_text = 'Microsecond'
        else:
            ans += str(self.microseconds) + ' Microseconds'
            self.microseconds_text = 'Microseconds'

    def set_microseconds(self, microseconds):
        self.microseconds = microseconds

    def set_weeks(self, weeks):
        self.weeks = weeks

    def set_days(self, days):
        self.days = days

    def set_hours(self, hours):
        self.hours = hours

    def set_minutes(self, minutes):
        self.minutes = minutes

    def set_seconds(self, seconds):
        self.seconds = seconds

    def get_weeks(self):
        return self.weeks

    def get_days(self):
        return self.days

    def get_hours(self):
        return self.hours

    def get_minutes(self):
        return self.minutes

    def get_seconds(self):
        return self.seconds

    def get_microseconds(self):
        return self.microseconds

    def get_weeks_text(self):
        return self.weeks_text

    def get_days_text(self):
        return self.days_text

    def get_hours_text(self):
        return self.hours_text

    def get_minutes_text(self):
        return self.minutes_text

    def get_seconds_text(self):
        return self.seconds_text

    def get_microseconds_text(self):
        return self.microseconds_text

    def get_runtime_seconds(self):
        end_time = datetime.datetime.now()
        return (end_time - self.begin_time).seconds

    def current_benchmark_without_stopping(self):
        """
        Print Current timings
        """
        # See where we currently are
        end_time = datetime.datetime.now()
        total_seconds = (end_time - self.begin_time).seconds
        microseconds = (end_time - self.begin_time).microseconds

        ans = ''

        # I didn't want changes to total_seconds affecting seconds
        # There has to be a better way to do this
        counter = 0
        while (counter < total_seconds):
            counter += 1

        # Makes it it's own number
        convert_seconds = counter

        # Weeks
        weeks = int(convert_seconds // 604800)
        if (weeks == 0):
            pass
        elif (weeks == 1):
            ans += str(weeks) + ' Week '
            weeks_text = 'Week'
        else:
            ans += str(weeks) + ' Weeks '
            weeks_text = 'Weeks'

        convert_seconds = convert_seconds - (weeks * 604800)

        # Days
        days = int(convert_seconds // 86400)
        if (days == 0):
            pass
        elif (days == 1):
            ans += str(days) + ' Day '
            days_text = 'Day'
        else:
            ans += str(days) + ' Days '
            days_text = 'Days'

        convert_seconds = convert_seconds - (days * 86400)

        # Hours
        hours = int(convert_seconds // 3600)
        if (hours == 0):
            pass
        elif (hours == 1):
            ans += str(hours) + ' Hour '
            hours_text = 'Hour'
        else:
            ans += str(hours) + ' Hours '
            hours_text = 'Hours'

        convert_seconds = convert_seconds - (hours * 3600)

        # Minutes
        minutes = int(convert_seconds // 60)
        if (minutes == 0):
            pass
        elif (minutes == 1):
            ans += str(minutes) + ' Minute '
            minutes_text = 'Minute'
        else:
            ans += str(minutes) + ' Minutes '
            minutes_text = 'Minutes'

        convert_seconds = int(convert_seconds - (minutes * 60))

        # Seconds
        if (convert_seconds == 0):
            pass
        elif (convert_seconds == 1):
            ans += str(convert_seconds) + ' Second '
            seconds_text = 'Second'
        else:
            ans += str(convert_seconds) + ' Seconds '
            seconds_text = 'Seconds'

        # Microseconds
        if (microseconds == 0):
            pass
        elif (microseconds == 1):
            ans += str(microseconds) + ' Microsecond'
            microseconds_text = 'Microsecond'
        else:
            ans += str(microseconds) + ' Microseconds'
            microseconds_text = 'Microseconds'

        return ans

    def human_readable_string(self):
        """
        Returns a string of the elapsed time
        """

        ans = ''

        need_one_space = False

        if (self.boolean_running):
            return self.current_benchmark_without_stopping()
        else:
            if (self.weeks > 0):
                ans += str(self.weeks) + ' ' + self.weeks_text + ' '
            if (self.days > 0):
                ans += str(self.days) + ' ' + self.days_text + ' '
            if (self.hours > 0):
                ans += str(self.hours) + ' ' + self.hours_text + ' '
            if (self.minutes > 0):
                ans += str(self.minutes) + ' ' + self.minutes_text + ' '
            if (self.seconds > 0):
                ans += str(self.seconds) + ' ' + self.seconds_text + ' '
            ans += str(self.microseconds) + ' ' + self.microseconds_text
        return ans

    def human_readable_string_without_microseconds(self):
        """
        Returns a string of the elapsed time
        """

        ans = ''

        need_one_space = False

        if (self.boolean_running):
            return self.current_benchmark_without_stopping()
        else:
            if (self.weeks > 0):
                ans += str(self.weeks) + ' ' + self.weeks_text + ' '
            if (self.days > 0):
                ans += str(self.days) + ' ' + self.days_text + ' '
            if (self.hours > 0):
                ans += str(self.hours) + ' ' + self.hours_text + ' '
            if (self.minutes > 0):
                ans += str(self.minutes) + ' ' + self.minutes_text + ' '
            if (self.seconds > 0):
                ans += str(self.seconds) + ' ' + self.seconds_text + ' '
        return ans

    def seconds_to_human_readable(self, seconds, return_type='string'):
        """
        Method to get the difference between times more human readable

        begin_time and end_time need to be datetime.datetime objects

        return_type can be:
             String
             Int (Seconds)
        """
        # If I ever make this a standalone method it'll need these imports
        # import datetime,sys,platform
        # from collections import namedtuple

        if (type(seconds) != type(0)):
            if (return_type == 'string'):
                return "Please call the method 'seconds_to_human_readable' with an integer"
            else:
                return self.get_seconds()
        else:
            # We're good to do calculations
            ans = ''

        # I didn't want changes to total_seconds affecting seconds
        counter = 0
        while (counter < self.total_seconds):
            counter += 1

        total_seconds = counter

        # Weeks
        weeks = int(total_seconds // 604800)
        if (weeks == 0):
            pass
        elif (weeks == 1):
            ans += str(weeks) + ' Week '
        else:
            ans += str(weeks) + ' Weeks '
        self.set_weeks(weeks)

        total_seconds = total_seconds - (weeks * 604800)

        # Days
        days = int(total_seconds // 86400)
        if (days == 0):
            pass
        elif (days == 1):
            ans += str(days) + ' Day '
        else:
            ans += str(days) + ' Days '
        self.set_days(days)

        total_seconds = total_seconds - (days * 86400)

        # Hours
        hours = int(total_seconds // 3600)
        if (hours == 0):
            pass
        elif (hours == 1):
            ans += str(hours) + ' Hour '
        else:
            ans += str(hours) + ' Hours '
        self.set_hours(hours)

        total_seconds = total_seconds - (hours * 3600)

        # Minutes
        minutes = int(total_seconds // 60)
        if (minutes == 0):
            pass
        elif (minutes == 1):
            ans += str(minutes) + ' Minute '
        else:
            ans += str(minutes) + ' Minutes '
        self.set_minutes(minutes)

        total_seconds = int(total_seconds - (minutes * 60))

        # Seconds
        if (total_seconds == 0):
            pass
        elif (total_seconds == 1):
            ans += str(total_seconds) + ' Second '
        else:
            ans += str(total_seconds) + ' Seconds '
        self.set_seconds(total_seconds)

        if (return_type == 'string'):
            if (ans == ''):
                return '0 Seconds'
            else:
                return ans.strip()
        else:
            return self.get_seconds()

class Parse:

    def __init__(self,input_parameter=['-','--']):

        # How do we identify the parameters being passed in?
        self.parameter_flags = []

        # Was the Class Object initialized successfully
        self.validation = False

        if type([]) == type(input_parameter):
            for item in input_parameter:
                self.parameter_flags.append(item)
                self.validation = True
        elif type('') == type(input_parameter):
            if len(input_parameter) > 0:
                self.parameter_flags.append(input_parameter)
                self.validation = True
        else:
            pass

        # Dictionary for holding all the Paramters and their Values
        self.parameters = {}

        # Expectations - what we are expecting to be passed in via commandline
        self.expected_parameters = {}

    #def add_paramter_flags(self,paramter_flags='-'):
    #    """
    #    <paramter_flags>
    #    What string should be used to identify a parameter
    #    '-'
    #    """
    #    self.parameter_flags.append(paramter_flags)

    def add_parameter(self,parameter_type,value,required,hidden,parameter_name):
        """
        <parameter_name>
        Name of the Parameter
        -filename hello.txt

        <parameter_type>
        Type of the Parameter - one of the following:
        string, int, float, list, array, set

        <required>
        Is the Parameter required?
        Boolean

        <hidden>
        If the Parameter is not passed in when it is prompted should the text be hidden?
        Boolean
        """
                                                    
        self.parameters[parameter_name] = Parameter(parameter_type,value,required,hidden,parameter_name,False)

    def set_value(self,parameter_name,value):
        """
        Attempts to set the Value of a Parameter to the Parameter
        """
        if parameter_name in get_parameter_names:
            self.parameters[parameter_name] = self.parameters[parameter_name].set_value(value)
            return True
        else:
            print(" Paramter Name: " + parameter_name + " is not a Parameter")
            return False

    def parse_commandline(self):
        """
        Parse the commandline arguments!
        """
        self.script_file = sys.argv[0]

        previous_item = ''
        save_next_value = False
        for item in sys.argv[1:]:

            if(item[0] == '-' or item[0:1] == '--'):
                parameter = item.strip('-')
                save_next_value = True
            elif(save_next_value):

                if
                
                self.parameters[parameter] = Parameter('string', item.strip('-'),False,False,previous_item,expected)
                save_next_value = False
                if(item[0] == '-' or item[0:1] == '--'):
                    parameter = item.strip('-')
                    save_next_value = True

            previous_item = item.strip('-')

    def add_expectation(self,parameter_name = 'unnamed',datatype = 'string', required = False,hidden = False):
        """
        What do we expect will be added as commandline parameters?
        """
        self.expected_parameters[parameter_name] = Parameter(datatype, None, required, hidden, parameter_name,True)

    def validate_requirements(self):
        """
        Should be called after parse_commandline
        """
        for key in list(self.expected_parameters.keys()):
            if key not in list(self.parameters.keys()) and self.expected_parameters[key].get_required():
                print("Missing: " + key)

                if self.expected_parameters[key].get_hidden():
                    value = getpass.getpass(key + ": ")
                else:
                    value = input(key + ": ")

                try:
                    value = int(value)
                except:
                    pass

                while(self.expected_parameters[key].get_parameter_type() != self.get_value_datatype(value)):

                    print(str(self.expected_parameters[key].get_parameter_type()) + " - " + self.get_value_datatype(value))

                    if self.expected_parameters[key].get_hidden:
                        value = getpass.getpass(key + ": ")
                    else:
                        value = input(key + ": ")

                    try:
                        value = int(value)
                    except:
                        pass

                try:
                    my_datatype = 'string'
                    if(type(value) == type(0)):
                        my_datatype = 'integer'
                except:
                    pass

                # This needs to be better written so the required and hidden fields are correctly passed in
                self.expected_parameters[key] = Parameter(my_datatype, value, self.expected_parameters[key].get_required(), self.expected_parameters[key].get_hidden(), key,expected)

    def get_value_datatype(self,value):
        """
        Used for identifying the datatype of the value passed in
        """
        try:
            test = int(value)
            return 'integer'
        except:
            pass

        try:
            test = float(value)
            return 'float'
        except:
            pass

        if type(value) == type([]):
            return 'list'
        elif type(value) == type({}):
            return 'dictionary'
        elif type(value) == type(complex(1j)):
            return 'complaex'
        elif type(value) == type(tuple(("apple", "orange"))):
            return 'tuple'
        elif type(value) == type(range(1)):
            return 'range'
        elif type(value) == type(set([1,2,3])):
            return 'set'
        elif type(value) == type(frozenset(("apple", "orange"))):
            return 'frozenset'
        elif type(value) == type(False):
            return 'boolean'
        elif type(value) == type(bytes(5)):
            return 'bytes'
        elif type(value) == bytearray(5):
            return 'bytearray'
        elif type(value) == memoryview(bytes(5)):
            return 'memoryview'
        else:
            return 'string'

    def get_parameter_names(self):
        return list(self.parameters.keys())

    def get_class_validation(self):
        return self.validation

    def get_parameter(self,parameter):
        return self.parameters[parameter]

    # Returns the python file being run
    def get_script_file(self):
        return self.script_file

    def display_parameters(self):
        """
        Used for debugging
        """

        for key in list(self.parameters.keys()):
            print(key)
            self.parameters[key].show_parameter()

        for key in list(self.expected_parameters.keys()):
            print(key)
            self.expected_parameters[key].show_parameter()

class Parameter:
    def __init__(self, parameter_type = 'string', value = None, required = False, hidden = False, parameter_name='', expected=False):
        self.parameter_type = parameter_type
        self.required = required
        self.hidden = hidden
        self.expected = expected
        self.value = value
        self.directory = False
        self.absolute_path_to_directory = False
        self.relative_path_to_directory = False
        self.absolute_path_to_file = False
        self.relative_path_to_file = False
        self.parameter_name = parameter_name

        # Initialize Checks
        dir_check = False
        relative_path = False

        this_value = value
        # See if it is a relative file path
        if(type(this_value) != type(None)):
            file_check = os.path.isfile(this_value)
        
            # See if it is an absolute file path
            if(OS_TYPE == 'windows'):
                if(os.path.isfile(os.getcwd() + '\\' + str(this_value))):
                    file_check = True
                elif(file_check):
                    relative_path = True

                # Is it a relative or an absolute directory
                if(os.path.isdir(os.getcwd() + '\\' + str(this_value))):
                    dir_check = True
                elif(os.path.isdir(str(this_value))):
                    dir_check = True
                    relative_path = True

                # Human readable text output
                if(file_check and not relative_path):
                    value_type = "Relative Path to File"
                    self.relative_path_to_file = True
                    self.parameter_type = 'file'
                elif(file_check and relative_path):
                    value_type = "Abosulte Path to File"
                    self.absolute_path_to_file = True
                    self.parameter_type = 'file'
                elif(dir_check and not relative_path):
                    value_type = "Relative Path to Directory"
                    self.relative_path_to_directory = True
                    self.parameter_type = 'directory'
                elif(dir_check and relative_path):
                    value_type = "Absolute Path to Directory"
                    self.absolute_path_to_directory = True
                    self.parameter_type = 'directory'
                else:
                    value_type = "Neither"
            
            # mac or Linux
            else:
                if(os.path.isfile(os.getcwd() + '/' + str(this_value))):
                    file_check = True
                elif(file_check):
                    relative_path = True

                # Is it a relative or an absolute directory
                if(os.path.isdir(os.getcwd() + '/' + str(this_value))):
                    dir_check = True
                elif(os.path.isdir(str(this_value))):
                    dir_check = True
                    relative_path = True

                # Human readable text output
                if(file_check and not relative_path):
                    value_type = "Relative Path to File"
                    self.relative_path_to_file = True
                    self.parameter_type = 'file'
                elif(file_check and relative_path):
                    value_type = "Abosulte Path to File"
                    self.absolute_path_to_file = True
                    self.parameter_type = 'file'
                elif(dir_check and not relative_path):
                    value_type = "Relative Path to Directory"
                    self.relative_path_to_directory = True
                    self.parameter_type = 'directory'
                elif(dir_check and relative_path):
                    value_type = "Absolute Path to Directory"
                    self.absolute_path_to_directory = True
                    self.parameter_type = 'directory'
                else:
                    value_type = "Neither"
        else:
            file_check = False

    # < --- Begin Setters --- >
    def set_value(self,value):
        self.value = value

    def set_parameter_type(self,parameter_type):
        self.parameter_type = parameter_type

    def set_hidden(self,hidden):
        self.hidden = hidden

    def set_required(self,required):
        self.required = required

    def set_parameter_name(self,parameter_name):
        self.parameter_name = parameter_name
    # < ---  End  Setters --- >

    # < --- Begin Getters --- >
    def get_value(self):
        return self.value

    def get_parameter_type(self):
        return self.parameter_type

    def get_hidden(self):
        return self.hidden

    def get_required(self):
        return self.required

    def get_parameter_name(self):
        return self.parameter_name
    # < ---  End  Getters --- >

    def show_parameter(self):
        """
        Displays all the parameters that have been entered
        """
        print("")
        print("Name:\t\t" + self.parameter_name)
        print("Datatype:\t" + self.parameter_type)
        print("Required:\t" + str(self.required))
        print("Hidden:\t\t" + str(self.hidden))
        print("Expected:\t\t" + str(self.expected))
        if(self.hidden):
            print("Value:\t\tHidden Because It's A Password")
        else:
            print("Value:\t\t" + str(self.value))
        print("")

