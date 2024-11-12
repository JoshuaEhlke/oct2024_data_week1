# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

filepath = "Resources/budget_data.csv"
file_to_output = "analysis/budget_analysis.txt"

total_months = 0
total_net = 0

last_month_prof = 0
current_month_prof = 0
total_change = 0

max_change = 0
max_month = ""

min_change = 0
min_month = ""


# Code ripped 3.2.8
with open(filepath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        total_months += 1
        total_net += int(row[1])

        if total_months == 1:
            last_month_prof = int(row[1])
        else:
            current_month_prof = int(row[1])
            change = current_month_prof - last_month_prof
            total_change += change

            last_month_prof = current_month_prof

            if change > max_change:
                max_change = change
                max_month = row[0]
            
            if change < min_change:
                min_change = change
                min_month = row[0]
            

output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_net}
Average Change: ${round(total_change / (total_months - 1), 2)}
Greatest Increase in Profits: {max_month} (${max_change})
Greatest Decrease in Profits: {min_month} (${min_change})
"""

print(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)