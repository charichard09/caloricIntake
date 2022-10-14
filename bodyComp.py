#This program asks the user to input their latest weight, date, and time > stores it in x, y, z variables >
# > creates a well formatted readable string of the data > prints to the user to confirm correct > opens and appends to bodyComp.txt 
# and closes the file 
#Version: 2.1 Date: 04/15/21 Pathc: Editing in "from laptop" branch. Adding ability for program to take cwd and output and edit files and
#                                   folders without the need for the user to manually input directory themselves in source code.
#Version 2.0 Update: Added automatic 7 day/entries and 28 day/entries comparisons from day/entry 1. Will copy bodyComp.txt to pastBodyCompInfo sub-folder and send2trash bodyComp.txt in anticipation for another 18
  

import logging
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
logging.disable(logging.CRITICAL)

import os
import pprint
import re
import shutil
import send2trash

def body_comp():
    logging.debug("Start of Program")
    
    weight_regex = re.compile(r"\d+(\.\d*)?")
    date_regex = re.compile(r"\d+-\d+-\d+")
    weight = input("Please enter your weight: (i.e. 175.56)\n")

    #checking if weight is proper format
    mo_weight_input = weight_regex.search(weight)
    while mo_weight_input == None:
        weight = input("Weight input error. Weight must be a whole or decimal number (i.e. 175.56)\n")
        mo_weight_input = weight_regex.search(weight)

    time = input("\nPlease enter the time recorded: (i.e. 3:15am)\n")
    date = input("\nPlease enter the date: (i.e. 4-1-2021)\n")

    #check if date is proper format
    mo_date_input = date_regex.search(date)
    while mo_date_input == None:
        date = input("Date input error. Date must be in format month-day-year (i.e. 4-1-2021)\n")
        mo_date_input = date_regex.search(date)

    #get current working directory and assign is current_dir
    current_dir = os.getcwd()
    logging.debug("current working directory is: " + current_dir)

    body_comp_file = open(current_dir + r"\bodyComp.txt", "a+")

    body_comp_file.write(weight.ljust(8) + date.ljust(12) + time.rjust(7) + "\n")

    body_comp_file.close()
    logging.debug("Program has just written data into bodyComp and closed.")

    #read the contents of bodyComp to check it against conditions
    body_comp_file = open(current_dir + r"\bodyComp.txt", "r")

    body_comp_content = body_comp_file.readlines()

    body_comp_file.close()
    logging.debug("Program has read all lines of bodyComp and closed: \n" + str(body_comp_content))

    print("Your weight has been recorded. Thank you.")

    #if 7 entries in body_comp_content
    #print("You have made 7 entries, as a progress update you have " + #algorithm to print either gained or loss)
    weekly_count = [7, 14, 21, 28]
    counter = 0
    weight_avg = 0
    end_weight = 0
    start_weight = 0
    
    logging.debug("len(body_comp_content) is " + str(len(body_comp_content)))
    if len(body_comp_content) in weekly_count:
        for line in reversed(body_comp_content):
            logging.debug("Value of line is " + line)
            logging.debug("Value of counter is " + str(counter))
            mo = weight_regex.search(line)
            try:
                weight_avg += float(mo.group())
            except AttributeError: #float() cant convert None, exception to running into newline only line
                continue
            logging.debug(mo.group() + " was added to weight_avg, which is " + str(weight_avg))
            #assign match object weight of last line to end_weight 
            if counter == 0:
                end_weight = mo.group()
                logging.debug("end_weight is " + end_weight + ", while mo.group() when counter == 0 is " + mo.group())
            #assign match object of 7th line from reverse to start_weight, and break loop
            if counter == 6:
                start_weight = mo.group()
                logging.debug("start_weight is, " + start_weight + ", mo.group() is " + mo.group())
                break
            counter += 1
        print("\nYou have made 7 entries, as a progress update, between days 1 and days 7, you differed in " + str(float(end_weight) - float(start_weight)) + " pounds.")
        #At 28 entries, give a 4 week update of day 1 to day 28 >> copy bodyComp
        if len(body_comp_content) == 28:
            logging.debug("Start of 28 days progress update.")
            start_month_string = body_comp_content[0]
            end_month_string = body_comp_content[27]
            logging.debug("start_month_string and end_month_string respectively: " + start_month_string + " " + end_month_string)

            mo1 = weight_regex.search(start_month_string)
            mo2 = weight_regex.search(end_month_string)
            logging.debug("mo1 (weight of entry 1) and mo2 (weight of entry 28) are: " + mo1.group() + " " + mo2.group())

            print("\nYou have made 28 entries, as a rough monthly progress update, between day 1 and day 28, you differed in " + str(float(mo2.group()) - float(mo1.group())) + " pounds.")

            mo3 = date_regex.search(start_month_string)
            mo4 = date_regex.search(end_month_string)
            logging.debug("mo3 (date of body_comp_content[0] and mo4 (date of body_comp_content[27]) are " + mo3.group() + " " + mo4.group() + " respectively.")

            save_month_as = mo3.group() + " - " + mo4.group() 
            logging.debug("save_month_as is " + save_month_as)

            #If \pastBodyCompInfo\ dir doesn't exist, create it.
            if not os.path.isdir(current_dir + r"\pastBodyCompInfo\\"):
                os.mkdir(current_dir + r"\pastBodyCompInfo\\")
            shutil.copy(current_dir + r"\bodyComp.txt", current_dir + r"\pastBodyCompInfo\\" + save_month_as + ".txt")

            #send2trash old file
            send2trash.send2trash(current_dir + r"\bodyComp.txt")