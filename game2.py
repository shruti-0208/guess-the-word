import random

def guess(A, b):
    d = input("Guess a letter of the word: ").lower()
    for i in range(len(A)):
        if d == A[i]:
            b = b[:i] + d + b[i+1:]
    return b

def play_game():
    print("\nLet's guess the word->_ _ _ _ _")
    print("You will be given 5 hints and 6 turns to guess the word!\n")

    fruits = ['apple', 'mango', 'grape', 'peach', 'lemon', 'berry', 'olive', 'guava', 
              'papaw', 'lychee', 'melon', 'cherry', 'pears', 'plums', 'prune', 'raisin', 
              'dates', 'banjo', 'honey', 'apric']
    hints_dict = {
        'apple': ["It is a popular fruit often associated with health.", 
                  "It is red, green, or yellow in color.", 
                  "It is commonly eaten raw or used in pies.", 
                  "It grows on trees in temperate climates.", 
                  "It is famously linked with Isaac Newton."],
        'mango': ["It is known as the 'king of fruits'.", 
                  "It is a tropical fruit with a sweet taste.", 
                  "It is yellow or orange in color when ripe.", 
                  "It is commonly used in smoothies and juices.", 
                  "It grows in summer and is popular in India."],
        'grape': ["It is a small, round fruit.", 
                  "It comes in green, red, or purple varieties.", 
                  "It is used to make wine and raisins.", 
                  "It grows in clusters on vines.", 
                  "It is juicy and often eaten fresh."],
        'peach': ["It has a soft, fuzzy skin.", 
                  "Its flesh is sweet and juicy.", 
                  "It is typically pinkish-orange in color.", 
                  "It is a stone fruit.", 
                  "It is often used in desserts and jams."],
        'lemon': ["It is yellow in color and sour in taste.", 
                  "It is often used in drinks and as a seasoning.", 
                  "It is high in vitamin C.", 
                  "It has a thick, textured rind.", 
                  "It is a citrus fruit."],
        
    }

    A = random.choice(fruits)
    b = '0' * len(A)
    g = b
    c = 1

    hints = hints_dict.get(A, [
        "Hint 1: It is a fruit.",
        "Hint 2: It grows on trees, shrubs, or vines.",
        "Hint 3: It is sweet, tangy, or juicy.",
        "Hint 4: It is commonly used in food or drinks.",
        "Hint 5: Its name has 5 or more letters."
    ])

    while c <= 6 and A != g:
        if c <= 5:
            print(hints[c-1])
        g = guess(A, g)
        print(g, "\n")
        if g == A:
            print(f"The word was '{A}'.\nYou won!")
            break
        c += 1

    if A != g:
        print(f"The word was '{A}'.\nYou lost.")

while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thanks for playing! Goodbye!")
        break
