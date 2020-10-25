#!/usr/bin/env python3

# Import CSV as list of lists
'''
restaurant, category, rating 0-1

list = [[mcdonalds, fast food, 0.2],[torizen, japanese, 0.9]]

rating is 0-1
is multiplier in odds
when voting up or down, change value by 15%

'''
import os
import csv
import random
import jefftadashi_utils as jtu
 
rlist = []

# Read CSV, skipping/saving header row
with open('foulette.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    header_passed = False
    for row in reader:
        if not header_passed:
            header = row # Save first row as header variable
            header_passed = True
        else:
            if row: #ignore empty list items, E.G. empty spaces at end of CSV file
                rlist.append(row)


#Sort list, seems to work simply by 1st element
rlist = sorted(rlist)

#build ordered restaurant list, ordered rating/weights lists (for random choice)
rest_ord_list = []
rate_ord_list = []
for x in rlist:
    rest_ord_list.append(x[0])
    rate_ord_list.append(float(x[2]))

#Make random choice with weights
rchoice = random.choices(population=rest_ord_list, weights=rate_ord_list)

# Print out choice
print ("")
print ("Your restaurant choice is: ", jtu.color.purple, rchoice[0].title(), jtu.color.end, sep="")
print ("")
os.system("say \"" + rchoice[0] + "\"") # " to surround text to ignore speical character issues

while True:
    did_like = input(jtu.color.bold + "Did you like this choice? " +  jtu.color.end + "(Y)es/(N)o/(U)ndecided  -  ").upper()
    if did_like == "Y":
        change_weight = 1.15
        break
    if did_like == "N":
        change_weight = 0.85
        break
    if did_like == "U":
        change_weight = 1
        break

# find rchoice in rlist and make rating/weight change in data
for x in rlist:
    if x[0] == rchoice[0]:
        new_rate = round(float(x[2]) * change_weight, 3)
        print (rchoice[0].title(), "now has rating of", new_rate)
        x[2] = str(new_rate)

# Write new version back to same file
with open('foulette.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for row in rlist:
        writer.writerow(row)
