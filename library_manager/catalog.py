"""
Модуль для управления каталогом библиотеки.
"""

from typing import List, Dict, Optional
from .utils.data_validation import validate_book_data


class Book:
    """Класс для представления книги."""
    
    def __init__(self, title: str, author: str, genre: str):
        self.title = title
        self.author = author
        self.genre = genre
    
    def to_dict(self) -> Dict:
        """Преобразует книгу в словарь."""
        return {
            'title': self.title,
            'author': self.author,
            'genre': self.genre
        }
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.genre}')"
    
    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return (self.title == other.title and 
                self.author == other.author and 
                self.genre == other.genre)


class Library:
    """Класс для управления библиотекой."""
    
    def __init__(self):
        self.books: List[Book] = []
    
    def add_book(self, title: str, author: str, genre: str) -> bool:
        """
        Добавляет книгу в библиотеку.
        
        Args:
            title: Название книги
            author: Автор книги
            genre: Жанр книги
            
        Returns:
            bool: True если книга успешно добавлена, False в противном случае
        """
        book_data = {
            'title': title,
            'author': author,
            'genre': genre
        }
        
        if not validate_book_data(book_data):
            return False
        
        # Проверяем, нет ли уже такой книги
        for book in self.books:
            if (book.title == title and 
                book.author == author and 
                book.genre == genre):
                return False
        
        new_book = Book(title, author, genre)
        self.books.append(new_book)
        return True
    
    def remove_book(self, title: str) -> bool:
        """
        Удаляет книгу по названию.
        
        Args:
            title: Название книги для удаления
            
        Returns:
            bool: True если книга найдена и удалена, False в противном случае
        """
        for i, book in enumerate(self.books):
            if book.title == title:
                self.books.pop(i)
                return True
        return False
    
    def search_by_title(self, title: str) -> List[Book]:
        """Ищет книги по названию."""
        return [book for book in self.books if title.lower() in book.title.lower()]
    
    def search_by_author(self, author: str) -> List[Book]:
        """Ищет книги по автору."""
        return [book for book in self.books if author.lower() in book.author.lower()]
    
    def search_by_genre(self, genre: str) -> List[Book]:
        """Ищет книги по жанру."""
        return [book for book in self.books if genre.lower() in book.genre.lower()]
    
    def search_books(self, title: Optional[str] = None, 
                    author: Optional[str] = None, 
                    genre: Optional[str] = None) -> List[Book]:
        """
        Ищет книги по различным критериям.
        
        Args:
            title: Название книги (частичное совпадение)
            author: Автор книги (частичное совпадение)
            genre: Жанр книги (частичное совпадение)
            
        Returns:
            List[Book]: Список найденных книг
        """
        results = self.books
        
        if title:
            results = [book for book in results if title.lower() in book.title.lower()]
        
        if author:
            results = [book for book in results if author.lower() in book.author.lower()]
        
        if genre:
            results = [book for book in results if genre.lower() in book.genre.lower()]
        
        return results
    
    def get_all_books(self) -> List[Book]:
        """Возвращает все книги в библиотеке."""
        return self.books.copy()
    
    def count_books(self) -> int:
        """Возвращает количество книг в библиотеке."""
        return len(self.books)
    
    def clear(self):
        """Очищает библиотеку."""
        self.books.clear()