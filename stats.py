def count_words(book_text):
	word_count = len(book_text.split())
	return word_count

def count_characters(book_text):
    ledger = {}
    book_words = book_text.split()
    for word in book_words:
        for char in word:
            char = char.lower()
            if char not in ledger:
                ledger[char] = 1
            else:
                ledger[char] += 1
    return ledger

def sort_on(items):
    return items["num"]

def order_characters(ledger):
    result = []
    for item in ledger:
        new_dict = {}
        new_dict["char"] = item
        new_dict["num"] = ledger[item]
        result.append(new_dict)
    result.sort(reverse=True, key=sort_on)
    return result