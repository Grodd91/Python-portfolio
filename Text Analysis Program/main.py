import re
from collections import Counter

def analyze_text(text):
    # Count number of words
    words = text.split()
    num_words = len(words)

    # Count number of sentences
    sentences = re.split(r'[.!?]', text)
    num_sentences = len([sentence for sentence in sentences if sentence.strip() != ''])

    # Most common words
    word_counter = Counter(words)
    most_common_words = word_counter.most_common(5)

    print("Text Analysis:")
    print(f"Number of words: {num_words}")
    print(f"Number of sentences: {num_sentences}")
    print("Most common words:")
    for word, count in most_common_words:
        print(f"'{word}': {count} times")

if __name__ == "__main__":
    input_text = input("Enter the text to analyze: ")
    analyze_text(input_text)
