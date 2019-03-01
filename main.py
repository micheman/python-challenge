# # main.py -- for election
# In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. 
# (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one,
#  but unfortunately, his concentration isn't what it used to be.)

# You will be give a set of poll data called election_data.csv. 
# The dataset is composed of three columns: Voter ID, County, and Candidate.
#  Your task is to create a Python script that 
# analyzes the votes and calculates each of the following:

# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.


# As an example, your analysis should look similar to the one below:

#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------

# In addition, your final script should both print the analysis to the terminal 
# and export a text file with the results.

# MM Question: Was there any voter fraud???

import os
import csv

with open('election_data.csv', 'r') as csvfile:

# Split the data on commas

# this is crazy but can you believ that without an indented block here...
# the .csv file I just opened gets closed!!!
    csvreader = csv.reader(csvfile, delimiter=',')

    rowcount = 0
    electionary = {}
    for row in csvreader: # Loop through the data
        # The dataset is composed of three columns: Voter ID, County, and Candidate.
        candidate = row[2]
        if candidate != "Candidate": #Skip the first row Candidate = the header
            if candidate in electionary:
                electionary[candidate] += 1
            else:
                electionary[candidate] = 1
                print(f'Adding candidate: {candidate} in electionary')
                print(f"Row # {rowcount}: Row Data--> {row}")
            rowcount += 1
            print(f'Records processed: {rowcount}', end="\r")
            #
            #remnants of test code...
            # if rowcount > 20:
            #    break
            #print(f'The results thus far are...')
            #print(electionary)
# now that we are done readith the .csv, is it safe to
#come out of the indented code block??

print('') # move on to the next line and add a space

# Now output the stats...
# totalvotes = 0
ElecRsltFH = open("Election_Results.txt","w") #open output text file to write to 

#this was test code... output some results to file and screen...
#print(f'length of electionary: {len(electionary)}')
#ElecRsltFH.write(f'length of electionary: {len(electionary)}')

totalvotescast = 0 #gear up to tally the total votes

# add up all the votes cast...
for keys in electionary:
    totalvotescast += electionary[keys]

print(' ')
print('-------------------------')
print('    Election Results')
print('-------------------------')
print(f'Total Votes: {totalvotescast}')

ElecRsltFH.write(' ')
ElecRsltFH.write('-------------------------\n')
ElecRsltFH.write('    Election Results\n')
ElecRsltFH.write('-------------------------\n')
ElecRsltFH.write(f'Total Votes: {totalvotescast}\n')

for keys in electionary:
    candidate_pctvotes = (electionary[keys] / totalvotescast) * 100
    print(f'{keys}: {candidate_pctvotes:.5}% ({electionary[keys]} votes)')
    ElecRsltFH.write(f'{keys}: {candidate_pctvotes:.5}% ({electionary[keys]} votes)\n')
    # "{:.3}".format(pwpct

print('-------------------------')
print(f'Winner: {max(electionary, key=electionary.get)}')
print('-------------------------')

ElecRsltFH.write('-------------------------\n')
ElecRsltFH.write(f'Winner: {max(electionary, key=electionary.get)}\n')
ElecRsltFH.write('-------------------------\n')

ElecRsltFH.close # doen I thoink...

# If time put the voter fraud detections code here...
# reopen the file 
# for each voter number
#  scan every line and see if that voter nuber repeats
#  if voter repeats flag a fraud alert (FA)
#    FAdiary = {voterid: FAtotal_count, {County_FA_list: 0, {county1:} }
#    fraud alert data record includes
#       voter ID, county, candidate
# THIS COULD TAKE A WHILE!
#     totalvotes +=  1

# print(f"Totals...{totalvotes} ")

#       Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------