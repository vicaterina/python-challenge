#PyBank Homework Assignment 3 / NU DataBootCamp / Vic Caterina


#Read in file budget_data.csv
import pandas as pd
a=[]
b=[]
c=[]
amount=0
change=0
total_change=0

#load csv file from local Git clone
data=pd.read_csv("~/Documents/GitHub/python-challenge/PyBank/budget_data.csv")

#convert to dataframe
df=pd.DataFrame(data)

#transform "Profit/Losses" column to integer
df['Profit/Losses']=df['Profit/Losses'].astype(int)

#Format the text report 
print("Financial Analysis")
print("______________________________________")

#Calculate the total months included in the dataset
tot_months = len(data)
print('Total Months: ', tot_months)

#Calculate and Print the net total Profit/Losses over the entire period (dataset)
total=df['Profit/Losses'].sum()
print('Total: $',total)

#Calculate and Print the average of the changes in "Profit/Losses" over the entire period (dataset)
for i in df["Profit/Losses"]:
    #print(i)
    a.append(i)
    b.append(i)
del a[0]

for i in range(len(a)):
    #print(i)
    #print(a[i])
    #print(b[i])
    change = (a[i]-b[i])
    #Create a list of the month-to-month changes in profit/loss
    c.append(change)
    #print("Monthly change " +str(change))
    total_change=total_change+change

#print("Total change " +str(total_change))
average_change=round(total_change/len(a),2)
print("Average Change: $" +str(average_change))

#Calculate and Print the greatest increases in Profits (date and amount) over the entire period
max_loc=(c.index(max(c)))+1
print('Greatest Increase in Profits: '+df["Date"].values[max_loc] +"  ($"+str(max(c))+")")

#Calculate and Print the greatest decrease in losses (date and amount) over the entire period
min_loc=(c.index(min(c)))+1
print('Greatest Decrease in Profits: '+df["Date"].values[min_loc] +"  ($"+str(min(c))+")")

#Export the results (print statements) to a text file
file=open("PyBank.txt","w")
file.write("Financial Analysis")
file.write("\n")
file.write("______________________________________")
file.write("\n")
file.write('Total Months: '+ str(tot_months))
file.write("\n")
file.write('Total: $'+str(total))
file.write("\n")
#file.write("Total change " +str(total_change))
#file.write("\n")
file.write("Average Change: $" +str(average_change))
file.write("\n")
file.write('Greatest Increase in Profits: '+df["Date"].values[max_loc] +"  ($"+str(max(c))+")")
file.write("\n")
file.write('Greatest Decrease in Profits: '+df["Date"].values[min_loc] +"  ($"+str(min(c))+")")
file.close()