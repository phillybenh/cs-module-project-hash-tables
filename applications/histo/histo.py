import re

def histogram(file_name):

    # Read in all the words in one go
    with open(file_name) as f:
        words = f.read()

    # Case should be ignored. Output keys must be lowercase.
    words = words.lower()
    """
    # Ignore each of the following characters:
    ignore = ['"', ':', ';', ',', '.', '-', '+',
              '=', '/', "\\", '|', '[', ']', '{',
              '}', '(', ')', '*', '^', '&']

    # for char in ignore:
    #     words = words.replace(char, "")
    """

    #implementing with regex
    words = re.sub(r'[^a-z\']', ' ', words).split()

    count = {}
    for w in words:
        if w not in count:
            count[w] = 0

        count[w] += 1
    sorted_words = {k: v for k, v in sorted(count.items(), \
        key=lambda item: item[1], reverse=True)}

    # find longest word
    longest_length = 0
    for word in sorted_words.keys():
        longest_word = ""
        if len(word) > len(longest_word):
            longest_word = word
        longest_length = len(longest_word)

    output_string = ""
    for element in sorted_words.items():
        spaces = longest_length - len(element[0]) + 2
        output = element[0] + (" " * spaces) + ("#" * element[1])
        output_string += output + '\n'
    return output_string
        

print(histogram("robin.txt"))
