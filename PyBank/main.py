import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
output_file = os.path.join('Analysis', 'budget_analysis.txt')

month_number = 0
net_total =0
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999]
total_net = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    first_row= next(csvreader)
    month_number = month_number + 1
    net_total += int(first_row[1])
    prev_net = int(first_row[1])

    for row in csvreader:
            month_number = month_number + 1
            print(month_number)
            net_total = net_total+int(row[1])
            print(net_total)

            net_change = int(row[1]) - prev_net
            prev_net = int(row[1])
            net_change_list = net_change_list + [net_change]

            if net_change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = net_change

            if net_change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = net_change

net_monthly_avg = sum(net_change_list) / len(net_change_list)

output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {month_number}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
with open(output_file, "w") as txt_file:
    txt_file.write(output)


        



