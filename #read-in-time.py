#read-in-time
import csv
from Message import Message


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
    messages = []
    m = "m"
    for row in csvreader: 
        rows.append(row) 
        #m = Message(row.Author, row.Date, row.Content, row.Attatchments, row.Reactions, filename)
        m = Message(row[1], row[2], row[3], row[4], row[5], filename)
        messages.append(m)
    print(str(csvreader.line_num) + " messages read")

#}