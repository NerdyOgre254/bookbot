from stats import get_book_wordcount
from stats import get_character_count
from stats import sort_on
from stats import get_sorted_dictionary
import sys

def main():
	if (len(sys.argv) !=2):
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	target_book = sys.argv[1]
	target_wordcount = get_book_wordcount(target_book)
	target_char_dict = get_character_count(target_book)
	sorted_dict = get_sorted_dictionary(target_char_dict)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {target_book}")
	print("----------- Word Count ----------")
	print(f"Found {target_wordcount} total words")
	print("--------- Character Count -------")
	for letter in sorted_dict:
		char = letter["char"]
		num = letter["num"]
		if char.isalpha():
			print(f"{char}: {num}")
	print("============= END ===============")

main()
