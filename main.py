import os
import csv

poll_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

result_row = []

with open(poll_csv , "r",encoding="utf-8-sig") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #skip the header
    csv_header = next(csv_reader)
    print(f"header : {csv_header}")
    print("-----------------------------")
    
    def count(csv_reader):
        n = len(csv_reader)
        total = 0
        for x in csv_reader:
            total = total + x
        return total 
    print(count(csv_reader))

    myList = [poll_csv]
    print(myList[3])

    for y in csv_reader:
        if float(y[3]) == "Khan":  
            print(f' Khan has {count(csv_reader)} votes')
        if float(y[3]) =="Li":  
            print(f' Li has {count(csv_reader)} votes')
        if float(y[3]) =="Correy":  
            print(f' Correy has {count(csv_reader)} votes')


output_file = "results.csv"
with open(output_file, "w") as file:
    csv_writer = csv.writer(file)

    csv_writer.writerows(output_file)
  



    

            









