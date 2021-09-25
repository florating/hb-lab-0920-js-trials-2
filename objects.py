def count_words(phrase):
    """Return a dictionary of each word and the no. of times they appear.

    You can assume that `phrase` does not contain any punctuation and that
    each word is separated with a space.

    Arguments:
        phrase (str): A string of space-separated words

    Returns:
        dict: {word: # of times word appears in `phrase`}
    """

    word_counts = {}

    for word in phrase.split(' '):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


def print_melon_at_price(price):
    """Return the list of melons that cost `price`.

    Arguments:
        price (float)

    Returns:
        list: List of melons that cost `price`
        None: If there are no melons that cost `price`
    """

    melon_prices = {
        2.50: ['Cantaloupe', 'Honeydew'],
        2.95: ['Watermelon'],
        3.25: ['Musk', 'Crenshaw'],
        14.25: ['Christmas']
    }

    if price not in melon_prices:
        return

    return sorted(melon_prices[price])