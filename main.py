import os
import csv

bank_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

result_row = []

with open(bank_csv, "r",encoding="utf-8-sig") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #skip the header
    csv_header = next(csv_reader)
    print(f"header : {csv_header}")
    print("-----------------------------")
    
    def count(csv_reader):
        t = len(csv_reader)
        total = 0
        for p in csv_reader:
            total = total + p
        return total 
    print(count(csv_reader))

    for m in csv_reader:
        print(f"Total profits/losses is {sum(m[2])}")

    def average(csv_reader):
        n = len(csv_reader)
        total = 0
        for x in csv_reader:
            total = total + x
        return total / n
    print(average(csv_reader))
           
    for y in csv_reader:
        if float(y[2]) >=0:  
            print(max(y))
        else:
            print(min(y))

output_file = "results.csv"
with open(output_file, "w") as file:
    csv_writer = csv.writer(file)

    csv_writer.writerows(output_file)




