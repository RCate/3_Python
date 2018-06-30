import os
import csv

filepath1 = "election_data_1.csv"
filepath2 = "election_data_2.csv"
def Counting_votes (file, output):

    vote_counts = {}
    max_votes = 0
    winner = ""

    count_voters = 0
    
    with open(file,"r",newline="")as csvfile1:
        csvreader1 = csv.reader(csvfile1,delimiter=",")
        next(csvreader1, None)
        for row in csvreader1:
            count_voters += 1

            current_candidate = row[2] 

            #intializa dictionary to zero
            if current_candidate not in vote_counts: 
                vote_counts[current_candidate] = 1
            else:
                vote_counts[current_candidate]+= 1

    print("---------------")
    print("Total Votes: ", count_voters)
    print("---------------")
    vote_percentage = 0 

    for name, votes in vote_counts.items():
        vote_percentage = round(votes/count_voters*100)
        if votes > max_votes: 
            max_votes = votes
            winner = name
    
        print (name, vote_percentage,"%", votes)
    print("----------------------------")
    print ("Winner:", winner)

    with open(output,"w+") as text:
    
        text.write("------------------------------------------------\n")
        text.write("Election Results \n")
        text.write("-----------------------------------------------\n")
        text.write("Total Votes: ")
        text.write(str(count_voters)+"\n")
        text.write("------------------------------------------------\n")
        for name, votes in vote_counts.items():
            vote_percentage = round(votes/count_voters*100)
            text.write(name+" "+str(vote_percentage)+"%"+" "+ str(votes)+"\n")

        text.write("Winner:")
        text.write(winner+'\n')
        text.write("------------------------------------------------\n")
    
Counting_votes(filepath1,"Poll_winner_1.txt")
Counting_votes(filepath2,"Poll_winner_2.txt")