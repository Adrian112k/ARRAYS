# Importing the functions from the MyText module
import MyText

# The given text
text = "An apple a day keeps the doctor away"

# Call the functions and print the results
print("Text:", text)
print("Number of words:", MyText.word_count(text))
print("Words from the longest to shortest:", ", ".join(MyText.words_by_length(text)))
print("Words ordered alphabetically:", ", ".join(MyText.words_alphabetically(text)))
