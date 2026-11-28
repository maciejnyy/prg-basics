def analyze_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            
        lines_count = len(content.splitlines())
        char_count = len(content)
        word_count = len(content.split())
        
        print(f"File name: {filename}")
        print(f"Number of lines: {lines_count}")
        print(f"Number of characters: {char_count}")
        print(f"Number of words: {word_count}")
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

if __name__ == "__main__":
    filename = input("Enter file name: ")
    analyze_file(filename)
