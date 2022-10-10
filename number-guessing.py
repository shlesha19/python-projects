
import random

x = random.randint(0,11)
def random_number():
   x = random.randint(0,11)
   y = input("Guess a number between 1 to 10 ")
   guess = 0

   if y.isdigit():
    y = int(y)

   if y == x:
               print("Yess you guessed it correct!!" + "you got it in" + str(guess) + "guesses") 
               guess += 1
   else:     
               print("Better luck next time!!")

   while guess <= 5:
               z = input("Guess a number again ")
               
               if z.isdigit():
                  z = int(z)

               if z == x:
                   print("Yess you guessed it correct!!" + "you got it in " + str(guess) + " guesses")
                   break
               else:
                   print("Better luck next time!!")
                   guess += 1

               continue
   return

random_number()

while True:
      b = input("Do you want to see the correct number? ")
      print(b)
      if b.lower() == "yes":
               print(x)

      c = input("Do you want to play again? ")
      print(c)
      if c.lower() == "yes":
               random_number()
      else:
               quit()
