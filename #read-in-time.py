#read-in-time
import csv
from Message import Message
from datetime import datetime


filename = "Aquiline Estate - calarics-mind [].csv"

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
        #extract channel from filename as made by Discord Chat Exporter
        chan = filename.split(" ")[3]
        #extract date as put in by Discord Chat Exporter
        da =  datetime.strptime(row[2], '%d-%b-%y %I:%M %p')

        m = Message(row[1], da, row[3], row[4], row[5], chan )
        messages.append(m)
        print(m.channel, m.date, m.content)
    print(str(csvreader.line_num) + " messages read")


#testing code
dt = "23-May-19 11:26 AM"
date = datetime.strptime(dt, '%d-%b-%y %I:%M %p')
print(date)

fil ="Aquiline Estate - tetsu’s-airship [505976426995122179].csv"
channel = fil.split(" ")[3]
print(channel)
fil = "Aquiline Estate - agents-airship [].csv"
channel = fil.split(" ")[3]
print(channel)