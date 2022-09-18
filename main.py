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


lst1 = []
st1 = st2 = v = ""
hp1 = 0
word = random.choice(words)
print(word)

i = len(word)

word1 = ""

t1 = "_" + " "
st1 = t1*i
f = 0

for i in word:
  j = i + " "
  word1 = word1 + j

print("HangMan?")
print("Choice 1 : Play the Game.")
print("Choice 2 : See Instructions/Help.")
print("Choice 3 : Exit the game.")

c1 = int(input("Would you like to play the game?: "))

if c1 == 1 :
  print("Welcome the brave one.")
  print("Let's Start the Game!")
  print("=====================")
  for z in st1:
        lst1.append(z)
  while True:
    print(hp[hp1])
    print("=============================")
    print("Take the guess brave one.")
    print("=============================")
    e = 0
    g1 = input("Enter One Alphabet Only. : ")
    print("=============================")
    if len(g1) == 1:
      for i in word:
        st2 = ""
        d = 0
        if g1 == i:
          a = i
          lst1[e] = a
          for q in lst1:
            st2 = st2 + q
          print(st2)
          print("================================================")
          print("Congratulations! Brave one your guess was right.")
          print("================================================")
          e = e+2
          break
        else:
          e = e+2
          d = d+1
      if st2 == word1:
        print("========================================")
        print("Indeed you are a Brave One. Well Played!")
        print("========================================")
        quit()
      if d > 0:
          print("====================")
          print("Issh! Wrong guess...")
          print("====================")
          hp1 = hp1 + 1
          if hp1 == 6:
            print("=========================")
            print("Aww!! You lost.Try again.")
            print("=========================")
            print(hp[hp1])
            f= f + 1
    else:
      print("====================================================================")
      print("Trying to be oversmart with me? Enter only one alphabat at one time.")
      print("====================================================================")
    if f > 0:
      break




elif c1 == 2 :
  print("Hangman is a guessing game for two or more players. One player thinks of a word, phrase or sentence and the other tries to guess it by suggesting letters within a certain number of guesses. Originally a Paper-and-pencil game, there are now electronic versions.Every wrong guess will take you one step closer to death.")

else:
  print("Boo!! Coward")
  quit()
