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
=========''']



st1 = ""
hp1 = 0
word = random.choice(words)
print(word)

i = len(word)

t1 = "_" + " "
st1 = t1*i

print("HangMan?")
print("Choice 1 : Play the Game.")
print("Choice 2 : See Instructions/Help.")
print("Choice 3 : Exit the game.")

c1 = int(input("Would you like to play the game?: "))

if c1 == 1 :
  print("Welcome the brave one.")
  print("Let's Start the Game!")
  while True:
    print(st1)
    print(hp[hp1])
    print("Take the guess the brave one.")
    g1 = input()
    if len(g1) == 1:
      for i in word:
        d = 0
        if g1 == i:
          a = i
          st1 = st1.replace("_",a) # PROBLEM
          print("Congratulations! Brave one your guess was right.")
          break
        else:
          d = d+1
      if d > 0:
          print("Issh! Wrong guess...")
          hp1 = hp1 + 1

    else:
      print("Trying to be oversmart with me? Enter only one alphabat at one time.")


elif c1 == 2 :
  print("Hangman is a guessing game for two or more players. One player thinks of a word, phrase or sentence and the other tries to guess it by suggesting letters within a certain number of guesses. Originally a Paper-and-pencil game, there are now electronic versions.Every wrong guess will take you one step closer to death.")

else:
  print("Boo!! Coward")
  quit()