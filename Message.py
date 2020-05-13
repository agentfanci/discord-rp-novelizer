from datetime import datetime



class Message:
   

    def __init__(self, auth, dt, cnt, attatch, rxns, fil):
        self.author = auth
        self.date = datetime.strptime(dt, '%d-%b-%y %I:%M %p')
        self.content = cnt
        self.tags = {"all"}
        self.channel = fil
        self.attachments = attatch
        self.reactions = rxns
    
    def add_tag(self, tag):
        self.tags.add(tag)



dt = "23-May-19 11:26 AM"
date = datetime.strptime(dt, '%d-%b-%y %I:%M %p')
print(date)
