import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")
file_output = "analysis/poll_results.txt"

voter_number = 0
vote_list=[]
candidate_list = []
vote_percent_list=[]
winner = ""

with open(election_csv, newline="")as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)

    for row in csv_reader:
        voter_number += 1

        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            vote_list.append(1)
        else:
            vote_list[candidate_list.index(row[2])] +=1

#Calculate the percentage of vote



        
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(voter_number))
print("-------------------------")

print("-------------------------")
print("Winner: " + winner)
print("-------------------------")