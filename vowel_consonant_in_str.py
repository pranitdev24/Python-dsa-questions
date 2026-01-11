vowels=['a','o','i','u','e']
stering=str(input("enter the word "))

countVowels=0
countConso = 0
for chr in stering:
    if chr in vowels:
        print(chr,"is a vowel")
        countVowels+=1
    else:
        print(chr, "is a Conso")
        countConso +=1


print("vowels count: ", countVowels, "conso counts ", countConso)





