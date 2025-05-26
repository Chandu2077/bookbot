import sys

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_char(text):
    char = text.lower()
    low_text = {}
    for i in char:
        if i in low_text:
            low_text[i] +=1 
        else:
            low_text[i] = 1
    return low_text

def sort_list(low_text):
    sorted_list = [] 
    for char, count in low_text.items():
        sorted_list.append({"char": char, "num": count})
    sorted_list.sort(reverse=True, key=lambda item: item["num"])
    return sorted_list

