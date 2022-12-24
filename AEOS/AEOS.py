import os
import psutil
import platform
import random
import time

#username = 1
#password = 1

adminUsername = "ILoveNasa"
adminPassword = "ILoveSpaceX"
adminLogIn = [adminUsername, adminPassword]

while True:
  username = input("Set Username: ")
  password = input("Set Password: ")
  while True:
    for i in range(100):
      print("")
    usernameLogIn = input("Username: ")
    passwordLogIn = input("Password: ")
    if usernameLogIn and passwordLogIn != username and password:
      print("Invalid username or Password, try again.")
    elif usernameLogIn == "" or passwordLogIn == "":
      print("You need something on both.")
    elif usernameLogIn == username and passwordLogIn == password and password or "ILoveNasa" and "ILoveSpaceX":
      print("Write '---help' for working syntax")
      while True:
        print("--------------------")
        syntax = input("What would you like to do: ")
        syntax.lower()
        if syntax == "--about":
          print("AEOS v0.1, Alpha, open Access"
                "AEOS is a primitive operating system on par with the DOS operating system\n"
                "(the first version of windows) but instead of being written in C/C++ it is written in Python.\n"
                "It is still a work in progress and I would love some feedback.\n")
        if syntax == "--help":
          print("Valid syntax:\n"
                "--about: Tells about AEOS.\n"
                "rbt\n"
                "exit\n"
                "clr\n"
                "settings\n"
                "sysinfo\n"
                "update\n"
                "")
        if syntax == "rbt":
          break
        if syntax == "exit":
          exit()
        if syntax == "clr":
          for i in range(50):
            print("")
        if syntax == "settings":
          print("Valid syntax:\n"
                "change username\n"
                "change password\n"
                "shw username\n"
                "shw password\n")
          while True:
            syntax = input("What settings: ")

            if syntax == "change username":
              print("Type 'exit' to cancel Username change.")
              while True:
                print("--------------------")
                newUsername = str(input("What username would you like to change to: "))

                if newUsername == "exit":
                  break
                newUsernameConfirm = input("Please input your username again to confirm: ")

                if newUsername == newUsernameConfirm:
                  username = newUsername
                  print("Username change successful!")
                  break
                elif newUsername != newUsernameConfirm:
                  print("Username change failed")

            elif syntax == "change psswrd":
              while True:
                print("--------------------")
                print("Type 'exit' to cancel Password change.")
                newPassword = str(input("What password do you want to change to: "))

                if newPassword == "exit":
                  break
                newPasswordConfirm = input("Please input your username again to confirm: ")

                if newPassword == newPasswordConfirm:
                  password = newPassword
                  print("Password change successful!")
                  break

                elif newPassword != newPasswordConfirm:
                  print("Password change failed")
            elif syntax == "shw username":
              while True:
                syntax = input("Are you sure. It could show your username to people you wouldn't like to show (Y/N): ")
                syntax.lower()
                if syntax == "y":
                  print(username)
                  break
                elif syntax == "n":
                  print("Didn't show your username.")
                  break
                else:
                  print("Invalid input.")
                  print("--------------------")

            elif syntax == "shw password":
              while True:
                syntax = input("Are you sure. It could show your password to people you wouldn't like to show (Y/N): ")
                syntax.lower()
                if syntax == "y":
                  print(password)
                  break
                elif syntax == "n":
                  print("Didn't show your password.")
                  break
                else:
                  print("Invalid input.")
                  print("--------------------")



            elif syntax == "exit":
              break
        if syntax == "sysinfo":
          print("---------------------")
          print("System info:")
          print(f"Computer network name: {platform.node()}")
          print(f"Machine type: {platform.machine()}")
          print(f"Processor type: {platform.processor()}")
          print(f"Platform type: {platform.platform()}")
          print(f"Operating system: {platform.system()}")
          print(f"Operating system release: {platform.release()}")
          print(f"Operating system version: {platform.version()}")
          print("---------------------")
          print("CPU cores:")
          print(f"Number of physical cores: {psutil.cpu_count(logical=False)}")
          print(f"Number of logical cores: {psutil.cpu_count(logical=True)}")
          print("---------------------")
          print("CPU frequency:")
          print(f"Current CPU frequency: {psutil.cpu_freq().current}")
          print(f"Min CPU frequency: {psutil.cpu_freq().min}")
          print(f"Max CPU frequency: {psutil.cpu_freq().max}")
          print("---------------------")
          print("RAM info:")
          print(f"Total RAM installed: {round(psutil.virtual_memory().total / 1000000000, 2)} GB")
          print(f"Available RAM: {round(psutil.virtual_memory().available / 1000000000, 2)} GB")
          print(f"Used RAM: {round(psutil.virtual_memory().used / 1000000000, 2)} GB")
          print(f"RAM usage: {psutil.virtual_memory().percent}%")

        if syntax == "update":
          print("Searching for updates")
          time.sleep(2)
          updateTime = 0
          for i in range(100):

            failProb = random.randint(1, 1000)
            waitTime = random.randint(0, 1)
            updateTime += 1
            time.sleep(waitTime)

            failureReasons = ["Error51: Unknown failure", "Error52: Failed to download all files", "Error53: Failed to fetch all downloaded files", "Error54: Failed to backup files", "Error55: Failed to implement files", "Error56: Failed to copy new files"]
            print("\033[92m", end="\r")
            print(updateTime,"%", end="\r")

            if failProb == 100:

              print('\033[91m')
              print("Update failed.")
              print(random.choice(failureReasons))
              print('\33[37m')
              break
            if updateTime == 100:
              print("Update complete")
              print('\33[37m')
              break



        else:
          print("Invalid syntax")
