print ("Welcome to my quiz game")
option = input("Do you want to start the game? ")

if option.lower() != "yes":
               quit()

print("Okay! Let's go!!")
score = 0

questionone = input("Who is the president of India? ")
if questionone.lower() == "ram nath kovind" :
               print ("correct")
               score +=1
else :
                              print ("incorrect")

questiontwo= input("Who is the prime minister of India? ")
if questiontwo.lower() == "narendra modi" :
               print ("correct")
               score +=1
else :
                              print ("incorrect")

questionthree= input("What is the national bird of India? ")
if questionthree.lower() == "peacock" :
               print ("correct")
               score +=1
else :
                              print ("incorrect")

questionfourth= input("What is the national animal of India? ")
if questionfourth.lower() == "tiger" :
               print ("correct")
               score +=1
else :
                              print ("incorrect")

print("Hurray!! your score is " +str(score)+ "/4")
