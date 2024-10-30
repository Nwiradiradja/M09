import pandas as pd

class BookLover:

    def __init__(self, name, email, fav_genre, num_books=0,
                 book_list=pd.DataFrame({'book_name': [], 'book_rating': []})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list

    def add_book(self, book_name, rating):
        if book_name in self.book_list['book_name'].values:
            print(f"'{book_name}' is already in your book list.")
        else:
            new_book = pd.DataFrame({
                'book_name': [book_name],
                'book_rating': [rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1

    def has_read(self, book_name):
        return book_name in self.book_list['book_name'].values

    def num_books_read(self):
        return self.num_books

    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]

if __name__ == '__main__':
    # Example to test the class
    test_object = BookLover("Arjun Dhar", "ArjunDhar@gmail.com", "Non-fiction")
    test_object.add_book("100 years of solitude", 5)
    test_object.add_book("Charlotte's Web", 1)
    test_object.add_book("Catcher in the Rye", 3)
    print(test_object.book_list)
    print(f"Has read '100 years of solitude'? {test_object.has_read('100 years of solitude')}")
    print(f"Number of books read: {test_object.num_books_read()}")
    print(f"Favorite books: {test_object.fav_books()}")
