vowel = ["a", "e", "i", "o", "u"]
user_input = input("Enter a text : ").lower()

isVowel = False
for char in vowel:
    if char in user_input:
        isVowel = True
        break
    else:
        isVowel = False
if isVowel:
    print("There is vowel")
else:
    print("There is no vowel")
