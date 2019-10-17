# import and locate file locations
import csv
import os

data = os.path.join("Resources", "election_data.csv")
save_location = os.path.join("Results", "election_final.txt")

# initial states for counters/trackers
total_votes = 0

c_options = []
c_votes = {}

win_candid = ""
win_count = 0

with open(data) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)

    for row in reader:

        total_votes = total_votes + 1
        name = row[2]

        if name not in c_options:
            c_options.append(name)
            c_votes[name] = 0
        c_votes[name] = c_votes[name] + 1

# print results to txt file AND terminal
with open(save_location, "w") as txt_file:

    results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(results, end="")

    txt_file.write(results)

    # find actual winner
    for candidate in c_votes:
        votes = c_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        if (votes > win_count):
            win_count = votes
            win_candid = candidate

        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")
        txt_file.write(voter_output)

    winner = (
        f"-------------------------\n"
        f"Winner: {win_candid}\n"
        f"-------------------------\n")
    print(winner)
    txt_file.write(winner)
