# Given a set of poll data called election_data.csv
# Dataset composed of three columns: Voter ID, County, Candidate
# Analyze the votes and calculate the following:
#   - The total number of votes cast
#   - A complete list of candidates who received votes
#   - The percentage of votes each candidate won
#   - The total number of votes each candidate won
#   - The winner of the election based on popular vote

# Import functions
import os
import csv

# Define the path of the CSV input file
#csvpath = os.path.join("Resources", "election_data.csv") DEBUG
file = "\Resources\election_data.csv"

# Define the path of the TXT output file
output_path = os.path.join("Analysis", "election_results.txt")
    
# Perform loop for all records within the CSV dataset
with open(file, "r", encoding="utf-8-sig") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Ignore the header row in the data set
    next(csvreader, None) 

    print(csvreader)
    print("Maybe this code will finally work")

# Things to do
# Import and read the file
# Need several counters
#   - Total number of votes
#   - Number of votes by each candidate
# Track the list of candidates
# Calculate the percentage won by each candidate (votes for won per candidate divided by total number of votes cast)
# Determine who has the most votes



