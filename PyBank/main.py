# Anaylize the financial records of the company
# Give a set of financial data called budget_data.csv
# Dataset has two columns, Date and Profit/Losses.
# Create a Python script that analyzes the records to calculate each of the following:
#   The total number of months included in the data set
#   The net total amount of "Profit/Losses" over the entire period
#   Caluclate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#   The greatest increase in profits (date and amount) over the entire period
#   The greatest decrease in profits (date and amount) over the entire period
# The output should be both to a text file and the terminal screen



# Open the data set
import os
import csv

file = "/Resources/budget_data.csv"

#csvpath = os.path("\Resources\budget_data.csv")

#with open(csvpath, "r", encoding="utf-8-sig") as csvfile:
with open(file, "r", encoding="utf-8-sig") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


# Pull the data into a variable
# Get the total number of records
# Sum the Profit/Losses
# The delta of Profit/Losses month to month, then the average
# The greatest delta increase
# The greatest delta decrease
# Output the to terminal and CSV file