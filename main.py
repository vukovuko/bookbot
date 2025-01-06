def count_words(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    print(count)

def main():
    with open('./books/frankenstein.txt') as f:
        file_contents = f.read()
        count_words(file_contents)

main()
