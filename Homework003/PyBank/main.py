import csv
import os

data = os.path.join("Resources", "budget_data.csv")
save_location = os.path.join("Results", "budget_final.txt")

total_mos = 0
month_change = []
netChange_list = []
greatest_inc = ["", 0]
greatest_dec = ["", 99999999999999999999999999999]
net = 0

with open(data) as budget_data:
    reader = csv.reader(budget_data)
    header = next(reader)
    first_row = next(reader)
    
    total_mos = total_mos + 1
    net = net + int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:
        total_mos = total_mos + 1
        net = net + int(row[1])

        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        netChange_list = netChange_list + [net_change]
        month_change = month_change + [row[0]]

        if net_change > greatest_inc[1]:
            greatest_inc[0] = row[0]
            greatest_inc[1] = net_change

        if net_change < greatest_dec[1]:
            greatest_dec[0] = row[0]
            greatest_dec[1] = net_change

monthly_avg = sum(netChange_list) / len(netChange_list)

results = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_mos}\n"
    f"Total: ${net}\n"
    f"Average  Change: ${monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_inc[0]} (${greatest_inc[1]})\n"
    f"Greatest Decrease in Profits: {greatest_dec[0]} (${greatest_dec[1]})\n")

print(results)

with open(save_location, "w") as txt_file:
    txt_file.write(results)
