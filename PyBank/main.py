import os
import csv

budget_csv = os.path.join('Resources','budget_data.csv')
month = 0
totalch = 0
tally = 0
prof_loss = []
months = []
changes = []


#Use the reader function to read the csv file
with open(budget_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
#Count the number of months. Make a list of the profit/loss and months they occured in.
    for row in csvreader:
     month = month+1
     prof_loss.append(int(row[1])) 
     months.append(row[0])

# Create a list of the monthly changes in profit/loss.
while tally < 85:
    changes.append(prof_loss[tally+1]-prof_loss[tally])
    tally = tally + 1

# Find index of the largest and smallest changes
maximum = (max(changes))
minimum = (min(changes))
maxindex = changes.index(maximum)
minindex = changes.index(minimum)

#Make final calculations and print in a readable form.
print("""Financial Analysis
----------------------
""")
print("Total Months: ",month)
print("Total: $",sum(prof_loss))
print("Average Change: $",'{:.2f}'.format(sum(changes)/(len(changes))))
print("Greatest Increase in profits: ",months[maxindex],"($",changes[maxindex],")")
print("Greatest Decrease in profits: ",months[minindex],"($",changes[minindex],")")
# Leftovers print (sum(prof_loss)/len(prof_loss))

#Print all results into a new text file in the 'analysis' folder
with open('analysis/results.txt', 'w') as f:
    print("""Financial Analysis
    ----------------------
    """,file=f)
    print("Total Months: ",month,file=f)
    print("Total: $",sum(prof_loss),file=f)
    print("Average Change: $",'{:.2f}'.format(sum(changes)/(len(changes))),file=f)
    print("Greatest Increase in profits: ",months[maxindex],"($",changes[maxindex],")",file=f)
    print("Greatest Decrease in profits: ",months[minindex],"($",changes[minindex],")",file=f)