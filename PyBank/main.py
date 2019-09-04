#Read in file budget_data.csv
import pandas as pd
a=[]
b=[]
c=[]
tick=0
amount=0
change=0
total_change=0
data=pd.read_csv("~/GitHub/python-challenge/PyBank/budget_data.csv")


df=pd.DataFrame(data)
df['Profit/Losses']=df['Profit/Losses'].astype(int)

#Structure the text display
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

#print("_________________")

for i in range(len(a)):
    #print(i)
    #print(a[i])
    #print(b[i])
    change = (a[i]-b[i])
    #Create a list of the month-to-month changes in profit/loss
    c.append(change)
    #print("Monthly change " +str(change))
    total_change=total_change+change

print("Total change " +str(total_change))
average_change=round(total_change/len(a),2)
print("Average Change: $" +str(average_change))

#Calculate and Print the greatest increases in Profits (date and amount) over the entire period
max_loc=(c.index(max(c)))+1
print('Greatest Increase in Profits: '+df["Date"].values[max_loc] +"  ($"+str(max(c))+")")






#Calculate and Print the greatest decrease in losses (date and amount) over the entire period
min_loc=(c.index(min(c)))+1
print('Greatest Decrease in Profits: '+df["Date"].values[min_loc] +"  ($"+str(min(c))+")")
#Export the results (print statements) to a text file