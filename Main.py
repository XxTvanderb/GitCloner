print("   _____ _ _    _____ _                       ")
print("  / ____(_) |  / ____| |                      ")
print(" | |  __ _| |_| |    | | ___  _ __   ___ _ __ ")
print(" | | |_ | | __| |    | |/ _ \| '_ \ / _ \ '__|")
print(" | |__| | | |_| |____| | (_) | | | |  __/ |   ")
print("  \_____|_|\__|\_____|_|\___/|_| |_|\___|_|  ")
print("\n")



vers = "v1.0"
print("By: Talon 'XxTvanderb' Vanderbeken")
print("Version: " + vers)

gitURL = input("Enter the link to the Github Repository: ")
directory = input("Eter directory to clone to: ")
import os
dire = directory
andAnd= " && "
url = gitURL
cloneC = "sudo git clone "
cd = "cd "
com = cd + andAnd + cd + dire + andAnd + cloneC + url
os.system(com)

    
                    


               

    
