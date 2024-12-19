# Function that returns the number of words in the text
def word_count(text):
    words = text.split()  # Split the text into words using spaces as delimiter
    return len(words)

# Function that returns an ordered array of words from longest to shortest
def words_by_length(text):
    words = text.split()
    words.sort(key=len, reverse=True)  # Sort words by length in descending order
    return words

# Function that returns an alphabetically ordered array of words
def words_alphabetically(text):
    words = text.split()
    words.sort()  # Sort words alphabetically
    return words
