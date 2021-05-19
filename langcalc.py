'''
This programme calculates the automated readability index (ARI) of a string, using the following formula:

4.71 * C/W + 0.5 * W/S - 21.43

'''
import string

# create dictionary to interpret scores
ari_to_age = {1:'5-6', 2:'6-7', 3:'7-9', 4:'9-10', 5:'10-11', 6:'11-12', 7:'12-13',
              8:'13-14', 9:'14-15', 10:'15-16', 11:'16-17', 12:'17-18', 13:'18-24', 14:'24+'}

# write function to calculate scores
def ari(s):
    # count sentences by counting full stops
    sentence_count = s.count('.')
    # account for a single sentence with no full stop at the end
    if sentence_count == 0:
        sentence_count = 1
    # remove punctuation
    s = s.translate(str.maketrans('', '', string.punctuation))
    # split string into individual words
    word_list = s.split()
    # count words
    word_count = len(word_list)
    # count non-space characters
    character_count = 0
    for word in word_list:
        character_count += len(word)
    # apply formula
    score = 4.71 * (character_count / word_count) + 0.5 * (word_count / sentence_count) - 21.43
    score = round(score)
    
    return score, ari_to_age[score]