def count_words(book_text):
    num_words = len(book_text.split())
    print(f"Found {num_words} total words")

def char_count(book_text):
    book_text_lower = book_text.lower()
    char_dict = {}
    for char in book_text_lower:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_dict(dictionary):
    def sort_on(items):
        return items["num"]
    
    dic_list = []
    for d in dictionary:
        dic_list.append({"char": d, "num": dictionary[d]})
    dic_list.sort(reverse=True, key=sort_on)
    return dic_list
