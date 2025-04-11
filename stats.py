def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    lowercase_text = text.lower()
    letter_count = {}
    for letter in lowercase_text:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
    return letter_count

def sort_letter_count(letters):
    chars_list = []
    for char, count in letters.items():
        if char.isalpha():
            chars_list.append({'char': char, 'count': count})

    chars_list.sort(key=lambda x: x['count'], reverse=True)
    return chars_list

def main():
    pass
main()