def count_words(book_text):
    num_words = book_text.split()
    #print(f"{len(num_words)} words found in the document")
    return len(num_words)

def count_chars(book_text):
    char_dict = {}
    words = book_text.split()
    for word in words:
        for letter in word:
            if letter.lower() not in char_dict:
                char_dict[letter.lower()] = 1
            else:
                char_dict[letter.lower()] += 1
    return char_dict

def sort_on(items):
    return items["num"]

def pretty_report(raw_dict):
    pretty_list = []
    # loop to get data from raw dictionary.
    # char gets the value from the key, e.g. "a", and num is the int
    # that counts how many times it occurs

    for key in raw_dict:
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = raw_dict[key]
        pretty_list.append(new_dict)
        new_dict = {}

    pretty_list.sort(reverse=True, key=sort_on)

    return pretty_list