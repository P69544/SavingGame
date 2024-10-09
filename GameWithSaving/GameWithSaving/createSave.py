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
  return age

def selectAttributes(age):
  file = open(STATS, "r")
  data = file.readlines()
  count = -1
  for item in data:
    count += 1
    if item[:6] == "[ATTR]":
        break
  
  skillPoints = 20
  selecting = True
  adding = -1
  
  # ----- Starter values for aging ----- #
  if age >= 60:
    print("Due to your age, you are a lot wiser, but your strength, dexterity and agility took a significant hit!")
    strength = 2
    dex = 2
    ag = 1
    wis = 6
  elif age <= 25:
     print("Due to your age, your strength and agility are significantly boosted, and your dexterity mildly boosted too!\nAt the cost of your wisdom...")
     strength = 5
     dex = 4
     ag = 6
     wis = 1
  elif age == 16:
     print("Due to your age, your dexterity and agility are significantly boosted!\nAt the cost of your wisdom...")
     strength = 3
     dex = 6
     ag = 6
     wis = 1
  else:
     print("Your age is about average. All stats start at 3.")
     strength = 3
     dex = 3
     ag = 3
     wis = 3
  luck = 3
  
  # ----- Alloting skill points ----- #
  while selecting:
    print("Note: If you have no more, just enter zero until it continues.")
    while adding > skillPoints or adding < 0:
        print("Skill Points:",skillPoints)
        print("Current Level:",strength)
        adding = int(input("Enter Strength: "))
    strength += adding
    skillPoints -= adding
    adding = -1
    
    while adding > skillPoints or adding < 0:
        print("Skill Points:",skillPoints)
        print("Current Level:",dex)
        adding = int(input("Enter Dexterity: "))
    dex += adding
    skillPoints -= adding
    adding = -1
    
    while adding > skillPoints or adding < 0:
        print("Skill Points:",skillPoints)
        print("Current Level:",ag)
        adding = int(input("Enter Agility: "))
    ag += adding
    skillPoints -= adding
    adding = -1
    
    while adding > skillPoints or adding < 0:
        print("Skill Points:",skillPoints)
        print("Current Level:",luck)
        adding = int(input("Enter Luck: "))
    luck += adding
    skillPoints -= adding
    adding = -1
    
    while adding > skillPoints or adding < 0:
        print("Skill Points:",skillPoints)
        print("Current Level:",wis)
        adding = int(input("Enter Wisdom: "))
    wis += adding
    skillPoints -= adding
    
    adding = -1
    if skillPoints == 0:
       selecting = False
  
  print(strength, dex, ag, luck, wis)
  for each in range(count+1, count+7):
    if data[each][:2] == "S=":
        data[each] = ("S="+str(strength)+"\n")
    elif data[each][:2] == "D=":
        data[each] = ("D="+str(dex)+"\n")
    elif data[each][:2] == "A=":
        data[each] = ("A="+str(ag)+"\n")
    elif data[each][:2] == "L=":
        data[each] = ("L="+str(luck)+"\n")
    elif data[each][:2] == "W=":
        data[each] = ("W="+str(wis)+"\n")
    else:
       print("Error")
    
  # ----- Curse + Blessing Selection goes here ----- #