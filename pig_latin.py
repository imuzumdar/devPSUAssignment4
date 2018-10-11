def piglatin(text):
    text = text.split(" ")
    words = []
    for word in text:
        if word[0] in "aeiouy":
            word = word + "yay"
            words.append(word)
        else:
            new_word = ""
            count = 0
            for character in word:
                if character not in "aeiouy":
                    new_word += character
                    count += 1
                else:
                    break
            new_word = word[count:] + new_word + "ay"
            words.append(new_word)
    return " ".join(words)

print(piglatin("i cant speak pig latin"))
