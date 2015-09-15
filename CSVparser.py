import csv

data = open(raw_input("What is the file name?" ))

for row in csv.reader(data):
    print(row)
