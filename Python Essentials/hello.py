import random

question = input("Ask Magic 8 ball a question")

answer = random.randint(1,8)

if answer == 1:
    print("It is certain")
    
elif answer == 2:
    print("outlook good")
    
elif answer == 3:
    print("You may rely on it")
    
elif answer == 4:
    print("Ask Again Later")
    
elif answer == 5:
    print("Concentrate & ask again")
    
elif answer == 6:
    print("try again")
    print("Smoke a j")
    
elif answer == 7:
    print("chill")
    
elif answer == 8:
    print("stick it to the man")
    
else:
    print ("That's not a question")
    
print("The End")
    

