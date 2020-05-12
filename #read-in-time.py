#read-in-time
import csv


#class messageReader {
filename = "Aquiline Estate - calarics-mind.csv"

with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    fields = next(csvreader) 
    print(fields)

    # extracting each data row one by one 
    rows = []
    for row in csvreader: 
        rows.append(row) 

#}