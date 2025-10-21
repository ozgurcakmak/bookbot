from stats import count_words
from stats import count_characters
from stats import order_characters

def get_book_text(file_path):
	file_contents = ""
	with open (file_path) as f:
		file_contents = f.read()
	return file_contents

def draft_report(book_path, word_count, ledger):
	report_text =  f"""
	============ BOOKBOT ============
	Analyzing book found at {book_path}...
	----------- Word Count ----------
	Found {word_count} total words
	--------- Character Count -------
	"""

	for item in ledger:
		if item['char'].isalpha():
			report_text += f"{item['char']}: {item['num']}\n\t"

	report_text += "============= END ==============="
	return report_text

def main():
	import sys
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	
	book_path = sys.argv[1]
	book_text = get_book_text(book_path)
	word_count = count_words(book_text)
	# print(f"Found {word_count} total words")
	ledger = count_characters(book_text)
	#print(ledger)
	ledger = order_characters(ledger)
	report = draft_report(book_path,word_count, ledger)
	print(report)

main()

