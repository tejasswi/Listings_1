import sys
VOWELS = "aeiou"

while True:
    word = input("Type word and get its pig Latin translation:")
    if word[0] in VOWELS:
        pig_Latin = word+'way'
    else:
        pig_Latin = word[1:]+word[0]+ "ay"
    print()
    print(f'{pig_Latin}.file = sys.stderr')
    try_again = input("\n\nTry again?(Press Enter else n to stop)\n")
    if try_again.lower() == "n":
        sys.exit()
        