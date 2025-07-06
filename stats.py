def count_num_words(text: str) -> int:
    return len(text.split(sep=None, maxsplit=-1))

def count_chars(text: str):
    chars_count = {}

    for char in text.lower():
        if char in chars_count:
            chars_count[char] += 1
        else:
            chars_count[char] = 1

    return chars_count

def sort_on(items):
    return items["num"]

def sorted_list_of_chars_count(chars_dict):
    sorted_list_of_chars_dict = [{"char": key,"num": value} for key, value in chars_dict.items()]

    # for key, value in chars_dict.items():
    #     sorted_list_of_chars_dict.append({"char": key,"num": value})

    sorted_list_of_chars_dict.sort(key=sort_on, reverse=True)
    filtered_list = [key for key in sorted_list_of_chars_dict if key["char"].isalpha()]
    
    return filtered_list
