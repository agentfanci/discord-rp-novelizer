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
        with open(filename, 'r', encoding='utf-8') as csvfile: 
            # creating a csv reader object 
            csvreader = csv.reader(csvfile) 
      
            # extracting field names through first row 
            fields = next(csvreader) 
            print(fields)

            # extracting each data row one by one 
            m = "m"
            #extract channel from filename as made by Discord Chat Exporter
            chan = filename.split(" ")[3]
            for row in csvreader: 
                
                #extract date as put in by Discord Chat Exporter
                da =  datetime.strptime(row[2], '%d-%b-%y %I:%M %p')
                m = Message(row[1], da, row[3], row[4], row[5], chan )
                self.messages.append(m)
                #print(m.channel, m.date, m.content)
            
            self.channels.append(chan)
            print(str(csvreader.line_num) + " messages read")

    def read_in(self, filename):
        self.read_from_DCE_csv(filename)
        #alias bc this is the only kind of reading in for the momen
    

nov1 = Novelizer()

nov1.read_from_DCE_csv("Aquiline Estate - calarics-mind [].csv")

nov1.read_in(r"C:\Users\A\Documents\Discord RP\Estate CSVs\Airships\Aquiline Estate - alex’s-airship [505579394828468224].csv")

