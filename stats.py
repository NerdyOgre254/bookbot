def get_book_wordcount(filepath):
	with open(filepath) as f:
		book_text = f.read()
		book_text_list = book_text.split()
		return len(book_text_list)

def get_character_count(filepath):
	character_count = {}
	with open(filepath) as f:
		content = f.read()
		content_without_newlines = content.replace("\n","")
		content_lower = content_without_newlines.lower()
		for letter in content_lower:
			if letter not in character_count:
				character_count[f"{letter}"]=1
			else:
				character_count[f"{letter}"]+=1
	return character_count

def sort_on(items):
	return items["num"]

def get_sorted_dictionary(dictionary):
	sorted_list = []
	for ch in dictionary:
		num = dictionary[ch]
		sorted_list.append({"char":ch, "num": num})
	sorted_list.sort(reverse=True, key= sort_on)
	return sorted_list 
