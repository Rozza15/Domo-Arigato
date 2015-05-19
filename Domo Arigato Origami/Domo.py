import os
import datetime
"""
Domo.py, a solution to the Unit 3 SAC prototype solution Outcome 2 2014
    Copyright (C) 2015  Rory Buchanan

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    For a copy of the GNU General Public License, see <http://www.gnu.org/licenses/>.
    
    Email me at: rbuchanan.1997@gmail.com

THIS IS AN EDUCATIONAL PROGRAM.
"""
print("""Domo.py  Copyright (C) 2015  Rory Buchanan
    This program comes with ABSOLUTELY NO WARRANTY; for details see source""")
input("")
"""
Domo Arigato Origami
Instruction sessions: Discount of 20% if 5+ booked
Discount 10% if $50 of supplies bought
"""
pricefile = 'Cost_of_Lesson.txt'
ordersfile = 'Order_Receipts.txt'


def validate(n): #this is the validate function
    test_1 = 0 #test_1 is just used to control the while loop
    while test_1 is 0:
        try: float(n) #this checks whether the input can be a float
        except ValueError: #if it can't, it will return 0
            return 0 #leading to the loop repeating
        else:
            test_1 = 1 #otherwise, the program will continue
            return 1


def changeprice(): #This function changes the number stored in the price document
    mx = 0
    while mx is 0:
        with open(pricefile,'w') as f:
            newprice = input("Please enter the price per lesson: ($) ")
            if validate(newprice) is 0: #Just checking whther it is a floatable number
                print("Invalid input. Please enter the new price. Remember to leave out any special characters and write it in numbers only.")
            else:
                f.write(newprice) #This will write the new price to the price document
                mx = 1

def cost(): #This reads the price doc and prints the value (ie the cost of a lesson)
    c = 0
    while c is 0:
        with open(pricefile,'r') as f:
            price = f.readline()
            if validate(price) is 0: #If the value in the price doc is not floatable
                changeprice() #It will prompt you to input a reasonable value and then will recheck
            else:
                print("$",price,"per lesson") #And will print it
                c = 1

def booking(): #This is the function to book a lesson and pay for things and then write it to the order history doc
    with open(pricefile,'r') as f:
            price = f.readline() #This finds the price as string in the price doc
            prise = float(price) #This declares the price as a workable float
    name = input("Name? ") #Sets the name of the booker
    my = 0
    while my is 0:
        numlessons_str = input("Number of lessons? ") #This gets the number of lessons as a string
        if validate(numlessons_str) is 0: #This makes sure the input is in fact a number
            print("Value Error")
        else:
            numlessons = float(numlessons_str) #This floats the number
            my = 1
    if int(numlessons) > 1: #This checks if there is more than 1 lesson and asks then for the frequency
        freq = input("How often would you like your lessons? ") #Then sets it as a string
    date = input("When would you like your first/only lesson to be booked for? ") #Just gets the date as a string
    while my is 1:
        costpur_str = input("Cost of additional purchases ($): ") #This is the input for the extra costs
        if validate(costpur_str) is 0: #This checks as usual whether it is a number
            print("Value Error")
        else:
            my = 2
            costpur = float(costpur_str) #Then it is floated
            if numlessons < 5:
                if costpur >= 50.0:
                    totalowepur = costpur * 0.9 #This means that they get a 10% discount if they spend $50 or more
                else:
                    totalowepur = costpur
            else:
                totalowepur = costpur
    if numlessons >= 5: #This checks whether the customer is eligible for the 20% discount for purchasing 5 or more lessons at a time
        costless = (numlessons * prise) * 0.8 #If so, it calculates the price based on the value prise from the price doc, and then gives a 20% discount
    else:
        costless = numlessons * prise #Otherwise it just multiplies the number of lessons by the price per lesson
    totalowe = totalowepur + costless #This is adding the two costs together to find the total price of the transaction
    print("Name",name) #
    print("Number of lessons",numlessons) #
    print("Date of first/only lesson",date) #
    if int(numlessons) > 1: #
        print("Frequency of lessons",freq) # THESE PRINT THE INFO GIVEN
    print("Cost of Purchases $",totalowepur) #
    print("Cost of lessons $",costless) #
    print("Total Owing $",totalowe) #
    with open(ordersfile,'a') as f: #These write the info given to the orderhistory doc
        f.write(' {}\n '.format(datetime.date.today()))
        f.write('Name: ')
        f.write(name)
        f.write('\n ')
        f.write(str(int(numlessons)))
        f.write(' Lessons')
        f.write('\n Date of Lesson(s): ')
        f.write(date)
        if int(numlessons) > 1:
            f.write('\n Frequency of lessons: ')
            f.write(freq)
        f.write('\n Cost of Purchases: $')
        f.write(str(totalowepur))
        f.write('\n Cost of Lessons: $')
        f.write(str(costless))
        f.write('\n Total Owing: $')
        f.write(str(totalowe))
        f.write('\n')
        f.write('\n')

def transfunc(): #This means that if the function stoops for whatever reason, it can be restarted by typing in transfunc()
    cost() #This runs the cost function immediately
    mm = 0
    while mm is 0:
        yn = input("Is this the correct price? (Y/N) ") #This confirms the price
        if yn is "n":
            changeprice()
            cost()
        elif yn is "N":
            changeprice()
            cost()
        else:
            mm = 1
    while mm is 1:
        yn = input("Would you like to make a Transaction? (Y/N) ") #This asks whether a transaction will be taking place
        if yn is "y":
            booking()
        elif yn is "Y":
            booking()
        else:
            mm = 2
    exit(1)

mr = 0
while mr is 0:
    if not os.path.isfile(pricefile): #This checks whether there is a price document, and, if there isn't, makes one
        with open(pricefile,'w') as f:
            f.write('') #This makes the price file
        changeprice()
    else:
        mr = 1 #Thus endeth the loop

transfunc() #This starts the process straight away
