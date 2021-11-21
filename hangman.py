correct=False
count=0
while correct==False:
    if count!=0:
        print("Incorrect Input. Try Again")
    print("Enter choice \n 1 for animal \n 2 for object")
    choice=int(input())
    if choice==1 or choice==2:
         correct=True
    count+=1
animal=("ant", "cat", "rat", "pig", "bee", "ape")
objectl=("van", "egg", "zip", "log", "sim")
import random as rnd
if choice==1:
    choice=rnd.choice(animal)
elif choice==2:
    choice=rnd.choice(objectl)
print(choice)
wordarr=["", "" , "" ]
guessarr=["_", "_", "_" ]
for i in range(3):
    wordarr[i]= choice[i]
def out():
    print("\n"*100)
    print(guessarr)
out()
def game(word):
    found=False
    chances=10
    guesslol=0
    while chances!=0:
        found=False
        guess = input("Please input guess: ")
        if len(guess)>1:
            print("invalid entry")
            continue
        for x in range(3):
            if guess==wordarr[x]:
                guessarr[x]=wordarr[x]
                found = True
                guesslol+=1
        if found==True:
            if guesslol==3:
                out()
                print("U win!!!!! YAYYYYY")
                break
            else:
                out()
                continue
        else: 
            chances-= 1
            out()
            print("chances left: " + str(chances))
            if chances==0:
                print("U lose :((")
                print("The word was " + choice)
                break
            else:
                continue
game(choice)