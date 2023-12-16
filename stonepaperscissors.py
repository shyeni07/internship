import random as rand
#importing random function as rand 
x = str(input("enter your choise from stone as s, paper as p and scissor as sc :- "))
#taking input from the user for stone paper or scissors
list = ["s","p","sc"]
#declaring a list for computer to make a choice
y = rand.choice(list)
#assigning a random string from the list to y using choice method
if (x==y) :
    print("whoops!! computer choice was",y,", its a tie!")
    #if user choice and computer choice is same its a tie
elif (x=="s" and y=="sc") :
    print("hurray!!computer choice was",y,", you win !! ;)")
    #if user chose stone and computer chose scissors then its a win for user
elif (x=="sc" and y=="p") :
    print("hurray!!computer choice was",y,", you win !! ;)")
    #if user chose scissors and computer chose paper then its a win for user
elif (x=="p" and y=="s") :
    print("hurray!!computer choice was",y,", you win !! ;)")
    #if user chose paper and computer chose stone then its a win for user
else :
    print("oops!!computer choice was",y,", you loss,better luck next time!")
    #else in every condition user is loosing