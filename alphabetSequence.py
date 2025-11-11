"""
you will be given a random string of letters
and tasked with returning them as a string of comma-separated sequences sorted alphabetically,
with each sequence starting with an uppercase character followed by n-1 lowercase characters,
where n is the letter's alphabet position 1-26.

Example
"ZpglnRxqenU" -> "Eeeee,Ggggggg,Llllllllllll,Nnnnnnnnnnnnnn,Nnnnnnnnnnnnnn,Pppppppppppppppp,Qqqqqqqqqqqqqqqqq,Rrrrrrrrrrrrrrrrrr,Uuuuuuuuuuuuuuuuuuuuu,Xxxxxxxxxxxxxxxxxxxxxxxx,Zzzzzzzzzzzzzzzzzzzzzzzzzz"

The string will include only letters.
The first letter of each sequence is uppercase followed by n-1 lowercase.
Each sequence is separated with a comma.
Return value needs to be a string.
"""

def alphabet_sequence(string):
    """
    my approach
    """

    #create mutable sequence of alphabets;
    #alphabets = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    #sequence_str = []
    #pos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    #assigning position to each alphabet;
    #pos_alphabet = dict(zip(alphabets, pos))
    #traversing the string;
    #for letter in string:
    #    pos = pos_alphabet.get(letter.upper()) - 1
    #    sequence = letter.upper() + letter.lower()*pos
    #    sequence_str.append(sequence)

    #sequence_str.sort()
    #','.join(sequence_str)

    #return str(sequence_str)

    """
    efficient approach
    """

    #creating an empty sequence;
    sequence = []
    for letter in string:
        #check if character is alphabet otherwise continue;
        if not letter.isalpha():
            continue

        #store upper and lower case in different variables;
        upper = letter.upper()
        lower = letter.lower()

        #get position of the alphabets;
        pos = ord(upper) - ord('A') + 1

        #add the character sequence in list;
        sequence.append(upper + lower*(pos - 1))

    #sort the list;
    sequence.sort()
    return ','.join(sequence)

print(alphabet_sequence("ZpglnRxqenU"))