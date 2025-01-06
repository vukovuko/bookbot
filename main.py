def sort_on(entry):
    return entry["num"]

def count_characters(text):
    characters = {}
    for character in text:
        if character.isalpha():
            if character in characters:
                characters[character] += 1
            else:
                characters[character] = 1
    return characters

def count_words(text):
    words = text.split()
    return len(words)

def main():
    with open('./books/frankenstein.txt') as f:
        print("--- Begin report of books/frankenstein.txt ---")

        file_contents = f.read()
        words_in_document = count_words(file_contents)
        print(f"{words_in_document} words found in the document\n")

        character_list = []
        characters_in_document = count_characters(file_contents)
        for char, count in characters_in_document.items():
            character_list.append({"char": char, "num": count})

        character_list.sort(reverse=True, key=sort_on)

        for entry in character_list:
            print(f"The '{entry['char']}' character was found {entry['num']} times")

        print("--- End report ---")

main()

