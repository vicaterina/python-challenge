#PyPoll Homework Assignment 3 / NU DataBootCamp / Vic Caterina

import pandas as pd
candidate_votes=0
#Read in election.data.csv
data=pd.read_csv("~/GitHub/python-challenge/PyPoll/election_data.csv")

#Create a dataframe 
df=pd.DataFrame(data)
df.head()

grouped=df.groupby(['Candidate'])
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
#Total number of votes each candidate won

candidate_votes=df["Candidate"].value_counts()
print(candidate_votes)

#create 2nd dataframe
candidate_df=pd.DataFrame(candidate_votes)
candidate_df.head()
#candidate_df=pd.DataFrame([candidate_df], columns =["Candidate", "Votes"])

#The percentage of votes each candidate won
#Add column to candidate_votes DataFrame
for candidate in candidate_df["Candidate"]:
    pct_vote=(df["Candidate"].value_counts()/total_votes*100)

pct_vote_df=pd.DataFrame(pct_vote)
print(pct_vote_df)

frames=[candidate_df, pct_vote_df]

final_df=pd.concat([candidate_df, pct_vote_df],axis=1)
final_df.index.names=["Candidate"]

final_df.rename(columns={'Candidate':"",'Candidate':""}, inplace=True)
final_df
#The winner of the election based on popular vote