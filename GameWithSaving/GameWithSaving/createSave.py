import random

STATS = "stats.txt"

def createCharacter():
  age = 0
  difficulty = 0
  permaDeath = ""
  # ----- Define variables for character ----- #
  name = input("Enter Character Name (MAX 10): ")[:10]
  while age > 80 or age < 16:
    age = int(input("Enter Character Age (16-80): "))
    
  while difficulty > 10 or difficulty < 1:
    difficulty = int(input("Enter Difficulty Number (1-10)"))
  
  while permaDeath.upper() != "Y" and permaDeath.upper() != "N":
    permaDeath = input("Permadeath? Y/N")[0]
  # ----- WRITE TO FILE ----- #
  file = open(STATS, "r")
  data = file.readlines()
  count = -1
  for item in data:
    count += 1
    if item[:4] == "[PS]":
        break
  
  # ----- APPLY TO DATA LIST ----- #
  for each in range(count+1, count+5):
    if data[each][:2] == "N=":
      data[each] = ("N="+name+"\n")
    elif data[each][:2] == "A=":
      data[each] = ("A="+str(age)+"\n")
    elif data[each][:2] == "D=":
      data[each] = ("D="+str(difficulty)+"\n")
    elif data[each][:3] == "PD=":
      data[each] = ("PD="+permaDeath.upper()+"\n")
    else:
      print("Unknown error when checking data")
  data[0] = "EXISTING\n"
  # ----- WRITE TO FILE ----- #
  file.close()
  file = open(STATS, "w")
  file.writelines(data)
      
def selectAttributes():
  file = open(STATS, "r")
  data = file.readlines()
  count = -1
  for item in data:
    count += 1
    if item[:6] == "[ATTR]":
        break
    
  for each in range(count+1, count+9):
    pass