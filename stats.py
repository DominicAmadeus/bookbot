# take book text as string and count the words
def count_words(book_text):
    # using space as a delimiter, put each word into a list
    words_list = book_text.split(sep=None, maxsplit=-1)
    return len(words_list)

# take book text as string and count each character
def count_characters(book_text):
    # init dictionary to store and count chars
    # convert all characters to lower
    char_dictionary = {}
    book_lower = book_text.lower()

    # iterate over each char, for each first char encountered, initialize value to 1
    for char in book_lower:
        if char_dictionary.get(char) is None:
            char_dictionary.update({char:1})
        else:
            x = char_dictionary.get(char)
            x += 1
            char_dictionary.update({char: x})

    return char_dictionary

# returns list of dictionaries of chars and their counts in descending order of counts
def sort_dictionary(char_dictionary):
    sorted_list = []
    for char, count in char_dictionary.items():
        temp_dictionary = {'char': 0, 'count': 0}
        temp_dictionary['char'] = char
        temp_dictionary['count'] = count
        sorted_list.append(temp_dictionary)
    sorted_list.sort(key=lambda d: d['count'], reverse=True)
    
    return sorted_list


