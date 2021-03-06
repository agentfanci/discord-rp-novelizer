from datetime import datetime
from datetime import timedelta
import csv
import os



class Novelizer:

    def __init__(self):
        #so we want a couple lists, right
        self.messages = []
        self.channels = []
        self.scenes = []
        #we can add more later!
    
    def read_from_DCE_csv(self, filename):
        #filename variable should actually be a file path unless your novelizer is in the same directory
        with open(filename, 'r', encoding='utf-8') as csvfile: 
            # creating a csv reader object 
            csvreader = csv.reader(csvfile) 
      
            # extracting field names through first row 
            fields = next(csvreader) 

            # extracting each data row one by one 
            m = "m"
            #extract channel from filename as made by Discord Chat Exporter
            chan = filename.split(" ")[-2]
            print(chan)
            current_channel = Channel(chan)
            for row in csvreader: 
                
                #extract date as put in by Discord Chat Exporter
                da =  datetime.strptime(row[2], '%d-%b-%y %I:%M %p')
                #make message object
                m = Message(row[1], da, row[3], row[4], row[5], chan )
                #add to novelizer messages
                self.messages.append(m)
                #and to its channel
                current_channel.add_message(m)
                #print(m.channel, m.date, m.content)
            
            self.channels.append(current_channel)
            
            print(str(csvreader.line_num) + " messages read")

    def read_in(self, filename):
        self.read_from_DCE_csv(filename)
        #alias bc this is the only kind of reading in for the moment
    
    def sort_all_scenes(self, time):
        enes = []
        for ch in self.channels:
            sce = ch.make_scenes(time) #ask each channel to split iteslf into scenes
            enes = enes + sce #make a master list of all scenes from all channels 
        enes.sort() #sort scenes (they sort by start time)
        self.scenes = enes #apply the list to the scenes list
        return enes #and also return it

    def novelize(self, min_time_between_scenes, output_file):
        t = min_time_between_scenes 
        fil = open(output_file, "w", encoding='utf-8') #create or open requested file
        self.sort_all_scenes(t) 
        for s in self.scenes:
            print(s, file = fil) #print scenes in order to file
            #print("\n", file = fil) #add line between scenes
            print("------------", file = fil) #add divider between scenes
        return fil

    def read_from_folder_of_DCE_csv(self, folderpath):
        
        #code modified from https://realpython.com/working-with-files-in-python/#traversing-directories-and-processing-files
        for dirpath, dirnames, files in os.walk(folderpath):
            print(f'Reading directory: {dirpath}')

            for file_name in files:
                filepath = os.path.join(dirpath, file_name)
                self.read_from_DCE_csv(filepath)
    



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
        #should be a timedelta object
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
             space = nex.date - m.date 

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

    def __lt__(self, other):
        return self.start < other.start #sorts by start time
    
    def __eq__(self, other):
        return self.start == other.start

    def __str__(self):
        lis = []
        for m in self.messages:
            st = m.author + ": " + m.content  #make each message into author: content
            lis.append(st)
        out_st = self.channel + '\n'+'\n'.join(lis) #make a string with a newline between each message
        return out_st

    def __repr__(self):
        st = "Channel: " + self.channel + ", Start: " + self.start #identify scenes by start time and channel- no other scene should have both of them the same. 
        return st

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




    



