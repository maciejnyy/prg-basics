def read_file_in_chunks(filename, chunk_size=5):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = []
            for line in file:
                lines.append(line.strip())
                if len(lines) == chunk_size:
                    for l in lines:
                        print(l)
                    input("Press Enter key...")
                    lines = []
            
            # Print any remaining lines
            if lines:
                for l in lines:
                    print(l)
    except FileNotFoundError:
        print(f"File {filename} not found.")

if __name__ == "__main__":
    read_file_in_chunks('it_company.csv')
