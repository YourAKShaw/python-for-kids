# Write a dictionary object which contains 5 words and their definitions.
'''
Example: 
words = {
    "cat": "A small domesticated carnivorous mammal.",
    ...
}
'''
# Accept a word from user and print its definition if found, else print "Word is absent in our dictionary".


def get_meaning_of_word(word):

    # dictionary of words with their meanings
    words = {
        "Herbivores": 'Animals that only eat plants.',
        "Carnivores": 'Animals that eat only flesh of other other animals.',
        "Omnivores":  'Animals that eat both flesh and plants.',
        "Scavengers": 'Animals that eat dead or decaying animals.',
        "Decomposers": 'Organisms that eat dead or deecaying plants and animals.'
    }

    return words.get(word, "Word is absent in our dictionary.")


word = input('Enter a word: ')
print(get_meaning_of_word(word))
