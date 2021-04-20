vowels = "aieou"
sentence = "Javascript ne vaxtdan proqramlasdirma dili olub?"
totalVowels = 0

for i in sentence:
    if i in vowels:
        totalVowels += 1

print(totalVowels)
