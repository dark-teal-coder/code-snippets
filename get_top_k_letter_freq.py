import re

def get_only_letters(text):
    ## Replace anything that is NOT a-z or A-Z with nothing.
    ## [^a-zA-Z] will match any character except for [a-z] and [A-Z] (https://docs.python.org/3/library/re.html).
    only_letters = re.sub(r'[^a-zA-Z]', '', text)
    only_letters = only_letters.lower()
    return only_letters

def calculate_letter_freq(text):
    frequencies = {}

    for char in text:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1

    return frequencies

def get_top_k_letter_freq(sorted_letter_freq, k):
    top_k_letter_freq = sorted_letter_freq[:k]
    # print("top_k_letter_freq:", top_k_letter_freq)
    kth_freq = top_k_letter_freq[-1][-1]
    # print("kth_freq:", kth_freq)
    after_top_k_letter_freq = sorted_letter_freq[k:]
    # print("after_top_k_letter_freq:", after_top_k_letter_freq)
    extra_pair = []
    for pair in after_top_k_letter_freq:
        if pair[-1] == kth_freq:
            extra_pair.append(pair)
    # print("extra_pair:", extra_pair)
    top_k_letter_freq_combined = top_k_letter_freq + extra_pair
    return top_k_letter_freq_combined

if __name__ == "__main__": 
    ## Force the user to input only an integer between 1 and 26.
    while True:
        try: 
            k = int(input("Enter an integer between 1 and 26: "))
            if 1 <= k <= 26:
                break
            else:
                print("Please enter a whole number between 1 and 26.")
        except ValueError:
            print("Only an integer between 1 and 26 is allowed.")
    text = input("Please enter a text with at least one valid letter: ")
    only_letters = get_only_letters(text)
    letter_freq = calculate_letter_freq(only_letters)
    # print("letter_freq:", letter_freq)
    ## Order dictionary items according to their values in descending order.
    sorted_letter_freq = sorted(letter_freq.items(), key=lambda item: item[1], reverse=True)
    # print("sorted_letter_freq:", sorted_letter_freq)
    top_k_letter_freq_combined = get_top_k_letter_freq(sorted_letter_freq, k)
    ## Get only the keys (letters) from key-value pairs. 
    sorted_letters = ''.join(sorted([pair[0] for pair in top_k_letter_freq_combined]))
    # print("sorted_letters:", sorted_letters)
    output = sorted_letters.upper()
    print(output)