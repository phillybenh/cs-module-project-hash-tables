def letter_count(string):
    counts = {}

    for count in string:
        if count not in counts:
            counts[count] = 0

        counts[count] += 1

        """
        # another way to write this
        if count in counts:
            counts[count] += 1
        else:
            counts[count] = 1
        """

    return counts



print(letter_count("aabbcaacb"))