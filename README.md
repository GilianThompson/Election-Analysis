# Election-Analysis

### Overview of Project 
In this project, Python was utilized to analyize data for a Colorado election audit. The goal was the analyize the data in order to state the winner, as well as provide a breakdown of the votes casted. ```PyPoll_Challenge.py``` is the file containing the code used for the analysis. 

### Results 
- There were **369,711 total votes** casted in this election
- There were three counties in this election: Jefferson, Denver, and Arapahoe.  
-     Jefferson had 10.5% of the votes, (38,213 votes)
-     Denver had 82.8% of the votes, (306,055 votes)
-     Arapahoe had 6.7% of the votes, (11,606 votes) 
From this, it can be seen that **Denver had the largest voter turnout** 
- There were three candidates in this election: Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane. 
-     Charles Casper Stockham accounted for 23.0% of the votes, (85,213 votes)
-     Diana DeGette accounted for 73.8% of the votes, (272,892)
-     Raymon Anthony Doane accounted for 3.1% of the votes (11,606)
- **The winner of the election is Diana DeGette** with a total of 272,892 votes, accounting for 73.8% of the total votes casted. 

### Further Development 
This script can modified to calculate the results of other elections. To use this script on other elections, it would be important to change the location of where the script reads the data election data from. In the script, the following path is used to access the data file, election_results.csv:
```
# Add a variable to load a file from a path.
file_to_load = os.path.join( "Resources", "election_results.csv")
```
This variable can be changed to read in other files by changing the path specified. 

For this election, the data file had a format of "Ballot ID, County, Candidate" as seen below in the first four lines of the file:

<img width="372" alt="Screen Shot 2021-07-03 at 1 02 28 PM" src="https://user-images.githubusercontent.com/85901073/124361801-f562c880-dbfe-11eb-8f75-769b9bedb263.png">

The script written for this election accomodated for this format when reading the data from election_results.csv, but the script can be modified to take in different information by adjusting how the script reads through the file. In this script, each row of the data file was treated as an array, and the items in each row were separated by commas. So, county was read as the second item in the array, and candidate name as the third item. For other data files, the array items can be changed to hold different or additional data as needed for specific election aduits. 



