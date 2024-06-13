import unittest
import sqlite3
from models.author import Author
from models.magazine import Magazine
from models.article import Article

def clear_database():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM authors')
    cursor.execute('DELETE FROM magazines')
    cursor.execute('DELETE FROM articles')
    connection.commit()
    connection.close()

class TestModels(unittest.TestCase):
    def setUp(self):
        clear_database()

    def test_author_creation(self):
        author = Author(1, 'John Doe')
        self.assertEqual(author.name, 'John Doe')

    def test_article_creation(self):
        author = Author(1, 'John Doe')
        magazine = Magazine(1, 'Tech Weekly', 'Technology')
        article = Article(author, magazine, 'Test Title')
        self.assertEqual(article.title, 'Test Title')
        self.assertEqual(article.author.name, 'John Doe')
        self.assertEqual(article.magazine.name, 'Tech Weekly')

    def test_magazine_creation(self):
        magazine = Magazine(1, 'Tech Weekly', 'Technology')
        self.assertEqual(magazine.name, 'Tech Weekly')
        self.assertEqual(magazine.category, 'Technology')

if __name__ == '__main__':
    unittest.main()
