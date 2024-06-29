from decrees import *
#import pickle
#from joblib import dump, load

def clearall():
  buildings.clear()
  families.clear()
  humans.clear()

def savehuman(hum):
  humans = humans

def savefamily(fam):
  humans = humans
  
def saving():
  with open("target.py", "r") as file:
    lines = file.readlines()

  with open("target.py", "w") as file:
    for line in lines:
        if line.strip() == "#family":
            file.write("x = 42\n")  # замена "x = 10" на "x = 42"
        else:
            file.write(line)