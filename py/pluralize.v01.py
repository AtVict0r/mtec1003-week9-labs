def pluralize(word):
    if word.isalpha():
        if word.lower() == 'moose':
            return "The plural of " + word + " is " + word
        elif word.lower() == 'mouse': 
            return "The plural of " + word + " is " + "mice"
        elif word.lower() == 'automaton':
            return "The plural of " + word + " is " + "automata"
        return "The plural of " + word + " is " + word + "s"
    return word + " is not a string"

wordToPluralize = str(input('Enter a word please: '))
pluralizedWord = pluralize(wordToPluralize)
print(pluralizedWord)
