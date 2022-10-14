
#!python
#Write a program that prompts the user if they are inputting daily or weekly calories. If weekly call function weekly, if daily call function daily. 
#Both of which input total calories per given, day or week, adds them, and in the case of week, subtracts them from estimated caloric intake (17500), compares it to weekly caloric intake goal (14500), and prints that in a format to be pasted to a word doc.
#Version: 2.2 Date: 10/04/21 Patch: added ability to search for food and return top 10 calorie results
#Version: 2.1 Date: 08/07/21 Patch: added ability to allow basic arithmetic in dailyCaloricIntake following food name using the eval() function
#Version: 2.0 Date: 04/02/21 Patch: made more universally user friendly.
#version: 1.9 Date: 03/24/21 Patch: added import of weeklyCaloricIntake.py for new weekly_caloric_intake() that calculates weekly caloric intake > appends to caloricIntake.txt > copies caloricIntake.txt as date and pastes
#                                   into folder ./pastWeeklyCaloricIntake > sends caloricIntake.txt to trash for the next week.
#                                   pip freeze: pyperclip==1.8.2, Send2Trash==1.5.0
#version: 1.8 Date: 03/17/21 Patch: added read/write capabilities.
#version: 1.7 Date: 02/28/21 Patch: added current total caloric intake as the user is inputting daily caloric intake
#version: 1.6 Date: 02/27/21 Patch: added ability to paste daily total when finished
#version: 1.5 Date: 02/25/21 Patch: added pyperclip library which automatically copies daily and weekly calories to clipboard to be pasted.      
#version: 1.0 Date: 02/21

from selenium import webdriver
import weeklyCaloricIntake, shutil, send2trash, re
import dailyCaloricIntake, requests, bs4, os, sys, subprocess, get_calories
import bodyComp, pprint


while True:
    response = input("""What you would like to do?
    1. Input daily calories.
    2. Find out weekly calories.
    3. Input daily weigh in. 
    
    : """)
    if not response.isdigit():
        print("\n       ERROR: Please enter the number of the option and press ENTER.\n")
        continue

    #responses
    if response == "1":
        x = dailyCaloricIntake.daily_calories()
        print(x)
    elif response == "2":
        weeklyCaloricIntake.weekly_caloric_intake()                                                                                 
    elif response == "3":
        bodyComp.body_comp()
    else:                                                                                                                                     
        print("\n         ERROR: Response must be one of the numbered options listed.\n")
        continue

    #asks the user if eveything looks correct, if yes, exits program, if no, restarts program from the beginning
    print('\nIs there anything else you\'d like to do? (y/n)')                                                                   
    answer = input()                                                                                                             
    if (answer in ['yes', 'y', 'yeah', 'yup', 'yah']):
        print("")
        continue
    elif (answer in ['n', 'no', 'nope', 'nadda', 'nah']):
        print("\nThank you and have a great day!")
        break
    else:
        print('That is not a correct response. Program will now restart.')
        continue
