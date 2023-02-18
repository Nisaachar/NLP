from nltk.util import bigrams
import re
from nltk.util import pad_sequence
from nltk.lm.preprocessing import pad_both_ends
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk.lm import MLE

# text = [['a', 'b', 'c'], ['a', 'c', 'd', 'c', 'e', 'f']]
# print(list(bigrams(pad_both_ends(text[0], n=2))))

file = open("train.csv/train.csv", 'r', encoding = 'windows-1252')

# while True:
#     content = file.readline()
#     content = re.sub(r'\t\n', '', content) #removing tabs and newlines to form a dictionary. 
#     content = content.lower() #lowercasing the text, in case if it wasn't.
        
#     if not content: #braking the loop at the end of file
#         break

#     n = 2
#     train_data, padded_sents = padded_everygram_pipeline(n, content)
#     model = MLE(n)
#     model.fit(train_data, padded_sents)

#     # Generate some random text using the language model
#     generated_text = model.generate(20, random_seed=42)

#     # Print the generated text
#     print(' '.join(generated_text))


content = file.readlines()
# content = re.sub(r'\t\n', '', content) #removing tabs and newlines to form a dictionary. 
# content = content.lower() #lowercasing the text, in case if it wasn't.

n = 2
train_data, padded_sents = padded_everygram_pipeline(n, content)
model = MLE(n)
model.fit(train_data, padded_sents)

    # Generate some random text using the language model
generated_text = model.generate(20, random_seed=42)

    # Print the generated text
print(' '.join(generated_text))