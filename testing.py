
from Novelizer import *
from datetime import timedelta, datetime
#testing things

nov1 = Novelizer()

nov1.read_from_DCE_csv("Aquiline Estate - calarics-mind [].csv")
#nov1.read_in(r"C:\Users\A\Documents\Discord RP\Estate CSVs\Airships\Aquiline Estate - agents-airship [].csv")
#nov1.read_in(r"C:\Users\A\Documents\Discord RP\Estate CSVs\Main House\Aquiline Estate - front-hall [485893106194186277].csv")
#nov1.read_in(r"C:\Users\A\Documents\Discord RP\Estate CSVs\Main House\Aquiline Estate - terrace [485906652902719508].csv")

#nov1.read_in(r"C:\Users\A\Documents\Discord RP\Estate CSVs\Airships\Aquiline Estate - alex’s-airship [505579394828468224].csv")
#t = timedelta(hours = 1)
#sc = nov1.sort_all_scenes(t)

#print(len(nov1.scenes))
#print(nov1.scenes[-1])
#print(sc[0])
#test1 = open("estate_test_2.txt", "w", encoding='utf-8')
#for s in nov1.scenes:
    #print(s.channel)
   # print(s, file=test1)



nov2 = Novelizer()
#nov2.read_in(r'C:\Users\A\Documents\Discord RP\Estate CSVs\Main House\Aquiline Estate - terrace [485906652902719508].csv')
#nov2.read_in(r'C:\Users\A\Documents\Discord RP\Estate CSVs\Main House\Aquiline Estate - garden [485906948449894411].csv')
t= timedelta(hours = 0.5)

nov2.novelize(t, "estate_test_3.txt")
