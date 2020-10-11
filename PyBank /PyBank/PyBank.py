import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

file_output = "analysis/results.txt"

#initializing the variables
total_months =0
total_revenue = 0
previous_profit = 0
changes_of_profit = []
date_count = []
greatest_increase = 0
greatest_increase_date = 0
greatest_decrease = 0
greatest_decrease_date = 0 

#Open the CSV
with open(budget_csv, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")
    header= next(csv_reader)

#Total number of months and total revenue
    # previous_profit = int(first_row[1])
    # greatest_increase = int(first_row[1])
    # greatest_increase_date = first_row[0]
    
    for row in csv_reader:
        total_months = total_months +1
        total_revenue = total_revenue + int(row[1])
        
        # Calculate changes occur from last month to this month
        change = int(row[1]) - previous_profit
        previous_profit = int(row[1])
        changes_of_profit.append(change)
        date_count.append(row[0])

        #Find the great increase in profits over the entire period
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_date = row[0]

        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_date = row[0]
    

average_changes = sum(changes_of_profit)/len(changes_of_profit)

print("Financial Analysis")
print("--------------------------------")
print("Total Months: " + str(total_months))
print("Total Amount: " + str(total_revenue))
print("Average Change: " + str(average_changes))
print("Greatest Increase in Profits: " + greatest_increase_date + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + greatest_decrease_date + " ($" + str(greatest_decrease) + ")")


with open(file_output, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % total_months)
    file.write("Total Amount: $%d\n" % total_revenue)
    file.write("Average Change $%d\n" % average_changes)
    file.write("Greatest Increase in Profits: %s ($%s)\n" % (greatest_increase_date, greatest_increase))
    file.write("Greatest Decrease in Profits: %s ($%s)\n" % (greatest_decrease_date, greatest_decrease))


        


    
      


    
