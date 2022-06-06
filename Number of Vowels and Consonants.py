text = str(input("Enter the sentence and hit enter: "))
vowelList = ["A", "E", "I", "O", "U", "a", "e", "i", "o", 'u']
consonantList = ["B", "b", "C", "c", "D", "d", "F", "f", "G", "g", "H", "h", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"]
numOfVowels = 0
numOfConsonants = 0
for char in text:
    if char in vowelList:
        numOfVowels+=1
    if char in consonantList:
        numOfConsonants+=1
print("Vowels: " + str(numOfVowels))
print("Consonants: " + str(numOfConsonants))