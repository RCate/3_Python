import os
import csv

filepath1 = "election_data_1.csv"
voter1 = []
current_candidate = []
candidates_list = []
vote_counts = {}
max_votes = 0
winner = ""

count_voters = 0
 
with open(filepath1,"r",newline="")as csvfile1:
    csvreader1 = csv.reader(csvfile1,delimiter=",")
    next(csvreader1, None)
    for row in csvreader1:
        count_voters += 1
        current_candidate = row[2] 
        if current_candidate not in candidates_list:
            candidates_list.append(current_candidate)
        #intializa dictionary to zero
        if current_candidate not in vote_counts: 
            vote_counts[current_candidate] = 1
        else:
            vote_counts[current_candidate]+= 1
    print("---------------")
    print("Total Votes1: ", count_voters)
    print("---------------")
    vote_percentage = 0 

for name in vote_counts:
    vote_percentage = (vote_counts[name]/count_voters*100)
    if vote_counts[name] > max_votes: 
        max_votes = vote_counts[name]
        winner = name
   
    print (name, vote_percentage,"%", vote_counts[name])
print("----------------------------")
print ("Winner:", winner)

import json

PyPoll_text_file1 =  "pyPoll_output1.txt"
with open(PyPoll_text_file1,"w+") as text:
  
    text.write("------------------------------------------------\n")
    text.write("Election Results \n")
    text.write("-----------------------------------------------\n")
    text.write("Total Votes: ")
    text.write(str(count_voters)+"\n")
    text.write("------------------------------------------------\n")
    for name in vote_counts:
        vote_percentage = round(vote_counts[name]/count_voters*100)
        text.write(name+" "+str(vote_percentage)+"%"+" "+ str(vote_counts[name])+"\n")

    text.write("Winner:")
    text.write(winner+'\n')
    text.write("------------------------------------------------\n")
    
import os
import csv

filepath2 = "election_data_2.csv"
voter1 = []
current_candidate = []
candidates_list = []
vote_counts = {}
max_votes = 0
winner = ""
count_voters = 0
 
with open(filepath2,"r",newline="")as csvfile2:
    csvreader2 = csv.reader(csvfile2,delimiter=",")
    next(csvreader2, None)
    for row in csvreader2:
        count_voters += 1
        current_candidate = row[2] 
        if current_candidate not in candidates_list:
            candidates_list.append(current_candidate)
        #intializa dictionary to zero
        if current_candidate not in vote_counts: 
            vote_counts[current_candidate] = 1
        else:
            vote_counts[current_candidate] += 1
    print("---------------")
    print("Total Votes2: ", count_voters)
    print("---------------")
    vote_percentage = 0 

for name in vote_counts:
    vote_percentage = round(vote_counts[name]/count_voters*100)
    if vote_counts[name] > max_votes: 
        max_votes = vote_counts[name]
        winner = name
    print (name, vote_percentage,"%", vote_counts[name])
print("----------------------------")
print ("Winner:", winner)




PyPoll_text_file2 =  "pyPoll_output2.txt"

with open(PyPoll_text_file2,"w+") as text:
    text.write("------------------------------------------------\n")
    text.write("Election Results \n")
    text.write("-----------------------------------------------\n")
    text.write("Total Votes: ")
    text.write(str(count_voters)+"\n")
    text.write("------------------------------------------------\n")
    for name in vote_counts:
        vote_percentage = round(vote_counts[name]/count_voters*100)
        text.write(name+" "+str(vote_percentage)+"%"+" "+ str(vote_counts[name])+"\n")

    text.write("Winner:")
    text.write(winner+'\n')
    text.write("------------------------------------------------\n")