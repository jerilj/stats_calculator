# import to read csv files
import csv

# list to hold numbers from out file
dataSet = []

def readCSV(csvFile):
    with open(csvFile) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            row = row.pop(0)
            row = int(row, base=10)
            dataSet.append(row)

    return dataSet

# you can pass in any csv file you want here
# readCSV('CSV_files/test.csv')