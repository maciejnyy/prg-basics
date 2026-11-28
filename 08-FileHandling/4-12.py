import csv

def filter_books_by_genre(input_file):
    genres = {
        'Fantasy': 'books_fantasy.txt',
        'Historical': 'books_historical.txt',
        'Romance': 'books_romance.txt',
        'Classic': 'books_classic.txt'
    }
    
    # Initialize files (clear them)
    for file in genres.values():
        open(file, 'w', encoding='utf-8').close()

    try:
        with open(input_file, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            
            for row in csv_reader:
                genre = row.get('Genre')
                if genre in genres:
                    output_file = genres[genre]
                    with open(output_file, 'a', encoding='utf-8') as out_f:
                        # Assuming we want to write the whole row or specific format. 
                        # Writing Title and Author for simplicity.
                        out_f.write(f"{row['Title']}, {row['Author']}\n")
    except FileNotFoundError:
        print(f"File {input_file} not found.")

if __name__ == "__main__":
    filter_books_by_genre('books.csv')
