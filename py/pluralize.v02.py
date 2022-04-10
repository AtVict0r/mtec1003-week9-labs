def pluralize(word):
    if word.isalpha():
        if word.endswith('y'):
            return "The plural of " + word + " is " + word[:-1] + "ies"
        elif word.endswith('s'):
            return "The plural of " + word + " is " + word + "es"
        elif word.lower() == 'moose':
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
