from datetime import datetime



class Message:
   

    def __init__(self, auth, dt, cnt, attatch, rxns, fil):
        #just get the author
        self.author = auth
        #turn the date into a datetime object
        self.date = datetime.strptime(dt, '%d-%b-%y %I:%M %p')
        #the message itself!
        self.content = cnt
        #tags- for the future, should be more ways to sort by
        self.tags = {"all"}
        #extract the channel name from the file name- made for Discord Chat Exporter Excel-format CSVs
        self.channel = fil.split(" ")[3]
        #get attatchments and reactions- shouldn't make too much difference, and I might want them
        self.attachments = attatch
        self.reactions = rxns
    
    def add_tag(self, tag):
        self.tags.add(tag)

    def __lt__(self, other):
        return self.date < other.date



dt = "23-May-19 11:26 AM"
date = datetime.strptime(dt, '%d-%b-%y %I:%M %p')
print(date)

fil ="Aquiline Estate - tetsu’s-airship [505976426995122179].csv"
channel = fil.split(" ")[3]
print(channel)
fil = "Aquiline Estate - agents-airship [].csv"
channel = fil.split(" ")[3]
print(channel)