import time

print("NOTE: Please enter all responses with lowercase letters. (with the exception of your name)")

time.sleep(2)

name = input("Greetings, Adventurer. What is your name? ")

time.sleep(2)

print("Ah yes,",name,".")

time.sleep(2)

while True:
  sex = input("Now, are you male or female? ")
  if sex == "male":
    time.sleep(2)
    print("A man I see.")
    break
  elif sex == "female":
    time.sleep(2)
    print("A woman I see.")
    break
  else:
    print("What? Can you repeat that? (not a valid input)")
  
time.sleep(2)

while True:
 race = input("And where do you stand, exactly? Are you with the intelligence of humankind? Maybe the sheer force of the ogres? How about the graceful elves? Possibly the resourceful foresters? Or maybe the resilient lizardpeople? (choose human, ogre, elf, forester, or lizardperson.) ")
 if race == "human":
   time.sleep(2)
   print("Ah, the humans. Not gifted physically but they are surely the most creatve and intelligent out of them all.")
   break
 elif race == "ogre":
   time.sleep(2)
   print("The ogres and their people are incredibly strong and tall, to make up for their sorely missed intelligence")
   break
 elif race == "elf":
   time.sleep(2)
   print("Gracious and dexterious, elves are majestic beings that, while physically weak, are foes to be reckoned with")
   break
 elif race == "forester":
   time.sleep(2)
   print("Living almost exclusively in forests, these creatures are cunning, witty, and resourceful, but not usually head on fighters.")
   break
 elif race == "lizardperson":
   time.sleep(2)
   print("Lizardpeople are hardy and resiliant, from living in the desert for most of their lives, with thick scales and a resistance to heat. On the other hand, traveling long           distances with them will undoubtbly test your patience.")
   break
 else:
   time.sleep(2)
   print("What? Can you repeat that? (not a valid input)")

time.sleep(2)

print("So, adventurer. If my facts are correct you are",name,", a",sex,race,". Is that correct?")

confirm = input("Type y to continue")
if confirm == "y":
  print("So, your story begins... (End of code 4 now)")
else:
    print("What? Can you repeat that? (not a valid input)")

