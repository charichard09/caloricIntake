#This program reads caloricIntake.txt and using a regex finds the 7 last appended "Total daily caloric intake:    x" strings, reads the integer of "x" and
#returns a sum to give the total weekly caloric intake. Once weekly caloric intake is calculated and printed to caloricIntake file, script will 
#copy caloricIntake > rename it "caloricIntake of week monthdayyear" > paste it in folder pastWeeklyCaloricIntake > then delete old caloricIntake for the next week  
#Version: 1.0 Date: 

import shutil
import send2trash
import re
import os

def weekly_caloric_intake():
    current_dir = os.getcwd()
    all_total_calories_regex = re.compile(r"(Total\sdaily\scaloric\sintake:\s*)(\d+)", re.IGNORECASE)

    caloric_intake_file = open(current_dir + r"\caloricIntake.txt", "r+", encoding="utf8")   
    #CAREFUL: r+ argument allows read and write. Through order of operations  
    #we are reading FIRST from the initial file positin of the beginning of the file to the end of  the file,   
    #THEN when the file position is at the end of the file, writing to the file, thus simulating appending. Without reading FIRST, you will write OVER your text file. 
    
    #calculate total weekly calories
    caloric_intake_content = caloric_intake_file.read()                                                                                                 
                                                                                                                                                        
    all_total_calories_list = all_total_calories_regex.findall(caloric_intake_content)

    weekly_calories = 0

    for i in all_total_calories_list:
        weekly_calories += int(i[1])

    #format weekly calories string to append to end of caloricIntake.txt
    date = input("What is this the week of? (i.e. 3-11 - 3-17)\n")

    #   Checking calories against goal
    goal = ""
    if (weekly_calories - 17500) > -3500:
        goal = " under my goal. You got this this week! I know you can do it!\n"
    elif (weekly_calories - 17500) < -3500:
        goal = " over my goal. Great Job!\n"
    elif (weekly_calories - 17500) == -3500:
        goal = ". right on the money! Wow!\n"

    weekly_calories_string = ("\nWeekly caloric intake for the week of " + date + " is:\n" + str(weekly_calories) + "\nOut of a 17500 estimated caloric intake,\nI want to be -3500 calories. This week I am " + str(weekly_calories - 17500) + " calories" + goal)

    #   Check if everything looks correct
    print(caloric_intake_content + weekly_calories_string)
    answer = input("Does everything look correct? (y\\n)\n")

    if answer == "y":
        caloric_intake_file.write(weekly_calories_string)

    caloric_intake_file.close()   

    #Todo: after writing to caloricIntake.txt, rename it "caloricIntake of week (date variable).txt" and paste it in folder pastWeeklyCaloricIntake > then delete old caloricIntake for the next week  
    if answer == "y":
        #check if \pastWeeklyCaloricIntake directory exists, if not then make \pastWeeklyCaloricIntake
        if not os.path.isdir(current_dir + r"\pastWeeklyCaloricIntake\\"):
            os.mkdir(current_dir + r"\pastWeeklyCaloricIntake\\")

        #copy caloricIntake.txt to /pastWeeklyCaloricIntake as "caloricIntake" + date
        shutil.copy(current_dir + r"\caloricIntake.txt", (current_dir + r"\pastWeeklyCaloricIntake\\" + date + ".txt"))

    #send2trash caloricIntake.txt
        send2trash.send2trash(current_dir + r"\caloricIntake.txt")

    return 
