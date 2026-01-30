import sys
import json

def normalize(text):
    words = text.split()
    words = [word.strip('.,!?¿;"\'()[]') for word in words]
    filtered_words = [word for word in words if word]
    return filtered_words

def count_words(words):
    return len(words)

def most_frequent_words(words):
    frequency = {}
    for word in words:
        word = word.lower()
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    sorted_freq = sorted(frequency, key=frequency.get, reverse=True)
    top_words = [(word, frequency[word]) for word in sorted_freq[:3]]
    return top_words

def main(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = normalize(f.read())
            if not content:
                print("The file does not contain any valid words.")
                sys.exit(0)
            counted_words = count_words(content)
            most_frequent = most_frequent_words(content)
            result ={
                "total_words": counted_words,
                "most_frequent": [
                    {"word": word, "count": freq} 
                    for word, freq in most_frequent
                ]
            }
            #Create the Json file
            with open('result.json', 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=4, ensure_ascii=False)
            
            print("Words in text: " + str(counted_words))
            print("Most frequent words: ")
            for word, freq in most_frequent:
                print(f"'{word}' appears {freq} times")
    except FileNotFoundError:
        print(f"File '{text}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        text = sys.argv[1]
    elif len(sys.argv) > 2:
        print("Program usage: python main.py [filename]")
        sys.exit(1)
    else:
        text = 'text.txt'
    main(text)