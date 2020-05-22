from Message import Message
import datetime

class Channel: 

    def __init__(self, nam):
        self.title = nam
        self.messages = []

    def add_message(self, mes):
        self.messages.append(mes)
    
    def make_scenes(self, interval):
        #interval is the time interval to split scenes on! 
        #so it can be customized a bit for diff servers n such
        #should be a timedelta object- will take some doing 
        # should probs make a helper function to do that for people
        #oh boy this is the big thing!
        #well, a big thing
        scenes = []
        proto = []
        
        for m in self.messages:
            #if last
                #end current scene, return list of scenes
            #else: 
                #space = m.date - next.date
                #for a beginning: if space < interval, add to current proto-scene
                #if space > than interval, make new protp-scene & add this, create scene with last prot-scene & put it in the scenes list
                # all right I think that's what I wanna do, for now at least
                pass



class Scene:

    def __init__(self, mess_list):
        self.messages = mess_list
        self.start = mess_list[0].date
        self.end = mess_list[-1].date
        self.authors = {}
        self.characters = {}
        self.channel = mess_list[0].channel

    def get_authors(self):
        #if it's not empty return it
        #if empty, run through messages & make a set of the authors
        #make the authors instance variable private if i can manage that
        pass
    
