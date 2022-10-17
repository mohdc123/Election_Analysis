import csv
rowcount=0
candidate = {}
with open("election_results.csv",newline='') as csvfile: 
    csvrow = csv.reader(csvfile, delimiter=',')
    header = next(csvfile)
    NoOfVotes=0
    for csvline in csvrow:
        
        if candidate.get(csvline[2]) == None:
             NoOfVotes = 1
             candidate[csvline[2]] = NoOfVotes
        else: 
             

             candidate[csvline[2]] +=1 

        # print(csvline)
        rowcount+=1

# print(str(header))
print(f"\n Total votes {str(rowcount)}")
 

print(f" Candidate {sorted(candidate.items(), key = lambda item: item[1])[-1]} is the winner")
#print(sorted(candidate.values(),reverse=True)[0])
print(candidate) # display

total_votes = rowcount    
winning_candidate = sorted(candidate.items(), key = lambda item: item[1])[-1][0]#
winning_count = sorted(candidate.items(), key = lambda item: item[1])[-1][1]
winning_percentage = (winning_count/rowcount)* 100
print(f"winning Candidate {winning_candidate}  Received {winning_count} votes and  {winning_percentage} % of votes")
election_result = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")    
with open("election_analysis.txt",mode="w+") as election_data:
     election_data.write(election_result)
     for name, votes in candidate.items():
       # find the % votes by candidate
       print(f"Candidate {name} received {(votes/rowcount)*100} %")
       election_data.write(f"{name}: {(votes/rowcount)*100:.1f} % ({votes:,}) \n")
     #file_pointer = csv.write(election_data)
    
     election_data.write(winning_candidate_summary)
     