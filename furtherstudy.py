words = set()

animals = set(['python', 'zebra'])

def words_in_common(words1, words2):
    """Return a list of unique words that appear in `words1` and `words2`

    Arguments:
        words1 (list): A list of words
        words2 (list): Another list of words

    Returns:
        list: A list of unique words
    """

    words1_set = set(words1)
    words2_set = set(words2)

    result = set()

    for word in words1_set:
        if word in words2_set:
            result.add(word)

    return list(result)


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
      Since "bagon" ends with n, find the *first* word starting
      with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
      been used, it can't be used again --- so we'll never get to
      use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
      Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    # Get first word and remove from consideration; add it to our output
    output = [names.pop(0)]

    first_letter_to_words = {}

    # Make a dictionary of {first-letter: [words-starting-with-that-letter]}
    # Note that we could also use .setdefault here
    for name in names:

        if name[0] not in first_letter_to_words:
            first_letter_to_words[name[0]] = [name]

        else:
            first_letter_to_words[name[0]].append(name)

    # Chain together words until we run out
    while True:

        # Our starting letter will be the last letter of last word
        start_letter = output[-1][-1]

        # If there are no candidate words, we're done
        if not first_letter_to_words.get(start_letter):
            break

        # Get the first word with that letter and remove it
        word = first_letter_to_words[start_letter].pop(0)
        output.append(word)

    return output


if __name__ == '__main__':
    print(kids_game(["apple", "berry", "cherry"]))
    print(kids_game(["noon", "naan", "nun"]))