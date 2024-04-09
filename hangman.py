word="school"
turns=5
letters="abcdefghijklmnopqrstuvwxyz"
word_guessed="______"
guesses=""
print("hello, Welcom to hangman!")
while(turns>0):
    print("You have",turns,"left")
    print("Available letters:",letters)
    ch=input("enter a letter:")
    if(ch in guesses):
        print("Letter already guesses")
        print()
        continue
    if(ch not in letters):
        print("enter a valied letter")
        print()
        continue
    if(ch in word):
        print("Good Guess:",end=" ")
        for i in range (len(word)):
            if(ch==word[i]):
                word_guessed=word_guessed[:i]+ch+word_guessed[i+1:]
        print(word_guessed)
    else:
        turns=turns-1
        print("Your word:",word_guessed)
    if(word_guessed==word):
        print("Congrats, You won!")
        break
    letters=letters.replace(ch,"")
    guesses+=ch
    print()
if(word!=word_guessed):
    print("You missed the word,Better luck next time")
    print("Correct word is:",word)
