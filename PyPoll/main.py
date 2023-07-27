import csv

file_path = "Resources/election_data.csv"
output_file = "analysis/election_results.txt"

total_votes = 0
candidates = {}

with open(file_path, newline="") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)

    for row in reader:
        total_votes += 1
        candidate = row[2]
        if candidate not in candidates:
            candidates[candidate] = 0
        candidates[candidate] += 1

with open(output_file, "w") as txtfile:
    txtfile.write(f'Election Results\n'
                  f'-------------------\n'
                  f"Total Votes: {total_votes}\n"
                f'-------------------\n')

    max_votes = 0
    winner = ""

    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

        if votes > max_votes:
            max_votes = votes
            winner = candidate

    txtfile.write(f'-------------------\n'
                  f"Winner: {winner}\n"
                  f'-------------------\n')
