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
for name, votes in candidate.items():
    # find the % votes by candidate
    print(f"Candidate {name} received {(votes/rowcount)*100} %")