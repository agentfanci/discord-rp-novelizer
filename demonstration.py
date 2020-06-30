from Novelizer import *
from datetime import datetime, timedelta

t = timedelta(hours = 0.5)

nov1 = Novelizer()
nov1.read_in(r"C:\Users\A\Documents\Discord RP\Estate CSVs\Airships\Aquiline Estate - alex’s-airship [505579394828468224].csv")

nov1.novelize(t, "demonstration.txt")

