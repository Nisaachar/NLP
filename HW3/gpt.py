import nltk
import pandas as pd
from nltk.util import ngrams
from nltk.lm.preprocessing import pad_both_ends, flatten

# Load the CSV file
df = pd.read_csv("train.csv/train.csv")

print('The model is being trained.... \n')

# Combine all text data into a single string
text_data = " ".join(df["comment_text"].tolist())



# Tokenize the text data
tokenized_data = nltk.word_tokenize(text_data)

# Create n-grams from tokenized data
n = 2
ngrams_data = list(ngrams(tokenized_data, n, pad_left=True, pad_right=True, pad_symbol=None))


# Remove the <<UNK>> tokens from the n-grams
cleaned_ngrams = [ngram for ngram in ngrams_data if '<<UNK>>' not in ngram]

# # Flatten the list of n-grams
# flattened_ngrams = list(flatten(padded_ngrams))

# Create the language model
lm = nltk.lm.MLE(order=n)
lm.fit([cleaned_ngrams], vocabulary_text=tokenized_data)

# Save the trained model
lm.save("example_model.pickle")
