import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

file_path = "random_paragraphs.txt"
with open(file_path, 'r') as file:
    text = file.read()

words = nltk.word_tokenize(text)

filtered_words = [word for word in words if word.lower() not in stop_words and word.isalpha()]

word_freq = {}
for word in filtered_words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1


sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

for word, freq in sorted_word_freq:
     print(f"{word}: {freq}")
