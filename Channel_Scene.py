from Message import Message
import datetime

class Channel: 

    def __init__(self, nam):
        self.title = nam
        self.messages = []
        self.scenes = []

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
        for i in range(len(self.messages)-1):
             #won't do the last one! bc range is exclusive of the end value
             m = self.messages[i]
             nex = self.messages[i+1]
             #to look forward or backward...
             #gonna go with forward so the end is the special case I think- hmm it feels Weird but still

             #add current message to current proto-scene
             proto.append(m)
             #figure out how far away the next one is
             space = m.date - nex.date 

             if space < interval:
                  #next goes into current proto-scene
                  #so no need to do more things
                  pass
             else:
                 #if space >= than interval
                 #create scene with last proto-scene & put it in the scenes list
                 sce = Scene(proto)
                 scenes.append(sce)
                 proto = []
                 #make a new proto-scene and put it in as the current one, so the next message will go in it

         #handle last- do the scene end stuff
        m = self.messages[-1]
        proto.append(m)
        sce = Scene(proto)
        scenes.append(sce)
        self.scenes = scenes
        return scenes
        #return list of scenes



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
    
