from datetime import datetime
from Message import Message
import csv


class Novelizer:

    def __init__(self):
        #so we want a couple lists, right
        self.messages = []
        self.channels = []
        #we can add more later!
    
    def read_from_DCE_csv(self, filename):
        with open(filename, 'r') as csvfile: 
            # creating a csv reader object 
            csvreader = csv.reader(csvfile) 
      
            # extracting field names through first row 
            fields = next(csvreader) 
            print(fields)

            # extracting each data row one by one 
            m = "m"
            for row in csvreader: 
                #extract channel from filename as made by Discord Chat Exporter
                chan = filename.split(" ")[3]
                #extract date as put in by Discord Chat Exporter
                da =  datetime.strptime(row[2], '%d-%b-%y %I:%M %p')
                m = Message(row[1], da, row[3], row[4], row[5], chan )
                self.messages.append(m)
                print(m.channel, m.date, m.content)
            
            print(str(csvreader.line_num) + " messages read")


nov1 = Novelizer()

nov1.read_from_DCE_csv("Aquiline Estate - calarics-mind [].csv")