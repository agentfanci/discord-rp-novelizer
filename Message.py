class Message:
   

    def __init__(self, auth, dt, cnt, attatch, rxns, fil):
        self.author = auth
        self.date = dt
        self.content = cnt
        self.tags = {}
        self.channel = fil
        self.attachments = attatch
        self.reactions = rxns
    