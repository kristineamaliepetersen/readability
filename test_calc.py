'''Author: Kristine Petersen. 
This program is for unit tests for the readability app Version: 1.0
'''

from langcalc import ari

    # Tests that the app can deal with extreme values. I.e. one of the longest and shortest paragraphs/sentences in the English language.
    # Tests that the rounded score calculation is an integer data type
    
    # character_count = count non-space characters
    # word_cound = count words seperated by spaces
    # sentence_count = count sentences by counting full stops

def test_longest_paragraph():
    # Using one of the longest recorded paragraph
    # According to The Guinness Book of Records the longest proper sentence is by William Faulkner in his novel 'Absalom, Absalom!' (1,287 words)
    character_count = 5836
    word_count = 1287
    sentence_count = 8
    score = 4.71 * (character_count / word_count) + 0.5 * (word_count / sentence_count) - 21.43
    assert score, ari_to_age[score] == '14, 24+'
    
   
def test_one_sentence_shortest_word():
    # Test that the function can deal with the shortest sentence in English.
    # According to google this is 'I am'.
    character_count = 3
    word_count = 2
    sentence_count = 1 
    score = 4.71 * (character_count / word_count) + 0.5 * (word_count / sentence_count) - 21.43
    assert score, ari_to_age[score] == '1, 5-6'
    
    
def test_output_is_integer():
    # Testing that the score data type, after rounding, is an integer
    character_count = 59
    word_count = 14
    sentence_count = 1 
    score = 4.71 * (character_count / word_count) + 0.5 * (word_count / sentence_count) - 21.43
    assert isinstance(round(score), int) 

