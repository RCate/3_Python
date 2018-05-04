import os
import csv

filepath1 = "election_data_1.csv"
voter1 = []
current_candidate = []
candidates_list = []
Vestal_count = 0
Torres_count = 0
Cordin_count = 0
Seth_count = 0

count_voters = 0
 
with open(filepath1,"r",newline="")as csvfile1:
    csvreader1 = csv.reader(csvfile1,delimiter=",")
    next(csvreader1, None)
    for row in csvreader1:
        count_voters += 1
        current_candidate = row[2] 
        if current_candidate not in candidates_list:
            candidates_list.append(current_candidate)

        if row[2] == str('Vestal'):
            Vestal_count += 1
        elif row[2] == str("Torres"):
            Torres_count += 1
        elif row[2] == str("Cordin"):
            Cordin_count += 1
        elif row[2] == str("Seth"):
            Seth_count += 1
candidates_votes = [Vestal_count, Torres_count, Cordin_count, Seth_count]
maybe_winner = 0

for c in candidates_votes:
    if c > maybe_winner: 
        maybe_winner = c
        winner = candidates_votes.index(c)
  
if winner == 0: 
        name_winner = "Vestal"
elif winner == 1:
        name_winner = "Torres"
elif winner == 2: 
        name_winner = "Cordin"
elif winner == 3: 
        name_winner = "Seth"
        
    
print(name_winner)

Vestal_Percentage = round(Vestal_count/count_voters*100)
Torres_Percentage = round(Torres_count/count_voters*100)
Cordin_Percentage = round(Cordin_count/count_voters*100)
Seth_Percentage = round(Seth_count/count_voters*100)

print("Election Results")
print("----------------------------------")
print("Total Votes: ", count_voters)
print("----------------------------------")
print("Candidates: ", candidates_list)
print("Vestal: ", Vestal_Percentage,"%",Vestal_count)
print("Torres: ", Torres_Percentage,"%", Torres_count)
print("Cordin: ", Cordin_Percentage,"%", Cordin_count)
print("Seth: ", Seth_Percentage,"%", Seth_count)



PyPoll_text_file1 =  "pyPoll_output1.txt"
with open(PyPoll_text_file1,"w+") as text:
  
    text.write("------------------------------------------------\n")
    text.write("Election Results \n")
    text.write("-----------------------------------------------\n")
    text.write("Total Votes: ")
    text.write(str(count_voters)+"\n")
    text.write("------------------------------------------------\n ")
    text.write("Vestal:")
    text.write(str(Vestal_Percentage))
    text.write("$")
    text.write(str(Vestal_count) +'\n')
    text.write("Torres:")
    text.write(str(Torres_Percentage))
    text.write("%")
    text.write(str(Torres_count) +'\n')
    text.write("Cordin:")
    text.write(str(Cordin_Percentage))
    text.write("%")
    text.write(str(Cordin_count) +'\n')
    text.write("Seth:")
    text.write(str(Seth_Percentage))
    text.write("%")
    text.write(str(Seth_count)+'\n')
    text.write("------------------------------------------------\n")
    text.write("Winner:")
    text.write(name_winner+'\n')
    text.write("------------------------------------------------\n")
    