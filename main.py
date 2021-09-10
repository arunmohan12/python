import csv
filename = "test.csv"
s=1
with open(filename, 'rt') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    print("Rows at even positions are:")
    for row in csvreader:
        s=s+1
        if (s%2) == 0:
            print(row)

