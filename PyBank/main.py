# Financial records analysis
# Raw data in budget_data.csv with two columns: "Date" and "Profit/Losses"

# Import functions
import os
import csv

# Declare variables
row_count = 0                   # variable for the total number of records
profit_losses_total = 0         # variable for the total profit/losses for the dataset
delta = 0                       # difference between current year profit/losses and previous year profit/losses
delta_sum = 0                   # accumulation of the profit/losses of each period
greatest_increase_delta = 0     # greatest increase in profit/loss in any period in the data set
greatest_decrease_delta = 0     # greatest decrease in profit/loss in any period in the data set
greatest_increase_date = str    # period of the greatest increase in profit/loss 
greatest_decrease_date = str    # period of the greatest decrease in profit/loss 

# Define the path of the CSV input file
csvpath = os.path.join("Resources", "budget_data.csv")

# Define the path of the TXT output file
output_path = os.path.join("Analysis", "financial_analysis.txt")

# Perform loop for all records within the CSV dataset
with open(csvpath, "r", encoding="utf-8-sig") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Ignore the header row in the data set
    next(csvreader, None) 

    # Perform analysis for each row within the dataset
    for row in csvreader:
        
        # Increase the row counter
        row_count = row_count + 1   
        
        # Accumulate the profit/losses for each record into the total
        profit_losses_total = profit_losses_total + int(row[1])     
        
        # For the first record, there is no previous record to perform a difference in profit/loss, so skip analysis
        if row_count == 1:
            delta = 0
            prior_period = int(row[1])
            delta_sum = delta_sum + delta
        
        # Perform the analysis for change in profit/loss from prior period
        else:
            delta = int(row[1]) - prior_period
            delta_sum = delta_sum + delta
            prior_period = int(row[1])
            
            # Review for Greatest Decrease in profits
            if delta < greatest_decrease_delta:
                greatest_decrease_delta = delta
                greatest_decrease_date = str(row[0])
            
            # Review for Greatest Increase in Profits
            if delta > greatest_increase_delta:
                greatest_increase_delta = delta
                greatest_increase_date = str(row[0])

# Calculate the avarage change in profit/losses
average_delta = delta_sum / (row_count - 1)  #calculate the average change in profit/losses

# Output the analysis into a text file
with open(output_path, "w", newline="") as f:
    f.write("Financial Analysis\n")
    f.write("-------------------------------------------------------------\n")
    f.write(f"Total Months: {row_count}\n")
    f.write("Total Profit/Losses: " + "${:,.0f}\n".format(profit_losses_total))
    f.write("Average Change: " + "${:,.2f}\n".format(average_delta))
    f.write("Greatest Increase in Profits: " + greatest_increase_date + " " + "(" + str("${:,.0f}".format(greatest_increase_delta)) + ")\n")
    f.write("Greatest Decrease in Profits: " + greatest_decrease_date + " " + "(" + str("${:,.0f}".format(greatest_decrease_delta)) + ")\n")


# Output the analysis in the terminal screen
print("Financial Analysis")
print("---------------------------------------------------------------------")
print(f"Total Months: {row_count}")
print("Total Profit/Losses: " + "${:,.0f}".format(profit_losses_total))
print("Average Change: " + "${:,.2f}".format(average_delta))
print("Greatest Increase in Profits: " + greatest_increase_date + " " + "(" + str("${:,.0f}".format(greatest_increase_delta)) + ")")
print("Greatest Decrease in Profits: " + greatest_decrease_date + " " + "(" + str("${:,.0f}".format(greatest_decrease_delta)) + ")")