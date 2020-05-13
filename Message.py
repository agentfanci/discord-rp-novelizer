import datetime



class Message:
   

    def __init__(self, auth, dt, cnt, attatch, rxns, fil):
        self.author = auth
        self.date = dt
        self.content = cnt
        self.tags = {"all"}
        self.channel = fil
        self.attachments = attatch
        self.reactions = rxns
    
    def add_tag(self, tag):
        self.tags.add(tag)
    
    def to_24_time_and_date(self, dt):
        #format: "23-May-19 11:26 AM"
        #so how to convert
        date, time, merd = self.dt.split(" ")



    
