# FinalProject.py (programmed by Kurt Colonia). Serves as the "Main" class of the program.

# import for used packages and user-made classes
import os
import InputValidation
import Options

print("\nFinal Project: Reservation System\nBy Colonia, Kurt Robin P.\n2BSIT-2\n")

# default value, sets the header values for each column in reservations.txt
header = "Date|Time|Name|Adults|Children"

if os.path.exists("reservations.txt"):
      print("Reservations Record exists. Opening Reservations.")
      if os.stat("reservations.txt").st_size == 0:
            resFile = open("reservations.txt", "w")
            resFile.writelines(header)
            resFile.close()
      runProgram = True
else:
      print("Reservations Record not found.")
      while True:
            makeFileInput = input("Would you like to create a new Reservations Record file? [ Y / N ]: ").upper()
            match makeFileInput:
                  case "Y":
                        resFile = open("reservations.txt", "w")
                        resFile.writelines(header)
                        resFile.close()
                        runProgram = True
                        break
                  case "N":
                        print("No file created. Exiting Program")
                        runProgram = False
                        break
                  case _:
                        print("Input Invalid. Please enter either Y or N.")

while runProgram:

      print("\nRESTAURANT RESERVATION SYSTEM\n\n"
            "System Menu\n\n"
            "a. View all Reservations\n"
            "b. Make Reservation\n"
            "c. Delete Reservation\n"
            "d. Generate Report\n"
            "e. Exit\n")

      menuInput = InputValidation.inputString("Please enter your choice: ").lower()

      match menuInput:
            case "a":
                  print()
                  Options.viewRes()
            case "b":
                  print()
                  Options.makeRes()
            case "c":
                  Options.delRes()
            case "d":
                  print()
                  Options.genReport()
            case "e":
                  print("\nThank you!")
                  runProgram = False
            case _:
                  print("Invalid input. Please only choose from letters A to E")

# Programmed by Kurt Colonia, 2BSIT-2 A.Y. 2022-2023