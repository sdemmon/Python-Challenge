import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

# Initialize variables
totalVotes = 0
candidates = []
candidateVotes = {}
totalCharles = []
totalDiana = []
totalRaymon = []
maxDecrease =[]
dates = []

# Read the CSV file
with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Skip header row
    header = next(csvreader)
    
    csvreader = list(csvreader)

# Loop through the rows in the CSV file    
for i, row in enumerate(csvreader):
    ballot = row[0]
    #add total vote count
    totalVotes += 1
    candidate_name = row[2]
    
    # If the candidate is not in the list of candidates, add them
    if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidateVotes[candidate_name] = 0
    
    #Add candidates vote count    
    candidateVotes[candidate_name] += 1

with open("analysis/PyPoll_analysis.txt", "w") as out_file:
    # Print the analysis results
    # print("Election Results")
    # print("---------------------------")
    # print(f"Total Votes: {totalVotes}")
    # print("---------------------------")

    results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {totalVotes}\n"
        f"-------------------------\n")

    print(results)

    out_file.write(results)  
    
    # Initialize variables to find the winner   
    winner = ""
    maxVotes = 0
    for candidate in candidates: 
        votes = candidateVotes[candidate]
        percentage = (votes / totalVotes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes})\n")
        out_file.write(
            f"{candidate}: {percentage:.3f}% ({votes})\n"
        )
        
        # Check for the winner
        if votes > maxVotes:
            maxVotes = votes
            winner = candidate

    # Print the analysis results
    summary = (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------\n")
    print(summary)

    out_file.write(summary)
    # print("---------------------------")

    # print(f"Winner: {winner}")

    # print("---------------------------")

    
