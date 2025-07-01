def hangedman(wrong):
   spaces="                                                            "
   print(f"{spaces}-------")
   print(f"{spaces}|     |")
   if wrong >= 1:
      print(f"{spaces}|     O")
      if wrong==2:
        print(f"{spaces}|     | ")
        
      elif wrong==3:
        print(f"{spaces}|    /| ")

      elif wrong==4 or wrong==5 or wrong==6:
         print(f"{spaces}|    /|\ ")
      else:
         print(f"{spaces}|       ")
         
      if wrong<=4:
         print(f"{spaces}|       ")
      else:
         if wrong==5:
            print(f"{spaces}|    / ")
         elif wrong==6:
            print(f"{spaces}|    / \ ")
           
   else:
      print(f"{spaces}|    ")
      print(f"{spaces}|    ")   

   print(f"{spaces}|_________")

import random

spaces="                                                            "
possible_phrases = ["Hrick is a Super Meanie", "NYANYANYA", "Potatoes are delicious"]
current= random.choice(possible_phrases)
print("Here's the line, try to guess it!")

hyphenstring=''
numletters=0
for c in current:
   if (ord(c) >= ord('A') and ord(c)<=ord('Z')) or (ord(c)>=ord('a') and ord(c)<=ord('z')):
      hyphenstring=hyphenstring+"_"
      numletters+=1
   else:
       hyphenstring+=c

print(hyphenstring)
print()
found=0
wrong=0
max_errors=6
howmanyletters=1
letters=[]
while found<numletters and wrong<max_errors:
     currentletter=input(f"your {howmanyletters}° letter: ")
     while currentletter<'A' or currentletter>'z' or (currentletter>'Z' and currentletter<'a'):
          currentletter=input("Don't be silly, write a LETTER!:")
     currentletter=currentletter.lower()
     if currentletter in letters:
         print("Wrong! Letter already mentioned")
         wrong+=1
         hangedman(wrong)
         continue
     else:
        letters.append(currentletter)
        indexes= []
        i=-1
        for ch in current:
           i+=1
           if currentletter == ch or chr(ord(currentletter)-32) == ch:
             found+=1
             indexes.append(i)
         
        if len(indexes)==0:
          wrong+=1
          print("Aww, the letter is not present!")
          print(hyphenstring)
        else:
           for ind in indexes:
                hyphenstring=hyphenstring[:ind] + current[ind] + hyphenstring[ind+1:]
           num=len(indexes)
           if num==1:
              print("You have found 1 letter!")
           else:
              print(f"You have found {num} letters!")
           print()
           print(hyphenstring)
        hangedman(wrong)
     howmanyletters+=1
   
if found==numletters:
   print("You won!")
else:
   print()
   print()
   print("6 mistakes done. You have been hanged :(")
   hangedman(wrong)
         
   

         
         
