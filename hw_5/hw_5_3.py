import string

# Asking the user to enter a sentence
user_input = input("Enter a sentence you want to turn into a hashtag: ")

# Remove punctuation
clean_input = user_input.translate(str.maketrans('', '', string.punctuation))

# Split into words, each word starts with a capital letter
words = clean_input.split()
capitalized_words = [word.capitalize() for word in words]

# Combine all words by adding “#” at the beginning
hashtag = "#" + "".join(capitalized_words)

# If the length of the hashtag is more than 140 characters, trim it
if len(hashtag) > 140:
    hashtag = hashtag[:140]

# Output the result
print(hashtag)
