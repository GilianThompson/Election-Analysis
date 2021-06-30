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

#initializing variables 
total_votes = 0 
candidate_options = [] #create empty array 
candidate_votes= {} #create empty dictionary 
winning_candidate = ""
winning_count = 0 
winning_percentage = 0 

#open csv file to read, save as election_data
with open(file_to_load) as election_data:
    #read file object with reader function
    file_reader = csv.reader(election_data)
    #read header line (first row)
    headers = next(file_reader)
    
    for row in file_reader:
        total_votes += 1 
        candidate_name = row[2]
        if candidate_name not in candidate_options: 
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0 
        #increment vote count for the appropriate candidate     
        candidate_votes[candidate_name] += 1 

with open(file_to_save, 'w') as txt_file:
    election_results = (
        f"\nElection results\n"
        f"---------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)

    for candidate_name in candidate_options:
        votes = candidate_votes[candidate_name] 
        vote_percentage = float(votes)/float(total_votes) *100 
        if (votes > winning_count) and (vote_percentage > winning_percentage): 
            winning_count = votes 
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
    winning_candidate_summary = (
        f"------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

