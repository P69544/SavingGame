import random
import time
import createSave
STATS = "stats.txt"
  
# ----- CHECK IF SAVE EXISTS ----- #
save = open(STATS,"r")
for line in save:
  if line[:3] == "NEW":
    print("CREATING SAVE..")
    a = createSave.createCharacter()
    createSave.selectAttributes(a)
    break