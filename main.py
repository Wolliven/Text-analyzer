import sys

def count_words(text):
    counter = 0
    for i in range(len(text.split())):
        counter += 1
    return counter

def most_frequent_word(text):
    words = text.split()
    frequency = {}
    for word in words:
        word = word.lower()
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    most_frequent = max(frequency, key=frequency.get)
    return most_frequent, frequency[most_frequent]

def main(text):
    with open(text, 'r', encoding='utf-8') as f:
        content = f.read()
        print("Words in text: " + str(count_words(content)))
        print("Most frequent word: " + str(most_frequent_word(content)))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        text = sys.argv[1]
    elif len(sys.argv) > 2:
        print("Program usage: python main.py [filename]")
        sys.exit(1)
    else:
        text = 'text.txt'
    main(text)