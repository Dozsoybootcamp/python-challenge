import csv

# Create file path
filepath = "PyBank/Resources/budget_data.csv"

# Initialize variables
total_rows = 0
date_values = set()
colmn_index = 1
net_profit_loss = 0
previous_value = None
total_change = 0
change_count = 0
greatest_increase = float('-inf')
greatest_decrease = float('inf')
greatest_increase_date = ''
greatest_decrease_date = ''

# Read the CSV file
with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    
    for row in csvreader:
        total_rows += 1
        date_value = row[0]
        if date_value:
            date_values.add(date_value)
        
        # Calculate net profit/loss
        profit_loss = int(row[1])
        net_profit_loss += profit_loss
        
        # Calculate changes in profit/loss
        if previous_value is not None:
            change = profit_loss - previous_value
            total_change += change
            change_count += 1
            
            # Determine greatest increase/decrease
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = date_value
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = date_value
        
        previous_value = profit_loss

# Calculate the total number of months
total_no_months = len(date_values)

# Calculate the average change in profit/loss
average_change = total_change / change_count if change_count != 0 else 0

# Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_no_months}")
print(f"Total: ${net_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Export the analysis to a text file
output_path = 'financial_analysis.txt'
with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_no_months}\n")
    file.write(f"Total: ${net_profit_loss}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
