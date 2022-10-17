import csv
rowcount=0
with open("election_results.csv",newline='') as csvfile: 
    csvrow = csv.reader(csvfile, delimiter=',')
    header = next(csvfile)
    for csvline in csvrow:
         
        # print(csvline)
        rowcount+=1

print(str(header))
print(f"\n Total votes {str(rowcount)}")