import os
import csv

#Set variables and load csv file from folder
poll_csv = os.path.join('Resources','election_data.csv')
totalvotes = 0
candidates = []
votecount = []
candpercent = []
index = ''



#Use the reader function to read the csv file
with open(poll_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    #Check if candidate is in list. If not, add them and initialize their vote total.
    for row in csvreader:
        if row[2] not in candidates:
            candidates.append(row[2])
            votecount.append(0)
    #Count the number of votes and total votes for each candidate
        totalvotes += 1
        index = candidates.index(row[2])
        votecount [index] += 1
for a in votecount:
    voteper = '{:.3%}'.format(a / totalvotes)
    candpercent.append(voteper)
#Determine the index of the winning candidate
winnerTotal = max(votecount)
winnerIndex = votecount.index(winnerTotal)

#Print out all of the results
print("""Election results
------------------""")
print("Total Votes: ",totalvotes)
print("------------------")
print(candidates[0],": ", candpercent[0], " (",votecount[0],")")
print(candidates[1],": ", candpercent[1], " (",votecount[1],")")
print(candidates[2],": ", candpercent[2], " (",votecount[2],")")
print("------------------")
print("Winner: ", candidates[winnerIndex])
print("------------------")

#Print out the same results to an external file named results.txt
with open('analysis/results.txt', 'w') as f:
    print("""Election results
------------------""", file=f)
    print("Total Votes: ",totalvotes,file=f)
    print("------------------",file=f)
    print(candidates[0],": ", candpercent[0], " (",votecount[0],")",file=f)
    print(candidates[1],": ", candpercent[1], " (",votecount[1],")",file=f)
    print(candidates[2],": ", candpercent[2], " (",votecount[2],")",file=f)
    print("------------------",file=f)
    print("Winner: ", candidates[winnerIndex],file=f)
    print("------------------",file=f)
    
    

#prints for testing
#print (winnerIndex)
#print (candpercent)
#print (totalvotes)
#print (votecount)
#print (candidates)
