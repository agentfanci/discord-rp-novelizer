from Message import Message
from datetime import datetime

class Channel: 

    def __init__(self, nam):
        self.title = nam
        self.messages = []

    def add_message(self, mes):
        self.messages.append(mes)
    
    def make_scenes(self):
        #oh boy this is the big thing!
        #well, a big thing
        scenes = []
        mess_list = []
        
        for m in self.messages:
            #if last
                #end current scene, return list of scenes
            #else: 
                #space = m.date - next.date
                #for a beginning: if space < 1 hr, add to current proto-scene
                #if space > than 1 hr, make new protp-scene & add this, create scene with last prot-scene & put it in the scenes list
                # all right I think that's what I wanna do, for now at least 
            
            





class Scene:

    def __init__(self, mess_list):
        self.messages = mess_list
        self.start = list[0].date
        self.end = list[-1].date
        self.authors = {}
        self.characters = {}
        self.channel = list[0].channel
    
