import csv

# Create file path
filepath = "PyPoll/Resources/election_data.csv"

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
max_votes = 0

# Read the CSV file
try:
    with open(filepath, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)
        
        for row in csvreader:
            total_votes += 1
            candidate = row[2]
            
            if candidate not in candidates:
                candidates[candidate] = 0
            candidates[candidate] += 1
    
    # Calculate percentages and determine the winner
    results = []
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        results.append(f"{candidate}: {percentage:.3f}% ({votes})")
        if votes > max_votes:
            max_votes = votes
            winner = candidate

    # Print the analysis to the terminal
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for result in results:
        print(result)
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    # Export the analysis to a text file
    output_path = 'election_results.txt'
    with open(output_path, 'w') as file:
        file.write("Election Results\n")
        file.write("-------------------------\n")
        file.write(f"Total Votes: {total_votes}\n")
        file.write("-------------------------\n")
        for result in results:
            file.write(result + "\n")
        file.write("-------------------------\n")
        file.write(f"Winner: {winner}\n")
        file.write("-------------------------\n")

except FileNotFoundError:
    print(f"Error: File not found at {filepath}")
