


from random import random


def newGame():
  guesses = []
  correctGuesses = 0
  currentQuestionNumber = 1
  for key in questios:
    print("-----------------------")
    print(key)
    for i in options[currentQuestionNumber - 1]:
      print(i)
    guess = input("Enter: (A, B, C ,D) ").upper()
    guesses.append(guess)
    
    correctGuesses += checkAns(questios.get(key),guess)
    currentQuestionNumber += 1
    
  displayScore(correctGuesses,guesses)

def checkAns(answer,guess):
  if(answer == guess):
    print('correct')
    return 1
  else:
    print('WRONG')
    return 0

def displayScore(correctGuesses,guesses):
  print("-----------------------")
  print("RESULT")
  print("-----------------------")
  print("Answers: ", end="")
  for i in questios:
    print(questios.get(i),end=" ")
  print("\n")
  print("GUESSES: ", end="")
  for i in guesses:
    print(i,end=" ")
  print("\n")
  
  score = int((correctGuesses/len(questios)) * 100)
  print("Your score is: "+ str(score)+"%" )
  
def playAgain():
  response = input("Do you still what to play? (yes or no) ").upper()
  if response == 'YES':
    # random.shuffle(options)
    return True
  else:
    return False
  


questios = {
  'who created python?: ':'A',
  'when was python created?: ':'B',
  'python is attributed?: ':'C',
  'Is the earth round?: ':'A'
}


options = [
  ['A. Guide Van Rossum','B. Elon Musk','C.Bill Gate','D. Mark Zuckeburg'],
  ['A. 1989','B. 1991','C. 2000','D. 2016'],
  ['A. Lonely Island','B. Smosh','C. Monty python','D. SNL'],
  ['A. True','B. False','C. Somtimes','Boths A and B']
]

newGame()

while playAgain():
  newGame()