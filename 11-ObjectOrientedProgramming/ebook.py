class EBook:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1
        self.is_open = False

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

    def next_page(self):
        if not self.is_open:
            print("Cannot turn page: the book is closed.")
        elif self.current_page < self.pages:
            self.current_page += 1

    def previous_page(self):
        if not self.is_open:
            print("Cannot turn page: the book is closed.")
        elif self.current_page > 1:
            self.current_page -= 1

    def show_status(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, Current page: {self.current_page}")
