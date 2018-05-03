import os
import csv

filepath1 = "budget_data_1.csv"

date1 = []
revenue1 = []
change1 = []
count_months = 0
total_change = 0
average_rev_change = 0

sum = 0.0
 
with open(filepath1,"r",newline="")as csvfile1:
    csvreader1 = csv.reader(csvfile1,delimiter=",")
    #next(csvreader1, None) - used to remove the header if that were needed in the data. 
    for row in csvreader1:
        date1.append(row[0])
        revenue1.append(row[1])
        count_months += 1
        sum += int(row[1])

print(count_months, sum) 
    
i = 0
j = 1
for i in range(count_months-1):
    delta = int(revenue1[j])-int(revenue1[i])
    change1.append(delta)
    i = i + 1
#i += 1
    j = j + 1    
    total_change = total_change + delta
    
average_rev_change = total_change/count_months


greatest_increase = 0
greatest_decrease = 0

for changeup in change1: 
    if greatest_increase < changeup: 
        greatest_increase = changeup
        greatindex = change1.index(changeup)
date_great = date1[greatindex + 1]



for changedown in change1: 
    if greatest_decrease > changedown: 
        greatest_decrease = changedown
        leastindex = change1.index(changedown)
date_least = date1[leastindex + 1]


print ("Financial Anaylsis Data Set 1")
print ("-----------------------------------------------")
print("Total Months: ", count_months)
print("Total Revenue: ", "$",sum)
print("Average Revenue Change: ", "$",average_rev_change)
print ("Greatest Increase in Revenue: ", date_great,"$" ,greatest_increase)
print ("Greatest Decrease in Revenue: ", date_least,"$",greatest_decrease)

PyBank_text_file1 =  "pybank_output1.txt"
with open(PyBank_text_file1,"w+") as text:
  
    text.write("------------------------------------------------\n")
    text.write("Financial Analysis Data Set 1\n")
    text.write("-----------------------------------------------\n")
    text.write("Total Months: ")
    text.write(str(count_months)+"\n")
    text.write("Total Revenue: ")
    text.write("$")
    text.write(str(sum)+'\n')
    text.write("Average Revenue Change: ")
    text.write("$")
    text.write(str(average_rev_change)+'\n')
    text.write("Greatest Increase in Revenue: ")
    text.write("$")
    text.write(str(greatest_increase)+'\n')
    text.write("Greatest Decrease in Revenue: ")
    text.write("$")
    text.write(str(greatest_decrease))

import os
import csv

filepath2 = "budget_data_2.csv"

date2 = []
revenue2 = []
change2 = []
count_months = 0
total_change = 0
average_rev_change = 0
delta = 0

sum = 0.0
 
with open(filepath2,"r",newline="")as csvfile1:
    csvreader1 = csv.reader(csvfile1,delimiter=",")
    next(csvreader1, None)  
    for row in csvreader1:
        date2.append(row[0])
        revenue2.append(row[1])
        count_months += 1
        sum += int(row[1])

    
i = 0
j = 1
for i in range(count_months-1):
    delta = int(revenue2[j])-int(revenue2[i])
    change2.append(delta)
    i = i + 1
#i += 1
    j = j + 1    
    total_change = total_change + delta
    
average_rev_change = total_change/count_months


greatest_increase = 0
greatest_decrease = 0

for changeup in change2: 
    if greatest_increase < changeup: 
        greatest_increase = changeup
        greatindex = change2.index(changeup)
date_great = date2[greatindex + 1]



for changedown in change2: 
    if greatest_decrease > changedown: 
        greatest_decrease = changedown
        leastindex = change2.index(changedown)
date_least = date2[leastindex + 1]

print("------------------------------------------------")
print ("Financial Analysis Data Set 2")
print ("-----------------------------------------------")
print("Total Months: ", count_months)
print("Total Revenue: ", "$",sum)
print("Average Revenue Change: ", "$",average_rev_change)
print ("Greatest Increase in Revenue: ", date_great,"$" ,greatest_increase)
print ("Greatest Decrease in Revenue: ", date_least,"$",greatest_decrease)



PyBank_text_file2 =  "pybank_output2.txt"
with open(PyBank_text_file2,"w+") as text:
  
    text.write("------------------------------------------------\n")
    text.write("Financial Analysis Data Set 2\n")
    text.write("-----------------------------------------------\n")
    text.write("Total Months: ")
    text.write(str(count_months)+"\n")
    text.write("Total Revenue: ")
    text.write("$")
    text.write(str(sum)+'\n')
    text.write("Average Revenue Change: ")
    text.write("$")
    text.write(str(average_rev_change)+'\n')
    text.write("Greatest Increase in Revenue: ")
    text.write("$")
    text.write(str(greatest_increase)+'\n')
    text.write("Greatest Decrease in Revenue: ")
    text.write("$")
    text.write(str(greatest_decrease))





        