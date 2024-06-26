from enum import Enum
from restricted_input import r_input
from decimal import Decimal
import datetime
import time as gettime
import colorama as colour
import os
import math

class TimeTypes(Enum):
    SECONDS = 0
    MINUTES = 1
    HOURS = 2
    DAYS = 3
    MONTHS = 4
    YEARS = 5

#ref for date timestamps
#short date and time = :f, long date and time = :F
#long date = :D, short date = :d
#long time = :T, short time = :t
#relative time = :R
class TimeStampFormat(Enum):
    LongDateAndTime = 0
    ShortDateAndTime = 1
    LongDate = 2
    ShortDate = 3
    LongTime = 4
    ShortTime = 5
    RelativeTime = 6

#handles which format we want to use
def ChooseFormat(timeStampFormat: str):
    chosenFormat : str = ''

    if timeStampFormat == TimeStampFormat.LongDateAndTime.name:
        chosenFormat = 'F'
    elif timeStampFormat == TimeStampFormat.ShortDateAndTime.name:
        chosenFormat = 'f'
    elif timeStampFormat == TimeStampFormat.LongDate.name:
        chosenFormat = 'D'
    elif timeStampFormat == TimeStampFormat.ShortDate.name:
        chosenFormat = 'd'
    elif timeStampFormat == TimeStampFormat.LongTime.name:
        chosenFormat = 'T'
    elif timeStampFormat == TimeStampFormat.ShortTime.name:
        chosenFormat = 't'
    elif timeStampFormat == TimeStampFormat.RelativeTime.name:
        chosenFormat = 'R'
    else:
        chosenFormat = 'error'

    print(colour.Fore.WHITE + '\nChosen Format: {}\n'.format(chosenFormat))
    return chosenFormat

#ref for date timestamps
#short date and time = :f, long date and time = :F
#long date = :D, short date = :d
#long time = :T, short time = :t
#relative time = :R

#forms the final timestamp for copying
def FormTimeStamp(seconds : float, chosenFormat: str):
    timeStamp : str = ''

    if seconds == -1:
        print(colour.Fore.RED + 'Invalid Time')
        return
    elif chosenFormat == 'error':
        print(colour.Fore.RED + 'Invalid Format')
        return
    
    timeStamp = '<t:{}:{}>'.format(math.trunc(seconds), chosenFormat)
    return timeStamp

#ensures user doesnt input something invalid
def CheckMonthAndDay(month : int, day : int):
    isCorrect : bool = False
    if day < 1:
        isCorrect = False
        print(colour.Fore.RED + 'You inputted no days.')
    elif (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and day > 31:
        isCorrect = False
        print(colour.Fore.RED + 'You inputted {} when this month ({}) has less than that date.'.format(day, month))
    elif month == 2 and day > 27:
        isCorrect = False
        print(colour.Fore.RED + 'You inputted {} when this month ({}) has less than that date.'.format(day, month))
    elif (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
        isCorrect = False
        print(colour.Fore.RED + 'You inputted {} when this month ({}) has less than that date.'.format(day, month))
    else:
        isCorrect = True

    return isCorrect

def ClearTerminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    #appVersion, change accordingly
    appVersion : str = '1.1.0'
    print(colour.Fore.YELLOW + 'Discord Date and Time Converter\nCreated by YellowySmile979\nVersion {}\n'.format(appVersion))

def Main():
    #appVersion, change accordingly
    # appVersion : str = '1.1.0'
    # print(colour.Fore.YELLOW + 'Discord Date and Time Converter\nCreated by YellowySmile979\nVersion {}\n'.format(appVersion))
    ClearTerminal()

    print(colour.Fore.WHITE + '\nWelcome! To use, firstly, please choose your format.')
    print(colour.Fore.LIGHTBLUE_EX + '\nLong Date and Time: 0\nShort Date and Time: 1\nLong Date: 2\nShort Date: 3\nLong Time: 4\nShort Time: 5\nRelative Time: 6\n')
    finalisedTimeStamp : str = ''

    chosenFormat = float(r_input(colour.Fore.WHITE + 'Format: ', 'integer'))
    
    time : float = 0.0
    time = Decimal(time)

    #ensures that the chosen format is actually something within the bounds
    if float(chosenFormat) > 6:
        print(colour.Fore.RED + 'That is NOT a valid number')
        return
    elif float(chosenFormat) < 0:
        print(colour.Fore.RED + 'That is NOT a valid number')
        return
    
    ClearTerminal()
    format : str = ChooseFormat(TimeStampFormat(chosenFormat).name)

    #inputs for the time and day
    print(colour.Fore.LIGHTBLUE_EX + '\nNow, please input the values according to the displayed text.\n')
    year : int = int(r_input(colour.Fore.WHITE + 'Year: ', 'integer'))
    month : int = int(r_input(colour.Fore.WHITE + 'Month: ', 'integer'))
    day : int = int(r_input(colour.Fore.WHITE + 'Day: ', 'integer'))
    hour : int = int(r_input(colour.Fore.WHITE + 'Hour (24-hour): ', 'integer'))
    minute : int = int(r_input(colour.Fore.WHITE + 'Minute(s): ', 'integer'))

    #checks all these cases to ensure that the user inputs an actual valid date
    if year < 1970:
        print(colour.Fore.RED + 'The date cannot be less than 1970!')
        return
    elif year == 1970 and month == 1 and day == 1 and hour < 8:
        print(colour.Fore.RED + 'The date cannot be less than the Unix epoch!')
        return
    elif month > 12 or month < 1 or hour > 23 or minute > 59:
        print(colour.Fore.RED + 'You inputted a month greater than 12 or lesser than 1, or an hour greater than 23 (24:00 is 00:00), or minute(s) greater than 59')
        return
    elif CheckMonthAndDay(month, day) == False:
        return
    else:
        date = datetime.datetime(year, month, day, hour, minute)
        time = gettime.mktime(date.timetuple())
        #print(time)

    #forms the final timestamp for the user to copy and paste
    finalisedTimeStamp = FormTimeStamp(time, format)
    
    ClearTerminal()
    print(colour.Fore.WHITE + '\nFormat: {}\nGiven Date and Time: {}'.format(format, date))
    print(colour.Fore.LIGHTBLUE_EX + 'Highlight the text in the "<>" including "<>": ' + colour.Fore.WHITE + '{}'.format(finalisedTimeStamp))
    
Main()
#gettime.sleep(5)
gettime.sleep(10)