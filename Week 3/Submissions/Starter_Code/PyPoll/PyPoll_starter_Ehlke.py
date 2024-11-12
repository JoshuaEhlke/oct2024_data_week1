# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

filepath = "Resources/election_data.csv"
file_to_output = "analysis/election_results_ehlke.txt"

total_votes = 0
vote_dic = {}

with open(filepath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        total_votes += 1

        cand = row[2]
        if cand in vote_dic.keys():
            vote_dic[cand] += 1
        else:
            vote_dic[cand] = 1

win = ""
max_votes = 0

output = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
"""
for cand in vote_dic.keys():
    votes = vote_dic[cand]
    vote_perc = round(100 * votes / total_votes, 3)
    
    if votes > max_votes:
        max_votes = votes
        win = cand

    txt = f"{cand}: {vote_perc}% ({votes})\n"
    output += txt


win_txt = f"""
-------------------------
Winner: {win}
-------------------------
"""
output += win_txt

print(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)