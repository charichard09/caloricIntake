from selenium import webdriver
import requests, bs4, os, sys, subprocess, get_calories

def daily_calories():
    
    food = {}
    a = 2
    paste_this = []
    current_total = 0
    current_dir = os.getcwd()

    while True:    
        try:
            item, icalories = input("\nEnter food and how many calories or food and 'search' to lookup food? (pizza, 750)\n").split(',')            #to check input correction, could also use if icalories.isdecimal() to return true if string stored is a number
        except ValueError:
            print("    Error: Input should be in the form of 'food, calories'\n")
            continue
        
        # Search online for calories of item and return results then restart loop
        if icalories == " search":
            get_calories.get_calories(item)
            continue

        # TODO: take icalories string and convert to an evaluatable expression if possible i.e. if icalories = "750 * 5"
        try:
            icalories = eval(icalories)
        except TypeError:
            print("    Error: calories must be of integer and expression format.\n")
            continue

        if item in food:                                                                                                                            #If the item already exists, rename the item string to item string 2, etc, etc.
            item = item + str(a)
            a += 1
        food[item] = icalories                                                                                                                      #assign input of icalories to newly created input item in dictonary
        current_total += icalories                                                                                                                  #add input of calories of current item to current_total each iteration to get ongoing tracking of calories

        answer = input("\nYour current calorie intake is " + str(current_total) + ". Are there more items you'd like to input? (y/n)\n")
        if answer == "n":
            print("")
            break
        elif answer == "y":
            continue
        else:
            answer = input("\n      ERROR: You didn't enter y/n. Are there more items you'd like to input? (y/n)\n")
            if answer == "n":
                print("")
                break
            elif answer == "y":
                continue
        
    day = input("What day is it today?\n")
    paste_this.append("\n" + day.center(27 + 6))

    total = 0
    for i, j in food.items():
        paste_this.append(i.ljust(27, '.') + str(j).rjust(7))
        total += int(j)

    paste_this.append("Total daily caloric intake: ".ljust(27, '.') + str(total).rjust(6) + "\n")

    caloric_intake_file = open(current_dir + r"\caloricIntake.txt", "a", encoding="utf8")

    caloric_intake_file.write("\n".join(paste_this))

    caloric_intake_file.close()

    return "\n".join(paste_this)

# Test daily_calories()
#daily_calories()
