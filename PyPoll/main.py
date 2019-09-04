#PyPoll Homework Assignment 3 / NU DataBootCamp / Vic Caterina

import pandas as pd

#Read in election.data.csv
data=pd.read_csv("~/GitHub/python-challenge/PyPoll/election_data.csv")

#Create a dataframe 
df=pd.DataFrame(data)
df.head()
df[""]

#Format header
print("Election Results")
print("__________________________________")
print("\n")

#Calculate the toal number of votes cast
total_votes=len(df)
print("Total Votes Cast: " +str(total_votes))
print("__________________________________")

#A complete list of candidates who received votes
#Group by candidate
#candidate_votes=df["Candidate"].value_counts()
print(candidate_votes)

#Total number of votes each candidate won

#The percentage of votes each candidate won

#The winner of the election based on popular vote