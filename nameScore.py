#What's my name score?
"""
The 26 letters of the English alphabets are randomly divided into 5 groups of 5 letters with the remaining letter being ignored. Each of the group is assigned a score of more than 0. The ignored letter always has a score of 0.

With this kata, write a function to work out the score of a name that is passed to the function.

The output should be returned as an object:

{'Mary Jane':20}
"""

import random
#create a  scoring system;
def score_system():
    alphabets = list("ABCDEEFGHIJKLMNOPQRSTUVWXYZ")
    random.shuffle(alphabets)

    #group scores;
    group_score = [1, 2, 3, 4, 5]

    letter_score = {}
    start_index = 0

    for score in group_score:
        #assigning groups;
        group_letters = alphabets[start_index:start_index + 5]

        #assigning group scores;
        for letter  in group_letters:
            letter_score[letter] = score

        start_index += 5

    ignored_letter = alphabets[-1]
    letter_score[ignored_letter] = 0

    print("--- Scoring System Generated ---")
    print(f"Group 1 (Score {group_score[0]}): {', '.join(alphabets[0:5])}")
    print(f"Group 2 (Score {group_score[1]}): {', '.join(alphabets[5:10])}")
    print(f"Group 3 (Score {group_score[2]}): {', '.join(alphabets[10:15])}")
    print(f"Group 4 (Score {group_score[3]}): {', '.join(alphabets[15:20])}")
    print(f"Group 5 (Score {group_score[4]}): {', '.join(alphabets[20:25])}")
    print(f"Ignored Letter (Score 0): {ignored_letter}")
    print("----------------------------------\n")

    return letter_score

score_map = score_system()

def name_score(name):
    total_score = 0

    for char in name.upper():
        total_score += score_map.get(char, 0)

    return {name: total_score}

print("--- Score Calculations ---")
print(name_score('Mary Jane'))
print(name_score('Python'))
print(name_score('Alphabet'))
print(name_score('This is a test 123!'))




