def titlize(sentence):
    words = sentence.split()
    print(words)
    new_words = []

    for word in words:
        if len(word) > 2:
            word = word.capitalize()
            print(word)
        new_words.append(word)
        print(new_words)

    return ' '.join(new_words)

title = 'hello world of programming'
print(titlize(title))