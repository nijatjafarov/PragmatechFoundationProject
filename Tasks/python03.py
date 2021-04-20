alphabet = "abcdefghijklmnopqrstuvwxyz"
sentence = "Javascript ne vaxtdan proqramlasdirma dili olub?"
letters = 0

for i in sentence.lower():
    if i in alphabet:
        letters += 1
print(letters)
