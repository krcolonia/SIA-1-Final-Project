
# import for RegEx package
import re

def inputString(title):
    validStr = False
    while not validStr:
        strInput = input(title)
        if bool(re.search("[A-Za-z\\.\s]+", strInput)) and (strInput.isspace() == False):
            validStr = True
        else:
            print("Input invalid. Please only enter alphabetic values.")
    return strInput

def inputInt(title):
    validInt = False
    while not validInt:
        intInput = input(title)
        if intInput.isdigit() and (int(intInput) >= 0):
            validInt = True
        else:
            print("Input invalid. Please enter only a valid number.")
    return intInput


def inputTime(title):
    validTime = False
    while not validTime:
        time = input(title)
        if bool(re.search("^(1[0-2]|0?[1-9]):[0-5][0-9](A|P|a|p)(M|m)$", time)):
            validTime = True
        else:
            print("Input invalid. Please only enter a valid time.")
    return time

def inputDate(title):
    validDate = False
    while not validDate:
        date = input(title)
        if bool(re.search("^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (([0-9])|([0-2][0-9])|([3][0-1]))\, \d{4}$", date)):
            validDate = True
        else:
            print("Input invalid. Please use this format in inputing your date: Jan 1, 2000")
    return date

# Programmed by Kurt Colonia, 2BSIT-2 A.Y. 2022-2023