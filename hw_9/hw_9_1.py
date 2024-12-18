def popular_words(text: str, words: list[str]) -> dict[str, int]:
    """
    Counts the number of occurrences of each word in the list in the given text, regardless of case.

    Args:
        text (str): The text in which words are searched.
        words (list[str]): A list of words for which you want to determine the number of occurrences.

    Returns:
        dict[str, int]: A dictionary where the keys are words from the `words` list,
                        and the values are the number of their occurrences in the text.
                        If a word is not found, its value is 0.

    Example:
        >>> popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
        ...               ['i', 'was', 'three', 'near'])
        {'i': 4, 'was': 3, 'three': 0, 'near': 0}
    """

    # Convert all text to lowercase and split it into words
    normalized_text = text.lower().split()

    # Counting the number of words from the word list
    result = {word: normalized_text.count(word) for word in words}

    return result


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'

print('OK')
