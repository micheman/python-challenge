# # main.py -- for budget

# In this challenge, you are tasked with creating a Python script 
# for analyzing the financial records of your company. 
# You will give a set of financial data called budget_data.csv. 
# The dataset is composed of two columns: Date and Profit/Losses. 
# (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# Your task is to create a Python script that analyzes the records to calculate each of the following:

# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

# As an example, your analysis should look similar to the one below:

#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)

# In addition, your final script should both print the analysis to the terminal 
# and export a text file with the results.

import os
import csv

rowcount = 0
TotalMonths = 0
TotalRevenue = 0.0
lastmonthrevenue = 0.0
thismonthrevenue = 0.0
#
m2mchange = 0.0
m2mchangeCumulative = 0.0
#GI: Greatest Increase in Profits: 
GImonth = ""
GIamount = -1.0
#GD: Greatest Decrease in Profits: 
GDmonth = ""
GDamount = 1.0

#get it working wiith brute force above
# riunnign out of time
#SumOfAverages = 0.0
#GIPdiary = {date: '', amount: 0.0}
#GDPdiary = {date: '', amount: 0.0}

with open("budget_data.csv", 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #
    for row in csvreader: # Loop through the data
        if rowcount > 0: # if 0 skip, to ignore the header
            TotalMonths += 1
            thismonthrevenue = int(row[1])
            TotalRevenue += thismonthrevenue
            if rowcount > 1: #only calc change after first month which is row 1
                m2mchange = thismonthrevenue - lastmonthrevenue
                m2mchangeCumulative += m2mchange
                if m2mchange > 0: # if > 0 this is an increase month
                    if m2mchange > GIamount: #check if its the largest increase thus far
                        GIamount = m2mchange # if so update hte greatest increas amount
                        GImonth = row[0] # and the GI month
                elif m2mchange < 0:
                    if m2mchange < GDamount: #check if its the largest increase thus far
                        GDamount = m2mchange # if so update hte greatest increas amount
                        GDmonth = row[0] # and the GI month
                lastmonthrevenue = thismonthrevenue
            # endif of rowcount > 1
        rowcount += 1
    print(f'')
    print(f'Records processed: {rowcount}', end="\r")
#output results
print("\n")
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:            {TotalMonths}")
print(f"Total Revenue:          ${int(TotalRevenue)}")
print(f"Average Monthly Change: ${int(m2mchangeCumulative/TotalMonths)}")
print(f"Greatest Increase in Profits: {GImonth} ($ {GIamount})")
print(f"Greatest Decrease in Profits: {GDmonth} (${GDamount})")
print("\n")

# Now output stats to file...
budget_data_outFH = open("budget_data_output.txt","w") #open output text file to write to 

budget_data_outFH.write("\n")
budget_data_outFH.write('Financial Analysis\n')
budget_data_outFH.write('----------------------------\n')
budget_data_outFH.write(f'Total Months:            {TotalMonths}\n')
budget_data_outFH.write(f"Total Revenue:          ${int(TotalRevenue)}\n")
budget_data_outFH.write(f"Average Monthly Change: ${int(m2mchangeCumulative/TotalMonths)}\n")
budget_data_outFH.write(f"Greatest Increase in Profits: {GImonth} ($ {GIamount})\n")
budget_data_outFH.write(f"Greatest Decrease in Profits: {GDmonth} (${GDamount})\n")
budget_data_outFH.write(f"\n")

budget_data_outFH.close 
