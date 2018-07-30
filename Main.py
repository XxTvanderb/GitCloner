from git import *

logo = """
  _____ _ _    _____ _   
 / ____(_) |  / ____| |                      
| |  __ _| |_| |    | | ___  _ __   ___ _ __
| | |_ | | __| |    | |/ _ \| '_ \ / _ \ '__|
| |__| | | |_| |____| | (_) | | | |  __/ |
 \_____|_|\__|\_____|_|\___/|_| |_|\___|_|"""
print(logo)
vers = "v1.0"
print("By: Talon 'XxTvanderb' Vanderbeken")
print("Version: " + vers)

gitURL = input("Enter the link to the Github Repository: ")
directory = input("Enter directory to clone to: ")
branch = input("Enter the repo's branch ")

repo = Repo.clone_from(
     gitURL, directory,
     branch=branch
)

print("Cloned", gitURL, "into", directory)

