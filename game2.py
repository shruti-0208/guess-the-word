# Guess the word
import random
print("Lets guess the word->_ _ _ _ _\nYou will be given 5 Hints and 6 turns to guess the word\n")
c=1
def guess(A,b):
    d=input("Guess a letter of the word : ").lower()
    for i in range(5):
        if d==A[i]:
            b=b[:i]+d+b[i+1:]
    return b
        
fruits=['apple', 'mango', 'grape', 'peach', 'lemon', 'berry', 'olive', 'guava', 'papaw', 'lychee', 'melon', 'cherry', 'pears', 'plums', 'prune', 'raisin', 'dates', 'banjo', 'honey', 'apric']  
x=random.randint(1,3)   
A=fruits[x-1]
b='00000'
g=b
while c<=6 and A!=g :
    
    if c==1:
        print("Hint 1: It belongs to biotic factor of the environments.")
        g=guess(A,b)
        print(g,"\n")
        c+=1

    elif c==2:
        print("Hint 2: It is a tree.")
        g=guess(A,g)
        print(g,"\n")
        c+=1 

    elif c==3:
        print("Hint 3: It grows in hot and humid regions.")
        g=guess(A,g)
        print(g,"\n")
        c+=1

    elif c==4:
        print("Hint 4: It is a fruit.")
        g=guess(A,g)
        print(g,"\n")
        c+=1      

    elif c==5:
        print("Hint 5: It grows in summer.")
        g=guess(A,g)
        print(g,"\n")
        c+=1

    elif c==6:
        
        g=guess(A,g)
        print(g,"\n")
        
    

if A==g:
    print("The word was '",A,"'\n You won")  
else:
    print("The word was '",A,"'\n You lost") 
    