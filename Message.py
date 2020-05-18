from datetime import datetime



class Message:
   

    def __init__(self, auth, dt, cnt, attatch, rxns, chan):
        #just get the author
        self.author = auth
        #get the date- should already be an object- allows for more versatility
        self.date = dt
        #the message itself!
        self.content = cnt
        #tags- for the future, should be more ways to sort by
        self.tags = {"all"}
        #for more versatility, this will just get the date from the inputs
        self.channel = chan
        #get attatchments and reactions- shouldn't make too much difference, and I might want them
        self.attachments = attatch
        self.reactions = rxns
    
    def add_tag(self, tag):
        self.tags.add(tag)

    def __lt__(self, other):
        return self.date < other.date

    def __eq__(self, other):
        return self.date == other.date



