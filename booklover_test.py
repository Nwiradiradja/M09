import unittest
import pandas as pd
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        # Add a book and test if it is in `book_list`.
        test_object = BookLover("Arjun Dhar", "ArjunDhar@gmail.com", "Non-fiction")
        test_object.add_book("Hunger Games", 5)
        print(f"Test 1 - Add Book: {'Hunger Games' in test_object.book_list['book_name'].values} | Expected: True")
        self.assertTrue("Hunger Games" in test_object.book_list['book_name'].values)

    def test_2_add_book(self):
        # Add the same book twice. Test if it's in `book_list` only once.
        test_object = BookLover("Arjun Dhar", "ArjunDhar@gmail.com", "Non-fiction")
        test_object.add_book("100 years of solitude", 5)
        test_object.add_book("100 years of solitude", 3)
        print(f"Test 2 - Add Duplicate Book: num_books = {test_object.num_books} | Expected: 1")
        self.assertEqual(len(test_object.book_list), 1)  
        self.assertEqual(test_object.num_books, 1)

    def test_3_has_read(self):
        # Pass a book in the list and test if the answer is `True`.
        test_object = BookLover("Arjun Dhar", "ArjunDhar@gmail.com", "Non-fiction")
        test_object.add_book("Catcher in the Rye", 4)
        print(f"Test 3 - Has Read: {test_object.has_read('Catcher in the Rye')} | Expected: True")
        self.assertTrue(test_object.has_read("Catcher in the Rye"))

    def test_4_has_read(self):
        # Pass a book NOT in the list and use `assert False` to test the answer is `True`.
        test_object = BookLover("Arjun Dhar", "ArjunDhar@gmail.com", "Non-fiction")
        test_object.add_book("Hunger Games", 5)
        print(f"Test 4 - Has Read (not in list): {test_object.has_read('Spongebob')} | Expected: False")
        self.assertFalse(test_object.has_read("Spongebob")) 
    def test_5_num_books_read(self):
        # Add some books to the list, and test num_books matches expected.
        test_object = BookLover("Arjun Dhar", "ArjunDhar@gmail.com", "Non-fiction")
        test_object.add_book("Hunger Games", 5)
        test_object.add_book("1984", 4)
        print(f"Test 5 - Number of Books Read: {test_object.num_books_read()} | Expected: 2")
        self.assertEqual(test_object.num_books_read(), 2)

    def test_6_fav_books(self):
        # Add some books with ratings to the list, making sure some of them have rating > 3.
        test_object = BookLover("Arjun Dhar", "ArjunDhar@gmail.com", "Non-fiction")
        test_object.add_book("Hunger Games", 5)
        test_object.add_book("Charlotte's Web", 1)
        test_object.add_book("1984", 4)
        fav_books = test_object.fav_books()
        print(f"Test 6 - Favorite Books: {'Hunger Games' in fav_books['book_name'].values} | Expected: True")
        self.assertTrue("Hunger Games" in fav_books['book_name'].values)
        self.assertFalse("Charlotte's Web" in fav_books['book_name'].values)  

if __name__ == '__main__':
    unittest.main(verbosity=3)
