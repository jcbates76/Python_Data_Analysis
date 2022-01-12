


# Import functions
import os
import csv

total_votes = 0
candidate_list = []
candidate_vote_total = []
candidate = str


# Define the path of the CSV input file
csvpath = os.path.join("Resources", "election_data.csv")

# Define the path of the TXT output file
output_path = os.path.join("Analysis", "election_resuts.txt")

# Perform loop for all records within the CSV dataset
with open(csvpath, "r", encoding="utf-8-sig") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Ignore the header row in the data set
    next(csvreader, None) 

    # Iterate through all rows of the dataset
    for row in csvreader:
        
        # Accumulate total number of votes cast
        total_votes = total_votes + 1

        # Determine if candidate is accounted for in list of candidates
        candidate = row[2]

        # Check to see if the candidate is in the candidiate list, if not, add them and append the vote total list at the same time
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            candidate_vote_total.append(0)
            
        
        # Increment the vote total for that candidate
        candidate_index = candidate_list.index(candidate)
    
        candidate_vote_total[candidate_index] = candidate_vote_total[candidate_index] + 1

for candidate in candidate_list:
    print(candidate + ": " + str(candidate_vote_total[candidate_list.index(candidate)]/total_votes) + "(" + str(candidate_vote_total[candidate_list.index(candidate)]) + ")")


print(total_votes)