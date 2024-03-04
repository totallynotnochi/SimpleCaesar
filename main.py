def caesarcrypter(word, shift):
    '''

    Function that implements the Caesar Cypher given the shift, and the actual string itself

    :param word: The string that would be encrypted
    :param shift: The shift of the word that would be done (integer)
    :return: The encrypted message
    '''

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ModifiedWord = list(word)
    counter = 0
    shift = int(shift)

    for i in word:

        if((alphabet.find(i) + shift) > 25):
            ActualShift = (alphabet.find(i) + shift) - (int((alphabet.find(i) + shift)%26)*26)
        else:
            ActualShift = alphabet.find(i) + shift

        ModifiedWord[counter] = alphabet[ActualShift]
        counter += 1

    EncryptedWord = "".join(ModifiedWord)
    return(EncryptedWord)


print("Please enter a word, followed by the shift you want")
print(caesarcrypter(input(), input()))

