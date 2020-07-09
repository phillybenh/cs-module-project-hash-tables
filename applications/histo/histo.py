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
    return count

print(histogram("robin.txt"))
