import os

today = str(date.today())

if not(os.path.isdir(today)):
   os.mkdir(os.path.join(today))