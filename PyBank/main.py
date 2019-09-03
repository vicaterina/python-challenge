#Read in file budget_data.csv
import csv
csvpath="budget_data.csv"

with open(csvpath, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    
    print(csvreader)

#Calculate the total months included in the dataset

#Calculate and Print the net total Profit/Losses over the entire period (dataset)

#Calculate and Print the average of the changes in "Profit/Losses" over the entire period (dataset)

#Calculate and Print the greatest increases in Profits (date and amount) over the entire period

#Calculate and Print the greatest decrease in losses (date and amount) over the entire period

#Export the results (print statements) to a text file