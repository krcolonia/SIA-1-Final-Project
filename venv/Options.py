# Options.py (programmed by Kurt Colonia). Serves as the class that holds all functions for each option in Main Menu

# import for Input Validation class
import InputValidation

# Initialization of variables to be used in functions
adultArr = []
childArr = []
adultSubtotal = 0
childSubtotal = 0

# Functions for each option
def viewRes():
    resFile = open("reservations.txt", "r")
    resLines = resFile.readlines()
    if len(resLines) < 2:
        print("Cannot view records. File is empty!")
    else:
        resFile.seek(0)
        for count, line in enumerate(resLines):
            resData = line.strip().split("|")
            if count == 0:
                # executed if reading Table Header
                print("#".ljust(8) + resData[0].ljust(20) + resData[1].ljust(16) + resData[2].ljust(20) + resData[3].center(12) + resData[4].center(12))
            else:
                print("{}".format(str(count)).ljust(8) + resData[0].ljust(20) + resData[1].ljust(16) + resData[2].ljust(20) + resData[3].center(12) + resData[4].center(12))
        resFile.close()

def makeRes():
    resFile = open("reservations.txt", "a+")
    resFile.seek(0)
    date = InputValidation.inputDate("Date: ")
    time = InputValidation.inputTime("Time: ")
    name = InputValidation.inputString("Name: ")
    validRes = False
    while not validRes:
        numAdults = InputValidation.inputInt("No. of Adults: ")
        numChild = InputValidation.inputInt("No. of Children: ")
        if int(numAdults + numChild) < 1:
            print("Please enter at least 1 person in your reservation.")
        else:
            validRes = True
    resFile.writelines("{}|{}|{}|{}|{}\n".format(date, time, name, numAdults, numChild))
    resFile.close()

def delRes():
    resFile = open("reservations.txt", "r+")
    resLines = resFile.readlines()
    resFile.seek(0)
    if len(resLines) == 1:
        print("\nReservations list is empty. Cannot continue with DELETE function!")
    else:
        resFile.truncate()
        while True:
            print()
            resFile.seek(0)
            for count, line in enumerate(resLines):
                resData = line.strip().split("|")
                if count == 0:
                    # executed if reading Table Header
                    print("#".ljust(8) + resData[0].ljust(20) + resData[1].ljust(16) + resData[2].ljust(20) + resData[
                        3].center(12) + resData[4].center(12))
                else:
                    # executed if reading Table Data
                    print("{}".format(str(count)).ljust(8) + resData[0].ljust(20) + resData[1].ljust(16) + resData[2].ljust(
                        20) + resData[3].center(12) + resData[4].center(12))
            lineToDel = InputValidation.inputInt("\nPlease enter the reservation to be deleted [1-{}]: ".format(len(resLines)-1))
            if int(lineToDel) < 1:
                print("Please only enter positive values")
            elif int(lineToDel) >= len(resLines):
                print("Please only enter positive values that are less than or equal to {}".format(len(resLines)-1))
            else:
                break
        for lineNum, line in enumerate(resLines):
            if lineNum not in [int(lineToDel)]:
                resFile.write(line)
        resFile.close()

def genReport():
    resFile = open("reservations.txt")
    resFile.seek(0)
    resLines = resFile.readlines()

    grandTotal = 0

    for count, line in enumerate(resLines):
        resData = line.strip().split("|")
        if count == 0:
            adultTotalNum = 0
            childTotalNum = 0
            adultArr = []
            childArr = []
        else:
            adultArr.append(int(resData[3]))
            childArr.append(int(resData[4]))

            adultTotalNum += int(resData[3])
            childTotalNum += int(resData[4])
    resFile.seek(0)
    repFile = open("report.txt", "w")
    repFile.seek(0)
    repFile.writelines("REPORT\n".rjust(59))
    for count, line in enumerate(resLines):
        resData = line.strip().split("|")

        if count == 0:
            subtotal = [None]
            # executed if reading Table Header
            repFile.writelines("#".ljust(8) + resData[0].ljust(20) + resData[1].ljust(16) + resData[2].ljust(20) + resData[3].center(12) + resData[4].center(12) + "\tSubtotal\n")
        else:
            # executed if reading Table Data
            adultSubtotal = int(resData[3]) * 500
            childSubtotal = int(resData[4]) * 300
            subtotal += [int(adultSubtotal + childSubtotal)]

            nameLength = len(resData[2])
            repFile.writelines("{}".format(str(count)).ljust(8) + resData[0].ljust(20) + resData[1].ljust(16) + resData[2].ljust(20) + resData[3].center(12) + resData[4].center(12) + "\t{:.2f}\n".format(subtotal[count]))
            grandTotal += subtotal[count]

    repFile.writelines(
        "\nTotal Number of Adults: {}\nTotal Number of Children: {}\nGrand Total: PHP {:.2f}".format(adultTotalNum,
                                                                                                       childTotalNum,
                                                                                                       grandTotal))

    repFile.writelines("\n\n_______________________________________________ nothing follows _______________________________________________")

    repFile.close()
    resFile.close()

    print("Report Generated! Please see report.txt for full Reservations Report.")

# Programmed by Kurt Colonia, 2BSIT-2 A.Y. 2022-2023