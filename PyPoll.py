import csv
import random
import os
# The data we need to retrieve 
#1. Total number of votes cast
#2. A complete list of candidates who recieved votes
#3. Percentage of votes each candidate won 
#4. Total number of votes eaach candidate won 
#5. Winner of the election based on popular vote 

#store file path in variable file_to_load 
file_to_load = 'Resources/election_results.csv'

#indirect file path i guess
file_to_save = os.path.join("analysis","election_analysis.txt") 
# outfile = open(file_to_save, 'w')
# outfile.write("Hello World")
# outfile.close()

with open(file_to_save, 'w') as txt_file:
    #txt_file.write("Hello World.")
    txt_file.write("Counties in the Election\n")
    txt_file.write("---------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")

#open csv file to read, save as election_data
with open(file_to_load) as election_data:
    #read file object with reader function
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)

