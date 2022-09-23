import random


words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra ').split()

hp = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  +---+
THANKS|
      |
 \O/  |
  |   |
 / \  |
=========''']

word1 = word2 = j = st1 = ""

hpi = f = 0
word = random.choice(words)

for i in word:
  i = i + " "
  word1 = word1 + i


i = len(word)
j = "_" + " " 
word2 = j*i


lst1 = []
lst2 = []

for i in word2:
  lst1.append(i)

for k in word1:
  lst2.append(k)


print("HangMan?")
print("Choice 1 : Play the Game.")
print("Choice 2 : See Instructions/Help.")
print("Choice 3 : Exit the game.")

c1 = int(input("Would you like to play the game?: "))

if c1 == 1 :
  print("=====================")
  print("Welcome the brave one.")
  print("=====================")
  print("=====================")
  print("Let's Start the Game!")
  print("=====================")

  while True:
    print(hp[hpi])
    print("=============================")
    print(word2)
    print("=============================")
    print("Take the guess brave one.")
    print("=============================")
    print("=============================")
    input1 = input("Enter One Alphabet Only. : ").lower()
    print("=============================")
    if len(input1) == 1:
      for i in lst2:
        d = 0
        if i == input1:
          lst3 = [a for a, x in enumerate(lst2) if x == input1]
          for k in lst3:
              st1 = ""
              lst1[k] = input1
              for q in lst1:
                st1 = st1 + q
          word2 = st1
          print("================================================")
          print("Congratulations! Brave one your guess was right.")
          print("================================================")
          break
        else:
          d = d + 1
    else:
      print("====================================================================")
      print("Trying to be oversmart with me? Enter only one alphabat at one time.")
      print("====================================================================")
    if st1 == word1:
            print(hp[7])
            print(word2)
            print("========================================")
            print("Indeed you are a Brave One. Well Played!")
            print("========================================")
            quit()
    if d == 1:
        print("====================")
        print("Issh! Wrong guess...")
        print("====================")
        hpi = hpi + 1
        if hpi == 6:
          print("=========================")
          print("Aww!! You lost.Try again.")
          print("=========================")
          print(hp[hpi])
          f= f + 1
    if f > 0:
      break

elif c1 == 2 :
  print("Hangman is a guessing game for two or more players. One player thinks of a word, phrase or sentence and the other tries to guess it by suggesting letters within a certain number of guesses. Originally a Paper-and-pencil game, there are now electronic versions.Every wrong guess will take you one step closer to death.")

else:
  print("Boo!! Coward")
  quit()



