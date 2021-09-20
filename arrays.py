def print_indices(items):
    """Print each item in the list, followed by its index.

    The output should look like this:
        apple 0
        berry 1
        cherry 2

    Arguments:
        items (list)

    Returns:
        None
    """

    for i in range(len(items)):
        print(f'{items[i]} {i}')


def every_other_item(items):
    """Print a list of every other item in `items`

    Start with index 0.

    Arguments:
        items (list)
    """

    result = []

    for i in range(len(items)):
        if i % 2 == 0:
            result.append(items[i])

    print(result)


def smallest_n_items(items, n):
    """Print a list of the `n` smallest integers in `items`.

    Order the integers in descending order.

    You can assume that `n` will be less than the length of the list.

    Arguments:
        items (list[int]): A list of integers
        n (int): Desired length for the resulting list
    """

    sorted_items = sorted(items)
    sorted_n_items = sorted_items[:n]
    sorted_n_items.reverse()

    print(sorted_n_items)