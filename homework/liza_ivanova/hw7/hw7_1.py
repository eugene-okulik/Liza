words = {"I": 3, "love": 5, "Python": 1, "!": 50}


def number_of_words(dictionary):
    for word, number in dictionary.items():
    i = 0
    print()
    while (i < number):
        if (i <= number):
            print(word, end="")
            i += 1
        else:
            break


number_of_words(words)
